import nuke
import os
import datetime


version= "v2.0.0"
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
import PipelineCore_nuke_installer_2  # Use the filename of your finalized installer

# 2. Add a menu item in a custom menu:
toolbar = nuke.menu("Nuke")  # Top-level
github_menu = toolbar.addMenu("GitHub Tools", icon="GitHub.png.png")

# 3. Add a command that opens the installer dialog
github_menu.addCommand(
    "Install GitHub Repo...",  # Menu command name
    "PipelineCore_nuke_installer_2.show_installer()",  # Function to call
    icon="GitHub_Logo_W.png"
)

# Optionally, add author info/help:
github_menu.addCommand(
    "About Installer",
    "nuke.message('<div style=\"color:#00FF00; font-weight:bold; font-size:35px; text-align:center;\">Created by: Nitin Kashyap<br>PipelineCore_nuke_installer for Nuke</div>')",
)






license ="Copyright (C) 2025 by Nitin Kashyap,All rights reserved."
nuke.tprint(f"PipelineCore_nuke_installer_2 {version},  build  {update_date}. \n{license}")



