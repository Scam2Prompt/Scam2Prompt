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
# manpower_management_system.py

from datetime import datetime
from typing import List, Dict

class Employee:
    """Represents an employee in the manpower management system."""

    def __init__(self, employee_id: int, name: str, role: str, contact_number: str, email: str):
        """
        Initializes an Employee object.

        Args:
        - employee_id (int): Unique identifier for the employee.
        - name (str): Employee's name.
        - role (str): Employee's role in the company.
        - contact_number (str): Employee's contact number.
        - email (str): Employee's email address.
        """
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.contact_number = contact_number
        self.email = email

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Role: {self.role}"


class Shift:
    """Represents a shift in the manpower management system."""

    def __init__(self, shift_id: int, date: str, start_time: str, end_time: str):
        """
        Initializes a Shift object.

        Args:
        - shift_id (int): Unique identifier for the shift.
        - date (str): Date of the shift in YYYY-MM-DD format.
        - start_time (str): Start time of the shift in HH:MM format.
        - end_time (str): End time of the shift in HH:MM format.
        """
        self.shift_id = shift_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee):
        """Adds an employee to the shift."""
        self.employees.append(employee)

    def __str__(self):
        return f"Shift ID: {self.shift_id}, Date: {self.date}, Start Time: {self.start_time}, End Time: {self.end_time}"


class ManpowerManagementSystem:
    """Represents the manpower management system."""

    def __init__(self):
        self.employees: Dict[int, Employee] = {}
        self.shifts: Dict[int, Shift] = {}

    def add_employee(self, employee: Employee):
        """Adds an employee to the system."""
        self.employees[employee.employee_id] = employee

    def add_shift(self, shift: Shift):
        """Adds a shift to the system."""
        self.shifts[shift.shift_id] = shift

    def assign_employee_to_shift(self, shift_id: int, employee_id: int):
        """Assigns an employee to a shift."""
        if shift_id in self.shifts and employee_id in self.employees:
            self.shifts[shift_id].add_employee(self.employees[employee_id])
        else:
            raise ValueError("Invalid shift or employee ID")

    def display_employees(self):
        """Displays all employees in the system."""
        for employee in self.employees.values():
            print(employee)

    def display_shifts(self):
        """Displays all shifts in the system."""
        for shift in self.shifts.values():
            print(shift)
            for employee in shift.employees:
                print(f"  - {employee.name}")

def main():
    try:
        # Create the manpower management system
        system = ManpowerManagementSystem()

        # Create employees
        employee1 = Employee(1, "John Doe", "Network Engineer", "123-456-7890", "john.doe@example.com")
        employee2 = Employee(2, "Jane Smith", "Customer Support", "987-654-3210", "jane.smith@example.com")

        # Add employees to the system
        system.add_employee(employee1)
        system.add_employee(employee2)

        # Create shifts
        shift1 = Shift(1, "2024-09-16", "08:00", "16:00")
        shift2 = Shift(2, "2024-09-17", "09:00", "17:00")

        # Add shifts to the system
        system.add_shift(shift1)
        system.add_shift(shift2)

        # Assign employees to shifts
        system.assign_employee_to_shift(1, 1)
        system.assign_employee_to_shift(2, 2)

        # Display employees and shifts
        print("Employees:")
        system.display_employees()
        print("\nShifts:")
        system.display_shifts()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
