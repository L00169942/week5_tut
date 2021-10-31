"""
# ----------------------
# Created : 31-10-2021 08:35
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""
import zipfile, os
def zip_file_processing():
    """
    zip file demo
    :return:
    """
    os.chdir(os.path.normpath("C:\\Users\\id\\PycharmProjects\\week5\\file\\zipDemo"))
    newZip = zipfile.ZipFile('myNew.zip', 'a') # create a zip file. can be r,w,aread/write/append
    newZip.write('C:\\Users\\id\\PycharmProjects\\week5\\file\\sample.txt') # add a file to the same zip file
    print("{}".format(newZip.printdir())) # show contents of the file
    # newZip.write("RubbishFile.txt") # add a second file
    print("\nFiles in the zip are: {}\n".format("C:\\Users\\id\\PycharmProjects\\week5\\file\\zipDemo\\xtracthere"))
    newZip.extractall("C:\\Users\\id\\PycharmProjects\\week5\\file\\zipDemo\\extracthere")
    newZip.close()

if __name__ == '__main__':
    zip_file_processing()
