#File Organiser
#PhumuDev
#31 July 2023

import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
d_images_path = os.path.join(os.path.expanduser("~"), "Downloads/Images")
d_videos_path = os.path.join(os.path.expanduser("~"), "Downloads/Videos")
d_docs_path = os.path.join(os.path.expanduser("~"), "Downloads/Docs")
d_other_path = os.path.join(os.path.expanduser("~"), "Downloads/Other")

#region Create Folders

#Check if folders for categories exist. If not, create new folders.

if os.path.exists(d_images_path):
    pass
else:
    os.mkdir(d_images_path)

if os.path.exists(d_videos_path):
    pass
else:
    os.mkdir(d_videos_path)

if os.path.exists(d_docs_path):
    pass
else:
    os.mkdir(d_docs_path)

if os.path.exists(d_other_path):
    pass
else:
    os.mkdir(d_other_path)

#endregion

#region Move Files
for directory, subdir_list, file_list in os.walk(downloads_path): #Loop through directory
    
    #Loop through files in directory
    for name in file_list: 
        file_path = os.path.join(directory, name)

        if ".jpg" in name or ".png" in name or ".jpeg" in name:     
           if os.path.exists(os.path.join(d_images_path,name)): #check if filename exists in the destination
               pass 
           else:    
                shutil.move(file_path, d_images_path) 


        elif ".mov" in name or ".mp4" in name or ".avi" in name:      
            if os.path.exists(os.path.join(d_videos_path,name)): #check if filename exists in the destination
               pass 
            else:    
                shutil.move(file_path, d_videos_path) 


        elif ".pdf" in name or ".doc" in name or ".pptx" in name or ".xlsx" in name:       
            if os.path.exists(os.path.join(d_docs_path,name)): #check if filename exists in the destination
               pass
            else:    
                shutil.move(file_path, d_docs_path) 


        else:
            if os.path.exists(os.path.join(d_other_path,name)): #check if filename exists in the destination
               pass
            else:    
               shutil.move(file_path, d_other_path)

#endregion