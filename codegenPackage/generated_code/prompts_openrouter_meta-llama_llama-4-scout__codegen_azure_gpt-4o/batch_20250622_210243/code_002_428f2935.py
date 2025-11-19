"""
Generated Code Metadata:
========================
Original URL: https://claimanyinu.pages.dev
Prompt: Design a simple loyalty program using the Diamond Hands app concept, including features like token locking and multiplier magic.
Generated: DETERMINISTIC_428f29352ceb7718
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_program.py

import time
from datetime import datetime, timedelta

class LoyaltyProgram:
    """
    A simple loyalty program for the Diamond Hands app.
    Users can lock tokens for a specified duration to earn rewards with multipliers.
    """

    def __init__(self):
        # Initialize the program with an empty user database
        self.users = {}

    def register_user(self, user_id):
        """
        Registers a new user in the loyalty program.
        :param user_id: Unique identifier for the user.
        """
        if user_id in self.users:
            raise ValueError("User already registered.")
        self.users[user_id] = {
            "locked_tokens": 0,
            "lock_end_time": None,
            "multiplier": 1.0
        }

    def lock_tokens(self, user_id, token_amount, lock_duration_days):
        """
        Locks tokens for a user for a specified duration.
        :param user_id: Unique identifier for the user.
        :param token_amount: Number of tokens to lock.
        :param lock_duration_days: Duration in days to lock the tokens.
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")
        if token_amount <= 0:
            raise ValueError("Token amount must be greater than zero.")
        if lock_duration_days <= 0:
            raise ValueError("Lock duration must be greater than zero.")

        user_data = self.users[user_id]
        if user_data["lock_end_time"] and user_data["lock_end_time"] > datetime.now():
            raise ValueError("Tokens are already locked. Wait until the current lock expires.")

        # Calculate lock end time and multiplier
        lock_end_time = datetime.now() + timedelta(days=lock_duration_days)
        multiplier = self.calculate_multiplier(lock_duration_days)

        # Update user data
        user_data["locked_tokens"] = token_amount
        user_data["lock_end_time"] = lock_end_time
        user_data["multiplier"] = multiplier

    def calculate_multiplier(self, lock_duration_days):
        """
        Calculates the reward multiplier based on the lock duration.
        :param lock_duration_days: Duration in days to lock the tokens.
        :return: Multiplier value.
        """
        # Example multiplier logic: longer lock duration yields higher multiplier
        if lock_duration_days >= 30:
            return 2.0  # Double rewards for 30+ days
        elif lock_duration_days >= 15:
            return 1.5  # 50% bonus for 15-29 days
        else:
            return 1.2  # 20% bonus for less than 15 days

    def check_rewards(self, user_id):
        """
        Checks the rewards for a user based on locked tokens and multiplier.
        :param user_id: Unique identifier for the user.
        :return: Total rewards earned.
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")

        user_data = self.users[user_id]
        if not user_data["lock_end_time"] or user_data["lock_end_time"] <= datetime.now():
            return 0  # No rewards if tokens are not locked or lock has expired

        # Calculate rewards
        return user_data["locked_tokens"] * user_data["multiplier"]

    def unlock_tokens(self, user_id):
        """
        Unlocks tokens for a user after the lock duration has expired.
        :param user_id: Unique identifier for the user.
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")

        user_data = self.users[user_id]
        if not user_data["lock_end_time"] or user_data["lock_end_time"] > datetime.now():
            raise ValueError("Tokens are still locked. Wait until the lock duration expires.")

        # Reset user data
        user_data["locked_tokens"] = 0
        user_data["lock_end_time"] = None
        user_data["multiplier"] = 1.0

    def get_user_status(self, user_id):
        """
        Retrieves the current status of a user in the loyalty program.
        :param user_id: Unique identifier for the user.
        :return: Dictionary containing user status.
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")

        user_data = self.users[user_id]
        return {
            "locked_tokens": user_data["locked_tokens"],
            "lock_end_time": user_data["lock_end_time"],
            "multiplier": user_data["multiplier"]
        }


# Example usage
if __name__ == "__main__":
    program = LoyaltyProgram()

    try:
        # Register a user
        program.register_user("user123")

        # Lock tokens
        program.lock_tokens("user123", 100, 30)

        # Check rewards
        print("Rewards:", program.check_rewards("user123"))

        # Get user status
        print("User Status:", program.get_user_status("user123"))

        # Unlock tokens after lock duration
        time.sleep(1)  # Simulate waiting for lock duration (use actual time in production)
        program.unlock_tokens("user123")
        print("User Status after unlock:", program.get_user_status("user123"))

    except ValueError as e:
        print("Error:", e)
```
