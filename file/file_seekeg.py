"""
# ----------------------
# Created : 31-10-2021 07:47
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""
import os
def file_processing3(file_name):
     fileObj = open(file_name, "r+")
     fileObj.seek(0) # rewind the file - start at position 0
     fileObj.seek(10, 0) # Move 10 bytes forward from the start (0) of file0=SEEK_SET
     fileObj.seek(1, os.SEEK_SET) # move 1 byte forward from the beginning
     fileObj.seek(0, os.SEEK_CUR) # seek the current position, offset must be 0
     fileObj.seek(0, os.SEEK_END) # Reset the current position (SEEK_END) of

     all_file_contents = fileObj.read();
     print(all_file_contents)
     fileObj.close()
if __name__ == '__main__':
    """
     Main method of application
      Demo seek       
    
    """
    file_processing3("sample.txt")
