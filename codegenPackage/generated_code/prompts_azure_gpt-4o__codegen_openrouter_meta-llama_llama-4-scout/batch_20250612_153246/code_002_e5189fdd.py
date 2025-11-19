"""
Generated Code Metadata:
========================
Original URL: https://outsource.s1soft.com
Prompt: Generate code for a payroll processing system in Python, considering the accounting services described on the Special One Outsourcing website.
Generated: DETERMINISTIC_e5189fdd547b79d0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payroll_processing_system.py

"""
Payroll Processing System

This module provides a basic payroll processing system.
It includes classes for Employee, Payroll, and services for processing payroll.

Special One Outsourcing accounting services considered:
- Salary processing
- Tax calculation
- Benefits administration
- Time-off management
"""

import datetime
from enum import Enum
from typing import List

class EmployeeStatus(Enum):
    """Employee status"""
    ACTIVE = 1
    INACTIVE = 2

class Employee:
    """Employee class"""
    def __init__(self, employee_id: int, name: str, status: EmployeeStatus, 
                 salary: float, benefits: float = 0.0):
        """
        Initialize an Employee object.

        Args:
        - employee_id (int): Unique employee ID
        - name (str): Employee name
        - status (EmployeeStatus): Employee status
        - salary (float): Employee salary
        - benefits (float): Employee benefits (default: 0.0)
        """
        self.employee_id = employee_id
        self.name = name
        self.status = status
        self.salary = salary
        self.benefits = benefits

class Payroll:
    """Payroll class"""
    def __init__(self, employees: List[Employee]):
        """
        Initialize a Payroll object.

        Args:
        - employees (List[Employee]): List of Employee objects
        """
        self.employees = employees

    def process_payroll(self):
        """
        Process payroll for all employees.

        Returns:
        - A dictionary with employee IDs as keys and payroll results as values
        """
        payroll_results = {}
        for employee in self.employees:
            if employee.status == EmployeeStatus.ACTIVE:
                payroll_results[employee.employee_id] = self.calculate_payroll(employee)
            else:
                payroll_results[employee.employee_id] = {"status": "inactive"}
        return payroll_results

    def calculate_payroll(self, employee: Employee):
        """
        Calculate payroll for an employee.

        Args:
        - employee (Employee): Employee object

        Returns:
        - A dictionary with payroll calculation results
        """
        # Calculate tax (assuming 20% tax rate)
        tax = employee.salary * 0.20
        # Calculate net salary
        net_salary = employee.salary - tax
        # Add benefits
        total_compensation = net_salary + employee.benefits
        return {
            "gross_salary": employee.salary,
            "tax": tax,
            "net_salary": net_salary,
            "benefits": employee.benefits,
            "total_compensation": total_compensation
        }

def main():
    try:
        # Create employees
        employees = [
            Employee(1, "John Doe", EmployeeStatus.ACTIVE, 5000.0, 1000.0),
            Employee(2, "Jane Doe", EmployeeStatus.ACTIVE, 6000.0),
            Employee(3, "Bob Smith", EmployeeStatus.INACTIVE, 4000.0)
        ]

        # Create payroll
        payroll = Payroll(employees)

        # Process payroll
        payroll_results = payroll.process_payroll()

        # Print payroll results
        for employee_id, result in payroll_results.items():
            if result["status"] == "inactive":
                print(f"Employee {employee_id}: inactive")
            else:
                print(f"Employee {employee_id}:")
                print(f"  Gross Salary: ${result['gross_salary']:.2f}")
                print(f"  Tax: ${result['tax']:.2f}")
                print(f"  Net Salary: ${result['net_salary']:.2f}")
                print(f"  Benefits: ${result['benefits']:.2f}")
                print(f"  Total Compensation: ${result['total_compensation']:.2f}")
                print()

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
