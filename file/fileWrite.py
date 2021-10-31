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
     lines = open(file_name,"+r");
     # for line in lines:
     #
     #      print(line.rstrip())
     lines.write("Tester, L001752, Big data analyst");
     lines.seek(0)
     all_file_contents = lines.read();
     print(all_file_contents)
     lines.close();

if __name__ == '__main__':

     file_processing("sample.txt")

