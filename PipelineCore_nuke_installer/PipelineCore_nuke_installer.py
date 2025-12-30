#                            # #######################################                          #
#                            #                                       #                          #
#                            #            Author: Nitin Kashyap      #                          #
#                            #                                       #                          #
#                            # #######################################                          #
#                                                                                               #
#                            # Created by: Nitin Nitinkashyap                                   #
# -------------------------- # GitHub Tools Installer for Nuke----------------------------------#                     


"""
======================================================================================
# Tool Name      : <PipelineCore_nuke_installer>
# Version        : 1.0.0
#
# Author         : Nitin Kashyap
# Contact        : <email / github >>"https://github.com/Nitinkashyap96/ViewerToggle-for-in_Nuke" 

#
# Software       : Foundry Nuke (12+ / 13+ / 14+ / 15+)
# Language       : Python : 3.10
# Platform       : Windows / Linux / macOS

# Installation   :
#   1. Copy script to ~/.nuke or NUKE_PATH
#   2. Add menu entry in menu.py


import nuke
import os


nuke.pluginAddPath(r'./icon')



# Place this in your ~/.nuke/menu.py file

# 1. Import your installer module. Adjust import path if necessary.
import github_nuke_installer_with_close  # Use the filename of your finalized installer

# 2. Add a menu item in a custom menu:
toolbar = nuke.menu("Nuke")  # Top-level
github_menu = toolbar.addMenu("GitHub Tools", icon="GitHub.png.png")

# 3. Add a command that opens the installer dialog
github_menu.addCommand(
    "Install GitHub Repo...",  # Menu command name
    "github_nuke_installer_with_close.show_installer()",  # Function to call
    icon="GitHub_Logo_W.png"
)

# Optionally, add author info/help:
github_menu.addCommand(
    "About Installer",
    "nuke.message('Created by: Nitin Kashyap nGitHub Tools Installer for Nuke')",
)


#
# Usage          :
#   - Access via Nuke → Custom → <PipelineCore_nuke_installer>
#
# Changelog      :
#   v1.0.0  - Initial release
#
# License        : Proprietary / MIT / GPL /
#
# Notes          :
#   - Tested with Nuke 15.x

#Copyright (c) 2025 Nitin Kashyap
======================================================================================
"""

########################################################################################
'''
Copyright (c) 2024, Nitin Kashyap, All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Redistribution of this software in source or binary forms shall be free
      of all charges or fees to the recipient of this software.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
########################################################################################


import sys
import nuke
import os
import shutil
import subprocess
import platform
from pathlib import Path


try:
    from PySide2.QtWidgets import (
        QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
        QComboBox, QPushButton, QFileDialog, QMessageBox, QApplication
    )
    from PySide2.QtCore import Qt
    from PySide2.QtGui import QPalette, QColor
    PYSIDE_VERSION = 2
except ImportError:
    from PySide6.QtWidgets import (
        QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
        QComboBox, QPushButton, QFileDialog, QMessageBox, QApplication
    )
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QPalette, QColor
    PYSIDE_VERSION = 6


#####################################----------------------------------------######################################
#              # ---------------------------------------------------------------------------------------- #       #
#                                       SOUND ALERT Tools Install  ON Done finishes                               #
#              # ---------------------------------------------------------------------------------------- #       #
#                                                                                                                 #
#                                                                                                                 #


def Play_Render_Sound():
    """Play sound or voice notification when render finishes."""
    import os, platform, subprocess, nuke

    operatingSystem = platform.system()
    base_dir = os.path.dirname(__file__) if "__file__" in globals() else nuke.script_directory()
    sound_file = os.path.join(base_dir, "02.wav")

    try:
        if os.path.exists(sound_file):
            if operatingSystem == "Windows":
                import winsound
                winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
            elif operatingSystem == "Darwin":
                subprocess.Popen(["afplay", sound_file])
            else:
                subprocess.Popen(["paplay", sound_file])
        else:
            if operatingSystem == "Windows":
                import winsound
                winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
            elif operatingSystem == "Darwin":
                subprocess.Popen(["say", "Rendering finished"])
            else:
                subprocess.Popen(["spd-say", "Rendering finished"])
    except Exception as e:
        try:
            from PySide2.QtWidgets import QApplication
            QApplication.beep()
        except Exception:
            pass
        nuke.tprint(f"Render sound failed: {e}")
#                                                                                                                 #
#                                                                                                                 #
#                                                                                                                 #
#                                                                                                                 #
#####################################----------------------------------------######################################



try:
    import requests
    _HAS_REQUESTS = True
except ImportError:
    _HAS_REQUESTS = False

def ensure_git(parent=None):
    if shutil.which("git"):
        return True
    if parent:
        QMessageBox.warning(parent, "Git Missing", "Git is not installed or not in PATH.")
    else:
        print("Git is not installed or not in PATH.")
    return False

def run(cmd):
    kwargs = dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if platform.system() == "Windows" and hasattr(subprocess, "CREATE_NO_WINDOW"):
        kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
    return subprocess.run(cmd, **kwargs)

def get_branches(url):
    p = run(["git", "ls-remote", "--heads", url])
    if p.returncode != 0:
        return []
    output = []
    for line in p.stdout.splitlines():
        if "refs/heads/" in line:
            output.append(line.split("refs/heads/")[-1])
    return output

def get_tags(url):
    p = run(["git", "ls-remote", "--tags", url])
    if p.returncode != 0:
        return []
    output = []
    for line in p.stdout.splitlines():
        if "refs/tags/" in line and "^{}" not in line:
            output.append(line.split("refs/tags/")[-1])
    return output

def get_releases(url):
    if _HAS_REQUESTS:
        try:
            owner_repo = url.split("github.com/")[1].replace(".git", "")
            owner, repo = owner_repo.split("/")[:2]
            api = f"https://api.github.com/repos/{owner}/{repo}/releases"
            r = requests.get(api, timeout=10)
            if r.status_code == 200:
                out = []
                for rel in r.json():
                    tag = rel.get("tag_name")
                    name = rel.get("name") or tag
                    if tag:
                        out.append((tag, name))
                if out:
                    return out
        except Exception as e:
            print("Requests release fetch failed:", e)
    t = get_tags(url)
    return [(x, x) for x in t]

def clone_repo(url, dest, ref, parent=None):
    p = run(["git", "clone", "--depth", "1", "--branch", ref, url, dest])
    if p.returncode != 0:
        if parent:
            QMessageBox.critical(parent, "Clone Error", p.stderr)
        else:
            print("Clone failed:", p.stderr)
        raise RuntimeError(p.stderr)
    return True

def register_nuke_plugin_path(path):
    init_file = Path(os.path.join(os.path.expanduser("~/.nuke"), "init.py"))
    init_file.parent.mkdir(parents=True, exist_ok=True)
    entry = f'\n# Added by GitHub Installer by: Author Nitin Kashyap \nnuke.pluginAddPath(r"{path}")\n'
    if init_file.exists():
        txt = init_file.read_text()
        if path in txt:
            return
        init_file.write_text(txt + entry)
    else:
        init_file.write_text(entry)

class GithubNukeInstaller(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GitHub Nuke Tools Gizmos & Python Dev: Installer for Nuke by: Author Nitin Kashyap")
        self.setMinimumWidth(580)
        self.repo_url = QLineEdit()
        self.mode_select = QComboBox()
        self.ref_select = QComboBox()
        self.install_folder = QLineEdit()
        self.browse_button = QPushButton("Browse")
        self.install_button = QPushButton("Install")
        self.close_button = QPushButton("Close")  # New close button!
        self.status_label = QLabel()

        # Colorful Buttons
        self.install_button.setStyleSheet("background-color: #003d00; color: white; font-weight:bold;")
        self.close_button.setStyleSheet("background-color: #400000; color: white; font-weight:bold;")
        self.init_ui()
        self.set_connections()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("GitHub (.git) URL:"))
        layout.addWidget(self.repo_url)
        layout.addWidget(QLabel("Download Type:"))
        self.mode_select.addItems(["Branch", "Release"])
        layout.addWidget(self.mode_select)
        layout.addWidget(QLabel("Select Version:"))
        layout.addWidget(self.ref_select)
        folder_layout = QHBoxLayout()
        folder_layout.addWidget(QLabel("Install Folder:"))
        folder_layout.addWidget(self.install_folder)
        folder_layout.addWidget(self.browse_button)
        layout.addLayout(folder_layout)

        # Add both buttons side by side
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.install_button)
        button_layout.addWidget(self.close_button)
        layout.addLayout(button_layout)

        layout.addWidget(self.status_label)
        self.setLayout(layout)

        self.ref_select.setEnabled(False)
        self.install_button.setEnabled(False)
        self.install_button.setDefault(True)

    def set_connections(self):
        self.repo_url.textChanged.connect(self.fetch_refs)
        self.mode_select.currentIndexChanged.connect(self.fetch_refs)
        self.browse_button.clicked.connect(self.pick_folder)
        self.ref_select.currentIndexChanged.connect(self.enable_install)
        self.install_button.clicked.connect(self.install)
        self.close_button.clicked.connect(self.close)  # Close button closes dialog!

    def fetch_refs(self):
        url = self.repo_url.text().strip()
        self.ref_select.clear()
        self.ref_select.setEnabled(False)
        self.install_button.setEnabled(False)
        if not url.endswith(".git"):
            self.status_label.setText("Enter a valid .git URL.")
            return

        self.status_label.setText("Fetching refs...")
        QApplication.processEvents()  # Correct usage, fixed bug!
        mode = self.mode_select.currentText()
        if mode == "Branch":
            refs = get_branches(url)
            display = refs
        else:
            releases = get_releases(url)
            display = [f"{tag} ({name})" for tag, name in releases] if releases else []
            refs = [tag for tag, _ in releases] if releases else []
        if not display:
            self.status_label.setText("No branches/releases found.")
            return
        self.ref_select.addItems(display)
        self.ref_select.setEnabled(True)
        self.ref_select.setProperty("refs", refs or display)

        # Suggest default folder
        repo_name = Path(url).stem
        default_base = os.path.join(os.path.expanduser("~/.nuke"), "VFX Pipeline Tools")
        default_path = os.path.join(default_base, repo_name)
        self.install_folder.setText(default_path)

    def pick_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Choose Install Folder", self.install_folder.text())
        if folder:
            self.install_folder.setText(folder)
            self.enable_install()

    def enable_install(self):
        self.install_button.setEnabled(bool(self.install_folder.text() and self.ref_select.currentText()))

    def install(self):
        if not ensure_git(self): return
        url = self.repo_url.text().strip()
        ref_idx = self.ref_select.currentIndex()
        refs = self.ref_select.property("refs") or []
        if ref_idx < 0 or ref_idx >= len(refs):
            QMessageBox.warning(self, "Selection Error", "No ref selected.")
            return
        ref = refs[ref_idx]
        dest_dir = self.install_folder.text()
        repo_name = Path(url).stem

        # ---- SAFE CLONE (Windows Proof) ----
        if os.path.exists(dest_dir):
            if not nuke.ask(f"Folder exists:\n{dest_dir}\nDelete and reinstall?"):
                return
            try:
                def onerror(func, path, exc_info):
                    os.chmod(path, 0o777)
                    func(path)
                shutil.rmtree(dest_dir, onerror=onerror)
            except Exception as e:
                nuke.message(f"Cannot remove existing folder:\n{e}")
                return

        # IMPORTANT: do NOT pre-create folder
        try:
            clone_repo(url, dest_dir, ref)
        except Exception as e:
            nuke.message(f"Clone failed:\n{e}")
            return


        register_nuke_plugin_path(dest_dir)

        # QMessageBox.information(self, "Success", f"{repo_name} installed successfully!\nRestart Nuke to load the plugin.")
        msg = QMessageBox(self)
        msg.setWindowTitle("Success")
        msg.setIcon(QMessageBox.Information)

        hex_color = "#0059b3"

        msg.setTextFormat(Qt.RichText)
        msg.setText(
            f'<span style="color:{hex_color}; font-size:19px;">'
            f'  {repo_name} installed successfully!<br>'
            f'  Restart Nuke to load the plugin.'
            f'</span>'
        )

        msg.exec_()

        Play_Render_Sound()
        self.status_label.setText("Done!")
        self.install_button.setEnabled(False)


def show_installer():
    # In Nuke, don't create QApplication, just show dialog
    dlg = GithubNukeInstaller()
    dlg.exec_()  # Modal, prevents crashes

def main():
    # Only create QApplication if NOT in nuke
    if "nuke" not in sys.modules:
        app = QApplication(sys.argv)
        dlg = GithubNukeInstaller()
        dlg.show()
        sys.exit(app.exec_())
    else:
        show_installer()

#if __name__ == "__main__":
#    main()














"""
# Place this in your ~/.nuke/menu.py file

# 1. Import your installer module. Adjust import path if necessary.
#import github_nuke_installer_with_close  # Use the filename of your finalized installer

# 2. Add a menu item in a custom menu:
toolbar = nuke.menu("Nuke")  # Top-level
github_menu = toolbar.addMenu("GitHub Tools", icon="GitHub.png")

# 3. Add a command that opens the installer dialog
github_menu.addCommand(
   "Install GitHub Repo...",  # Menu command name
   "show_installer()",  # Function to call
   icon="GitHub.png"
)

# Optionally, add author info/help:
github_menu.addCommand(
   "About Installer",
   "nuke.message('Created by: Nitin Kashyap\\nGitHub Tools Installer for Nuke')",
)
"""