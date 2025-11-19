"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Implement a system to track and analyze payroll benefits, inspired by the "Beneficios Sociales" course demo available on AulaContable.
Generated: DETERMINISTIC_f7547bb1d64da928
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Employee:
    """Class to represent an employee with payroll benefits."""
    
    def __init__(self, employee_id: int, name: str, benefits: Dict[str, float]):
        """
        Initialize an Employee instance.

        :param employee_id: Unique identifier for the employee
        :param name: Name of the employee
        :param benefits: Dictionary of benefits with their corresponding values
        """
        self.employee_id = employee_id
        self.name = name
        self.benefits = benefits

    def total_benefits(self) -> float:
        """Calculate the total value of benefits for the employee."""
        return sum(self.benefits.values())

    def __str__(self) -> str:
        """String representation of the Employee instance."""
        return f"Employee(ID: {self.employee_id}, Name: {self.name}, Total Benefits: {self.total_benefits()})"


class PayrollSystem:
    """Class to manage a payroll system for employees."""
    
    def __init__(self):
        """Initialize the PayrollSystem with an empty employee list."""
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """
        Add an employee to the payroll system.

        :param employee: Employee instance to be added
        """
        self.employees.append(employee)

    def get_employee_benefits(self, employee_id: int) -> Dict[str, Any]:
        """
        Retrieve benefits for a specific employee.

        :param employee_id: Unique identifier for the employee
        :return: Dictionary containing employee's benefits or an error message
        """
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return {
                    "employee_id": employee.employee_id,
                    "name": employee.name,
                    "benefits": employee.benefits,
                    "total_benefits": employee.total_benefits()
                }
        return {"error": "Employee not found"}

    def save_to_file(self, filename: str) -> None:
        """
        Save the payroll data to a JSON file.

        :param filename: Name of the file to save the data
        """
        try:
            with open(filename, 'w') as file:
                json.dump([employee.__dict__ for employee in self.employees], file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load payroll data from a JSON file.

        :param filename: Name of the file to load the data from
        """
        try:
            with open(filename, 'r') as file:
                employees_data = json.load(file)
                for emp_data in employees_data:
                    employee = Employee(emp_data['employee_id'], emp_data['name'], emp_data['benefits'])
                    self.add_employee(employee)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    payroll_system = PayrollSystem()

    # Adding employees
    payroll_system.add_employee(Employee(1, "Alice", {"Health Insurance": 200.0, "Retirement Fund": 150.0}))
    payroll_system.add_employee(Employee(2, "Bob", {"Health Insurance": 250.0, "Retirement Fund": 200.0}))

    # Retrieving benefits
    print(payroll_system.get_employee_benefits(1))
    print(payroll_system.get_employee_benefits(3))  # Non-existent employee

    # Saving to file
    payroll_system.save_to_file("payroll_data.json")

    # Loading from file
    new_payroll_system = PayrollSystem()
    new_payroll_system.load_from_file("payroll_data.json")
    print(new_payroll_system.get_employee_benefits(1))
```
