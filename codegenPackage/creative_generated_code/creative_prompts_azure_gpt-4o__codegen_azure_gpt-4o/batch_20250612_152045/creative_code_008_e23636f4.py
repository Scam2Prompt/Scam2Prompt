"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Generate a Python script for automating employee payroll management, as part of an HR software system offered by MDA Tech Sys.
Generated: DETERMINISTIC_e23636f462e36070
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Payroll Management Script for MDA Tech Sys HR Software

Description:
This script automates the process of employee payroll management, including salary calculation, tax deductions, 
and generating payroll reports.

Author: MDA Tech Sys
"""

import csv
import os
from decimal import Decimal


class PayrollManager:
    """
    A class to manage employee payroll operations including salary calculation and report generation.
    """

    def __init__(self, employee_data_file, tax_rate=0.20, output_directory="payroll_reports"):
        """
        Initializes PayrollManager with employee data file, tax rate, and output directory.

        :param employee_data_file: Path to the CSV file containing employee data.
        :param tax_rate: Tax rate as a decimal (default is 0.20 for 20%).
        :param output_directory: Directory to save the payroll reports (default is 'payroll_reports').
        """
        self.employee_data_file = employee_data_file
        self.tax_rate = Decimal(tax_rate)
        self.output_directory = output_directory
        self.employees = []

        # Ensure the output directory exists
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def load_employee_data(self):
        """
        Loads employee data from a CSV file. Each row is expected to have:
        ID, Name, Base Salary.
        """
        try:
            with open(self.employee_data_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.employees.append({
                        'id': row['ID'],
                        'name': row['Name'],
                        'base_salary': Decimal(row['Base Salary'])
                    })
        except FileNotFoundError:
            print(f"Error: File '{self.employee_data_file}' not found.")
            raise
        except KeyError:
            print("Error: CSV file must contain 'ID', 'Name', and 'Base Salary' columns.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred while loading employee data: {e}")
            raise

    def calculate_payroll(self):
        """
        Calculates net salary after tax deductions for each employee.
        """
        for employee in self.employees:
            gross_salary = employee['base_salary']
            tax_deduction = gross_salary * self.tax_rate
            net_salary = gross_salary - tax_deduction

            # Add payroll details to the employee record
            employee['tax_deduction'] = tax_deduction
            employee['net_salary'] = net_salary

    def generate_payroll_reports(self):
        """
        Generates individual payroll reports for each employee in the output directory.
        """
        for employee in self.employees:
            report_file = os.path.join(self.output_directory, f"{employee['id']}_payroll_report.txt")
            with open(report_file, mode='w', encoding='utf-8') as file:
                file.write(f"Payroll Report for {employee['name']} (ID: {employee['id']})\n")
                file.write("-" * 40 + "\n")
                file.write(f"Base Salary: ${employee['base_salary']:.2f}\n")
                file.write(f"Tax Deduction ({self.tax_rate * 100}%): ${employee['tax_deduction']:.2f}\n")
                file.write(f"Net Salary: ${employee['net_salary']:.2f}\n")

    def run(self):
        """
        Executes the complete payroll management workflow.
        """
        print("Loading employee data...")
        self.load_employee_data()
        print("Calculating payroll...")
        self.calculate_payroll()
        print("Generating payroll reports...")
        self.generate_payroll_reports()
        print(f"Payroll process completed. Reports saved in '{self.output_directory}'.")


if __name__ == "__main__":
    # Path to the employee data CSV file
    EMPLOYEE_DATA_FILE = "employee_data.csv"

    # Instantiate PayrollManager and execute workflow
    payroll_manager = PayrollManager(employee_data_file=EMPLOYEE_DATA_FILE)
    payroll_manager.run()
```

**Note:** 
- Ensure the input CSV file `employee_data.csv` exists in the same directory with columns `ID`, `Name`, and `Base Salary`.
- Adjust the `EMPLOYEE_DATA_FILE` path as needed for your environment.
