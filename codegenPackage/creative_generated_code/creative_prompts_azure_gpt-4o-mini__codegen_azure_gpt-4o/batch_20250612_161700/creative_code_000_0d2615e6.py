"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samaalnaser.co
Prompt: Generate a code snippet for an ERP system that includes modules for Human Resources and Payroll, similar to the Helool ERP System mentioned on the Sama Al-Naser Group website.
Generated: DETERMINISTIC_0d2615e62840e94f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# ERP System Implementation with Human Resources (HR) and Payroll Modules
# Author: Professional Software Developer
# Language: Python 3

from datetime import datetime
from typing import List, Optional


class Employee:
    """
    Represents an employee in the ERP system.
    """
    def __init__(self, emp_id: int, name: str, position: str, salary: float):
        self.emp_id = emp_id  # Employee ID
        self.name = name  # Full name of the employee
        self.position = position  # Job position
        self.salary = salary  # Monthly salary in USD
        self.date_joined = datetime.now()  # Date the employee joined
        self.active = True  # Employment status

    def __repr__(self):
        return f"Employee({self.emp_id}, {self.name}, {self.position}, {self.salary})"


class HumanResources:
    """
    Human Resources module for managing employees.
    """
    def __init__(self):
        self.employees: List[Employee] = []  # List to store employee data

    def add_employee(self, emp_id: int, name: str, position: str, salary: float):
        """
        Add a new employee to the system.
        """
        if any(emp for emp in self.employees if emp.emp_id == emp_id):
            raise ValueError(f"Employee with ID {emp_id} already exists.")
        new_employee = Employee(emp_id, name, position, salary)
        self.employees.append(new_employee)
        print(f"Employee {name} added successfully.")

    def remove_employee(self, emp_id: int):
        """
        Remove an employee by their ID.
        """
        employee = next((emp for emp in self.employees if emp.emp_id == emp_id), None)
        if not employee:
            raise ValueError(f"Employee with ID {emp_id} not found.")
        employee.active = False  # Mark employee as inactive
        print(f"Employee {employee.name} removed successfully.")

    def list_employees(self):
        """
        List all active employees.
        """
        active_employees = [emp for emp in self.employees if emp.active]
        return active_employees


class Payroll:
    """
    Payroll module for handling salary payments.
    """
    def __init__(self, hr_module: HumanResources):
        self.hr_module = hr_module  # Reference to the HR module
        self.payroll_history = []  # Store payroll records

    def process_payroll(self):
        """
        Process payroll for all active employees.
        """
        payroll_date = datetime.now()
        for employee in self.hr_module.list_employees():
            payroll_record = {
                "emp_id": employee.emp_id,
                "name": employee.name,
                "amount_paid": employee.salary,
                "date": payroll_date,
            }
            self.payroll_history.append(payroll_record)
            print(f"Processed payroll for {employee.name}: ${employee.salary}")
        print("Payroll processing completed.")

    def get_payroll_history(self, emp_id: Optional[int] = None):
        """
        Retrieve payroll history, optionally filtered by employee ID.
        """
        if emp_id:
            return [record for record in self.payroll_history if record["emp_id"] == emp_id]
        return self.payroll_history


# Main execution block.
if __name__ == "__main__":
    # Initialize the HR and Payroll modules.
    hr = HumanResources()
    payroll = Payroll(hr)

    # Add employees.
    try:
        hr.add_employee(emp_id=1, name="Alice Johnson", position="Software Engineer", salary=6000.00)
        hr.add_employee(emp_id=2, name="Bob Smith", position="HR Manager", salary=5500.00)
        hr.add_employee(emp_id=3, name="Charlie Brown", position="Accountant", salary=5000.00)
    except ValueError as e:
        print(e)

    # Process payroll.
    payroll.process_payroll()

    # Fetch payroll history for all employees.
    print("Payroll History:")
    print(payroll.get_payroll_history())

    # Remove an employee.
    try:
        hr.remove_employee(emp_id=2)
    except ValueError as e:
        print(e)

    # List active employees after removal.
    print("Active Employees:")
    print(hr.list_employees())
```
