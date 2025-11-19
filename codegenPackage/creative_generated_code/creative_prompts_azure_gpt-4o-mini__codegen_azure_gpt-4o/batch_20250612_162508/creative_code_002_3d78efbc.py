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
import datetime


class Employee:
    """
    A class to represent an employee in the payroll system.
    """

    def __init__(self, employee_id, name, hourly_rate):
        """
        Initialize the employee with ID, name, and hourly rate.
        :param employee_id: Unique identifier for the employee.
        :param name: Full name of the employee.
        :param hourly_rate: Hourly wage of the employee.
        """
        self.employee_id = employee_id
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0
        self.pay_history = []

    def log_hours(self, hours):
        """
        Log the hours worked by the employee.
        :param hours: Number of hours worked.
        :raises ValueError: If hours are negative.
        """
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        self.hours_worked += hours

    def calculate_pay(self):
        """
        Calculate the pay for the current period based on hours worked.
        :return: Total pay for the current pay period.
        """
        return self.hours_worked * self.hourly_rate

    def process_payment(self):
        """
        Process the payment for the employee, resetting hours worked and storing pay history.
        :return: Payment details for the processed period.
        """
        pay = self.calculate_pay()
        payment_record = {
            "date": datetime.date.today(),
            "hours_worked": self.hours_worked,
            "pay": pay,
        }
        self.pay_history.append(payment_record)
        self.hours_worked = 0  # Reset hours after payment
        return payment_record


class PayrollSystem:
    """
    A class to manage payroll for multiple employees.
    """

    def __init__(self):
        """
        Initialize the payroll system with an empty employee registry.
        """
        self.employees = {}

    def add_employee(self, employee):
        """
        Add an employee to the payroll system.
        :param employee: An instance of the Employee class.
        :raises ValueError: If an employee with the same ID already exists.
        """
        if employee.employee_id in self.employees:
            raise ValueError(f"Employee ID {employee.employee_id} already exists.")
        self.employees[employee.employee_id] = employee

    def log_hours(self, employee_id, hours):
        """
        Log hours worked for a specific employee.
        :param employee_id: ID of the employee.
        :param hours: Number of hours worked.
        :raises KeyError: If the employee ID does not exist.
        """
        if employee_id not in self.employees:
            raise KeyError(f"Employee ID {employee_id} not found.")
        self.employees[employee_id].log_hours(hours)

    def process_payroll(self):
        """
        Process payroll for all employees.
        :return: List of payment records for all employees.
        """
        payroll_records = []
        for employee in self.employees.values():
            payroll_records.append(employee.process_payment())
        return payroll_records

    def get_employee_pay_history(self, employee_id):
        """
        Retrieve the pay history for a specific employee.
        :param employee_id: ID of the employee.
        :return: List of payment records for the employee.
        :raises KeyError: If the employee ID does not exist.
        """
        if employee_id not in self.employees:
            raise KeyError(f"Employee ID {employee_id} not found.")
        return self.employees[employee_id].pay_history


if __name__ == "__main__":
    # Example usage of the payroll system.

    try:
        payroll = PayrollSystem()

        # Add employees
        payroll.add_employee(Employee(employee_id=1, name="Alice Johnson", hourly_rate=20.0))
        payroll.add_employee(Employee(employee_id=2, name="Bob Smith", hourly_rate=15.0))

        # Log hours worked
        payroll.log_hours(employee_id=1, hours=40)
        payroll.log_hours(employee_id=2, hours=35)

        # Process payroll for all employees
        payments = payroll.process_payroll()
        for payment in payments:
            print(payment)

        # Retrieve pay history for an employee
        pay_history = payroll.get_employee_pay_history(employee_id=1)
        print("Pay history for employee 1:", pay_history)

    except Exception as e:
        print(f"An error occurred: {e}")
```
