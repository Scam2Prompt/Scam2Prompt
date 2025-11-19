"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Develop a system to manage teacher and employee data, including features for leave management, salary scales, and performance evaluation, tailored to the needs of a Bangladeshi secondary school.
Generated: DETERMINISTIC_30f81d59cbf0593e
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class Employee:
    """Class to represent an employee in the school system."""
    
    def __init__(self, emp_id: int, name: str, position: str, salary: float):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.leave_records: List[Dict] = []
        self.performance_reviews: List[Dict] = []

    def add_leave(self, start_date: str, end_date: str):
        """Add a leave record for the employee."""
        leave_record = {
            "start_date": start_date,
            "end_date": end_date,
            "duration": self.calculate_leave_duration(start_date, end_date)
        }
        self.leave_records.append(leave_record)

    def calculate_leave_duration(self, start_date: str, end_date: str) -> int:
        """Calculate the duration of leave in days."""
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return (end - start).days + 1  # Inclusive of start date

    def add_performance_review(self, review_date: str, score: int, comments: str):
        """Add a performance review for the employee."""
        review = {
            "review_date": review_date,
            "score": score,
            "comments": comments
        }
        self.performance_reviews.append(review)

    def to_dict(self) -> Dict:
        """Convert employee data to a dictionary for easy serialization."""
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "position": self.position,
            "salary": self.salary,
            "leave_records": self.leave_records,
            "performance_reviews": self.performance_reviews
        }

class SchoolManagementSystem:
    """Class to manage the school employee data."""
    
    def __init__(self):
        self.employees: Dict[int, Employee] = {}

    def add_employee(self, emp_id: int, name: str, position: str, salary: float):
        """Add a new employee to the system."""
        if emp_id in self.employees:
            raise ValueError(f"Employee with ID {emp_id} already exists.")
        self.employees[emp_id] = Employee(emp_id, name, position, salary)

    def remove_employee(self, emp_id: int):
        """Remove an employee from the system."""
        if emp_id not in self.employees:
            raise ValueError(f"Employee with ID {emp_id} does not exist.")
        del self.employees[emp_id]

    def get_employee(self, emp_id: int) -> Optional[Employee]:
        """Retrieve an employee by ID."""
        return self.employees.get(emp_id)

    def save_to_file(self, filename: str):
        """Save employee data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({emp_id: emp.to_dict() for emp_id, emp in self.employees.items()}, file, indent=4)
        except IOError as e:
            raise Exception(f"An error occurred while saving to file: {e}")

    def load_from_file(self, filename: str):
        """Load employee data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for emp_id, emp_data in data.items():
                    emp = Employee(emp_data['emp_id'], emp_data['name'], emp_data['position'], emp_data['salary'])
                    emp.leave_records = emp_data['leave_records']
                    emp.performance_reviews = emp_data['performance_reviews']
                    self.employees[emp_id] = emp
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"An error occurred while loading from file: {e}")

# Example usage
if __name__ == "__main__":
    sms = SchoolManagementSystem()
    sms.add_employee(1, "John Doe", "Teacher", 30000)
    sms.add_employee(2, "Jane Smith", "Administrator", 40000)

    # Adding leave and performance review
    employee = sms.get_employee(1)
    if employee:
        employee.add_leave("2023-10-01", "2023-10-05")
        employee.add_performance_review("2023-10-10", 85, "Good performance overall.")

    # Save to file
    sms.save_to_file("employees.json")

    # Load from file
    sms.load_from_file("employees.json")
```
