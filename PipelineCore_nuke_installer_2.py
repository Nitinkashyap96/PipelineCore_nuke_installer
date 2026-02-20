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
# Tool Name      : <PipelineCore_nuke_installer_v2.0.0>
# Version        : 2.0.0
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
#   - Access via Nuke → Custom → <PipelineCore_nuke_installer_v2>
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




__tool_name__ = "PipelineCore_nuke_installer"
__version__ = "2.0.0"
__author__ = "Nitin Kashyap"







import sys
import nuke
import os
import shutil
import webbrowser
import subprocess
import platform
from pathlib import Path


# ----------------- Installer Version Info -----------------
INSTALLER_NAME = "GitHub Tools Installer for Nuke"
INSTALLER_VERSION = "2.0.0"
INSTALLER_GITHUB_USER = "Nitinkashyap96"
INSTALLER_GITHUB_REPO = "PipelineCore_nuke_installer"
INSTALLER_GITHUB_URL = f"https://github.com/{INSTALLER_GITHUB_USER}/{INSTALLER_GITHUB_REPO}"
INSTALLER_RELEASES_URL = INSTALLER_GITHUB_URL + "/releases"

nuke.pluginAddPath(r'./icon')


# ----------------- Nuke Version Handling -----------------
NUKE_MAJOR = nuke.NUKE_VERSION_MAJOR
NUKE_MINOR = nuke.NUKE_VERSION_MINOR
current_nuke_version = f"{NUKE_MAJOR}.{NUKE_MINOR}"

nuke_versions = [
    "17.0", "17.1",
    "15.1", "16.1",
    "15.0", "16.0",
    "14.2", "14.1", "14.0",
    "13.2", "13.1", "13.0",
    "12.2", "12.1", "12.0",
    "11.3", "11.2", "11.1", "11.0",
]

if current_nuke_version not in nuke_versions:
    nuke_versions.insert(0, current_nuke_version)



# ----------------- PySide Compatibility (Nuke 9 → 17) -----------------
try:
    # Nuke 15.1+ (some builds)
    from PySide6.QtWidgets import (
        QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
        QComboBox, QPushButton, QFileDialog, QMessageBox,
        QApplication, QCheckBox, QWidget, QFrame
    )
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QPixmap

    PYSIDE_VERSION = 6

except ImportError:
    try:
        # Nuke 10 → 15
        from PySide2.QtWidgets import (
            QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
            QComboBox, QPushButton, QFileDialog, QMessageBox,
            QApplication, QCheckBox, QWidget, QFrame
        )
        from PySide2.QtCore import Qt
        from PySide2.QtGui import QPixmap

        PYSIDE_VERSION = 2

    except ImportError:
        #  Nuke 9 and older (Qt4)
        from PySide.QtGui import (
            QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
            QComboBox, QPushButton, QFileDialog, QMessageBox,
            QApplication, QCheckBox, QWidget, QFrame, QPixmap
        )
        from PySide.QtCore import Qt

        PYSIDE_VERSION = 1

#nuke.tprint(f"Loaded PySide version: {PYSIDE_VERSION}")


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




# ----------------- Installer UI -----------------
def ensure_git(parent=None):
    if shutil.which("git"):
        return True
    if parent:
        QMessageBox.warning(parent, "Git Missing", "Git is not installed or not in PATH.")
    return False

def run(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def get_branches(url):
    p = run(["git", "ls-remote", "--heads", url])
    return [l.split("refs/heads/")[-1] for l in p.stdout.splitlines()] if p.returncode == 0 else []

def get_tags(url):
    p = run(["git", "ls-remote", "--tags", url])
    return [l.split("refs/tags/")[-1] for l in p.stdout.splitlines() if "^{}" not in l] if p.returncode == 0 else []

def clone_repo(url, dest, ref):
    p = run(["git", "clone", "--depth", "1", "--branch", ref, url, dest])
    if p.returncode != 0:
        raise RuntimeError(p.stderr)

# ----------------- init.py Registration -----------------
def register_nuke_plugin_path(path, target_nuke_version, major_only=True):
    init_file = Path(os.path.expanduser("~/.nuke/init.py"))
    init_file.parent.mkdir(parents=True, exist_ok=True)

    major = target_nuke_version.split(".")[0]
    path = path.replace("\\", "/")

    header = (
        f"# ==== PipelineCore_nuke_installer | Nuke {target_nuke_version} "
        f"| Author: Nitin Kashyap ===="
    )

    if major_only:
        block_start = f"if nuke.NUKE_VERSION_MAJOR == {major}:"
        indent = "    "
    else:
        block_start = None
        indent = ""

    new_line = f'{indent}nuke.pluginAddPath(r"{path}")'

    # Read existing file
    text = init_file.read_text() if init_file.exists() else ""

    # --------------------------------------------
    # CASE 1: Exact path already registered
    # --------------------------------------------
    if path in text:
        return  # already installed → do nothing

    lines = text.splitlines()

    # --------------------------------------------
    # CASE 2: Version block exists → append inside
    # --------------------------------------------
    if major_only and block_start in lines:
        idx = lines.index(block_start) + 1

        while idx < len(lines) and lines[idx].startswith(indent):
            idx += 1

        lines.insert(idx, new_line)
        init_file.write_text("\n".join(lines) + "\n")
        return

    # --------------------------------------------
    # CASE 3: Create new block
    # --------------------------------------------
    block = []
    block.append("")
    block.append(header)

    if major_only:
        block.append(block_start)
        block.append(new_line)
    else:
        block.append(new_line)

    block.append("")

    init_file.write_text(text + "\n".join(block) + "\n")

# ----------------- Installer UI -----------------
class GithubNukeInstaller(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"Nuke Tools Gizmos & Python Dev: Installer for Nuke Toool | by: Author Nitin Kashyap")
        self.resize(850, 100)

        self.setWindowFlags(
            Qt.Window |
            Qt.WindowMinimizeButtonHint |
            Qt.WindowMaximizeButtonHint |
            Qt.WindowCloseButtonHint
        )

        self.repo_url = QLineEdit()
        self.mode_select = QComboBox()
        self.ref_select = QComboBox()
        self.nuke_version_select = QComboBox()
        self.install_folder = QLineEdit()
        self.major_checkbox = QCheckBox("Selected Nuke major version")
        self.major_checkbox.setChecked(False)

        self.browse_button = QPushButton("Browse")
        self.install_button = QPushButton("Install")
        self.close_button = QPushButton("Close")
        self.open_folder_button = QPushButton("Open Folder")
        self.update_button = QPushButton("Check for Updates")
        self.restart_button = QPushButton("Restart_Nuke")
        self.status_label = QLabel()

        # Colorful Buttons
        self.install_button.setStyleSheet("background-color: #003d00; color:white; font-weight:bold; font-size:16px;")
        self.close_button.setStyleSheet("background-color: #400000; color:white; font-weight:bold; font-size:16px;")
        self.update_button.setStyleSheet("background-color: #1f3b73;color:white; font-weight:bold; font-size:15px;")
        self.mode_select.setStyleSheet("color:white; font-weight:bold; font-size:15px;")
        self.browse_button.setStyleSheet("color:white; font-weight:bold; font-size:15px;")
        self.major_checkbox.setStyleSheet("color:white; font-weight:bold; font-size:15px;")
        self.nuke_version_select.setStyleSheet("color:white; font-weight:bold; font-size:15px;")
        self.open_folder_button.setStyleSheet("color:white; font-weight:bold; font-size:15px")

        self.init_ui()
        self.set_connections()

    def init_ui(self):
        self.setStyleSheet("QDialog{background:#171717;} QLabel{color:white;}")
        layout = QVBoxLayout(self)

        #layout.addWidget(QLabel("GitHub (.git) URL"))

        icon_label = QLabel()
        icon_path = os.path.join(os.path.dirname(__file__), "icon", "GitHub.png")
        pixmap = QPixmap(icon_path)

        if not pixmap.isNull():
            icon_label.setPixmap(
                pixmap.scaled(22, 22, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )

        text_label = QLabel("GitHub (.git) URL")
        text_label.setStyleSheet("""
        QLabel {
            background-color: #2b2b2b;
            color: white;
            padding: 8px 12px;
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;
        }
        """)

        row = QHBoxLayout()
        row.addWidget(icon_label)
        row.addWidget(text_label)
        row.addStretch()

        layout.addLayout(row)


        layout.addWidget(self.repo_url)

        self.mode_select.addItems(["Branch", "Release"])
        #layout.addWidget(QLabel("Download Type"))
        label = QLabel("Download Type ↑ ")
        label.setStyleSheet("""
            QLabel {
                background-color: #2b2b2b;
                color: white;
                padding: 3px;
                border-radius: 10px;
                font-weight: bold;
                font-size:13px;
            }
        """)
        layout.addWidget(label)
        layout.addWidget(self.mode_select)

        #layout.addWidget(QLabel("Repository Version"))
        label = QLabel("Repository Version  ↆↆ")
        label.setStyleSheet("""
        QLabel {
            background-color: #2b2b2b;
            color: white;
            padding: 3px;
            border-radius: 10px;
            font-weight: bold;
            font-size:13px;
        }
        """)
        layout.addWidget(label)

        layout.addWidget(self.ref_select)

        self.nuke_version_select.addItems(nuke_versions)
        self.nuke_version_select.setCurrentText(current_nuke_version)
        label = QLabel("Target Nuke Version")
        label.setStyleSheet("""
            QLabel {
                background-color: #2b2b2b;
                color: white;
                padding: 3px;
                border-radius: 10px;
                font-weight: bold;
                font-size:13px;
            }
        """)
        layout.addWidget(label)
        layout.addWidget(self.nuke_version_select)

        layout.addWidget(self.major_checkbox)

        

        fl = QHBoxLayout()
        
        fl.addWidget(QLabel("Install Folder"))
        fl.addWidget(self.install_folder)
        self.install_folder.setStyleSheet("""
        QLineEdit {
            background-color: #262626;
            color: #dddddd;
            color:white;
            font-weight:bold;
            font-size:15px;
        }
        """)
        
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color:#333333;")
        layout.addWidget(line)


        # restart_button
        self.restart_button.setFixedWidth(220)

        restart_row = QHBoxLayout()
        restart_row.addStretch()
        restart_row.addWidget(self.restart_button)
        self.restart_button.setStyleSheet("""
        QPushButton {
            background-color: #f39c12;
            color: white;
            font-weight: bold;
            font-size: 14px;
            padding: 6px 6px;
            border-radius: 6px;
        }
        QPushButton:hover {
            background-color: #b50600;
        }
        QPushButton:pressed {
            background-color: #d68910;
        }
        """)

        restart_row.addStretch()

        layout.addLayout(restart_row)


        
        fl.addWidget(self.browse_button)
        layout.addLayout(fl)
        
        bl = QHBoxLayout()
        bl.addWidget(self.install_button)
        bl.addWidget(self.open_folder_button)
        bl.addWidget(self.update_button)
        # bl.addWidget(self.restart_button)
        

        bl.addWidget(self.close_button)
        bl.addWidget(self.restart_button, alignment=Qt.AlignCenter)
        layout.addLayout(bl)


        version_label = QLabel("Version 1.2.0  |  Supported (Nuke 10 → 17)")
        version_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        version_label.setStyleSheet("""
        QLabel {
            color: #58d68d;
            font-size: 13px;
            font-weight: bold;
            padding: 20px;
        }
        """)
        
        
        layout.addWidget(version_label)

        github_label = QLabel(
            '<a href="https://github.com/Nitinkashyap96">'
            'GitHub: https://github.com/Nitinkashyap'
            '</b>'
        )
        github_label.setTextFormat(Qt.RichText)
        github_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        github_label.setOpenExternalLinks(True)
        github_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        github_label.setStyleSheet("""
        QLabel {
            color: #008000;          /* green */
            font-size: 15px;
            font-weight: bold;
            padding: 3px;
        }
        
        QLabel:hover {
            color: #008000;          /* lighter green on hover */
        }
        """)
        
        layout.addWidget(github_label)


        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background-color: #444; max-height:1px;")
        
        author_label = QLabel("Author: Nitin Kashyap")
        author_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        author_label.setStyleSheet("""
        QLabel {
            color: #f1c40f;
            font-size: 13px;
            font-weight: bold;
            padding: 4px;
        }
        """)
        
        layout.addWidget(line)
        layout.addWidget(author_label)
        layout.addWidget(line)




    # -------- Divider --------
    def divider(self, text):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background:#444;")

        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color:#ffffff;font-size:12px;padding:4px;")

        box = QVBoxLayout()
        box.addWidget(line)
        box.addWidget(label)
        box.addWidget(line)

        frame = QFrame()
        frame.setLayout(box)
        return frame
        layout.addWidget(self.status_label)

        self.install_button.setEnabled(False)
        self.ref_select.setEnabled(False)


    def set_connections(self):
        self.repo_url.textChanged.connect(self.fetch_refs)
        self.mode_select.currentIndexChanged.connect(self.fetch_refs)
        self.nuke_version_select.currentIndexChanged.connect(self.update_install_path)
        self.ref_select.currentIndexChanged.connect(self.enable_install)
        self.browse_button.clicked.connect(self.pick_folder)
        self.install_button.clicked.connect(self.install)
        self.open_folder_button.clicked.connect(self.open_plugin_folder)
        self.update_button.clicked.connect(self.check_for_updates)
        self.restart_button.clicked.connect(self.restart_nuke)
        self.close_button.clicked.connect(self.close)

    def update_install_path(self):
        repo = Path(self.repo_url.text()).stem if self.repo_url.text() else "plugin"
        nuke_ver = self.nuke_version_select.currentText()
        base = os.path.join(os.path.expanduser("~/.nuke"), "VFX Pipeline Tools", f"Nuke{nuke_ver}")
        self.install_folder.setText(os.path.join(base, repo))

    def fetch_refs(self):
        url = self.repo_url.text().strip()
        self.ref_select.clear()
        self.install_button.setEnabled(False)

        if not url.endswith(".git"):
            return

        refs = get_branches(url) if self.mode_select.currentText() == "Branch" else get_tags(url)
        if not refs:
            return

        self.ref_select.addItems(refs)
        self.ref_select.setEnabled(True)
        self.update_install_path()

    def pick_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Choose Install Folder")
        if folder:
            self.install_folder.setText(folder)
            self.enable_install()

    def enable_install(self):
        self.install_button.setEnabled(bool(self.install_folder.text() and self.ref_select.currentText()))

    def open_plugin_folder(self):
        nuke_ver = self.nuke_version_select.currentText()
        base_path = os.path.join(
            os.path.expanduser("~/.nuke"),
            "VFX Pipeline Tools",
            #f"Nuke{nuke_ver}"
        )
    
        # Create folder if it does not exist
        if not os.path.exists(base_path):
            os.makedirs(base_path)
    
        system = platform.system()
        if system == "Windows":
            os.startfile(base_path)
        elif system == "Darwin":
            subprocess.Popen(["open", base_path])
        else:
            subprocess.Popen(["xdg-open", base_path])



        # Ask to restart
    def restart_nuke(self):
        if not nuke.ask("Restart Nuke now?"):
            return

        # Current script
        script_path = nuke.root().name()
        reopen_script = script_path and script_path != "Root"

        system = platform.system()

        # Detect NukeX safely (works for all versions)
        is_nukex = bool(nuke.env.get("nukex"))

        # Detect executable path (ALL versions)
        exe_path = nuke.env.get("ExecutablePath")

        if system == "Windows":
            if not exe_path or not os.path.exists(exe_path):
                nuke.message("Cannot determine Nuke executable path.")
                return

            cmd = [exe_path]

            # NukeX flag (only when needed)
            if is_nukex:
                cmd.append("--nukex")

            if reopen_script:
                cmd.append(script_path)

            subprocess.Popen(cmd, shell=False)

        elif system == "Darwin":  # macOS
            app_name = "NukeX" if is_nukex else "Nuke"
            cmd = ["open", "-a", app_name]

            if reopen_script:
                cmd.append(script_path)

            subprocess.Popen(cmd)
        else:  # Linux
                    # Instead of just "nukex", use the full path provided by Nuke
                    if exe_path and os.path.exists(exe_path):
                        cmd = [exe_path]
                    else:
                        # Fallback to common naming if exe_path is missing
                        cmd = ["nukex" if is_nukex else "nuke"]

                    if is_nukex and "--nukex" not in cmd:
                        cmd.append("--nukex")

                    if reopen_script:
                        cmd.append(script_path)

                    subprocess.Popen(cmd)











            

    def install(self):
        if not ensure_git(self):
            return

        ref = self.ref_select.currentText()
        dest = self.install_folder.text()
        target_version = self.nuke_version_select.currentText()
        restrict_major = self.major_checkbox.isChecked()
        repo_name = Path(self.repo_url.text()).stem if self.repo_url.text() else "plugin"

        def force_remove(path):
            def onerror(func, path, exc_info):
                os.chmod(path, 0o777)
                func(path)
            if os.path.exists(path):
                shutil.rmtree(path, onerror=onerror)

        if os.path.exists(dest):
            if not nuke.ask(f"Folder exists:\n{dest}\nDelete and reinstall?"):
                return
            force_remove(dest)

        clone_repo(self.repo_url.text().strip(), dest, ref)
        register_nuke_plugin_path(dest, target_version, restrict_major)

        # QMessageBox.information(self, "Success", f"{repo_name} installed successfully!\nRestart Nuke to load the plugin.")
        msg = QMessageBox(self)
        msg.setWindowTitle("Success")
        msg.setIcon(QMessageBox.Information)

        hex_color = "#008000"

        msg.setTextFormat(Qt.RichText)
        msg.setText(
            f'<span style="color:{hex_color}; font-size:23px; font-weight: bold; ">'
            f'  {repo_name} installed successfully!<br>'
            f'  Restart Nuke to load the plugin.'
            f'</span>'
        )

        msg.exec_()
        self.restart_nuke()





        Play_Render_Sound()
        self.status_label.setText("Done!")
        self.install_button.setEnabled(False)
        self.restart_button.setEnabled(True)
        
    #import webbrowser  # Add at the top with other imports
    
    def check_for_updates(self):
        import json
        import urllib.request
        import zipfile
        import tempfile
    
        HEADERS = {"User-Agent": "Nuke-Installer"}
    
        def fetch_json(url):
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=5) as r:
                return json.loads(r.read().decode())
    
        try:
            latest_version = None
            zip_url = None
    
            # --------------------------------------------------
            # 1. Try GitHub Releases (includes pre-releases)
            # --------------------------------------------------
            try:
                releases = fetch_json(
                    f"https://api.github.com/repos/"
                    f"{INSTALLER_GITHUB_USER}/{INSTALLER_GITHUB_REPO}/releases"
                )
    
                if releases:
                    release = releases[0]  # newest (may be prerelease)
                    latest_version = release["tag_name"].lstrip("v")
                    zip_url = release["zipball_url"]
    
            except Exception:
                pass
    
            # --------------------------------------------------
            # 2. Fallback to Tags
            # --------------------------------------------------
            if not latest_version:
                tags = fetch_json(
                    f"https://api.github.com/repos/"
                    f"{INSTALLER_GITHUB_USER}/{INSTALLER_GITHUB_REPO}/tags"
                )
    
                if not tags:
                    raise RuntimeError("No releases or tags found")
    
                tag_name = tags[0]["name"]
                latest_version = tag_name.lstrip("v")
                zip_url = (
                    f"https://github.com/{INSTALLER_GITHUB_USER}/"
                    f"{INSTALLER_GITHUB_REPO}/archive/refs/tags/{tag_name}.zip"
                )
    
            # --------------------------------------------------
            # 3. Version check
            # --------------------------------------------------
            if latest_version == INSTALLER_VERSION:
                QMessageBox.information(
                    self,
                    "Up to Date",
                    f"You are using the latest version ({INSTALLER_VERSION})."
                )
                return
    
            # --------------------------------------------------
            # 4. Confirm update
            # --------------------------------------------------
            reply = QMessageBox.question(
                self,
                "Update Available",
                f"Installed version: {INSTALLER_VERSION}\n"
                f"Latest version: {latest_version}\n\n"
                f"Do you want to update now?",
                QMessageBox.Yes | QMessageBox.No
            )
    
            if reply != QMessageBox.Yes:
                return
    
            # --------------------------------------------------
            # 5. Download update
            # --------------------------------------------------
            temp_dir = tempfile.mkdtemp()
            zip_path = os.path.join(temp_dir, "update.zip")
            urllib.request.urlretrieve(zip_url, zip_path)
    
            # --------------------------------------------------
            # 6. Extract update
            # --------------------------------------------------
            with zipfile.ZipFile(zip_path, "r") as z:
                z.extractall(temp_dir)
    
            extracted_root = next(
                os.path.join(temp_dir, d)
                for d in os.listdir(temp_dir)
                if os.path.isdir(os.path.join(temp_dir, d))
            )
    
            # --------------------------------------------------
            # 7. Install to default installer directory
            # --------------------------------------------------
            installer_dir = Path(
                os.path.expanduser("~/.nuke/PipelineCore_nuke_installer")
            )
            installer_dir.mkdir(parents=True, exist_ok=True)
    
            for item in os.listdir(extracted_root):
                src = os.path.join(extracted_root, item)
                dst = installer_dir / item
    
                if dst.exists():
                    if dst.is_dir():
                        shutil.rmtree(dst)
                    else:
                        dst.unlink()
    
                if os.path.isdir(src):
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)
    
            QMessageBox.information(
                self,
                "Update Complete",
                "The installer has been updated successfully.\n\n"
                "Please restart Nuke to apply the update."
            )
    
            webbrowser.open(installer_dir.as_posix())
    
        except Exception as e:
            QMessageBox.warning(
                self,
                "Update Failed",
                f"{e}\n\nOpening GitHub repository."
            )
            webbrowser.open(INSTALLER_GITHUB_URL)

# ----------------- Launch -----------------
def show_installer():
    dlg = GithubNukeInstaller()
    dlg.setWindowModality(Qt.ApplicationModal)
    dlg.exec_() #if PYSIDE_VERSION == 2 else dlg.exec()

#show_installer()











