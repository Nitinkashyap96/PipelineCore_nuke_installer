import nuke
import os
import datetime


version= "v1.0"
update_date= "25 December 2025"


########################################
#                                      #
#            Author: Nitin Kashyap     #
#                                      #
########################################

#Created by: Nitin Kashyap
#GitHub Tools Installer for Nuke


nuke.pluginAddPath(r'./icon')



# Place this in your ~/.nuke/menu.py file

# 1. Import your installer module. Adjust import path if necessary.
import PipelineCore_nuke_installer  # Use the filename of your finalized installer

# 2. Add a menu item in a custom menu:
toolbar = nuke.menu("Nuke")  # Top-level
github_menu = toolbar.addMenu("GitHub Tools", icon="GitHub.png.png")

# 3. Add a command that opens the installer dialog
github_menu.addCommand(
    "Install GitHub Repo...",  # Menu command name
    "PipelineCore_nuke_installer.show_installer()",  # Function to call
    icon="GitHub_Logo_W.png"
)

# Optionally, add author info/help:
github_menu.addCommand(
    "About Installer",
    "nuke.message('Created by: Nitin Kashyap\\nPipelineCore_nuke_installer for Nuke')",
)





license ="Copyright (C) 2025 by Niti Kashyap,All rights reserved."
nuke.tprint(f"PipelineCore_nuke_installer {version},  build  {update_date}. \n{license}")