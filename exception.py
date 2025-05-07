# Try block to catch any exceptions that might occur
try:
    # Ask the user to enter the name of the file
    enter_file_name = input("Enter file name = ")

    # Open the file in read mode and assign it to 'file' using 'with' (auto-closes file)
    with open(enter_file_name, "r") as file:
        # Read and print the contents of the file
        print(file.read())

# Handle the case where the file doesn't exist
except FileNotFoundError:
    print("This file is not available")
