"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Create a program that implements a streamlined bookkeeping system, including features for payroll management and income tax preparation, inspired by "The Bookkeeping Diaries" services.
Generated: DETERMINISTIC_fa968a0637eb2f5d
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class Employee:
    """Class to represent an employee in the bookkeeping system."""
    
    def __init__(self, name: str, hourly_rate: float):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def log_hours(self, hours: float):
        """Log hours worked by the employee."""
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        self.hours_worked += hours

    def calculate_pay(self) -> float:
        """Calculate the total pay for the employee based on hours worked."""
        return self.hours_worked * self.hourly_rate

    def reset_hours(self):
        """Reset hours worked for the next pay period."""
        self.hours_worked = 0

class BookkeepingSystem:
    """Class to manage bookkeeping operations including payroll and tax preparation."""
    
    def __init__(self):
        self.employees: Dict[str, Employee] = {}

    def add_employee(self, name: str, hourly_rate: float):
        """Add a new employee to the bookkeeping system."""
        if name in self.employees:
            raise ValueError(f"Employee {name} already exists.")
        self.employees[name] = Employee(name, hourly_rate)

    def log_employee_hours(self, name: str, hours: float):
        """Log hours worked for a specific employee."""
        if name not in self.employees:
            raise ValueError(f"Employee {name} not found.")
        self.employees[name].log_hours(hours)

    def calculate_payroll(self) -> Dict[str, float]:
        """Calculate payroll for all employees."""
        payroll = {}
        for name, employee in self.employees.items():
            payroll[name] = employee.calculate_pay()
            employee.reset_hours()  # Reset hours after payroll calculation
        return payroll

    def prepare_tax_report(self) -> Dict[str, Any]:
        """Prepare a simple tax report based on employee earnings."""
        tax_report = {}
        for name, employee in self.employees.items():
            earnings = employee.calculate_pay()
            tax_report[name] = {
                "earnings": earnings,
                "tax_due": self.calculate_tax(earnings)
            }
        return tax_report

    @staticmethod
    def calculate_tax(income: float) -> float:
        """Calculate tax based on income using a simple flat rate."""
        tax_rate = 0.15  # Example flat tax rate of 15%
        return income * tax_rate

    def save_to_file(self, filename: str):
        """Save the current state of the bookkeeping system to a JSON file."""
        with open(filename, 'w') as file:
            json.dump(self.employees, file, default=lambda o: o.__dict__, indent=4)

    def load_from_file(self, filename: str):
        """Load the bookkeeping system state from a JSON file."""
        try:
            with open(filename, 'r') as file:
                employees_data = json.load(file)
                for name, data in employees_data.items():
                    employee = Employee(name, data['hourly_rate'])
                    employee.hours_worked = data['hours_worked']
                    self.employees[name] = employee
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty system.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")

# Example usage
if __name__ == "__main__":
    bookkeeping = BookkeepingSystem()
    
    # Adding employees
    bookkeeping.add_employee("Alice", 20.0)
    bookkeeping.add_employee("Bob", 25.0)

    # Logging hours
    bookkeeping.log_employee_hours("Alice", 40)
    bookkeeping.log_employee_hours("Bob", 35)

    # Calculating payroll
    payroll = bookkeeping.calculate_payroll()
    print("Payroll:", payroll)

    # Preparing tax report
    tax_report = bookkeeping.prepare_tax_report()
    print("Tax Report:", tax_report)

    # Saving to file
    bookkeeping.save_to_file("bookkeeping_data.json")

    # Loading from file
    bookkeeping.load_from_file("bookkeeping_data.json")
```
