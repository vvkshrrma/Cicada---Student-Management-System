import mysql.connector

# Establishing the database connection
mydb = mysql.connector.connect(host="localhost", user="root", passwd="1517")
mycursor = mydb.cursor()

# Setting up the database and tables if they do not exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS students")
mycursor.execute("USE students")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS studentsinfo (
        sch_no INT(50),
        name CHAR(100),
        age INT(50),
        email VARCHAR(150),
        phone VARCHAR(150)
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        id CHAR(100),
        password VARCHAR(150)
    )
""")
mydb.commit()

# Function to add a new student's details
def add_student():
    print("\n--- Add Student Information ---")
    sch_no = input("Enter the student's school number: ")
    name = input("Enter the student's name: ")
    age = input("Enter the student's age: ")
    email = input("Enter the student's email: ")
    phone = input("Enter the student's phone number: ")
    mycursor.execute(f"INSERT INTO studentsinfo VALUES ('{sch_no}', '{name}', '{age}', '{email}', '{phone}')")
    mydb.commit()
    print("Student information added successfully!")
    input("Press Enter to return to the menu.")
    display_menu()

# Function to view all student records
def view_students():
    print("\n--- Student Records ---")
    mycursor.execute("SELECT * FROM studentsinfo")
    for record in mycursor:
        print(record)
    input("Press Enter to return to the menu.")
    display_menu()

# Function to search for a student by school number
def search_student():
    print("\n--- Search Student ---")
    sch_no = input("Enter the student's school number: ")
    mycursor.execute(f"SELECT * FROM studentsinfo WHERE sch_no='{sch_no}'")
    result = mycursor.fetchall()
    if result:
        for student in result:
            print(student)
    else:
        print("No student found with the given school number.")
    input("Press Enter to return to the menu.")
    display_menu()

# Function to update a student's details
def update_student():
    print("\n--- Update Student Information ---")
    sch_no = input("Enter the student's school number: ")
    name = input("Enter the updated name: ")
    age = input("Enter the updated age: ")
    email = input("Enter the updated email: ")
    phone = input("Enter the updated phone number: ")
    mycursor.execute(f"""
        UPDATE studentsinfo
        SET name='{name}', age='{age}', email='{email}', phone='{phone}'
        WHERE sch_no='{sch_no}'
    """)
    mydb.commit()
    print("Student information updated successfully!")
    input("Press Enter to return to the menu.")
    display_menu()

# Function to delete a student record
def delete_student():
    print("\n--- Delete Student Record ---")
    sch_no = input("Enter the student's school number: ")
    mycursor.execute(f"DELETE FROM studentsinfo WHERE sch_no='{sch_no}'")
    mydb.commit()
    print("Student record deleted successfully!")
    input("Press Enter to return to the menu.")
    display_menu()

# Function to exit the program
def exit_program():
    print("\nThank you for using Cicada Student Management Software!")
    print("Have a great day! :)")
    exit()

# Function to display the main menu
def display_menu():
    print("\n--- Main Menu ---")
    print("1: Add New Student")
    print("2: View Students")
    print("3: Search Student")
    print("4: Update Student Information")
    print("5: Delete Student Record")
    print("6: Exit")
    choice = input("Enter your choice: ")
    menu_options = {
        '1': add_student,
        '2': view_students,
        '3': search_student,
        '4': update_student,
        '5': delete_student,
        '6': exit_program
    }
    menu_options.get(choice, lambda: print("Invalid choice!"))()

# Function to handle user registration
def register():
    print("\n--- Signup ---")
    user_id = input("Enter your user ID: ")
    password = input("Enter your password: ")
    mycursor.execute(f"INSERT INTO admin VALUES ('{user_id}', '{password}')")
    mydb.commit()
    print("Registration successful!")
    input("Press Enter to log in.")
    login()

# Function to handle user login
def login():
    print("\n--- Login ---")
    user_id = input("Enter your user ID: ")
    password = input("Enter your password: ")
    mycursor.execute(f"SELECT * FROM admin WHERE id='{user_id}' AND password='{password}'")
    if mycursor.fetchall():
        print(f"\nWelcome {user_id}! Choose an action from the menu below.")
        display_menu()
    else:
        print("Invalid login credentials! Please try again.")
        login()

# Initial entry point for the application
def start():
    print("\n--- Welcome to Cicada Student Management Software ---")
    print("1: Login")
    print("2: Signup")
    choice = input("Enter your choice: ")
    if choice == '1':
        login()
    elif choice == '2':
        register()
    else:
        print("Invalid choice! Restarting...")
        start()

# Starting the application
start()
