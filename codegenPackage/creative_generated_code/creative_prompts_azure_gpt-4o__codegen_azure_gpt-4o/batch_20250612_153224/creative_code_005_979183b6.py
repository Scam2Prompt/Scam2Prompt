"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Develop a payroll system for school staff, including pay slip generation and salary calculations, inspired by Him Saral's Payroll module.
Generated: DETERMINISTIC_979183b682e8791d
Batch ID: 20250612_153224
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
    Represents a school staff member with details required for payroll processing.
    Attributes:
        name (str): Name of the employee.
        employee_id (str): Unique ID for the employee.
        base_salary (float): Monthly base salary of the employee.
        allowances (float): Additional allowances.
        deductions (float): Deductions from the salary.
    """
    def __init__(self, name, employee_id, base_salary, allowances=0.0, deductions=0.0):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
        self.allowances = allowances
        self.deductions = deductions

    def calculate_net_salary(self):
        """
        Calculates the net salary of the employee after adding allowances and deducting deductions.
        Returns:
            float: Net salary of the employee.
        """
        return self.base_salary + self.allowances - self.deductions

    def generate_pay_slip(self):
        """
        Generates a pay slip for the employee.
        Returns:
            str: The formatted pay slip containing salary details.
        """
        net_salary = self.calculate_net_salary()
        pay_slip = (
            f"PAY SLIP\n"
            f"Date: {datetime.date.today()}\n"
            f"Employee Name: {self.name}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Base Salary: ${self.base_salary:.2f}\n"
            f"Allowances: ${self.allowances:.2f}\n"
            f"Deductions: ${self.deductions:.2f}\n"
            f"Net Salary: ${net_salary:.2f}\n"
        )
        return pay_slip


class SchoolPayrollSystem:
    """
    A payroll system for managing school staff salaries and pay slips.
    Attributes:
        employees (list): List of registered employees in the payroll system.
    """
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        """
        Adds a new employee to the payroll system.
        Args:
            employee (Employee): The Employee object to be added.
        """
        if not isinstance(employee, Employee):
            raise ValueError("Invalid employee object.")
        self.employees.append(employee)

    def generate_all_pay_slips(self):
        """
        Generates pay slips for all employees in the payroll system.
        Returns:
            list: List of pay slips for all employees.
        """
        pay_slips = []
        for employee in self.employees:
            pay_slips.append(employee.generate_pay_slip())
        return pay_slips

    def get_employee_by_id(self, employee_id):
        """
        Fetches the employee details using employee ID.
        Args:
            employee_id (str): Employee ID to search for.
        Returns:
            Employee: The requested Employee object or None if not found.
        """
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None


# Example Usage
if __name__ == "__main__":
    # Initialize the payroll system
    payroll_system = SchoolPayrollSystem()

    # Add employees
    employee1 = Employee(name="Alice Johnson", employee_id="E001", base_salary=5000.00, allowances=300.00, deductions=100.00)
    employee2 = Employee(name="Bob Smith", employee_id="E002", base_salary=4500.00, allowances=250.00, deductions=75.00)
    
    payroll_system.add_employee(employee1)
    payroll_system.add_employee(employee2)

    # Generate pay slips for all employees
    pay_slips = payroll_system.generate_all_pay_slips()
    for pay_slip in pay_slips:
        print(pay_slip)
        
    # Fetch an employee by ID
    employee = payroll_system.get_employee_by_id("E001")
    if employee:
        print(f"Employee Found: {employee.name}")
    else:
        print("Employee not found.")
```
