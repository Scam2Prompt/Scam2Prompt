"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegraph.live
Prompt: How can I implement a function to track GRT balance changes as users progress through different incentive levels on The Graph platform?
Generated: DETERMINISTIC_fcfcd2a81a5f8b7f
Batch ID: 20250612_155301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code to implement a function that tracks GRT balance changes as users progress through different incentive levels on The Graph platform:

```python
import logging

# Configure logging for error handling and tracking
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class GRTTracker:
    """
    A class to track GRT balance changes and user progress across incentive levels.
    """

    def __init__(self):
        """
        Initializes a new GRTTracker instance with an empty user database.
        """
        self.user_balances = {}  # Dictionary to store user GRT balances and levels

    def add_user(self, user_id, initial_balance=0, incentive_level=1):
        """
        Adds a new user to the tracker.

        :param user_id: Unique identifier for the user.
        :param initial_balance: Initial GRT balance for the user.
        :param incentive_level: Starting incentive level for the user.
        """
        if user_id in self.user_balances:
            logging.warning(f"User {user_id} already exists. Skipping addition.")
            return
        
        self.user_balances[user_id] = {
            "balance": initial_balance,
            "level": incentive_level
        }
        logging.info(f"User {user_id} added with balance {initial_balance} and level {incentive_level}.")

    def update_balance(self, user_id, amount):
        """
        Updates the GRT balance for a user.

        :param user_id: Unique identifier for the user.
        :param amount: Amount to add (positive) or subtract (negative) from the balance.
        :raises ValueError: If the user ID does not exist.
        """
        if user_id not in self.user_balances:
            logging.error(f"User {user_id} not found. Cannot update balance.")
            raise ValueError(f"User {user_id} does not exist.")
        
        self.user_balances[user_id]["balance"] += amount
        logging.info(f"User {user_id} balance updated by {amount}. New balance: {self.user_balances[user_id]['balance']}.")

    def update_incentive_level(self, user_id, new_level):
        """
        Updates the incentive level for a user.

        :param user_id: Unique identifier for the user.
        :param new_level: New incentive level to set.
        :raises ValueError: If the user ID does not exist.
        """
        if user_id not in self.user_balances:
            logging.error(f"User {user_id} not found. Cannot update incentive level.")
            raise ValueError(f"User {user_id} does not exist.")
        
        self.user_balances[user_id]["level"] = new_level
        logging.info(f"User {user_id} incentive level updated to {new_level}.")

    def get_user_info(self, user_id):
        """
        Retrieves the balance and incentive level for a user.

        :param user_id: Unique identifier for the user.
        :return: Dictionary containing the balance and incentive level.
        :raises ValueError: If the user ID does not exist.
        """
        if user_id not in self.user_balances:
            logging.error(f"User {user_id} not found. Cannot retrieve info.")
            raise ValueError(f"User {user_id} does not exist.")
        
        return self.user_balances[user_id]

# Example usage (uncomment the lines below to test the code):
# tracker = GRTTracker()
# tracker.add_user(user_id="user123", initial_balance=100, incentive_level=1)
# tracker.update_balance(user_id="user123", amount=50)
# tracker.update_incentive_level(user_id="user123", new_level=2)
# print(tracker.get_user_info(user_id="user123"))
```

This code is clean, production-ready, and includes error handling and logging to assist with debugging and tracking user progress.
