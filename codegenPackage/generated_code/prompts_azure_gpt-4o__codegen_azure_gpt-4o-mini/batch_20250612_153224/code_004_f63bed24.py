"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: Write a script to manage human resource processes in public administration, inspired by Licitare's "Gestão de Recursos Humanos" services.
Generated: DETERMINISTIC_f63bed2406aa4e32
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Employee:
    """Class to represent an employee in the HR management system."""
    
    def __init__(self, employee_id: int, name: str, position: str, department: str):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.department = department

    def to_dict(self) -> Dict[str, Any]:
        """Convert the employee object to a dictionary."""
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "position": self.position,
            "department": self.department
        }

class HRManagement:
    """Class to manage HR processes."""
    
    def __init__(self):
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add a new employee to the HR system."""
        self.employees.append(employee)
        logging.info(f"Added employee: {employee.name}")

    def remove_employee(self, employee_id: int) -> None:
        """Remove an employee from the HR system by employee ID."""
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]
        logging.info(f"Removed employee with ID: {employee_id}")

    def get_employee(self, employee_id: int) -> Employee:
        """Retrieve an employee by their ID."""
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        logging.error(f"Employee with ID {employee_id} not found.")
        raise ValueError(f"Employee with ID {employee_id} not found.")

    def list_employees(self) -> List[Dict[str, Any]]:
        """List all employees in the HR system."""
        return [emp.to_dict() for emp in self.employees]

    def save_to_file(self, filename: str) -> None:
        """Save the employee data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_employees(), file, indent=4)
            logging.info(f"Employee data saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save data to {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load employee data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                employees_data = json.load(file)
                self.employees = [Employee(**data) for data in employees_data]
            logging.info(f"Employee data loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load data from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    hr_system = HRManagement()
    
    # Adding employees
    hr_system.add_employee(Employee(1, "Alice Smith", "Manager", "HR"))
    hr_system.add_employee(Employee(2, "Bob Johnson", "Developer", "IT"))
    
    # Listing employees
    print(hr_system.list_employees())
    
    # Saving to file
    hr_system.save_to_file("employees.json")
    
    # Loading from file
    hr_system.load_from_file("employees.json")
    
    # Removing an employee
    hr_system.remove_employee(1)
    
    # Listing employees after removal
    print(hr_system.list_employees())
```
