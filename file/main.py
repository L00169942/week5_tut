"""
# ----------------------
# Created : 20-10-2021 16:37
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""
def file_processing(file_name):
     """
     Open an external file and read the name, number
     :param file_name:
     :return: null
     """
     lines = open(file_name).readlines()
     for line in lines:
          student,l_num,course = line.split(',')
          print("Student Name:{0} \nLnumber: \t{1} \t\t{2}\n".format(student,l_num,course))
          # print(line)


if __name__ == '__main__':

     file_processing("sample.txt")

