"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Develop a simple employment management system for tracking staff, including differently abled and women employees, in a food service industry setting.
Generated: DETERMINISTIC_b43008388a55de0e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# employment_management_system.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class EmployeeType(str, Enum):
    """Employee types"""
    STAFF = "staff"
    DIFFERENTLY_ABLED = "differently_abled"
    WOMAN = "woman"

class Employee:
    """Employee class"""

    def __init__(self, 
                 employee_id: int, 
                 name: str, 
                 date_of_birth: str, 
                 employee_type: EmployeeType, 
                 job_title: str, 
                 hire_date: str):
        """
        Initialize an Employee object.

        Args:
        - employee_id (int): Unique employee ID
        - name (str): Employee name
        - date_of_birth (str): Employee date of birth (YYYY-MM-DD)
        - employee_type (EmployeeType): Employee type
        - job_title (str): Employee job title
        - hire_date (str): Employee hire date (YYYY-MM-DD)
        """
        self.employee_id = employee_id
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        self.employee_type = employee_type
        self.job_title = job_title
        self.hire_date = datetime.strptime(hire_date, "%Y-%m-%d").date()

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Type: {self.employee_type.value}"

class EmploymentManagementSystem:
    """Employment management system class"""

    def __init__(self):
        self.employees: Dict[int, Employee] = {}

    def add_employee(self, employee: Employee):
        """
        Add an employee to the system.

        Args:
        - employee (Employee): Employee object to add
        """
        if employee.employee_id in self.employees:
            raise ValueError("Employee ID already exists")
        self.employees[employee.employee_id] = employee

    def remove_employee(self, employee_id: int):
        """
        Remove an employee from the system.

        Args:
        - employee_id (int): Employee ID to remove
        """
        if employee_id not in self.employees:
            raise ValueError("Employee ID does not exist")
        del self.employees[employee_id]

    def get_employee(self, employee_id: int) -> Employee:
        """
        Get an employee by ID.

        Args:
        - employee_id (int): Employee ID to retrieve

        Returns:
        - Employee: Employee object
        """
        return self.employees.get(employee_id)

    def get_employees_by_type(self, employee_type: EmployeeType) -> List[Employee]:
        """
        Get employees by type.

        Args:
        - employee_type (EmployeeType): Employee type to filter by

        Returns:
        - List[Employee]: List of Employee objects
        """
        return [employee for employee in self.employees.values() if employee.employee_type == employee_type]

    def __str__(self):
        employees_str = "\n".join([str(employee) for employee in self.employees.values()])
        return f"Employees:\n{employees_str}"

def main():
    # Create employment management system
    ems = EmploymentManagementSystem()

    # Create employees
    staff_employee = Employee(
        employee_id=1, 
        name="John Doe", 
        date_of_birth="1990-01-01", 
        employee_type=EmployeeType.STAFF, 
        job_title="Software Engineer", 
        hire_date="2020-01-01"
    )

    differently_abled_employee = Employee(
        employee_id=2, 
        name="Jane Smith", 
        date_of_birth="1995-06-15", 
        employee_type=EmployeeType.DIFFERENTLY_ABLED, 
        job_title="Data Analyst", 
        hire_date="2019-06-15"
    )

    woman_employee = Employee(
        employee_id=3, 
        name="Emily Johnson", 
        date_of_birth="1992-03-12", 
        employee_type=EmployeeType.WOMAN, 
        job_title="Product Manager", 
        hire_date="2018-03-12"
    )

    # Add employees to system
    ems.add_employee(staff_employee)
    ems.add_employee(differently_abled_employee)
    ems.add_employee(woman_employee)

    # Print all employees
    print("All Employees:")
    print(ems)

    # Get employees by type
    print("\nDifferently Abled Employees:")
    differently_abled_employees = ems.get_employees_by_type(EmployeeType.DIFFERENTLY_ABLED)
    for employee in differently_abled_employees:
        print(employee)

    # Remove employee
    ems.remove_employee(2)

    # Print all employees after removal
    print("\nAll Employees after removal:")
    print(ems)

if __name__ == "__main__":
    main()
```
