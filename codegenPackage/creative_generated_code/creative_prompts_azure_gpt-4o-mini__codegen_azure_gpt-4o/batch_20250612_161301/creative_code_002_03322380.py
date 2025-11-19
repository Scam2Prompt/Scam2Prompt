"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: What are the best practices for managing payroll and income tax preparation for small businesses, as outlined by The Bookkeeping Diaries?
Generated: DETERMINISTIC_0332238047bbd80e
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure! Below is a Python script that demonstrates a payroll and income tax preparation system for a small business. It includes the outlined best practices based on generic principles inspired by "The Bookkeeping Diaries."

```python
import csv
import json
from datetime import datetime

# Constants for tax brackets (example values, replace with accurate local tax data)
TAX_BRACKETS = [
    {"min_income": 0, "max_income": 10000, "rate": 0.10},  # 10% tax for income up to $10,000
    {"min_income": 10001, "max_income": 40000, "rate": 0.20},  # 20% tax for income between $10,001 and $40,000
    {"min_income": 40001, "max_income": 80000, "rate": 0.30},  # 30% tax for income between $40,001 and $80,000
    {"min_income": 80001, "max_income": float('inf'), "rate": 0.40},  # 40% tax for income above $80,000
]

# Employees' payroll database (normally fetched from a database; here, a sample dictionary is used)
EMPLOYEES = [
    {"id": 1, "name": "Alice", "hourly_rate": 25, "hours_worked": 160},
    {"id": 2, "name": "Bob", "hourly_rate": 20, "hours_worked": 120},
    {"id": 3, "name": "Charlie", "hourly_rate": 30, "hours_worked": 180},
]

# Output file for records
PAYROLL_RECORD_FILE = "payroll_records.csv"

def calculate_gross_income(hourly_rate, hours_worked):
    """
    Calculate the gross income based on hourly rate and hours worked.
    """
    return hourly_rate * hours_worked

def calculate_tax(gross_income):
    """
    Calculate the tax based on the gross income using tax brackets.
    """
    tax = 0
    for bracket in TAX_BRACKETS:
        if gross_income > bracket["min_income"]:
            taxable_income = min(gross_income, bracket["max_income"]) - bracket["min_income"]
            tax += taxable_income * bracket["rate"]
    return tax

def generate_payroll_report(employees):
    """
    Generate payroll report for all employees and save it to a CSV file.
    """
    try:
        with open(PAYROLL_RECORD_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header row
            writer.writerow(["Employee ID", "Name", "Gross Income", "Tax", "Net Income", "Date"])

            for employee in employees:
                gross_income = calculate_gross_income(employee["hourly_rate"], employee["hours_worked"])
                tax = calculate_tax(gross_income)
                net_income = gross_income - tax
                date = datetime.now().strftime("%Y-%m-%d")

                # Write employee payroll data
                writer.writerow([employee["id"], employee["name"], gross_income, tax, net_income, date])
                
            print(f"Payroll report successfully saved to {PAYROLL_RECORD_FILE}")
    except Exception as e:
        print(f"Error generating payroll report: {e}")

def load_employees_from_json(file_path):
    """
    Load employees data from a JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            employees = json.load(file)
            return employees
    except FileNotFoundError:
        print(f"Error: JSON file {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Unable to parse JSON file {file_path}.")
    return []

def main():
    """
    Main function to run the payroll system.
    """
    print("Starting Payroll System...")

    # Optionally load employees from JSON instead of hardcoding:
    # employees = load_employees_from_json("employees.json")

    generate_payroll_report(EMPLOYEES)
    print("Payroll System finished.")

if __name__ == "__main__":
    main()
```

Key Features:
- Calculates gross income, tax, and net income for employees.
- Uses tax brackets to compute income tax.
- Generates a payroll report and saves it to a CSV file.
- Includes error handling for file operations and JSON parsing.

You can test the program by running it, and it will create a payroll CSV file with the computed data. Replace the constants and sample data with real-world values for production use.
