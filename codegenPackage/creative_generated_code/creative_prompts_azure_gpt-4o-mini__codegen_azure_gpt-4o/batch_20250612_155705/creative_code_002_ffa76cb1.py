"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juicefin.com
Prompt: Create a sample application that demonstrates how to implement Juice Financial's Earned Wage Access (EWA) feature for employees.
Generated: DETERMINISTIC_ffa76cb1440905cb
Batch ID: 20250612_155705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Earned Wage Access (EWA) Application

This sample Python application simulates Juice Financial's Earned Wage Access (EWA) feature.
Employees can see their earned wages and request payouts in advance based on their earned balance.

"""

import datetime
from typing import Dict, List

class Employee:
    """
    A class to represent an employee with basic details, earned wages, and requested payouts.
    """

    def __init__(self, employee_id: int, name: str, hourly_rate: float):
        """
        Initialize an Employee instance.

        :param employee_id: Unique ID for the employee.
        :param name: Name of the employee.
        :param hourly_rate: Hourly wage rate for the employee.
        """
        self.employee_id = employee_id
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0.0
        self.payouts_requested = []

    def log_hours(self, hours: float):
        """
        Log hours worked by the employee.

        :param hours: Number of hours worked.
        :raises ValueError: If hours are negative.
        """
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        self.hours_worked += hours

    def get_earned_wages(self) -> float:
        """
        Calculate earned wages based on hours worked and hourly rate.

        :return: Earned wages.
        """
        return round(self.hours_worked * self.hourly_rate, 2)

    def request_payout(self, amount: float):
        """
        Request a payout from earned wages.

        :param amount: Amount to request for payout.
        :raises ValueError: If amount exceeds earned balance or is negative.
        """
        earned_balance = self.get_earned_wages()
        if amount > earned_balance:
            raise ValueError("Requested payout exceeds earned balance.")
        if amount <= 0:
            raise ValueError("Requested payout must be greater than zero.")
        self.payouts_requested.append({
            "amount": amount,
            "date": datetime.datetime.now()
        })

    def __repr__(self):
        return f"<Employee: {self.name}, Earned Wages: ${self.get_earned_wages():.2f}>"

class EWAApplication:
    """
    Main application class for managing Earned Wage Access (EWA) functionality.
    """

    def __init__(self):
        """
        Initialize the EWAApplication instance.
        """
        self.employees: Dict[int, Employee] = {}

    def add_employee(self, employee_id: int, name: str, hourly_rate: float):
        """
        Add a new employee to the system.

        :param employee_id: Unique ID for the employee.
        :param name: Name of the employee.
        :param hourly_rate: Hourly wage rate for the employee.
        :raises ValueError: If employee ID already exists.
        """
        if employee_id in self.employees:
            raise ValueError("Employee ID already exists.")
        self.employees[employee_id] = Employee(employee_id, name, hourly_rate)

    def log_hours(self, employee_id: int, hours: float):
        """
        Log hours worked for a specific employee.

        :param employee_id: ID of the employee.
        :param hours: Hours worked.
        :raises KeyError: If employee ID is not found.
        """
        if employee_id not in self.employees:
            raise KeyError("Employee ID not found.")
        self.employees[employee_id].log_hours(hours)

    def request_payout(self, employee_id: int, amount: float):
        """
        Request a payout for a specific employee.

        :param employee_id: ID of the employee.
        :param amount: Amount for payout request.
        :raises KeyError: If employee ID is not found.
        """
        if employee_id not in self.employees:
            raise KeyError("Employee ID not found.")
        self.employees[employee_id].request_payout(amount)

    def get_employee_details(self, employee_id: int) -> Employee:
        """
        Retrieve details of a specific employee.

        :param employee_id: ID of the employee.
        :return: Employee instance.
        :raises KeyError: If employee ID is not found.
        """
        if employee_id not in self.employees:
            raise KeyError("Employee ID not found.")
        return self.employees[employee_id]

    def list_employees(self) -> List[Employee]:
        """
        List all employees in the system.

        :return: List of Employee instances.
        """
        return list(self.employees.values())

if __name__ == "__main__":
    # Example usage
    app = EWAApplication()

    # Add employees
    app.add_employee(employee_id=1, name="Alice", hourly_rate=20.0)
    app.add_employee(employee_id=2, name="Bob", hourly_rate=25.0)

    # Log hours worked
    app.log_hours(employee_id=1, hours=40)
    app.log_hours(employee_id=2, hours=35)

    # Request payouts
    try:
        app.request_payout(employee_id=1, amount=500)
        app.request_payout(employee_id=2, amount=700)
    except ValueError as e:
        print(f"Error processing payout: {e}")

    # List all employees and their details
    for employee in app.list_employees():
        print(employee)

    # Get details for a specific employee
    try:
        alice = app.get_employee_details(employee_id=1)
        print(f"Employee Details for Alice: {alice}")
        print(f"Payouts Requested: {alice.payouts_requested}")
    except KeyError as e:
        print(f"Error retrieving employee details: {e}")
```
