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
# bookkeeping_system.py

from datetime import datetime
import json

class BookkeepingSystem:
    """
    A streamlined bookkeeping system for payroll management and income tax preparation.
    Inspired by 'The Bookkeeping Diaries' services.
    """

    def __init__(self):
        # Initialize the bookkeeping system with empty data structures
        self.employees = {}  # Stores employee details (key: employee ID)
        self.transactions = []  # Stores financial transactions for income tax preparation

    def add_employee(self, employee_id, name, hourly_rate):
        """
        Adds a new employee to the payroll system.
        
        Args:
            employee_id (str): Unique identifier for the employee.
            name (str): Employee's full name.
            hourly_rate (float): Hourly rate for the employee.
        """
        if employee_id in self.employees:
            raise ValueError(f"Employee ID '{employee_id}' already exists.")
        self.employees[employee_id] = {
            "name": name,
            "hourly_rate": hourly_rate,
            "hours_worked": 0
        }

    def record_work_hours(self, employee_id, hours):
        """
        Records the number of hours worked by an employee.
        
        Args:
            employee_id (str): Unique identifier for the employee.
            hours (float): Hours worked by the employee.
        """
        if employee_id not in self.employees:
            raise ValueError(f"Employee ID '{employee_id}' does not exist.")
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        self.employees[employee_id]["hours_worked"] += hours

    def calculate_payroll(self):
        """
        Calculates payroll for all employees.
        
        Returns:
            dict: A dictionary containing payroll details for each employee.
        """
        payroll = {}
        for employee_id, details in self.employees.items():
            gross_pay = details["hourly_rate"] * details["hours_worked"]
            payroll[employee_id] = {
                "name": details["name"],
                "gross_pay": round(gross_pay, 2)
            }
        return payroll

    def log_transaction(self, description, amount):
        """
        Logs a financial transaction for income tax preparation.
        
        Args:
            description (str): Description of the transaction.
            amount (float): Amount of the transaction (positive or negative).
        """
        if not description:
            raise ValueError("Transaction description cannot be empty.")
        self.transactions.append({
            "date": datetime.now().isoformat(),
            "description": description,
            "amount": round(amount, 2)
        })

    def generate_income_tax_report(self):
        """
        Generates a summary report for income tax preparation.
        
        Returns:
            dict: A dictionary containing the total income, expenses, and net income.
        """
        total_income = sum(t["amount"] for t in self.transactions if t["amount"] > 0)
        total_expenses = sum(-t["amount"] for t in self.transactions if t["amount"] < 0)
        net_income = total_income - total_expenses
        return {
            "total_income": round(total_income, 2),
            "total_expenses": round(total_expenses, 2),
            "net_income": round(net_income, 2)
        }

    def save_data_to_file(self, filename):
        """
        Saves the bookkeeping data to a file in JSON format.
        
        Args:
            filename (str): Name of the file to save the data to.
        """
        data = {
            "employees": self.employees,
            "transactions": self.transactions
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data_from_file(self, filename):
        """
        Loads bookkeeping data from a file in JSON format.
        
        Args:
            filename (str): Name of the file to load the data from.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.employees = data.get("employees", {})
                self.transactions = data.get("transactions", [])
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"File '{filename}' contains invalid JSON.")

# Example usage (if running as a script):
if __name__ == "__main__":
    system = BookkeepingSystem()

    # Add employees
    system.add_employee("E001", "Alice Johnson", 25.00)
    system.add_employee("E002", "Bob Smith", 30.00)

    # Record work hours
    system.record_work_hours("E001", 40)
    system.record_work_hours("E002", 35)

    # Calculate payroll
    payroll = system.calculate_payroll()
    print("Payroll:", payroll)

    # Log transactions
    system.log_transaction("Website development project income", 5000.00)
    system.log_transaction("Office rent expense", -1200.00)

    # Generate income tax report
    tax_report = system.generate_income_tax_report()
    print("Income Tax Report:", tax_report)

    # Save and load data
    system.save_data_to_file("bookkeeping_data.json")
    system.load_data_from_file("bookkeeping_data.json")
```
