"""
Generated Code Metadata:
========================
Original URL: https://betbax.xyz
Prompt: Create a script that implements a cashback system for losses in a casino environment, inspired by the loyalty programs mentioned on BaxBet.
Generated: DETERMINISTIC_23bac4d9fd2b9f27
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class CasinoCashbackSystem:
    """
    A class to implement a cashback system for losses in a casino environment.
    Inspired by loyalty programs, this system calculates cashback based on user losses.
    """

    def __init__(self, cashback_percentage=10):
        """
        Initialize the cashback system with a default cashback percentage.

        :param cashback_percentage: Percentage of losses to be returned as cashback (default: 10%)
        """
        if not (0 <= cashback_percentage <= 100):
            raise ValueError("Cashback percentage must be between 0 and 100.")
        self.cashback_percentage = cashback_percentage
        self.user_losses = {}  # Dictionary to track user losses

    def record_loss(self, user_id, amount):
        """
        Record a loss for a user.

        :param user_id: Unique identifier for the user
        :param amount: Amount of loss to record (must be positive)
        """
        if amount <= 0:
            raise ValueError("Loss amount must be greater than zero.")
        if user_id not in self.user_losses:
            self.user_losses[user_id] = 0
        self.user_losses[user_id] += amount

    def calculate_cashback(self, user_id):
        """
        Calculate the cashback amount for a user based on their recorded losses.

        :param user_id: Unique identifier for the user
        :return: Cashback amount (float)
        """
        if user_id not in self.user_losses:
            raise ValueError("No losses recorded for this user.")
        total_losses = self.user_losses[user_id]
        cashback = (total_losses * self.cashback_percentage) / 100
        return round(cashback, 2)

    def reset_losses(self, user_id):
        """
        Reset the recorded losses for a user after cashback is issued.

        :param user_id: Unique identifier for the user
        """
        if user_id in self.user_losses:
            self.user_losses[user_id] = 0

    def issue_cashback(self, user_id):
        """
        Issue cashback to a user and reset their losses.

        :param user_id: Unique identifier for the user
        :return: Cashback amount issued (float)
        """
        cashback = self.calculate_cashback(user_id)
        self.reset_losses(user_id)
        return cashback


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the cashback system with a 10% cashback rate
        casino_cashback = CasinoCashbackSystem(cashback_percentage=10)

        # Record losses for users
        casino_cashback.record_loss(user_id="user123", amount=500)
        casino_cashback.record_loss(user_id="user123", amount=300)
        casino_cashback.record_loss(user_id="user456", amount=1000)

        # Calculate and issue cashback for user123
        cashback_user123 = casino_cashback.issue_cashback(user_id="user123")
        print(f"Cashback issued to user123: ${cashback_user123}")

        # Calculate and issue cashback for user456
        cashback_user456 = casino_cashback.issue_cashback(user_id="user456")
        print(f"Cashback issued to user456: ${cashback_user456}")

    except Exception as e:
        print(f"Error: {e}")
```
