"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: Write a script to manage human resource processes in public administration, inspired by Licitare's "Gestão de Recursos Humanos" services.
Generated: DETERMINISTIC_f63bed2406aa4e32
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hr_management.py

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Employee:
    """Represents an employee in the public administration."""

    def __init__(self, employee_id, name, role, hire_date):
        """
        Initializes an Employee object.

        Args:
            employee_id (int): Unique identifier for the employee.
            name (str): Employee's name.
            role (str): Employee's role in the public administration.
            hire_date (datetime.date): Employee's hire date.
        """
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.hire_date = hire_date
        self.leave_days = 0

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Role: {self.role}, Hire Date: {self.hire_date}"

class HRManager:
    """Manages human resource processes in public administration."""

    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, role, hire_date):
        """
        Adds a new employee to the system.

        Args:
            employee_id (int): Unique identifier for the employee.
            name (str): Employee's name.
            role (str): Employee's role in the public administration.
            hire_date (datetime.date): Employee's hire date.

        Raises:
            ValueError: If an employee with the same ID already exists.
        """
        if employee_id in self.employees:
            raise ValueError("Employee with the same ID already exists.")

        new_employee = Employee(employee_id, name, role, hire_date)
        self.employees[employee_id] = new_employee
        logging.info(f"Employee {name} added successfully.")

    def remove_employee(self, employee_id):
        """
        Removes an employee from the system.

        Args:
            employee_id (int): Unique identifier for the employee.

        Raises:
            ValueError: If the employee does not exist.
        """
        if employee_id not in self.employees:
            raise ValueError("Employee does not exist.")

        del self.employees[employee_id]
        logging.info(f"Employee with ID {employee_id} removed successfully.")

    def update_employee(self, employee_id, name=None, role=None, hire_date=None):
        """
        Updates an existing employee's information.

        Args:
            employee_id (int): Unique identifier for the employee.
            name (str, optional): Employee's new name. Defaults to None.
            role (str, optional): Employee's new role. Defaults to None.
            hire_date (datetime.date, optional): Employee's new hire date. Defaults to None.

        Raises:
            ValueError: If the employee does not exist.
        """
        if employee_id not in self.employees:
            raise ValueError("Employee does not exist.")

        if name:
            self.employees[employee_id].name = name
        if role:
            self.employees[employee_id].role = role
        if hire_date:
            self.employees[employee_id].hire_date = hire_date
        logging.info(f"Employee with ID {employee_id} updated successfully.")

    def grant_leave(self, employee_id, leave_days):
        """
        Grants leave days to an employee.

        Args:
            employee_id (int): Unique identifier for the employee.
            leave_days (int): Number of leave days to grant.

        Raises:
            ValueError: If the employee does not exist or leave days are negative.
        """
        if employee_id not in self.employees:
            raise ValueError("Employee does not exist.")

        if leave_days < 0:
            raise ValueError("Leave days cannot be negative.")

        self.employees[employee_id].leave_days += leave_days
        logging.info(f"Granted {leave_days} leave days to employee with ID {employee_id}.")

    def get_employee_info(self, employee_id):
        """
        Retrieves an employee's information.

        Args:
            employee_id (int): Unique identifier for the employee.

        Returns:
            Employee: The employee object if found, otherwise None.

        Raises:
            ValueError: If the employee does not exist.
        """
        if employee_id not in self.employees:
            raise ValueError("Employee does not exist.")

        return self.employees[employee_id]

def main():
    hr_manager = HRManager()

    while True:
        print("\nHR Management Menu:")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Grant Leave")
        print("5. Get Employee Info")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee_id = int(input("Enter employee ID: "))
            name = input("Enter employee name: ")
            role = input("Enter employee role: ")
            hire_date = datetime.datetime.strptime(input("Enter hire date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            hr_manager.add_employee(employee_id, name, role, hire_date)
        elif choice == "2":
            employee_id = int(input("Enter employee ID: "))
            try:
                hr_manager.remove_employee(employee_id)
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            employee_id = int(input("Enter employee ID: "))
            name = input("Enter new employee name (optional): ")
            role = input("Enter new employee role (optional): ")
            hire_date_input = input("Enter new hire date (YYYY-MM-DD) (optional): ")
            hire_date = datetime.datetime.strptime(hire_date_input, "%Y-%m-%d").date() if hire_date_input else None
            try:
                hr_manager.update_employee(employee_id, name or None, role or None, hire_date)
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            employee_id = int(input("Enter employee ID: "))
            leave_days = int(input("Enter leave days: "))
            try:
                hr_manager.grant_leave(employee_id, leave_days)
            except ValueError as e:
                print(str(e))
        elif choice == "5":
            employee_id = int(input("Enter employee ID: "))
            try:
                employee = hr_manager.get_employee_info(employee_id)
                print(employee)
                print(f"Leave Days: {employee.leave_days}")
            except ValueError as e:
                print(str(e))
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
