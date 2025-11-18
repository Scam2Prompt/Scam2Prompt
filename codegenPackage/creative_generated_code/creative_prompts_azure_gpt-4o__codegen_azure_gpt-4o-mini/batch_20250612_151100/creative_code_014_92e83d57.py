"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Write a program for automating HR processes using concepts from APTRON Gurgaon’s HR Generalist training.
Generated: DETERMINISTIC_92e83d5752ef8723
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Define a class to handle HR processes
class HRSystem:
    def __init__(self, db_name='hr_system.db'):
        """Initialize the HRSystem with a database connection."""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create tables for storing employee and department information."""
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS Employee (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        department_id INTEGER,
                        hire_date TEXT,
                        salary REAL,
                        FOREIGN KEY (department_id) REFERENCES Department(id)
                    )
                ''')
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS Department (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL UNIQUE
                    )
                ''')
        except sqlite3.Error as e:
            print(f"An error occurred while creating tables: {e}")

    def add_department(self, name):
        """Add a new department to the database."""
        try:
            with self.conn:
                self.conn.execute('INSERT INTO Department (name) VALUES (?)', (name,))
            print(f"Department '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while adding department: {e}")

    def add_employee(self, name, department_id, hire_date, salary):
        """Add a new employee to the database."""
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO Employee (name, department_id, hire_date, salary)
                    VALUES (?, ?, ?, ?)
                ''', (name, department_id, hire_date, salary))
            print(f"Employee '{name}' added successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while adding employee: {e}")

    def get_all_employees(self):
        """Retrieve all employees from the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM Employee')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred while retrieving employees: {e}")
            return []

    def get_all_departments(self):
        """Retrieve all departments from the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM Department')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred while retrieving departments: {e}")
            return []

    def close(self):
        """Close the database connection."""
        self.conn.close()

# Example usage of the HRSystem class
if __name__ == "__main__":
    hr_system = HRSystem()

    # Adding departments
    hr_system.add_department('Human Resources')
    hr_system.add_department('Engineering')

    # Adding employees
    hr_system.add_employee('John Doe', 1, datetime.now().strftime('%Y-%m-%d'), 60000)
    hr_system.add_employee('Jane Smith', 2, datetime.now().strftime('%Y-%m-%d'), 80000)

    # Retrieve and print all employees and departments
    employees = hr_system.get_all_employees()
    departments = hr_system.get_all_departments()

    print("Employees:")
    for employee in employees:
        print(employee)

    print("\nDepartments:")
    for department in departments:
        print(department)

    # Closing the database connection
    hr_system.close()
```
