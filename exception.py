try:
   enter_file_name = input("Enter file name = ")
   with open(enter_file_name,"r") as file:
       print(file.read())

except FileNotFoundError:
    print("this file is not availabel")


