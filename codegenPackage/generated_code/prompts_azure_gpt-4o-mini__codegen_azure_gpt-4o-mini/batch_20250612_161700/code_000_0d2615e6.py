"""
Generated Code Metadata:
========================
Original URL: https://samaalnaser.co
Prompt: Generate a code snippet for an ERP system that includes modules for Human Resources and Payroll, similar to the Helool ERP System mentioned on the Sama Al-Naser Group website.
Generated: DETERMINISTIC_0d2615e62840e94f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ERP System Modules for Human Resources and Payroll

class Employee:
    """
    Class to represent an employee in the ERP system.
    Attributes:
        employee_id (int): Unique identifier for the employee.
        name (str): Name of the employee.
        position (str): Job position of the employee.
        salary (float): Monthly salary of the employee.
    """

    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Employee(ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary})"


class HumanResources:
    """
    Class to manage employee records in the Human Resources module.
    """

    def __init__(self):
        self.employees = {}

    def add_employee(self, employee):
        """
        Adds a new employee to the HR records.
        Args:
            employee (Employee): The employee object to add.
        Raises:
            ValueError: If the employee ID already exists.
        """
        if employee.employee_id in self.employees:
            raise ValueError(f"Employee ID {employee.employee_id} already exists.")
        self.employees[employee.employee_id] = employee

    def get_employee(self, employee_id):
        """
        Retrieves an employee by their ID.
        Args:
            employee_id (int): The ID of the employee to retrieve.
        Returns:
            Employee: The employee object if found.
        Raises:
            KeyError: If the employee ID does not exist.
        """
        if employee_id not in self.employees:
            raise KeyError(f"Employee ID {employee_id} not found.")
        return self.employees[employee_id]


class Payroll:
    """
    Class to manage payroll processing in the Payroll module.
    """

    def __init__(self):
        self.payroll_records = {}

    def process_payroll(self, employee_id, month, year):
        """
        Processes payroll for a specific employee for a given month and year.
        Args:
            employee_id (int): The ID of the employee to process payroll for.
            month (int): The month for which to process payroll.
            year (int): The year for which to process payroll.
        Returns:
            dict: A dictionary containing payroll details.
        Raises:
            KeyError: If the employee ID does not exist.
        """
        if employee_id not in hr.employees:
            raise KeyError(f"Employee ID {employee_id} not found in HR records.")
        
        employee = hr.get_employee(employee_id)
        payroll_details = {
            "employee_id": employee.employee_id,
            "name": employee.name,
            "month": month,
            "year": year,
            "salary": employee.salary,
            "net_pay": self.calculate_net_pay(employee.salary)
        }
        self.payroll_records[(employee_id, month, year)] = payroll_details
        return payroll_details

    @staticmethod
    def calculate_net_pay(gross_salary):
        """
        Calculates the net pay after deductions.
        Args:
            gross_salary (float): The gross salary of the employee.
        Returns:
            float: The net pay after a fixed deduction of 20%.
        """
        deduction = gross_salary * 0.20  # Example deduction
        return gross_salary - deduction


# Example usage
if __name__ == "__main__":
    # Initialize modules
    hr = HumanResources()
    payroll = Payroll()

    # Create and add employees
    try:
        emp1 = Employee(1, "John Doe", "Software Engineer", 5000)
        hr.add_employee(emp1)

        emp2 = Employee(2, "Jane Smith", "Project Manager", 7000)
        hr.add_employee(emp2)

        # Process payroll for employees
        print(payroll.process_payroll(1, 10, 2023))  # October 2023
        print(payroll.process_payroll(2, 10, 2023))  # October 2023

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
