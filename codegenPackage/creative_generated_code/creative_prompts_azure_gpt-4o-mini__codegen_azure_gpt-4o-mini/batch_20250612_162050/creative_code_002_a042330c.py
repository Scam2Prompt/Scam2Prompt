"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cgbokhald.is
Prompt: Write a code snippet that calculates payroll and generates payslips, referencing the payroll services provided by CGBókhald.
Generated: DETERMINISTIC_a042330cd5d0eb17
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any


class Employee:
    """Class to represent an employee for payroll purposes."""
    
    def __init__(self, id: int, name: str, hourly_rate: float):
        self.id = id
        self.name = name
        self.hourly_rate = hourly_rate
    
    def calculate_pay(self, hours_worked: float) -> float:
        """Calculate the total pay for the employee based on hours worked."""
        if hours_worked < 0:
            raise ValueError("Hours worked cannot be negative.")
        return self.hourly_rate * hours_worked


class Payroll:
    """Class to manage payroll calculations and payslip generation."""
    
    def __init__(self):
        self.employees: List[Employee] = []
    
    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the payroll system."""
        self.employees.append(employee)
    
    def generate_payslip(self, employee_id: int, hours_worked: float) -> Dict[str, Any]:
        """Generate a payslip for a specified employee."""
        # Find the employee by ID
        employee = next((emp for emp in self.employees if emp.id == employee_id), None)
        if employee is None:
            raise ValueError(f"Employee with ID {employee_id} not found.")
        
        # Calculate pay
        pay = employee.calculate_pay(hours_worked)
        
        # Create a payslip
        payslip = {
            "employee_id": employee.id,
            "employee_name": employee.name,
            "hours_worked": hours_worked,
            "pay": pay
        }
        return payslip
    
    def generate_payslips(self, hours_worked_dict: Dict[int, float]) -> List[Dict[str, Any]]:
        """Generate payslips for multiple employees based on a dictionary of hours worked."""
        payslips = []
        for employee_id, hours_worked in hours_worked_dict.items():
            try:
                payslip = self.generate_payslip(employee_id, hours_worked)
                payslips.append(payslip)
            except ValueError as e:
                print(f"Error generating payslip for Employee ID {employee_id}: {e}")
        return payslips


def main():
    """Main function to demonstrate payroll processing."""
    # Initialize payroll system
    payroll = Payroll()
    
    # Add employees
    payroll.add_employee(Employee(1, "Alice Johnson", 25.0))
    payroll.add_employee(Employee(2, "Bob Smith", 30.0))
    payroll.add_employee(Employee(3, "Charlie Brown", 28.0))
    
    # Define hours worked for each employee
    hours_worked_dict = {
        1: 40,
        2: 38,
        3: 42,
    }
    
    # Generate payslips
    payslips = payroll.generate_payslips(hours_worked_dict)
    
    # Output payslips as JSON
    print(json.dumps(payslips, indent=4))


if __name__ == "__main__":
    main()
```
