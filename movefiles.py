#import OS & Shutil
import os
import shutil

#Create two variables from_dir and to_dir to store source path and destination path, respectively
from_dir="C;/users/admin/downloads"
to_dir="c:/whjr"
#Create a variable, list_of_files , to store the names of all the files from the source path using os.listdir().
#As given in specific task 4
list_of_files= os.listdir(list_dir)
print(list_of_files)
#Create a for-in loop to traverse through the list_of_files
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #Write an if condition to check if the extension is blank, if the condition is true then continue
    if extension == '':
        continue
    #Create 3 variables for the name of the directory paths
    if extension in ['.txt', '.pdf', '.doc', '.docx']:

        path1 = from_dir + '/' + file_name                       # Example path1 : Downloads/ImageName1.jpg        
        path2 = to_dir + '/' + "Document_Files"                     # Example path2 : D:/My Files/Image_Files      
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name   # Example path3 : D:/My Files/Image_Files/ImageName1.jpg

#Check if the folder/directory path exists before moving using an if condition Else make a new folder/directory then move: (See Hint 1)
if os.path.exists(path2):
    print("Moving"+ file_name + "......")
    shutil.move(path1,path3)
else:
    os.markedirs(path2)
    print("Moving"+file_name+"......")
    shutil.move(path1,path3)
