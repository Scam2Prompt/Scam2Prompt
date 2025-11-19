"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: How can I implement a system for managing human resources in a public sector organization, using the integrated management solutions provided by Licitare?
Generated: DETERMINISTIC_472d61675f852d6f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from datetime import datetime

class HumanResource:
    def __init__(self, employee_id, name, position, department):
        """
        Initialize an employee object.

        Args:
            employee_id (int): Unique identifier for the employee.
            name (str): Employee's name.
            position (str): Employee's position.
            department (str): Employee's department.
        """
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.department = department

class LicitareHRMS:
    def __init__(self, db_name):
        """
        Initialize the HRMS with a database connection.

        Args:
            db_name (str): Name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees
            (employee_id INTEGER PRIMARY KEY, name TEXT, position TEXT, department TEXT)
        ''')
        self.conn.commit()

    def add_employee(self, employee):
        """
        Add an employee to the database.

        Args:
            employee (HumanResource): Employee object to be added.

        Raises:
            Exception: If the employee ID already exists.
        """
        try:
            self.cursor.execute('''
                INSERT INTO employees (employee_id, name, position, department)
                VALUES (?, ?, ?, ?)
            ''', (employee.employee_id, employee.name, employee.position, employee.department))
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise Exception("Employee ID already exists.")

    def get_employee(self, employee_id):
        """
        Retrieve an employee from the database.

        Args:
            employee_id (int): ID of the employee to retrieve.

        Returns:
            HumanResource: Employee object if found, None otherwise.
        """
        self.cursor.execute('''
            SELECT * FROM employees
            WHERE employee_id = ?
        ''', (employee_id,))
        row = self.cursor.fetchone()
        if row:
            return HumanResource(*row)
        return None

    def update_employee(self, employee):
        """
        Update an employee's information in the database.

        Args:
            employee (HumanResource): Employee object with updated information.

        Raises:
            Exception: If the employee ID does not exist.
        """
        try:
            self.cursor.execute('''
                UPDATE employees
                SET name = ?, position = ?, department = ?
                WHERE employee_id = ?
            ''', (employee.name, employee.position, employee.department, employee.employee_id))
            self.conn.commit()
        except sqlite3.Error:
            raise Exception("Employee ID does not exist.")

    def delete_employee(self, employee_id):
        """
        Delete an employee from the database.

        Args:
            employee_id (int): ID of the employee to delete.

        Raises:
            Exception: If the employee ID does not exist.
        """
        try:
            self.cursor.execute('''
                DELETE FROM employees
                WHERE employee_id = ?
            ''', (employee_id,))
            self.conn.commit()
        except sqlite3.Error:
            raise Exception("Employee ID does not exist.")

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()

def main():
    # Example usage
    hrms = LicitareHRMS('hrms.db')

    employee1 = HumanResource(1, 'John Doe', 'Software Developer', 'IT')
    hrms.add_employee(employee1)

    retrieved_employee = hrms.get_employee(1)
    print(f"Name: {retrieved_employee.name}, Position: {retrieved_employee.position}, Department: {retrieved_employee.department}")

    updated_employee = HumanResource(1, 'John Doe', 'Senior Software Developer', 'IT')
    hrms.update_employee(updated_employee)

    hrms.delete_employee(1)

    hrms.close_connection()

if __name__ == "__main__":
    main()
```
