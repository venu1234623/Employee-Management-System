import sqlite3

# Connect to database
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")
conn.commit()

# Add Employee
def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    cursor.execute(
        "INSERT INTO employees VALUES (?, ?, ?, ?)",
        (emp_id, name, department, salary)
    )
    conn.commit()
    print("Employee added successfully!")

# View Employees
def view_employees():
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()

    if not records:
        print("No employees found.")
    else:
        print("\nEmployee Records:")
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1]}, Department: {row[2]}, Salary: {row[3]}")

# Update Employee
def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))
    new_salary = float(input("Enter New Salary: "))

    cursor.execute(
        "UPDATE employees SET salary = ? WHERE emp_id = ?",
        (new_salary, emp_id)
    )
    conn.commit()
    print("Employee updated successfully!")

# Delete Employee
def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))

    cursor.execute(
        "DELETE FROM employees WHERE emp_id = ?",
        (emp_id,)
    )
    conn.commit()
    print("Employee deleted successfully!")

# Main Menu
while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

conn.close()
