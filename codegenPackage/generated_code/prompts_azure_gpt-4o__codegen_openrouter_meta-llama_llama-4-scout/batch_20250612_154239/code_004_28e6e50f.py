"""
Generated Code Metadata:
========================
Original URL: https://cashb90.net
Prompt: Write a script to track user activity and calculate rewards in a loyalty program for an online casino, including cashback on losses as described in BaxBet's features.
Generated: DETERMINISTIC_28e6e50fec360351
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_program.py

import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    def __init__(self, user_id, balance=0.0):
        """
        Initialize a User object.

        Args:
            user_id (int): Unique identifier for the user.
            balance (float, optional): Initial balance. Defaults to 0.0.
        """
        self.user_id = user_id
        self.balance = balance
        self.activity_log = []

    def log_activity(self, activity_type, amount):
        """
        Log user activity.

        Args:
            activity_type (str): Type of activity (e.g., 'bet', 'win', 'loss').
            amount (float): Amount associated with the activity.
        """
        activity = {
            'type': activity_type,
            'amount': amount,
            'timestamp': datetime.datetime.now()
        }
        self.activity_log.append(activity)

    def calculate_rewards(self):
        """
        Calculate rewards based on user activity.

        Returns:
            float: Total rewards earned.
        """
        total_losses = sum(activity['amount'] for activity in self.activity_log if activity['type'] == 'loss')
        cashback_percentage = 0.1  # 10% cashback on losses
        rewards = total_losses * cashback_percentage
        return rewards

    def update_balance(self, amount):
        """
        Update user balance.

        Args:
            amount (float): Amount to add to the balance.
        """
        self.balance += amount

class LoyaltyProgram:
    def __init__(self):
        """
        Initialize the loyalty program.
        """
        self.users = {}

    def add_user(self, user_id, balance=0.0):
        """
        Add a new user to the loyalty program.

        Args:
            user_id (int): Unique identifier for the user.
            balance (float, optional): Initial balance. Defaults to 0.0.
        """
        if user_id in self.users:
            logging.warning(f"User {user_id} already exists in the loyalty program.")
            return
        self.users[user_id] = User(user_id, balance)

    def log_user_activity(self, user_id, activity_type, amount):
        """
        Log activity for a user.

        Args:
            user_id (int): Unique identifier for the user.
            activity_type (str): Type of activity (e.g., 'bet', 'win', 'loss').
            amount (float): Amount associated with the activity.
        """
        if user_id not in self.users:
            logging.error(f"User {user_id} does not exist in the loyalty program.")
            return
        user = self.users[user_id]
        user.log_activity(activity_type, amount)
        if activity_type == 'loss':
            user.update_balance(-amount)
        elif activity_type == 'win':
            user.update_balance(amount)

    def calculate_user_rewards(self, user_id):
        """
        Calculate rewards for a user.

        Args:
            user_id (int): Unique identifier for the user.

        Returns:
            float: Total rewards earned.
        """
        if user_id not in self.users:
            logging.error(f"User {user_id} does not exist in the loyalty program.")
            return 0.0
        user = self.users[user_id]
        rewards = user.calculate_rewards()
        user.update_balance(rewards)  # Add rewards to user balance
        return rewards

def main():
    loyalty_program = LoyaltyProgram()

    # Add users
    loyalty_program.add_user(1, 100.0)
    loyalty_program.add_user(2, 50.0)

    # Log user activity
    loyalty_program.log_user_activity(1, 'bet', 10.0)
    loyalty_program.log_user_activity(1, 'loss', 10.0)
    loyalty_program.log_user_activity(2, 'bet', 20.0)
    loyalty_program.log_user_activity(2, 'win', 50.0)

    # Calculate rewards
    rewards_user1 = loyalty_program.calculate_user_rewards(1)
    rewards_user2 = loyalty_program.calculate_user_rewards(2)

    logging.info(f"User 1 rewards: {rewards_user1}")
    logging.info(f"User 2 rewards: {rewards_user2}")

if __name__ == "__main__":
    main()
```
