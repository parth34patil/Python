import sys  # Importing sys module

# Displaying welcome messages
print("Welcome to this code")
print("Welcome to the Google create account")

# Function to select the email provider
def select_option():
    # Display options
    print("1 = gmail.com")
    print("2 = yahoo.com")
    print("3 = outlook.com")

    # Ask for user input
    choose = int(input("Enter the number = "))
    
    # Call the corresponding function
    if choose == 1:
        first_option()
    elif choose == 2:
        second_option()
    elif choose == 3:
        third_option()
    else:
        exit()  # Exit if invalid input

# Gmail registration
def first_option():
    try:
        # Name input and validation
        while True:
            name = input("Enter your name: ")
            if not name.isalpha():
                print("Name should only contain letters. Please try again.")
            else:
                break

        # Email input and validation
        while True:
            email_id = input("Enter your email ID: ")
            if "@" not in email_id:
                print("Please check your email. It should contain '@'.")
            elif "gmail.com" not in email_id:
                print("Please check your email. It should contain 'gmail.com'.")
            else:
                break

        # Age input and validation
        while True:
            age = input("Enter your age: ")
            if not age.isdigit():
                print("Age should only contain numbers. Please try again.")
            else:
                break

        # Write data to file
        with open("data.txt", "w") as file:
            file.write(f"Name: {name},\nAge: {age},\nEmail ID: {email_id}\n")
            print("\nData written to file successfully.")

    except ValueError as e:
        print(f"\nError: {e}")

    except SyntaxError:
        print("This is a syntax error. Please check your code.")

# Yahoo registration
def second_option():
    try:
        while True:
            name = input("Enter your name: ")
            if not name.isalpha():
                print("Name should only contain letters. Please try again.")
            else:
                break

        while True:
            email_id = input("Enter your email ID: ")
            if "@" not in email_id:
                print("Please check your email. It should contain '@'.")
            elif "yahoo.com" not in email_id:
                print("Please check your email. It should contain 'yahoo.com'.")
            else:
                break

        while True:
            age = input("Enter your age: ")
            if not age.isdigit():
                print("Age should only contain numbers. Please try again.")
            else:
                break

        with open("data.txt", "w") as file:
            file.write(f"Name: {name},\nAge: {age},\nEmail ID: {email_id}\n")
            print("\nData written to file successfully.")

    except ValueError as e:
        print(f"\nError: {e}")

    except SyntaxError:
        print("This is a syntax error. Please check your code.")

# Outlook registration
def third_option():
    try:
        while True:
            name = input("Enter your name: ")
            if not name.isalpha():
                print("Name should only contain letters. Please try again.")
            else:
                break

        while True:
            email_id = input("Enter your email ID: ")
            if "@" not in email_id:
                print("Please check your email. It should contain '@'.")
            elif "outlook.com" not in email_id:
                print("Please check your email. It should contain 'outlook.com'.")
            else:
                break

        while True:
            age = input("Enter your age: ")
            if not age.isdigit():
                print("Age should only contain numbers. Please try again.")
            else:
                break

        with open("data.txt", "w") as file:
            file.write(f"Name: {name},\nAge: {age},\nEmail ID: {email_id}\n")
            print("\nData written to file successfully.")

    except ValueError as e:
        print(f"\nError: {e}")

    except SyntaxError:
        print("This is a syntax error. Please check your code.")

# Run the program
select_option()
