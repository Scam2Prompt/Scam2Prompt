"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ketoken.com
Prompt: Write a script to implement an employee retention program using KeToken's digital tokens as rewards for achieving performance milestones.
Generated: DETERMINISTIC_744c2d41167b1c35
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Employee:
    """Class representing an employee in the retention program."""
    
    def __init__(self, employee_id, name):
        """
        Initialize an Employee instance.
        
        Parameters:
            employee_id (str): Unique identifier for the employee.
            name (str): Name of the employee.
        """
        self.employee_id = employee_id
        self.name = name
        self.performance_milestones = []
        self.tokens = 0

    def add_performance_milestone(self, milestone):
        """
        Add a performance milestone for the employee.
        
        Parameters:
            milestone (str): Description of the performance milestone.
        """
        self.performance_milestones.append({
            'milestone': milestone,
            'date': datetime.now()
        })
        logging.info(f'Milestone added for {self.name}: {milestone}')

    def reward_tokens(self, token_amount):
        """
        Reward tokens to the employee for achieving milestones.
        
        Parameters:
            token_amount (int): The amount of tokens to be rewarded.
        """
        if token_amount < 0:
            raise ValueError("Token amount must be a positive integer.")
        self.tokens += token_amount
        logging.info(f'{token_amount} tokens rewarded to {self.name}. Total tokens: {self.tokens}')

    def to_dict(self):
        """Convert employee data to dictionary format for JSON serialization."""
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'performance_milestones': self.performance_milestones,
            'tokens': self.tokens
        }

class EmployeeRetentionProgram:
    """Class to manage the employee retention program."""
    
    def __init__(self):
        """Initialize the EmployeeRetentionProgram with an empty employee list."""
        self.employees = {}

    def add_employee(self, employee_id, name):
        """
        Add a new employee to the retention program.
        
        Parameters:
            employee_id (str): Unique identifier for the employee.
            name (str): Name of the employee.
        """
        if employee_id in self.employees:
            raise ValueError("Employee ID already exists.")
        employee = Employee(employee_id, name)
        self.employees[employee_id] = employee
        logging.info(f'Employee added: {name}')

    def record_milestone(self, employee_id, milestone):
        """
        Record a performance milestone for an employee.
        
        Parameters:
            employee_id (str): Unique identifier for the employee.
            milestone (str): Description of the performance milestone.
        """
        employee = self.employees.get(employee_id)
        if not employee:
            raise ValueError("Employee not found.")
        employee.add_performance_milestone(milestone)

    def reward_employee(self, employee_id, token_amount):
        """
        Reward tokens to an employee for milestones achieved.
        
        Parameters:
            employee_id (str): Unique identifier for the employee.
            token_amount (int): The amount of tokens to be rewarded.
        """
        employee = self.employees.get(employee_id)
        if not employee:
            raise ValueError("Employee not found.")
        employee.reward_tokens(token_amount)

    def save_program_data(self, filename):
        """
        Save the current state of the retention program to a JSON file.
        
        Parameters:
            filename (str): The name of the file to save the data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump({id: emp.to_dict() for id, emp in self.employees.items()}, file)
            logging.info(f'Data saved to {filename}')
        except Exception as e:
            logging.error(f'Error saving data: {e}')

# Example usage
if __name__ == "__main__":
    retention_program = EmployeeRetentionProgram()
    retention_program.add_employee("001", "Alice Johnson")
    retention_program.record_milestone("001", "Completed Project X")
    retention_program.reward_employee("001", 100)
    retention_program.save_program_data("employee_retention_data.json")
```
