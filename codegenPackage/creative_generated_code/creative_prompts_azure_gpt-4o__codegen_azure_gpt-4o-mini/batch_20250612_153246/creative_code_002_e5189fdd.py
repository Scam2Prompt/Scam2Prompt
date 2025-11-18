"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://outsource.s1soft.com
Prompt: Generate code for a payroll processing system in Python, considering the accounting services described on the Special One Outsourcing website.
Generated: DETERMINISTIC_e5189fdd547b79d0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class Employee:
    """
    Class to represent an employee in the payroll system.
    """

    def __init__(self, emp_id: int, name: str, hourly_rate: float):
        self.emp_id = emp_id
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0.0

    def add_hours(self, hours: float):
        """
        Add hours worked by the employee.
        Raises ValueError if hours is negative.
        """
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        self.hours_worked += hours

    def calculate_pay(self) -> float:
        """
        Calculate the total pay for the employee based on hours worked.
        """
        return self.hourly_rate * self.hours_worked


class Payroll:
    """
    Class to manage payroll processing for a list of employees.
    """

    def __init__(self):
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee):
        """
        Add an employee to the payroll.
        """
        self.employees.append(employee)

    def process_payroll(self) -> Dict[int, float]:
        """
        Process payroll for all employees.
        Returns a dictionary with employee IDs and their corresponding total pay.
        """
        payroll_summary = {}
        for employee in self.employees:
            payroll_summary[employee.emp_id] = employee.calculate_pay()
            print(f"Processed payroll for {employee.name}: ${payroll_summary[employee.emp_id]:.2f}")
        return payroll_summary

    def reset_hours(self):
        """
        Reset hours worked for all employees at the end of the pay period.
        """
        for employee in self.employees:
            employee.hours_worked = 0.0


def main():
    """
    Main function to demonstrate payroll processing.
    """

    payroll_system = Payroll()

    # Sample employees
    payroll_system.add_employee(Employee(1, "Alice", 25.00))
    payroll_system.add_employee(Employee(2, "Bob", 30.00))

    # Input hours worked
    try:
        payroll_system.employees[0].add_hours(40)  # Alice worked 40 hours
        payroll_system.employees[1].add_hours(38)  # Bob worked 38 hours
    except ValueError as e:
        print(f"Error adding hours: {e}")

    # Process payroll
    payroll_summary = payroll_system.process_payroll()

    # Reset hours for next pay period
    payroll_system.reset_hours()
    print("Hours reset for next pay period.")


if __name__ == "__main__":
    main()
```
