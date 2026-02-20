
# Pipeline-Tools-nuke_installer
HI im Nitin Kashyap   VFX Compositor


![Nuke](https://img.shields.io/badge/Nuke-Compatible-Green)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![GPL--3.0](https://img.shields.io/badge/GPL--3.0-red?style=for-the-badge)





<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=C++,py,qt," />
  </a>
</p>





<h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&center=true&vCenter=true&width=500&height=70&duration=5000&lines=Hi+There!+👋;+I'm+Nitin+Kashyap;" />
</h1>




# add Restart_Nuke Button

# Installation   :


    git clone https://github.com/Nitinkashyap96/Pipeline-Tools-nuke_installer.git

(( The plugin installer you are using is an intermediate-to-advanced-level VFX tool. Here's why: ))

Installation

    nuke.pluginAddPath(r"./PipelineCore_nuke_installer")
What the installer does (Overview)

Your installer is a pipeline utility that allows artists or TDs to:

Install Nuke plugins directly from GitHub

Select Branch or Release (Tag)

Install plugins into version-specific Nuke folders

Automatically register plugin paths in init.py

Open plugin folders in file explorer

Update the installer from GitHub



#################################################################################

    Platform       : Windows / Linux / macOS
    
    Python : 3.10
    
    Python : 3.11
                                            
    Tested on with Nuke (12+ / 13+ / 14+ / 15+ / 16+ )
#################################################################################

# Step Paste GitHub repository URL
Example:
  
    https://github.com/username/repository.git
# Internal behavior
  
      Validates .git URL
      
      Enables version fetching
      
      Step Select download type
      
      User selects:
      
      Branch → main, dev, etc.
      
      Release → GitHub tags (v1.0, v2.1)
      
      Code logic
      
      Step Select repository version
      
      Dropdown is populated with:
      
      Branch names or
      
      Tag names
      
      The Install button becomes enabled once:
      
      A valid version is selected
      
      Install path is valid
      
      3. Nuke version handling
      
      The installer reads the running Nuke version:
      
      nuke.NUKE_VERSION_MAJOR
      nuke.NUKE_VERSION_MINOR

#####################################################################################

 # Folder structure created automatically
  # Example:
  
        Nuke 15.1
        Folder structure created automatically
        
        Plugins are installed per-version to avoid conflicts:
        
        ~/.nuke/
         └── VFX Pipeline Tools/
             └── Nuke15.1/
                 └── PluginName/
        This allows:
        
        Multiple Nuke versions on the same machine
        
        Clean pipeline isolation
        
        Default install path logic
        
        If the user does not override the folder:
        
        ~/.nuke/VFX Pipeline Tools/Nuke{version}/{repo_name}
        Example:
        
        ~/.nuke/VFX Pipeline Tools/Nuke15.1/Stamps
        7. Register plugin path in Nuke
        
        The installer updates:
        
        ~/.nuke/init.py
        Major-restricted install
        
        if nuke.NUKE_VERSION_MAJOR == 15:
            nuke.pluginAddPath("path")
        Global install
        
        nuke.pluginAddPath("path")
        This ensures the plugin loads automatically when Nuke starts.


#####################################################################################



<img width="851" height="523" alt="Screenshot 2025-12-31 011546" src="https://github.com/user-attachments/assets/5749f798-aa05-4b85-87ac-4c60aba1559d" />

<img width="477" height="366" alt="Screenshot 2025-12-31 011656" src="https://github.com/user-attachments/assets/5e45df45-ba7a-4e0d-8598-b567e860d3d6" />

<img width="407" height="290" alt="Screenshot 2025-12-31 011722" src="https://github.com/user-attachments/assets/34e8f48f-ab96-4b2a-b5b1-a7bfb4e00e68" />

<img width="856" height="524" alt="Screenshot 2025-12-31 011803" src="https://github.com/user-attachments/assets/a513d4bf-bdc7-4f09-837d-ef90bc7ccd46" />

<img width="854" height="279" alt="Screenshot 2025-12-31 011859" src="https://github.com/user-attachments/assets/e94a1f4e-1e8c-4a73-9a07-6f08ac5a4f74" />

<img width="865" height="711" alt="Screenshot 2025-12-31 011939" src="https://github.com/user-attachments/assets/03f6a878-1060-446e-aec6-b6f3ab7b40cb" />

<img width="860" height="222" alt="Screenshot 2025-12-31 012003" src="https://github.com/user-attachments/assets/9300c322-60cb-4732-b3b3-50e6f5af0ddb" />

<img width="866" height="534" alt="Screenshot 2025-12-31 012028" src="https://github.com/user-attachments/assets/48bf0b6d-2ca8-4ea0-a9a4-f02e45866fb2" />

<img width="859" height="1040" alt="Screenshot 2025-12-31 012153" src="https://github.com/user-attachments/assets/508e89a2-ccf2-4c79-866d-b30b20500bc5" />

<img width="865" height="1022" alt="Screenshot 2025-12-31 012321" src="https://github.com/user-attachments/assets/12bfb2f0-7ca0-4f5a-9c43-6407333a66f1" />

<img width="855" height="759" alt="Screenshot 2025-12-31 012443" src="https://github.com/user-attachments/assets/c37c0bdc-0511-4893-92f5-121a2845aeab" />

<img width="908" height="787" alt="Screenshot 2025-12-31 012830" src="https://github.com/user-attachments/assets/358c69c2-e626-4b5f-9f8e-1003cae3f9e8" />

<img width="936" height="892" alt="Screenshot 2025-12-31 013042" src="https://github.com/user-attachments/assets/78947ba3-abe9-4213-9fb7-eb7ce0996fb2" />



  
# Nuke init.py Automatic path add
