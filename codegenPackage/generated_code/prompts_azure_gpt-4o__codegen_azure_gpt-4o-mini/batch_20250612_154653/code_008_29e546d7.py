"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: Generate a script to manage career development data for employees in a biotech company, incorporating diversity, equity, and inclusion metrics as outlined by CSL Seqirus UK.
Generated: DETERMINISTIC_29e546d73a193280
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class Employee:
    """Class to represent an employee's career development data."""
    
    def __init__(self, employee_id: str, name: str, role: str, diversity_metrics: Dict[str, Any]):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.diversity_metrics = diversity_metrics

    def to_dict(self) -> Dict[str, Any]:
        """Convert the employee data to a dictionary."""
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "role": self.role,
            "diversity_metrics": self.diversity_metrics
        }

class CareerDevelopmentManager:
    """Class to manage career development data for employees."""
    
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.employees: List[Employee] = []
        self.load_data()

    def load_data(self) -> None:
        """Load employee data from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    data = json.load(file)
                    self.employees = [Employee(**emp) for emp in data]
                except json.JSONDecodeError as e:
                    print(f"Error loading data: {e}")
        else:
            print("Data file does not exist. Starting with an empty employee list.")

    def save_data(self) -> None:
        """Save employee data to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump([emp.to_dict() for emp in self.employees], file, indent=4)

    def add_employee(self, employee_id: str, name: str, role: str, diversity_metrics: Dict[str, Any]) -> None:
        """Add a new employee to the list."""
        new_employee = Employee(employee_id, name, role, diversity_metrics)
        self.employees.append(new_employee)
        self.save_data()

    def get_employee(self, employee_id: str) -> Employee:
        """Retrieve an employee by their ID."""
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        raise ValueError(f"Employee with ID {employee_id} not found.")

    def update_employee(self, employee_id: str, **kwargs) -> None:
        """Update an existing employee's data."""
        employee = self.get_employee(employee_id)
        for key, value in kwargs.items():
            if hasattr(employee, key):
                setattr(employee, key, value)
            else:
                raise ValueError(f"Invalid attribute '{key}' for Employee.")
        self.save_data()

    def remove_employee(self, employee_id: str) -> None:
        """Remove an employee from the list."""
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]
        self.save_data()

# Example usage
if __name__ == "__main__":
    manager = CareerDevelopmentManager('employees.json')
    
    # Adding a new employee
    manager.add_employee(
        employee_id="E001",
        name="Alice Smith",
        role="Research Scientist",
        diversity_metrics={"gender": "female", "ethnicity": "Asian"}
    )
    
    # Updating an employee
    try:
        manager.update_employee("E001", role="Senior Research Scientist")
    except ValueError as e:
        print(e)

    # Retrieving an employee
    try:
        employee = manager.get_employee("E001")
        print(employee.to_dict())
    except ValueError as e:
        print(e)

    # Removing an employee
    manager.remove_employee("E001")
```
