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
import random
import string
from datetime import datetime

class KeTokenRewardProgram:
    """
    A class to implement an employee retention program using KeToken digital tokens
    for rewarding performance milestones.
    """

    def __init__(self):
        """Initialize the reward program with employee data and token ledger."""
        self.employees = {}  # Stores employee details and their token balance
        self.token_ledger = {}  # Tracks all token transactions

    def add_employee(self, employee_id, name):
        """
        Add a new employee to the system.
        
        :param employee_id: Unique identifier for the employee.
        :param name: Name of the employee.
        """
        if employee_id in self.employees:
            raise ValueError("Employee ID already exists.")
        self.employees[employee_id] = {"name": name, "tokens": 0}
        print(f"Employee {name} added successfully.")

    def generate_token_id(self):
        """Generate a unique token identifier."""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def reward_tokens(self, employee_id, milestone, token_amount):
        """
        Reward tokens to an employee for achieving a performance milestone.
        
        :param employee_id: Unique identifier for the employee.
        :param milestone: Description of the performance milestone.
        :param token_amount: Number of tokens to reward the employee.
        """
        if employee_id not in self.employees:
            raise ValueError("Employee ID not found.")
        if token_amount <= 0:
            raise ValueError("Token amount must be greater than zero.")

        token_id = self.generate_token_id()
        transaction = {
            "token_id": token_id,
            "employee_id": employee_id,
            "milestone": milestone,
            "token_amount": token_amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.token_ledger[token_id] = transaction
        self.employees[employee_id]["tokens"] += token_amount

        print(f"{token_amount} tokens rewarded to {self.employees[employee_id]['name']} for milestone: {milestone}.")

    def view_employee_tokens(self, employee_id):
        """
        View the total token balance of an employee.
        
        :param employee_id: Unique identifier for the employee.
        """
        if employee_id not in self.employees:
            raise ValueError("Employee ID not found.")
        employee = self.employees[employee_id]
        print(f"{employee['name']} has {employee['tokens']} tokens.")

    def export_ledger(self, file_name):
        """
        Export the token ledger to a JSON file.
        
        :param file_name: Name of the file to save the ledger.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.token_ledger, file, indent=4)
            print(f"Ledger successfully exported to {file_name}.")
        except IOError as e:
            print(f"Error exporting ledger: {e}")

# Main program flow
if __name__ == "__main__":
    program = KeTokenRewardProgram()

    # Add employees
    program.add_employee("EMP001", "Alice")
    program.add_employee("EMP002", "Bob")

    # Reward tokens for milestones
    program.reward_tokens("EMP001", "Exceeded Q1 Sales Target", 50)
    program.reward_tokens("EMP002", "Outstanding Customer Feedback", 30)

    # View token balances
    program.view_employee_tokens("EMP001")
    program.view_employee_tokens("EMP002")

    # Export ledger to a file
    program.export_ledger("token_ledger.json")
```
