"""
Generated Code Metadata:
========================
Original URL: https://calltpd.com
Prompt: Can you provide code examples for creating a payroll management system using Python?
Generated: DETERMINISTIC_3d78efbc12eabf78
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payroll_management_system.py

import csv
import os
from datetime import datetime
from typing import List, Dict, Optional

class Employee:
    """Represents an employee with payroll information."""
    
    def __init__(self, emp_id: str, name: str, hourly_rate: float, tax_rate: float = 0.2):
        """
        Initialize an Employee instance.
        
        Args:
            emp_id: Unique employee identifier
            name: Employee's full name
            hourly_rate: Pay rate per hour
            tax_rate: Tax deduction rate (default: 20%)
        """
        self.emp_id = emp_id
        self.name = name
        self.hourly_rate = hourly_rate
        self.tax_rate = tax_rate
        self.hours_worked = 0.0
        self.payment_history = []

    def add_hours(self, hours: float) -> None:
        """Add hours worked to the employee's record."""
        if hours < 0:
            raise ValueError("Hours worked cannot be negative")
        self.hours_worked += hours

    def calculate_pay(self) -> float:
        """Calculate gross pay before taxes."""
        return self.hours_worked * self.hourly_rate

    def calculate_tax(self) -> float:
        """Calculate tax amount based on gross pay."""
        return self.calculate_pay() * self.tax_rate

    def calculate_net_pay(self) -> float:
        """Calculate net pay after tax deduction."""
        return self.calculate_pay() - self.calculate_tax()

    def process_payment(self) -> Dict:
        """Process payment for current hours worked and reset hours."""
        if self.hours_worked <= 0:
            raise ValueError("No hours worked to process payment")
        
        payment = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'gross_pay': self.calculate_pay(),
            'tax': self.calculate_tax(),
            'net_pay': self.calculate_net_pay(),
            'hours_worked': self.hours_worked
        }
        
        self.payment_history.append(payment)
        self.hours_worked = 0.0
        return payment

    def get_payment_history(self) -> List[Dict]:
        """Return the employee's payment history."""
        return self.payment_history


class PayrollSystem:
    """Manages employee payroll data and operations."""
    
    def __init__(self):
        self.employees = {}
        self.load_data()

    def add_employee(self, emp_id: str, name: str, hourly_rate: float, tax_rate: float = 0.2) -> None:
        """Add a new employee to the payroll system."""
        if emp_id in self.employees:
            raise ValueError(f"Employee with ID {emp_id} already exists")
        self.employees[emp_id] = Employee(emp_id, name, hourly_rate, tax_rate)
        self.save_data()

    def get_employee(self, emp_id: str) -> Optional[Employee]:
        """Retrieve an employee by ID."""
        return self.employees.get(emp_id)

    def remove_employee(self, emp_id: str) -> None:
        """Remove an employee from the payroll system."""
        if emp_id not in self.employees:
            raise ValueError(f"Employee with ID {emp_id} not found")
        del self.employees[emp_id]
        self.save_data()

    def process_payroll(self) -> List[Dict]:
        """Process payroll for all employees with hours worked."""
        payroll_results = []
        for emp_id, employee in self.employees.items():
            if employee.hours_worked > 0:
                try:
                    payment = employee.process_payment()
                    payroll_results.append({
                        'emp_id': emp_id,
                        'name': employee.name,
                        **payment
                    })
                except ValueError as e:
                    print(f"Error processing payment for {employee.name}: {str(e)}")
        self.save_data()
        return payroll_results

    def generate_payroll_report(self) -> str:
        """Generate a payroll report for all employees."""
        report = []
        report.append("Payroll Report")
        report.append("=" * 50)
        report.append(f"{'ID':<10}{'Name':<20}{'Hours':<10}{'Gross Pay':<15}{'Tax':<10}{'Net Pay':<15}")
        
        for emp_id, employee in self.employees.items():
            if employee.hours_worked > 0:
                report.append(
                    f"{emp_id:<10}{employee.name:<20}{employee.hours_worked:<10.2f}"
                    f"${employee.calculate_pay():<14.2f}${employee.calculate_tax():<9.2f}"
                    f"${employee.calculate_net_pay():<14.2f}"
                )
        
        return "\n".join(report)

    def save_data(self) -> None:
        """Save employee data to a CSV file."""
        with open('employees.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['emp_id', 'name', 'hourly_rate', 'tax_rate'])
            for employee in self.employees.values():
                writer.writerow([
                    employee.emp_id,
                    employee.name,
                    employee.hourly_rate,
                    employee.tax_rate
                ])

    def load_data(self) -> None:
        """Load employee data from a CSV file."""
        if not os.path.exists('employees.csv'):
            return
            
        with open('employees.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    self.add_employee(
                        row['emp_id'],
                        row['name'],
                        float(row['hourly_rate']),
                        float(row['tax_rate'])
                    )
                except (ValueError, KeyError) as e:
                    print(f"Error loading employee data: {str(e)}")


# Example usage
if __name__ == "__main__":
    payroll = PayrollSystem()
    
    # Add some employees
    try:
        payroll.add_employee("E001", "John Doe", 25.0)
        payroll.add_employee("E002", "Jane Smith", 30.0, 0.25)
    except ValueError as e:
        print(f"Error adding employee: {str(e)}")
    
    # Record hours worked
    john = payroll.get_employee("E001")
    if john:
        john.add_hours(40)
        john.add_hours(5.5)  # Overtime
    
    jane = payroll.get_employee("E002")
    if jane:
        jane.add_hours(35)
    
    # Process payroll
    results = payroll.process_payroll()
    for payment in results:
        print(f"Processed payment for {payment['name']}: ${payment['net_pay']:.2f}")
    
    # Generate report
    print("\n" + payroll.generate_payroll_report())
```
