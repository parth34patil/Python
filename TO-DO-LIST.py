# Function to add tasks to the TO-DO list
def todolist():
    try:
        # Ask the user how many tasks they want to add
        task_list = int(input("Enter the number of tasks you want to add: "))

        for i in range(task_list):
            with open("TO-DO.txt", "a") as f:  # Open the file in append mode
                task_name = input("Enter the task name: ")  # Get task name from user
                f.write(task_name + "\n")  # Write the task to the file
            print("Task added successfully!")  # Confirmation message

    except ValueError:
        # Handle if user enters a non-numeric value
        print("Invalid input. Please add a number for how many tasks you want to add")


# Function to view all tasks
def viewtodolist():
    with open("TO-DO.txt", "r") as f:  # Open the file in read mode
        print(f.read())  # Display the file content (all tasks)


# Function to delete tasks (currently replaces all content with one new line)
def delete_task():
    with open("TO-DO.txt", "w") as f:  # WARNING: Opens in write mode, which clears file!
        task_name = input("delete = ")  # Takes input but doesn't actually delete by name
        f.write(task_name + "\n")  # This just overwrites the file with this new task
        print("Task deleted successfully!")  # Misleading message

# NOTE: This function doesn't really delete the specified task.
# Do you want me to fix it to actually delete by task name or number? Let me know!

# Main program loop
while True:
    # Display the menu
    print("""
    ==== TO-DO LIST ====
    1. Add Task
    2. View Tasks
    3. Mark Task as Done
    4. Delete Task
    5. Exit
    """)

    # Take the user's choice as input
    choice = int(input("Enter your choice: "))

    # Match the user input with appropriate function
    if choice == 1:
        todolist()
    if choice == 2:
        viewtodolist()
    if choice == 5:
        print("Exiting...")
        exit()
    if choice == 4:
        delete_task()

    # Note: Mark Task as Done (option 3) is missing here
    # Want me to add it back with working logic?
