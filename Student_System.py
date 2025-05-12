# Define a class to manage student data
class StudentSystem:
    
    def __init__(self):
        # Initialize an empty dictionary to store student data
        self.students = {}

    # Method to add student entries and allow searching
    def add_student_name(self):
        # Ask user how many student entries to add
        n = int(input("Enter the number of student entries: "))

        # Loop to gather student details
        for _ in range(n):
            name = input("Enter student name: ")
            roll_number = input("Enter student roll number: ")
            self.students[roll_number] = name  # Store in dictionary

        # Print the stored student data
        print("\nAll Students Data:")
        for roll, name in self.students.items():
            print(f"Roll No: {roll}  |  Name: {name}")

        # Ask user which student they want to search
        search_rollnumber = input("\nEnter a roll number to search for: ")

        # Check and display the searched student's info
        if search_rollnumber in self.students:
            print("\nStudent Found:")
            print(f"Roll Number: {search_rollnumber}")
            print(f"Name: {self.students[search_rollnumber]}")
        else:
            print("\nStudent not found.")


# Create an instance of the StudentSystem class
system = StudentSystem()

# Call the method to add and search for students
system.add_student_name()
