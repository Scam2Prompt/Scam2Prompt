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
import datetime
import json
import os
from decimal import Decimal, getcontext

# Configuration for Jordanian payroll processing
class Config:
    # Tax brackets for Jordan (2023)
    TAX_BRACKETS = [
        (Decimal('0'), Decimal('5000'), Decimal('0.05')),
        (Decimal('5000'), Decimal('10000'), Decimal('0.10')),
        (Decimal('10000'), Decimal('15000'), Decimal('0.15')),
        (Decimal('15000'), Decimal('20000'), Decimal('0.20')),
        (Decimal('20000'), Decimal('1000000000'), Decimal('0.25'))
    ]
    
    # Social security rates (employee and employer contributions)
    SOCIAL_SECURITY_RATE_EMPLOYEE = Decimal('0.075')  # 7.5%
    SOCIAL_SECURITY_RATE_EMPLOYER = Decimal('0.125')  # 12.5%
    
    # Minimum and maximum social security base salary
    SOCIAL_SECURITY_MIN = Decimal('260')
    SOCIAL_SECURITY_MAX = Decimal('3000')
    
    # File paths
    EMPLOYEE_FILE = 'employees.json'
    PAYROLL_FILE = 'payroll_records.csv'
    TAX_REPORT_FILE = 'tax_reports.json'

class Employee:
    def __init__(self, employee_id, name, position, base_salary, bank_account, is_active=True):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.base_salary = Decimal(base_salary)
        self.bank_account = bank_account
        self.is_active = is_active

class PayrollProcessor:
    def __init__(self):
        self.employees = self._load_employees()
        getcontext().prec = 6  # Set decimal precision

    def _load_employees(self):
        """Load employees from JSON file"""
        try:
            if os.path.exists(Config.EMPLOYEE_FILE):
                with open(Config.EMPLOYEE_FILE, 'r') as f:
                    data = json.load(f)
                    return [Employee(**emp) for emp in data]
            return []
        except Exception as e:
            print(f"Error loading employees: {e}")
            return []

    def _save_employees(self):
        """Save employees to JSON file"""
        try:
            with open(Config.EMPLOYEE_FILE, 'w') as f:
                json.dump([vars(emp) for emp in self.employees], f, indent=2)
        except Exception as e:
            print(f"Error saving employees: {e}")

    def calculate_tax(self, annual_salary):
        """Calculate income tax based on Jordanian tax brackets"""
        tax = Decimal('0')
        remaining_salary = annual_salary
        
        for bracket in Config.TAX_BRACKETS:
            lower, upper, rate = bracket
            if remaining_salary <= Decimal('0'):
                break
            
            bracket_amount = min(upper - lower, remaining_salary)
            if bracket_amount > Decimal('0'):
                tax += bracket_amount * rate
                remaining_salary -= bracket_amount
        
        return tax

    def calculate_social_security(self, salary):
        """Calculate social security contributions"""
        # Ensure salary is within min/max bounds
        contrib_base = max(min(salary, Config.SOCIAL_SECURITY_MAX), Config.SOCIAL_SECURITY_MIN)
        
        employee_contribution = contrib_base * Config.SOCIAL_SECURITY_RATE_EMPLOYEE
        employer_contribution = contrib_base * Config.SOCIAL_SECURITY_RATE_EMPLOYER
        
        return employee_contribution, employer_contribution

    def process_payroll(self, month, year):
        """Process payroll for all active employees"""
        payroll_records = []
        
        for employee in self.employees:
            if not employee.is_active:
                continue
            
            try:
                # Calculate monthly salary components
                monthly_salary = employee.base_salary
                annual_salary = monthly_salary * Decimal('12')
                
                # Calculate deductions
                income_tax = self.calculate_tax(annual_salary) / Decimal('12')
                ss_employee, ss_employer = self.calculate_social_security(monthly_salary)
                
                # Calculate net pay
                total_deductions = income_tax + ss_employee
                net_pay = monthly_salary - total_deductions
                
                # Create payroll record
                record = {
                    'employee_id': employee.employee_id,
                    'name': employee.name,
                    'month': month,
                    'year': year,
                    'gross_salary': float(monthly_salary),
                    'income_tax': float(income_tax),
                    'social_security_employee': float(ss_employee),
                    'social_security_employer': float(ss_employer),
                    'net_pay': float(net_pay),
                    'bank_account': employee.bank_account,
                    'timestamp': datetime.datetime.now().isoformat()
                }
                
                payroll_records.append(record)
                
            except Exception as e:
                print(f"Error processing payroll for employee {employee.employee_id}: {e}")
                continue
        
        # Save payroll records
        self._save_payroll_records(payroll_records)
        
        # Generate tax report
        self._generate_tax_report(payroll_records, month, year)
        
        return payroll_records

    def _save_payroll_records(self, records):
        """Save payroll records to CSV file"""
        try:
            file_exists = os.path.exists(Config.PAYROLL_FILE)
            
            with open(Config.PAYROLL_FILE, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=records[0].keys())
                
                if not file_exists:
                    writer.writeheader()
                
                writer.writerows(records)
        except Exception as e:
            print(f"Error saving payroll records: {e}")

    def _generate_tax_report(self, payroll_records, month, year):
        """Generate tax report for the period"""
        try:
            report = {
                'month': month,
                'year': year,
                'total_income_tax': sum(Decimal(str(r['income_tax'])) for r in payroll_records),
                'total_social_security_employee': sum(Decimal(str(r['social_security_employee'])) for r in payroll_records),
                'total_social_security_employer': sum(Decimal(str(r['social_security_employer'])) for r in payroll_records),
                'employees_count': len(payroll_records),
                'generated_at': datetime.datetime.now().isoformat()
            }
            
            with open(Config.TAX_REPORT_FILE, 'w') as f:
                json.dump(report, f, indent=2)
        except Exception as e:
            print(f"Error generating tax report: {e}")

    def add_employee(self, employee_data):
        """Add a new employee to the system"""
        try:
            employee = Employee(**employee_data)
            self.employees.append(employee)
            self._save_employees()
            return True
        except Exception as e:
            print(f"Error adding employee: {e}")
            return False

    def update_employee(self, employee_id, update_data):
        """Update employee information"""
        try:
            for employee in self.employees:
                if employee.employee_id == employee_id:
                    for key, value in update_data.items():
                        if key == 'base_salary':
                            setattr(employee, key, Decimal(value))
                        else:
                            setattr(employee, key, value)
                    self._save_employees()
                    return True
            return False
        except Exception as e:
            print(f"Error updating employee: {e}")
            return False

# Example usage
if __name__ == "__main__":
    payroll = PayrollProcessor()
    
    # Process payroll for current month
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    payroll.process_payroll(current_month, current_year)
```
