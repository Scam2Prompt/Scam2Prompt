"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samaalnaser.co
Prompt: Generate a code snippet for an ERP system that includes modules for Human Resources and Payroll, similar to the Helool ERP System mentioned on the Sama Al-Naser Group website.
Generated: DETERMINISTIC_0d2615e62840e94f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# ERP System Modules: Human Resources and Payroll

class Employee:
    """
    Class to represent an employee in the system.
    """
    def __init__(self, employee_id, name, position, salary):
        """
        Initialize a new Employee instance.

        :param employee_id: Unique identifier for the employee
        :param name: Full name of the employee
        :param position: Job position of the employee
        :param salary: Salary of the employee
        """
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        """
        Display the employee's information.
        """
        return f"ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"


class HRModule:
    """
    Class to handle Human Resources functionalities.
    """
    def __init__(self):
        """
        Initialize the HR Module with an empty employee list.
        """
        self.employees = {}

    def add_employee(self, employee):
        """
        Add a new employee to the system.

        :param employee: Employee instance to be added
        :raises ValueError: If employee with the same ID already exists
        """
        if employee.employee_id in self.employees:
            raise ValueError(f"Employee ID {employee.employee_id} already exists.")
        self.employees[employee.employee_id] = employee

    def get_employee(self, employee_id):
        """
        Retrieve an employee by ID.

        :param employee_id: ID of the employee to retrieve
        :return: Employee instance if found, else None
        """
        return self.employees.get(employee_id, None)

    def list_employees(self):
        """
        List all employees in the system.
        """
        return [emp.display_info() for emp in self.employees.values()]


class PayrollModule:
    """
    Class to handle Payroll functionalities.
    """
    def __init__(self, hr_module):
        """
        Initialize the Payroll Module with reference to HR Module.

        :param hr_module: Instance of HRModule to access employee data
        """
        self.hr_module = hr_module

    def calculate_payroll(self, employee_id):
        """
        Calculate the payroll for a specific employee.

        :param employee_id: ID of the employee to calculate payroll for
        :return: Payroll amount if employee exists, else None
        :raises ValueError: If employee does not exist
        """
        employee = self.hr_module.get_employee(employee_id)
        if not employee:
            raise ValueError(f"Employee with ID {employee_id} does not exist.")
        return employee.salary


# Example usage
if __name__ == "__main__":
    # Create HR Module
    hr_module = HRModule()

    # Add employees
    try:
        emp1 = Employee(1, "John Doe", "Software Engineer", 75000)
        emp2 = Employee(2, "Jane Smith", "Project Manager", 90000)
        
        hr_module.add_employee(emp1)
        hr_module.add_employee(emp2)

        # List employees
        for info in hr_module.list_employees():
            print(info)

        # Create Payroll Module
        payroll_module = PayrollModule(hr_module)

        # Calculate payroll for an employee
        payroll = payroll_module.calculate_payroll(1)
        print(f"Payroll for employee 1: ${payroll}")

    except ValueError as e:
        print(f"Error: {e}")
```
