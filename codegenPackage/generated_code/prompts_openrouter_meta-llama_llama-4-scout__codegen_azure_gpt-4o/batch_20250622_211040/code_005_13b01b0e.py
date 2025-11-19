"""
Generated Code Metadata:
========================
Original URL: https://ultiuos.com
Prompt: Develop a manpower management system for a telecommunication company using a suitable programming language, incorporating features from ULTIUOS's manpower management services.
Generated: DETERMINISTIC_13b01b0e8a4cc654
Batch ID: 20250622_211040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Manpower Management System for a Telecommunication Company
Language: Python
Features: Incorporates ULTIUOS's manpower management services
"""

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "manpower_management.db"

def initialize_database():
    """
    Initialize the database and create necessary tables.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create employees table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            department TEXT NOT NULL,
            contact TEXT NOT NULL,
            date_joined TEXT NOT NULL
        )
        """)
        
        # Create tasks table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            task_description TEXT NOT NULL,
            deadline TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending',
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_employee(name, role, department, contact):
    """
    Add a new employee to the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        date_joined = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("""
        INSERT INTO employees (name, role, department, contact, date_joined)
        VALUES (?, ?, ?, ?, ?)
        """, (name, role, department, contact, date_joined))
        
        conn.commit()
        print("Employee added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding employee: {e}")
    finally:
        conn.close()

def assign_task(employee_id, task_description, deadline):
    """
    Assign a task to an employee.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO tasks (employee_id, task_description, deadline)
        VALUES (?, ?, ?)
        """, (employee_id, task_description, deadline))
        
        conn.commit()
        print("Task assigned successfully.")
    except sqlite3.Error as e:
        print(f"Error assigning task: {e}")
    finally:
        conn.close()

def update_task_status(task_id, status):
    """
    Update the status of a task.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        UPDATE tasks
        SET status = ?
        WHERE id = ?
        """, (status, task_id))
        
        conn.commit()
        print("Task status updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating task status: {e}")
    finally:
        conn.close()

def view_employees():
    """
    View all employees in the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        
        print("Employees:")
        for emp in employees:
            print(emp)
    except sqlite3.Error as e:
        print(f"Error viewing employees: {e}")
    finally:
        conn.close()

def view_tasks():
    """
    View all tasks in the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        
        print("Tasks:")
        for task in tasks:
            print(task)
    except sqlite3.Error as e:
        print(f"Error viewing tasks: {e}")
    finally:
        conn.close()

# Main program
if __name__ == "__main__":
    initialize_database()
    
    # Example usage
    add_employee("John Doe", "Technician", "Maintenance", "123-456-7890")
    add_employee("Jane Smith", "Engineer", "Development", "987-654-3210")
    
    assign_task(1, "Fix network outage in Zone A", "2023-10-15")
    assign_task(2, "Develop new software module", "2023-10-20")
    
    update_task_status(1, "Completed")
    
    view_employees()
    view_tasks()
```
