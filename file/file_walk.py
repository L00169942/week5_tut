"""
# ----------------------
# Created : 31-10-2021 08:15
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""
import os
def walk_file_processing():
     for folder_name, sub_folders, file_names in os.walk("C:\\Users\\id\\PycharmProjects"):
          print("Folder: ".format(folder_name))
          for sub_folder in sub_folders:
             print("Folder Name: {0} is a sub-folder in {1}".format(folder_name,sub_folder))

          for file_name in file_names:
             print("{0} is a file inside {1}".format(file_name, folder_name))
          print("\n")


if __name__ == '__main__':
    walk_file_processing()
