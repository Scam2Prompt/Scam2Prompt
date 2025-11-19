"""
Generated Code Metadata:
========================
Original URL: https://earnifi.co
Prompt: "Design a system to manage debt-free financing using Earnifi's automatic payroll adjustments, and provide a code example in a programming language of your choice."
Generated: DETERMINISTIC_b4d5920156f79493
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class DebtFreeFinancingManager:
    def __init__(self):
        # Initialize the financing manager with an empty list of users
        self.users: List[Dict[str, Any]] = []

    def add_user(self, user_id: str, salary: float, debt: float) -> None:
        """
        Add a new user to the financing system.

        :param user_id: Unique identifier for the user
        :param salary: Monthly salary of the user
        :param debt: Current debt of the user
        """
        user = {
            'user_id': user_id,
            'salary': salary,
            'debt': debt,
            'adjusted_salary': salary
        }
        self.users.append(user)

    def adjust_payroll(self, user_id: str, adjustment_amount: float) -> None:
        """
        Adjust the payroll of a user to help manage their debt.

        :param user_id: Unique identifier for the user
        :param adjustment_amount: Amount to adjust the salary by
        :raises ValueError: If the adjustment amount is invalid
        """
        if adjustment_amount < 0:
            raise ValueError("Adjustment amount must be non-negative.")

        user = self._find_user(user_id)
        user['adjusted_salary'] -= adjustment_amount
        user['debt'] -= adjustment_amount

    def _find_user(self, user_id: str) -> Dict[str, Any]:
        """
        Find a user by their user ID.

        :param user_id: Unique identifier for the user
        :return: User dictionary if found
        :raises LookupError: If the user is not found
        """
        for user in self.users:
            if user['user_id'] == user_id:
                return user
        raise LookupError(f"User with ID {user_id} not found.")

    def get_user_info(self, user_id: str) -> Dict[str, Any]:
        """
        Retrieve user information.

        :param user_id: Unique identifier for the user
        :return: User information dictionary
        :raises LookupError: If the user is not found
        """
        user = self._find_user(user_id)
        return {
            'user_id': user['user_id'],
            'salary': user['salary'],
            'debt': user['debt'],
            'adjusted_salary': user['adjusted_salary']
        }

    def save_to_file(self, filename: str) -> None:
        """
        Save the current state of the financing manager to a JSON file.

        :param filename: Name of the file to save the data
        """
        with open(filename, 'w') as file:
            json.dump(self.users, file)

    def load_from_file(self, filename: str) -> None:
        """
        Load user data from a JSON file.

        :param filename: Name of the file to load the data from
        :raises FileNotFoundError: If the file does not exist
        """
        try:
            with open(filename, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filename} does not exist.")

# Example usage
if __name__ == "__main__":
    manager = DebtFreeFinancingManager()
    manager.add_user("user1", 5000, 2000)
    manager.adjust_payroll("user1", 500)
    print(manager.get_user_info("user1"))
    manager.save_to_file("users.json")
```
