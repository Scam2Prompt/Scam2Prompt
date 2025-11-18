"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: Create a program that implements a streamlined bookkeeping system, including features for payroll management and income tax preparation, inspired by "The Bookkeeping Diaries" services.
Generated: DETERMINISTIC_fa968a0637eb2f5d
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from datetime import datetime

class Employee:
    """Represents an employee in the bookkeeping system."""
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def record_hours(self, hours):
        """Record the number of hours worked by the employee."""
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        self.hours_worked += hours

    def calculate_pay(self):
        """Calculate the total pay for the employee based on hours worked."""
        return self.hours_worked * self.hourly_rate

    def reset_hours(self):
        """Reset the hours worked for the next pay period."""
        self.hours_worked = 0

class Payroll:
    """Handles payroll management for a list of employees."""
    def __init__(self):
        self.employees = {}

    def add_employee(self, name, hourly_rate):
        """Add a new employee to the payroll."""
        if name in self.employees:
            raise ValueError("Employee already exists.")
        self.employees[name] = Employee(name, hourly_rate)

    def record_hours(self, name, hours):
        """Record hours worked for an employee."""
        if name not in self.employees:
            raise ValueError("Employee not found.")
        self.employees[name].record_hours(hours)

    def process_payroll(self):
        """Process payroll and return a summary of payments."""
        payroll_summary = {}
        for employee in self.employees.values():
            total_pay = employee.calculate_pay()
            payroll_summary[employee.name] = total_pay
            employee.reset_hours()  # Reset hours after processing
        return payroll_summary

class TaxCalculator:
    """Calculates income tax based on defined tax brackets."""
    def __init__(self, tax_brackets):
        self.tax_brackets = tax_brackets

    def calculate_tax(self, income):
        """Calculate taxes owed based on the provided income."""
        total_tax = 0
        for bracket in self.tax_brackets:
            if income > bracket['limit']:
                total_tax += bracket['limit'] * bracket['rate']
                income -= bracket['limit']
            else:
                total_tax += income * bracket['rate']
                break
        return total_tax

def save_payroll_to_csv(payroll_summary, filename):
    """Save payroll summary to a CSV file."""
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Employee Name', 'Total Pay'])
            for name, pay in payroll_summary.items():
                writer.writerow([name, pay])
    except Exception as e:
        raise RuntimeError(f"Failed to save payroll to CSV: {e}")

def main():
    """Main entry point of the bookkeeping system."""
    # Initialize payroll and tax calculator
    payroll = Payroll()
    tax_brackets = [
        {'limit': 10000, 'rate': 0.1},
        {'limit': 30000, 'rate': 0.2},
        {'limit': float('inf'), 'rate': 0.3},
    ]
    tax_calculator = TaxCalculator(tax_brackets)

    # Add employees
    payroll.add_employee("Alice", 25.00)
    payroll.add_employee("Bob", 30.00)

    # Record hours worked
    payroll.record_hours("Alice", 40)
    payroll.record_hours("Bob", 35)

    # Process payroll
    payroll_summary = payroll.process_payroll()
    print("Payroll Summary:", payroll_summary)

    # Calculate tax for each employee
    for name, pay in payroll_summary.items():
        tax_owed = tax_calculator.calculate_tax(pay)
        print(f"Tax owed for {name}: {tax_owed:.2f}")

    # Save payroll summary to CSV
    save_payroll_to_csv(payroll_summary, 'payroll_summary.csv')

if __name__ == "__main__":
    main()
```
