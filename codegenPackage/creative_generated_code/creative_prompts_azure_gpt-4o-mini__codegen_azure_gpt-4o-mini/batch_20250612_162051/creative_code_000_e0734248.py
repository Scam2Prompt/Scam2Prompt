"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacodechile.com
Prompt: Generate a code snippet for a custom software solution that addresses management issues in a business, as described by MetaCode's services.
Generated: DETERMINISTIC_e0734248d378b1aa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging
from typing import List, Dict

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Employee:
    """Represents an employee in the organization."""

    def __init__(self, emp_id: int, name: str, department: str):
        """
        Initializes an Employee object.

        :param emp_id: Unique identifier for the employee
        :param name: Name of the employee
        :param department: Department where the employee works
        """
        self.emp_id = emp_id
        self.name = name
        self.department = department

class EmployeeManagementSystem:
    """Manages the employee records and related operations."""

    def __init__(self):
        """Initializes the management system with an empty employee list."""
        self.employees: List[Employee] = []

    def add_employee(self, emp_id: int, name: str, department: str) -> None:
        """
        Adds a new employee to the system.

        :param emp_id: Unique identifier for the employee
        :param name: Name of the employee
        :param department: Department where the employee works
        """
        try:
            # Check for duplicate employee ID
            if any(emp.emp_id == emp_id for emp in self.employees):
                raise ValueError(f"Employee ID {emp_id} already exists.")
            new_employee = Employee(emp_id, name, department)
            self.employees.append(new_employee)
            logging.info(f"Added employee: {new_employee.name}, ID: {new_employee.emp_id}")
        except Exception as e:
            logging.error(f"Failed to add employee: {e}")

    def remove_employee(self, emp_id: int) -> None:
        """
        Removes an employee from the system by their ID.

        :param emp_id: Unique identifier for the employee
        """
        try:
            self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]
            logging.info(f"Removed employee with ID: {emp_id}")
        except Exception as e:
            logging.error(f"Failed to remove employee: {e}")

    def get_employee_list(self) -> List[Dict]:
        """
        Retrieves a list of all employees with their details.

        :return: A list of dictionaries containing employee details
        """
        return [{"emp_id": emp.emp_id, "name": emp.name, "department": emp.department} for emp in self.employees]

# Example usage of the Employee Management System
if __name__ == "__main__":
    ems = EmployeeManagementSystem()
    ems.add_employee(1, "Alice Smith", "Engineering")
    ems.add_employee(2, "Bob Johnson", "Marketing")
    ems.remove_employee(1)

    # Fetch and print the employee list
    employee_list = ems.get_employee_list()
    logging.info("Current Employees: %s", employee_list)
```
