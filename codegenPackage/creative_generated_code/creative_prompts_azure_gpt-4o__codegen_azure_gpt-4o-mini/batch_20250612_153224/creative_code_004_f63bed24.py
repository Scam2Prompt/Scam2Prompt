"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: Write a script to manage human resource processes in public administration, inspired by Licitare's "Gestão de Recursos Humanos" services.
Generated: DETERMINISTIC_f63bed2406aa4e32
Batch ID: 20250612_153224
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
    """Class to represent an employee in the HR management system."""
    
    def __init__(self, emp_id: int, name: str, department: str, position: str):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.position = position

    def to_dict(self) -> Dict[str, Any]:
        """Convert the employee object to a dictionary."""
        return {
            'id': self.emp_id,
            'name': self.name,
            'department': self.department,
            'position': self.position
        }


class HRManagement:
    """Class to manage the HR processes for public administration."""
    
    def __init__(self):
        self.employees: List[Employee] = []

    def add_employee(self, emp_id: int, name: str, department: str, position: str) -> None:
        """Add a new employee to the HR system.
        
        Args:
            emp_id (int): The ID of the employee.
            name (str): The name of the employee.
            department (str): The department of the employee.
            position (str): The position of the employee.
        """
        new_employee = Employee(emp_id, name, department, position)
        self.employees.append(new_employee)
        print(f"Employee {name} added successfully.")

    def remove_employee(self, emp_id: int) -> None:
        """Remove an employee from the HR system by employee ID.
        
        Args:
            emp_id (int): The ID of the employee to be removed.
        
        Raises:
            ValueError: If the employee ID is not found.
        """
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print(f"Employee ID {emp_id} removed successfully.")
                return
        raise ValueError(f"Employee ID {emp_id} not found.")

    def get_employee(self, emp_id: int) -> Employee:
        """Retrieve an employee's information by employee ID.
        
        Args:
            emp_id (int): The ID of the employee to be retrieved.
        
        Returns:
            Employee: The employee object.
        
        Raises:
            ValueError: If the employee ID is not found.
        """
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee
        raise ValueError(f"Employee ID {emp_id} not found.")

    def list_employees(self) -> List[Dict[str, Any]]:
        """List all employees in the HR system.
        
        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing employee information.
        """
        return [employee.to_dict() for employee in self.employees]

    def save_to_file(self, filename: str) -> None:
        """Save employee data to a JSON file.
        
        Args:
            filename (str): The name of the file to save employee data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_employees(), file, indent=4)
            print(f"Employee data saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load employee data from a JSON file.
        
        Args:
            filename (str): The name of the file to load employee data from.
        
        Raises:
            Exception: If there is an error loading the file.
        """
        try:
            with open(filename, 'r') as file:
                employee_data = json.load(file)
                for data in employee_data:
                    self.add_employee(data['id'], data['name'], data['department'], data['position'])
            print(f"Employee data loaded from {filename}.")
        except Exception as e:
            print(f"An error occurred while loading from file: {e}")

# Example usage of the HRManagement class
if __name__ == "__main__":
    hr_system = HRManagement()
    
    # Adding employees
    hr_system.add_employee(1, "Alice Smith", "Finance", "Accountant")
    hr_system.add_employee(2, "Bob Johnson", "IT", "Developer")
    
    # Listing employees
    print(hr_system.list_employees())

    # Saving to file
    hr_system.save_to_file("employees.json")

    # Loading from file
    hr_system.load_from_file("employees.json")

    # Removing an employee
    try:
        hr_system.remove_employee(1)
    except ValueError as e:
        print(e)

    # Final employee list
    print(hr_system.list_employees())
```
