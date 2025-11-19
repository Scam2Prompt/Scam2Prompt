"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Write a code snippet that calculates payroll and generates payslips, referencing the payroll services provided by CGBókhald.
Generated: DETERMINISTIC_a042330cd5d0eb17
Batch ID: 20250612_162050
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
from decimal import Decimal, getcontext
from typing import List, Dict, Optional

# Set precision for Decimal calculations
getcontext().prec = 2

class Employee:
    """Represents an employee with payroll-related information."""
    
    def __init__(self, employee_id: str, name: str, hourly_rate: Decimal, tax_rate: Decimal):
        self.employee_id = employee_id
        self.name = name
        self.hourly_rate = hourly_rate
        self.tax_rate = tax_rate
        self.hours_worked = Decimal('0.00')
    
    def add_hours(self, hours: Decimal) -> None:
        """Add hours worked by the employee."""
        if hours < Decimal('0.00'):
            raise ValueError("Hours worked cannot be negative")
        self.hours_worked += hours
    
    def calculate_gross_pay(self) -> Decimal:
        """Calculate gross pay based on hours worked and hourly rate."""
        return self.hours_worked * self.hourly_rate
    
    def calculate_tax(self) -> Decimal:
        """Calculate tax amount based on gross pay and tax rate."""
        gross_pay = self.calculate_gross_pay()
        return gross_pay * self.tax_rate
    
    def calculate_net_pay(self) -> Decimal:
        """Calculate net pay after tax deductions."""
        gross_pay = self.calculate_gross_pay()
        tax = self.calculate_tax()
        return gross_pay - tax

class PayrollSystem:
    """Handles payroll calculations and payslip generation."""
    
    def __init__(self):
        self.employees: Dict[str, Employee] = {}
    
    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the payroll system."""
        if employee.employee_id in self.employees:
            raise ValueError(f"Employee with ID {employee.employee_id} already exists")
        self.employees[employee.employee_id] = employee
    
    def process_payroll(self, period_start: datetime.date, period_end: datetime.date) -> List[Dict]:
        """Process payroll for all employees and return payslip data."""
        if period_start > period_end:
            raise ValueError("Period start date cannot be after period end date")
        
        payslips = []
        for employee in self.employees.values():
            if employee.hours_worked <= Decimal('0.00'):
                continue  # Skip employees with no hours worked
            
            payslip = {
                'employee_id': employee.employee_id,
                'name': employee.name,
                'period_start': period_start.strftime('%Y-%m-%d'),
                'period_end': period_end.strftime('%Y-%m-%d'),
                'hours_worked': float(employee.hours_worked),
                'hourly_rate': float(employee.hourly_rate),
                'gross_pay': float(employee.calculate_gross_pay()),
                'tax_rate': float(employee.tax_rate),
                'tax_amount': float(employee.calculate_tax()),
                'net_pay': float(employee.calculate_net_pay()),
                'processed_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            payslips.append(payslip)
            employee.hours_worked = Decimal('0.00')  # Reset hours for next period
        
        return payslips
    
    def export_payslips_to_csv(self, payslips: List[Dict], filename: str) -> None:
        """Export payslip data to a CSV file."""
        if not payslips:
            raise ValueError("No payslip data to export")
        
        fieldnames = [
            'employee_id', 'name', 'period_start', 'period_end',
            'hours_worked', 'hourly_rate', 'gross_pay', 'tax_rate',
            'tax_amount', 'net_pay', 'processed_at'
        ]
        
        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(payslips)
        except IOError as e:
            raise IOError(f"Failed to write payslips to CSV: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize payroll system
    payroll = PayrollSystem()
    
    # Add employees (data would typically come from a database or external system like CGBókhald)
    payroll.add_employee(Employee("E001", "John Doe", Decimal('25.50'), Decimal('0.20')))
    payroll.add_employee(Employee("E002", "Jane Smith", Decimal('30.75'), Decimal('0.25')))
    
    # Record hours worked (would typically come from timesheets)
    payroll.employees["E001"].add_hours(Decimal('40.00'))
    payroll.employees["E002"].add_hours(Decimal('35.50'))
    
    # Process payroll for a period
    today = datetime.date.today()
    period_start = today - datetime.timedelta(days=14)
    payslips = payroll.process_payroll(period_start, today)
    
    # Export payslips to CSV
    try:
        payroll.export_payslips_to_csv(payslips, f"payslips_{today.strftime('%Y%m')}.csv")
        print(f"Successfully generated {len(payslips)} payslips")
    except Exception as e:
        print(f"Error generating payslips: {str(e)}")
```
