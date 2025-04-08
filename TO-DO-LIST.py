def todolist():

    try:
        task_list = int(input("Enter the number of tasks you want to add: "))

        for i in range(task_list):
            with open("TO-DO.txt","a") as f:
                task_name = input("Enter the task name: ")
                f.write(task_name + "\n")
            print("Task added successfully!")

    except ValueError:
        print("invalid input. please add a number how many task you want to add")


def viewtodolist():

    with open("TO-DO.txt","r") as f:
        print(f.read())


def  delete_task():
    with open("TO-DO.txt","w") as f:
        task_name = input("delete = ")
        f.write(task_name + "\n")
        print("Task deleted successfully!")


while True:
    print("""
    ==== TO-DO LIST ====
    1. Add Task
    2. View Tasks
    3. Mark Task as Done
    4. Delete Task
    5. Exit
    """)

    choice = int(input("Enter your choice: "))
    if choice == 1:
        todolist()
    if choice == 2:
        viewtodolist()
    if choice == 5:
        print("Exiting...")
        exit()
    if choice == 4:
        delete_task()

        