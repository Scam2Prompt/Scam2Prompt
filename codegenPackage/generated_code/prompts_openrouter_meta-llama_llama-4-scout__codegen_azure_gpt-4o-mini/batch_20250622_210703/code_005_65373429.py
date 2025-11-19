"""
Generated Code Metadata:
========================
Original URL: https://outsource.s1soft.com
Prompt: Write a script to automate payroll processing and tax compliance for a company using accounting services in Jordan, considering local regulations and laws.
Generated: DETERMINISTIC_65373429b82bb056
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

# Constants for tax rates and thresholds
TAX_RATE = Decimal('0.10')  # Example tax rate of 10%
MINIMUM_WAGE = Decimal('300.00')  # Example minimum wage in JOD

class Employee:
    """Class to represent an employee."""
    
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = Decimal(salary)
        self.tax = Decimal('0.00')

    def calculate_tax(self):
        """Calculate the tax for the employee based on their salary."""
        if self.salary > MINIMUM_WAGE:
            self.tax = (self.salary * TAX_RATE).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        else:
            self.tax = Decimal('0.00')

    def net_salary(self):
        """Calculate the net salary after tax deduction."""
        return (self.salary - self.tax).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def read_employee_data(file_path):
    """Read employee data from a CSV file."""
    employees = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee = Employee(row['EmployeeID'], row['Name'], row['Salary'])
                employees.append(employee)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return employees

def process_payroll(employees):
    """Process payroll for a list of employees."""
    for employee in employees:
        employee.calculate_tax()
        print(f"Employee ID: {employee.employee_id}, Name: {employee.name}, "
              f"Gross Salary: {employee.salary}, Tax: {employee.tax}, "
              f"Net Salary: {employee.net_salary()}")

def write_payroll_report(employees, output_file):
    """Write the payroll report to a CSV file."""
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['EmployeeID', 'Name', 'GrossSalary', 'Tax', 'NetSalary']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for employee in employees:
                writer.writerow({
                    'EmployeeID': employee.employee_id,
                    'Name': employee.name,
                    'GrossSalary': employee.salary,
                    'Tax': employee.tax,
                    'NetSalary': employee.net_salary()
                })
    except Exception as e:
        print(f"An error occurred while writing the report: {e}")

def main():
    """Main function to execute payroll processing."""
    input_file = 'employees.csv'  # Input CSV file with employee data
    output_file = 'payroll_report.csv'  # Output CSV file for payroll report

    employees = read_employee_data(input_file)
    if employees:
        process_payroll(employees)
        write_payroll_report(employees, output_file)
        print(f"Payroll processing completed. Report saved to {output_file}.")

if __name__ == "__main__":
    main()
```

### Note:
- Ensure that the input CSV file `employees.csv` contains the columns: `EmployeeID`, `Name`, and `Salary`.
- Adjust the `TAX_RATE` and `MINIMUM_WAGE` constants according to the latest local regulations in Jordan.
