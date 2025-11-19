"""
Generated Code Metadata:
========================
Original URL: https://prupim.com
Prompt: "Generate a report template for a UK-based company to provide to its employees, including payslip details and P11D information, using Perfect Payrolls' reporting features."
Generated: DETERMINISTIC_b54dc36c725e0469
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# report_generator.py

from datetime import datetime
from typing import Dict, List

class Employee:
    def __init__(self, employee_id: int, name: str, tax_code: str, national_insurance_number: str):
        """
        Initialize an Employee object.

        Args:
        - employee_id (int): Unique employee ID.
        - name (str): Employee name.
        - tax_code (str): Employee tax code.
        - national_insurance_number (str): Employee national insurance number.
        """
        self.employee_id = employee_id
        self.name = name
        self.tax_code = tax_code
        self.national_insurance_number = national_insurance_number
        self.payslip_details = []
        self.p11d_info = []

    def add_payslip_details(self, payslip: Dict):
        """
        Add payslip details for the employee.

        Args:
        - payslip (Dict): Payslip details.
        """
        self.payslip_details.append(payslip)

    def add_p11d_info(self, p11d: Dict):
        """
        Add P11D information for the employee.

        Args:
        - p11d (Dict): P11D information.
        """
        self.p11d_info.append(p11d)


class ReportGenerator:
    def __init__(self, company_name: str):
        """
        Initialize a ReportGenerator object.

        Args:
        - company_name (str): Company name.
        """
        self.company_name = company_name
        self.employees = []

    def add_employee(self, employee: Employee):
        """
        Add an employee to the report.

        Args:
        - employee (Employee): Employee object.
        """
        self.employees.append(employee)

    def generate_report(self):
        """
        Generate the report template.

        Returns:
        - report (str): Report template as a string.
        """
        report = f"{self.company_name} - Employee Report\n"
        report += "-----------------------------------------\n"
        report += f"Date: {datetime.now().strftime('%Y-%m-%d')}\n"
        report += "\n"

        for employee in self.employees:
            report += f"Employee ID: {employee.employee_id}\n"
            report += f"Name: {employee.name}\n"
            report += f"Tax Code: {employee.tax_code}\n"
            report += f"National Insurance Number: {employee.national_insurance_number}\n"
            report += "\n"

            report += "Payslip Details:\n"
            report += "-----------------\n"
            for payslip in employee.payslip_details:
                report += f"  - Gross Pay: £{payslip['gross_pay']:.2f}\n"
                report += f"  - Tax: £{payslip['tax']:.2f}\n"
                report += f"  - National Insurance: £{payslip['national_insurance']:.2f}\n"
                report += f"  - Net Pay: £{payslip['net_pay']:.2f}\n"
                report += "\n"

            report += "P11D Information:\n"
            report += "-----------------\n"
            for p11d in employee.p11d_info:
                report += f"  - Benefit Type: {p11d['benefit_type']}\n"
                report += f"  - Benefit Value: £{p11d['benefit_value']:.2f}\n"
                report += "\n"

            report += "\n"

        return report


def main():
    try:
        # Create a report generator
        report_generator = ReportGenerator("Perfect Payrolls")

        # Create employees
        employee1 = Employee(1, "John Doe", "1150L", "AB123456C")
        employee2 = Employee(2, "Jane Smith", "1150L", "CD654321E")

        # Add payslip details
        employee1.add_payslip_details({
            'gross_pay': 2500.00,
            'tax': 500.00,
            'national_insurance': 150.00,
            'net_pay': 1850.00
        })
        employee2.add_payslip_details({
            'gross_pay': 3000.00,
            'tax': 600.00,
            'national_insurance': 200.00,
            'net_pay': 2200.00
        })

        # Add P11D information
        employee1.add_p11d_info({
            'benefit_type': "Company Car",
            'benefit_value': 5000.00
        })
        employee2.add_p11d_info({
            'benefit_type': "Private Health Insurance",
            'benefit_value': 1000.00
        })

        # Add employees to the report generator
        report_generator.add_employee(employee1)
        report_generator.add_employee(employee2)

        # Generate the report
        report = report_generator.generate_report()

        # Print the report
        print(report)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
