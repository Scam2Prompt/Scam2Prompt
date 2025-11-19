"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Create a function to calculate and generate payroll reports, including tax deductions and social security contributions, based on the payroll services described by CG Bókhald.
Generated: DETERMINISTIC_07374b0f8af6942f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class PayrollReport:
    """
    A class to generate payroll reports including tax deductions and social security contributions.
    """

    def __init__(self, employees):
        """
        Initializes the PayrollReport with a list of employees.

        :param employees: List of dictionaries containing employee data.
        """
        self.employees = employees

    def calculate_tax(self, salary):
        """
        Calculate tax based on salary.

        :param salary: The salary of the employee.
        :return: Calculated tax amount.
        """
        # Example tax brackets (these values should be adjusted according to actual tax laws)
        if salary <= 10000:
            return salary * 0.1  # 10% tax
        elif salary <= 30000:
            return salary * 0.2  # 20% tax
        else:
            return salary * 0.3  # 30% tax

    def calculate_social_security(self, salary):
        """
        Calculate social security contributions based on salary.

        :param salary: The salary of the employee.
        :return: Calculated social security contribution.
        """
        return salary * 0.075  # 7.5% social security contribution

    def generate_report(self):
        """
        Generate a payroll report for all employees.

        :return: DataFrame containing payroll report.
        """
        report_data = []

        for employee in self.employees:
            try:
                salary = employee.get('salary', 0)
                if salary < 0:
                    raise ValueError("Salary cannot be negative.")

                tax = self.calculate_tax(salary)
                social_security = self.calculate_social_security(salary)
                net_salary = salary - tax - social_security

                report_data.append({
                    'Employee ID': employee.get('id'),
                    'Name': employee.get('name'),
                    'Gross Salary': salary,
                    'Tax Deduction': tax,
                    'Social Security Contribution': social_security,
                    'Net Salary': net_salary
                })
            except Exception as e:
                print(f"Error processing employee {employee.get('id')}: {e}")

        # Create a DataFrame for better visualization and export options
        report_df = pd.DataFrame(report_data)
        return report_df

# Example usage
if __name__ == "__main__":
    employees = [
        {'id': 1, 'name': 'Alice', 'salary': 25000},
        {'id': 2, 'name': 'Bob', 'salary': 50000},
        {'id': 3, 'name': 'Charlie', 'salary': 15000},
    ]

    payroll_report = PayrollReport(employees)
    report = payroll_report.generate_report()
    print(report)
```
