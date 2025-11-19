"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uagra.com.ua
Prompt: Write a code example for implementing a bonus system in a betting application that mimics the Parimatch bonus offerings for new users.
Generated: DETERMINISTIC_ff03cc8a30645c3c
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BettingBonusSystem:
    """
    A class to represent the bonus system for new users in a betting application.
    """

    def __init__(self):
        """
        Initializes the bonus system.
        """
        self.bonuses = {}  # Stores user bonuses in format: {user_id: {'amount': int, 'expiry': datetime}}

    def register_new_user(self, user_id):
        """
        Registers a new user in the bonus system and assigns a welcome bonus.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Returns:
            str: Success message or error if user already exists.
        """
        if user_id in self.bonuses:
            return f"User '{user_id}' is already registered and has a bonus assigned."
        
        # Assign a bonus for new users
        bonus_amount = 100  # Example bonus amount
        expiry_days = 7     # Bonus expires in 7 days
        expiry_date = datetime.datetime.now() + datetime.timedelta(days=expiry_days)

        self.bonuses[user_id] = {'amount': bonus_amount, 'expiry': expiry_date}
        return f"Welcome bonus of {bonus_amount} assigned to user '{user_id}' with expiry date {expiry_date}."

    def check_bonus(self, user_id):
        """
        Checks the bonus details for a user.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Returns:
            str: Bonus details for the user or error if user doesn't exist or bonus expired.
        """
        if user_id not in self.bonuses:
            return f"No bonus found for user '{user_id}'."
        
        bonus = self.bonuses[user_id]
        if bonus['expiry'] < datetime.datetime.now():
            del self.bonuses[user_id]  # Remove expired bonus
            return f"Bonus for user '{user_id}' has expired."
        
        return f"User '{user_id}' has a bonus of {bonus['amount']} which expires on {bonus['expiry']}."

    def use_bonus(self, user_id, amount):
        """
        Allows the user to use part or all of their bonus.
        
        Args:
            user_id (str): Unique identifier for the user.
            amount (int): Amount to use from the bonus.
        
        Returns:
            str: Success message or error if insufficient bonus or user doesn't exist.
        """
        if user_id not in self.bonuses:
            return f"No bonus found for user '{user_id}'."
        
        bonus = self.bonuses[user_id]
        if bonus['expiry'] < datetime.datetime.now():
            del self.bonuses[user_id]  # Remove expired bonus
            return f"Bonus for user '{user_id}' has expired."

        if amount > bonus['amount']:
            return f"Insufficient bonus balance. User '{user_id}' only has {bonus['amount']}."

        bonus['amount'] -= amount
        if bonus['amount'] == 0:
            del self.bonuses[user_id]  # Remove bonus if fully used
            return f"Bonus fully used by user '{user_id}'. Remaining balance: 0."
        
        return f"Bonus of {amount} used by user '{user_id}'. Remaining balance: {bonus['amount']}."

# Example usage
if __name__ == "__main__":
    system = BettingBonusSystem()

    # Register a new user
    print(system.register_new_user("user123"))

    # Check bonus for the user
    print(system.check_bonus("user123"))

    # Try using the bonus
    print(system.use_bonus("user123", 50))

    # Check bonus after partial usage
    print(system.check_bonus("user123"))

    # Try using the remaining bonus
    print(system.use_bonus("user123", 50))

    # Check bonus after fully using it
    print(system.check_bonus("user123"))
```
