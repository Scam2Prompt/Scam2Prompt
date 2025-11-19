"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: How can I implement a system for managing human resources in a public sector organization, using the integrated management solutions provided by Licitare?
Generated: DETERMINISTIC_472d61675f852d6f
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
import json
from typing import List, Dict, Any

# Define a class to represent an Employee in the HR system
class Employee:
    def __init__(self, emp_id: int, name: str, position: str):
        """
        Initialize an Employee instance.

        :param emp_id: Unique identifier for the employee
        :param name: Name of the employee
        :param position: Job position of the employee
        """
        self.emp_id = emp_id
        self.name = name
        self.position = position

    def to_dict(self) -> Dict[str, Any]:
        """Convert employee details to a dictionary."""
        return {
            'emp_id': self.emp_id,
            'name': self.name,
            'position': self.position
        }

# Define the HR Management System class
class HRManagementSystem:
    def __init__(self):
        """Initialize the HR Management System with an empty employee list."""
        self.employees: List[Employee] = []

    def add_employee(self, emp_id: int, name: str, position: str) -> None:
        """
        Add a new employee to the system.

        :param emp_id: Unique identifier for the employee
        :param name: Name of the employee
        :param position: Job position of the employee
        :raises ValueError: If an employee with the same ID already exists
        """
        if any(emp.emp_id == emp_id for emp in self.employees):
            raise ValueError(f"Employee with ID {emp_id} already exists.")
        new_employee = Employee(emp_id, name, position)
        self.employees.append(new_employee)

    def remove_employee(self, emp_id: int) -> None:
        """
        Remove an employee from the system by ID.

        :param emp_id: Unique identifier for the employee to be removed
        :raises ValueError: If no employee with the given ID exists
        """
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return
        raise ValueError(f"No employee found with ID {emp_id}.")

    def get_employee(self, emp_id: int) -> Dict[str, Any]:
        """
        Get an employee's details by ID.

        :param emp_id: Unique identifier for the employee
        :return: Employee details as a dictionary
        :raises ValueError: If no employee with the given ID exists
        """
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee.to_dict()
        raise ValueError(f"No employee found with ID {emp_id}.")

    def list_employees(self) -> List[Dict[str, Any]]:
        """List all employees in the system."""
        return [emp.to_dict() for emp in self.employees]

    def save_to_file(self, filename: str) -> None:
        """
        Save the employee data to a JSON file.

        :param filename: The name of the file to save data to
        :raises IOError: If there is an error writing to the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_employees(), file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load employee data from a JSON file.

        :param filename: The name of the file to load data from
        :raises IOError: If there is an error reading from the file
        :raises json.JSONDecodeError: If the file contains invalid JSON
        """
        try:
            with open(filename, 'r') as file:
                employee_data = json.load(file)
                for emp in employee_data:
                    self.add_employee(emp['emp_id'], emp['name'], emp['position'])
        except IOError as e:
            raise IOError(f"Error loading from file {filename}: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data in file {filename}: {e}")

# Example usage of the HR Management System
if __name__ == "__main__":
    hr_system = HRManagementSystem()
    try:
        # Adding employees
        hr_system.add_employee(1, "Alice Smith", "Manager")
        hr_system.add_employee(2, "Bob Johnson", "Developer")

        # Listing employees
        print("Employees:", hr_system.list_employees())

        # Saving to a file
        hr_system.save_to_file("employees.json")

        # Loading from a file
        hr_system.load_from_file("employees.json")
        print("Loaded Employees:", hr_system.list_employees())
        
        # Removing an employee
        hr_system.remove_employee(1)
        print("Employees after removal:", hr_system.list_employees())

    except Exception as e:
        print(f"An error occurred: {e}")
```
