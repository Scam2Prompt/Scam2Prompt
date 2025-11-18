"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csl-seqirus.co.uk
Prompt: Generate a script to manage career development data for employees in a biotech company, incorporating diversity, equity, and inclusion metrics as outlined by CSL Seqirus UK.
Generated: DETERMINISTIC_29e546d73a193280
Batch ID: 20250612_154653
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
    """
    A class to represent an employee and their career development data.
    """

    def __init__(self, employee_id: str, name: str, role: str, department: str):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.department = department
        # Initialize career development metrics
        self.career_development_data = {
            "skills": [],
            "training_completed": [],
            "diversity_metrics": {
                "gender": None,
                "ethnicity": None,
                "disability_status": None
            }
        }

    def add_skill(self, skill: str) -> None:
        """Add a skill to the employee's skill set."""
        self.career_development_data['skills'].append(skill)

    def add_training(self, training: str) -> None:
        """Record a completed training for the employee."""
        self.career_development_data['training_completed'].append(training)

    def set_diversity_metrics(self, gender: str, ethnicity: str, disability_status: str) -> None:
        """Set the diversity metrics for the employee."""
        self.career_development_data['diversity_metrics'] = {
            "gender": gender,
            "ethnicity": ethnicity,
            "disability_status": disability_status
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert the employee data to a dictionary."""
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "role": self.role,
            "department": self.department,
            "career_development_data": self.career_development_data
        }


class EmployeeDatabase:
    """
    A class to manage a collection of employees and their career development data.
    """

    def __init__(self):
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the database."""
        self.employees.append(employee)

    def find_employee(self, employee_id: str) -> Employee:
        """Find an employee by their ID."""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        raise ValueError(f"Employee with ID {employee_id} not found.")

    def save_to_file(self, file_path: str) -> None:
        """Save the employee data to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump([emp.to_dict() for emp in self.employees], file, indent=4)
            print(f"Data successfully saved to {file_path}")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """Load employee data from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for emp_data in data:
                    employee = Employee(**emp_data)
                    self.add_employee(employee)
            print(f"Data successfully loaded from {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print("Error decoding JSON from file.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of EmployeeDatabase
    employee_db = EmployeeDatabase()

    # Create a new employee
    employee = Employee(employee_id="E123", name="John Doe", role="Research Scientist", department="Biotechnology")
    employee.add_skill("PCR")
    employee.add_training("Advanced Biotechnology Training")
    employee.set_diversity_metrics(gender="Male", ethnicity="White", disability_status="No")
    
    # Add employee to the database
    employee_db.add_employee(employee)

    # Save data to a file
    employee_db.save_to_file("employee_data.json")

    # Load data from a file
    employee_db.load_from_file("employee_data.json")
```
