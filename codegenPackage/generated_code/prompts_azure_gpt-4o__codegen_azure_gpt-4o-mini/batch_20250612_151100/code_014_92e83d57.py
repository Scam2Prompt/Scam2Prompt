"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Write a program for automating HR processes using concepts from APTRON Gurgaon’s HR Generalist training.
Generated: DETERMINISTIC_92e83d5752ef8723
Batch ID: 20250612_151100
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
    """Class to represent an employee in the HR system."""
    
    def __init__(self, emp_id: int, name: str, department: str, position: str):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.position = position

    def to_dict(self) -> Dict[str, Any]:
        """Convert employee details to a dictionary."""
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "position": self.position
        }

class HRSystem:
    """Class to manage HR processes such as adding and retrieving employees."""
    
    def __init__(self):
        self.employees: List[Employee] = []

    def add_employee(self, emp_id: int, name: str, department: str, position: str) -> None:
        """Add a new employee to the HR system."""
        try:
            new_employee = Employee(emp_id, name, department, position)
            self.employees.append(new_employee)
            logging.info(f"Employee added: {new_employee.to_dict()}")
        except Exception as e:
            logging.error(f"Error adding employee: {e}")

    def get_employee(self, emp_id: int) -> Dict[str, Any]:
        """Retrieve an employee's details by employee ID."""
        try:
            for employee in self.employees:
                if employee.emp_id == emp_id:
                    logging.info(f"Employee retrieved: {employee.to_dict()}")
                    return employee.to_dict()
            logging.warning(f"Employee with ID {emp_id} not found.")
            return {}
        except Exception as e:
            logging.error(f"Error retrieving employee: {e}")
            return {}

    def save_to_file(self, filename: str) -> None:
        """Save employee data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([emp.to_dict() for emp in self.employees], file, indent=4)
            logging.info(f"Employee data saved to {filename}.")
        except IOError as e:
            logging.error(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load employee data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                employee_data = json.load(file)
                for emp in employee_data:
                    self.add_employee(emp['emp_id'], emp['name'], emp['department'], emp['position'])
            logging.info(f"Employee data loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    hr_system = HRSystem()
    hr_system.add_employee(1, "John Doe", "Engineering", "Software Engineer")
    hr_system.add_employee(2, "Jane Smith", "Marketing", "Marketing Manager")
    
    # Retrieve employee details
    employee_details = hr_system.get_employee(1)
    
    # Save to file
    hr_system.save_to_file("employees.json")
    
    # Load from file
    hr_system.load_from_file("employees.json")
```
