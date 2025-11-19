"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: "Write a code snippet for creating a simple database for managing human resources, based on the Recursos Humanos program at ISIV."
Generated: DETERMINISTIC_e8e3cbc3dcc804a3
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

class HRDatabase:
    """A class to manage a simple Human Resources database using SQLite."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for storing employee information."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            position TEXT NOT NULL,
            salary REAL NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Employees table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_employee(self, first_name, last_name, email, position, salary):
        """Add a new employee to the database."""
        insert_sql = """
        INSERT INTO employees (first_name, last_name, email, position, salary)
        VALUES (?, ?, ?, ?, ?);"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (first_name, last_name, email, position, salary))
            self.connection.commit()
            print(f"Employee {first_name} {last_name} added successfully.")
        except Error as e:
            print(f"Error adding employee: {e}")

    def fetch_all_employees(self):
        """Fetch all employees from the database."""
        select_sql = "SELECT * FROM employees;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_sql)
            employees = cursor.fetchall()
            return employees
        except Error as e:
            print(f"Error fetching employees: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    db = HRDatabase("hr_database.db")
    db.create_table()
    db.add_employee("John", "Doe", "john.doe@example.com", "Software Engineer", 70000)
    db.add_employee("Jane", "Smith", "jane.smith@example.com", "Project Manager", 80000)

    employees = db.fetch_all_employees()
    for emp in employees:
        print(emp)

    db.close_connection()
```
