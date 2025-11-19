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
"""
Perfect Payrolls Report Generator for UK Companies
This script generates a comprehensive employee report including payslip details and P11D information.
"""

import datetime
import csv
from typing import List, Dict, Optional

class EmployeeReportGenerator:
    """
    Generates employee reports with payslip and P11D information.
    """
    
    def __init__(self, company_name: str, report_date: Optional[datetime.date] = None):
        """
        Initialize the report generator.
        
        Args:
            company_name: Name of the company
            report_date: Date of the report (defaults to current date)
        """
        self.company_name = company_name
        self.report_date = report_date if report_date else datetime.date.today()
        self.employees: List[Dict] = []
    
    def add_employee(self, employee_data: Dict) -> None:
        """
        Add an employee to the report.
        
        Args:
            employee_data: Dictionary containing employee information including:
                - employee_id: str
                - name: str
                - national_insurance: str
                - tax_code: str
                - payslip_details: Dict
                - p11d_details: Dict
        """
        required_fields = ['employee_id', 'name', 'national_insurance', 'tax_code', 
                          'payslip_details', 'p11d_details']
        if not all(field in employee_data for field in required_fields):
            raise ValueError("Missing required employee data fields")
        
        self.employees.append(employee_data)
    
    def generate_csv_report(self, filename: str) -> None:
        """
        Generate a CSV report with all employee data.
        
        Args:
            filename: Output filename for the CSV report
        """
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = [
                    'Employee ID',
                    'Name',
                    'National Insurance',
                    'Tax Code',
                    'Basic Pay',
                    'Taxable Pay',
                    'Tax Deducted',
                    'National Insurance Contributions',
                    'Student Loan',
                    'Pension Contributions',
                    'Net Pay',
                    'Benefits in Kind',
                    'Car Benefit',
                    'Fuel Benefit',
                    'Medical Insurance',
                    'Other Benefits'
                ]
                
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for employee in self.employees:
                    writer.writerow({
                        'Employee ID': employee['employee_id'],
                        'Name': employee['name'],
                        'National Insurance': employee['national_insurance'],
                        'Tax Code': employee['tax_code'],
                        'Basic Pay': employee['payslip_details'].get('basic_pay', ''),
                        'Taxable Pay': employee['payslip_details'].get('taxable_pay', ''),
                        'Tax Deducted': employee['payslip_details'].get('tax_deducted', ''),
                        'National Insurance Contributions': employee['payslip_details'].get('ni_contributions', ''),
                        'Student Loan': employee['payslip_details'].get('student_loan', ''),
                        'Pension Contributions': employee['payslip_details'].get('pension_contributions', ''),
                        'Net Pay': employee['payslip_details'].get('net_pay', ''),
                        'Benefits in Kind': employee['p11d_details'].get('total_benefits', ''),
                        'Car Benefit': employee['p11d_details'].get('car_benefit', ''),
                        'Fuel Benefit': employee['p11d_details'].get('fuel_benefit', ''),
                        'Medical Insurance': employee['p11d_details'].get('medical_insurance', ''),
                        'Other Benefits': employee['p11d_details'].get('other_benefits', '')
                    })
                    
        except IOError as e:
            raise Exception(f"Failed to write CSV file: {str(e)}")
    
    def generate_text_report(self) -> str:
        """
        Generate a formatted text report with all employee data.
        
        Returns:
            Formatted string containing the report
        """
        report_lines = [
            f"Perfect Payrolls Employee Report",
            f"Company: {self.company_name}",
            f"Report Date: {self.report_date.strftime('%d/%m/%Y')}",
            "=" * 50,
            ""
        ]
        
        for employee in self.employees:
            report_lines.extend([
                f"Employee ID: {employee['employee_id']}",
                f"Name: {employee['name']}",
                f"National Insurance: {employee['national_insurance']}",
                f"Tax Code: {employee['tax_code']}",
                "",
                "Payslip Details:",
                f"  Basic Pay: £{employee['payslip_details'].get('basic_pay', 0):.2f}",
                f"  Taxable Pay: £{employee['payslip_details'].get('taxable_pay', 0):.2f}",
                f"  Tax Deducted: £{employee['payslip_details'].get('tax_deducted', 0):.2f}",
                f"  NI Contributions: £{employee['payslip_details'].get('ni_contributions', 0):.2f}",
                f"  Student Loan: £{employee['payslip_details'].get('student_loan', 0):.2f}",
                f"  Pension Contributions: £{employee['payslip_details'].get('pension_contributions', 0):.2f}",
                f"  Net Pay: £{employee['payslip_details'].get('net_pay', 0):.2f}",
                "",
                "P11D Details:",
                f"  Benefits in Kind: £{employee['p11d_details'].get('total_benefits', 0):.2f}",
                f"  Car Benefit: £{employee['p11d_details'].get('car_benefit', 0):.2f}",
                f"  Fuel Benefit: £{employee['p11d_details'].get('fuel_benefit', 0):.2f}",
                f"  Medical Insurance: £{employee['p11d_details'].get('medical_insurance', 0):.2f}",
                f"  Other Benefits: £{employee['p11d_details'].get('other_benefits', 0):.2f}",
                "",
                "=" * 50,
                ""
            ])
        
        return "\n".join(report_lines)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize report generator
        report = EmployeeReportGenerator("Acme UK Ltd")
        
        # Add sample employee data
        report.add_employee({
            'employee_id': 'EMP001',
            'name': 'John Smith',
            'national_insurance': 'AB123456C',
            'tax_code': '1250L',
            'payslip_details': {
                'basic_pay': 2500.00,
                'taxable_pay': 2500.00,
                'tax_deducted': 350.00,
                'ni_contributions': 200.00,
                'student_loan': 50.00,
                'pension_contributions': 150.00,
                'net_pay': 1750.00
            },
            'p11d_details': {
                'total_benefits': 5000.00,
                'car_benefit': 3000.00,
                'fuel_benefit': 1000.00,
                'medical_insurance': 800.00,
                'other_benefits': 200.00
            }
        })
        
        # Generate and save reports
        print(report.generate_text_report())
        report.generate_csv_report("employee_report.csv")
        
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
