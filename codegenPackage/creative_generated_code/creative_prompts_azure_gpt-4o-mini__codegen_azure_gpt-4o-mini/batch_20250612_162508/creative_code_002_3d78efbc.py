"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calltpd.com
Prompt: Can you provide code examples for creating a payroll management system using Python?
Generated: DETERMINISTIC_3d78efbc12eabf78
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# payroll_management.py

class Employee:
    """Class to represent an employee in the payroll system."""
    
    def __init__(self, employee_id, name, hourly_rate):
        """
        Initialize a new employee instance.
        
        :param employee_id: Unique identifier for the employee
        :param name: Name of the employee
        :param hourly_rate: Hourly wage of the employee
        """
        self.employee_id = employee_id
        self.name = name
        self.hourly_rate = hourly_rate

    def calculate_pay(self, hours_worked):
        """
        Calculate the total pay for the employee based on hours worked.
        
        :param hours_worked: Number of hours worked in the pay period
        :return: Total pay for the period
        """
        if hours_worked < 0:
            raise ValueError("Hours worked cannot be negative.")
        total_pay = self.hourly_rate * hours_worked
        return total_pay


class Payroll:
    """Class to manage payroll operations."""
    
    def __init__(self):
        """Initialize the payroll manager with an empty employee list."""
        self.employees = {}

    def add_employee(self, employee):
        """
        Add a new employee to the payroll system.
        
        :param employee: Employee object to add
        """
        if employee.employee_id in self.employees:
            raise ValueError(f"Employee ID {employee.employee_id} already exists.")
        self.employees[employee.employee_id] = employee

    def process_payroll(self, employee_id, hours_worked):
        """
        Calculate and return the payroll for a specific employee.
        
        :param employee_id: The ID of the employee to process
        :param hours_worked: Hours worked by the employee in the pay period
        :return: Total pay for the employee
        """
        if employee_id not in self.employees:
            raise ValueError(f"Employee ID {employee_id} not found.")
        
        employee = self.employees[employee_id]
        return employee.calculate_pay(hours_worked)


def main():
    """Main function to demonstrate the payroll management system."""
    payroll = Payroll()

    # Adding employees
    try:
        emp1 = Employee(employee_id=1, name="Alice Johnson", hourly_rate=25.00)
        emp2 = Employee(employee_id=2, name="Bob Smith", hourly_rate=30.00)

        payroll.add_employee(emp1)
        payroll.add_employee(emp2)

        # Process payroll for employees
        print(f"Payroll for {emp1.name}: ${payroll.process_payroll(emp1.employee_id, 40):.2f}")
        print(f"Payroll for {emp2.name}: ${payroll.process_payroll(emp2.employee_id, 35):.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

This code represents a simple payroll management system in Python, capable of managing employees and calculating payroll based on hours worked. Proper exception handling is included to manage errors gracefully.
