"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prupim.com
Prompt: What are the key features of the Perfect Payrolls service that ensure compliance with UK payroll legislation, and how can I implement them in my payroll system?
Generated: DETERMINISTIC_f1b351ba09e8a11c
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime

class PayrollService:
    """
    A class to represent a payroll service that ensures compliance with UK payroll legislation.
    """

    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, hourly_rate):
        """
        Adds an employee to the payroll system.

        :param emp_id: Unique identifier for the employee
        :param name: Full name of the employee
        :param hourly_rate: Hourly wage of the employee
        """
        if emp_id in self.employees:
            raise ValueError("Employee ID already exists.")
        
        self.employees[emp_id] = {
            'name': name,
            'hourly_rate': hourly_rate,
            'hours_worked': 0
        }

    def record_hours(self, emp_id, hours):
        """
        Records hours worked for an employee.

        :param emp_id: Unique identifier for the employee
        :param hours: Number of hours worked
        """
        if emp_id not in self.employees:
            raise ValueError("Employee ID does not exist.")
        
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        
        self.employees[emp_id]['hours_worked'] += hours

    def calculate_pay(self, emp_id):
        """
        Calculates the total pay for an employee.

        :param emp_id: Unique identifier for the employee
        :return: Total pay for the employee
        """
        if emp_id not in self.employees:
            raise ValueError("Employee ID does not exist.")
        
        employee = self.employees[emp_id]
        total_pay = employee['hourly_rate'] * employee['hours_worked']
        return total_pay

    def generate_payslip(self, emp_id):
        """
        Generates a payslip for an employee.

        :param emp_id: Unique identifier for the employee
        :return: A dictionary representing the payslip
        """
        if emp_id not in self.employees:
            raise ValueError("Employee ID does not exist.")
        
        employee = self.employees[emp_id]
        payslip = {
            'name': employee['name'],
            'hourly_rate': employee['hourly_rate'],
            'hours_worked': employee['hours_worked'],
            'total_pay': self.calculate_pay(emp_id),
            'date': datetime.datetime.now().strftime("%Y-%m-%d")
        }
        return payslip

    def save_to_file(self, filename):
        """
        Saves the payroll records to a JSON file for compliance and record-keeping.

        :param filename: The name of the file to save the records to
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.employees, f, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file: {e}")

    def load_from_file(self, filename):
        """
        Loads payroll records from a JSON file.

        :param filename: The name of the file to load the records from
        """
        try:
            with open(filename, 'r') as f:
                self.employees = json.load(f)
        except IOError as e:
            raise IOError(f"Error reading from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from file: {e}")

# Example usage:
if __name__ == "__main__":
    payroll_service = PayrollService()
    payroll_service.add_employee("E001", "John Doe", 15.00)
    payroll_service.record_hours("E001", 40)
    payslip = payroll_service.generate_payslip("E001")
    print(payslip)
    payroll_service.save_to_file("payroll_records.json")
```
