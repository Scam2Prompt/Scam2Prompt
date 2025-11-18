"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.info
Prompt: Generate code for a loyalty program system that calculates cashback on losses for users, inspired by BaxBet's cashback feature.
Generated: DETERMINISTIC_fba5bd14293ffd0c
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoyaltyProgram:
    """
    A class to represent a loyalty program that calculates cashback
    based on user losses in a betting system.
    """

    def __init__(self, cashback_percentage):
        """
        Initializes the LoyaltyProgram with a specified cashback percentage.

        Args:
            cashback_percentage (float): The percentage of cashback to be awarded.
        """
        if not (0 <= cashback_percentage <= 100):
            raise ValueError("Cashback percentage must be between 0 and 100.")
        self.cashback_percentage = cashback_percentage
        self.user_losses = {}

    def record_loss(self, user_id, loss_amount):
        """
        Records a user's loss.

        Args:
            user_id (str): The ID of the user.
            loss_amount (float): The amount of the loss.

        Raises:
            ValueError: If loss_amount is negative.
        """
        if loss_amount < 0:
            raise ValueError("Loss amount cannot be negative.")
        
        if user_id not in self.user_losses:
            self.user_losses[user_id] = 0
        
        self.user_losses[user_id] += loss_amount

    def calculate_cashback(self, user_id):
        """
        Calculates the cashback for a user based on their recorded losses.

        Args:
            user_id (str): The ID of the user.

        Returns:
            float: The amount of cashback owed to the user.

        Raises:
            KeyError: If the user_id does not exist in the records.
        """
        if user_id not in self.user_losses:
            raise KeyError("User ID not found in records.")
        
        total_losses = self.user_losses[user_id]
        cashback = (total_losses * self.cashback_percentage) / 100
        return cashback

    def reset_losses(self, user_id):
        """
        Resets the losses for a user.

        Args:
            user_id (str): The ID of the user.

        Raises:
            KeyError: If the user_id does not exist in the records.
        """
        if user_id not in self.user_losses:
            raise KeyError("User ID not found in records.")
        
        self.user_losses[user_id] = 0

# Example usage:
if __name__ == "__main__":
    try:
        loyalty_program = LoyaltyProgram(cashback_percentage=10.0)  # 10% cashback
        loyalty_program.record_loss(user_id="user123", loss_amount=200.0)
        cashback = loyalty_program.calculate_cashback(user_id="user123")
        print(f"User 'user123' has a cashback of: ${cashback:.2f}")
        
        # Resetting losses for the user
        loyalty_program.reset_losses(user_id="user123")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except KeyError as ke:
        print(f"Key error: {ke}")
```
