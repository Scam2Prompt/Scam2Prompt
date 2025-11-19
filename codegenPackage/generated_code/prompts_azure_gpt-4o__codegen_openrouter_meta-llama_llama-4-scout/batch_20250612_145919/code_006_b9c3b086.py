"""
Generated Code Metadata:
========================
Original URL: https://vatangame.games
Prompt: Develop a Python script for tracking and calculating cashback rewards based on user losses, as implemented in BaxBet's loyalty program.
Generated: DETERMINISTIC_b9c3b0863a96eac9
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
BaxBet Loyalty Program: Cashback Rewards Calculator

This script calculates cashback rewards based on user losses.
"""

class CashbackCalculator:
    def __init__(self, loss_threshold, cashback_percentage, max_cashback):
        """
        Initializes the CashbackCalculator.

        Args:
            loss_threshold (float): Minimum loss required to be eligible for cashback.
            cashback_percentage (float): Percentage of loss to be rewarded as cashback.
            max_cashback (float): Maximum cashback reward.
        """
        self.loss_threshold = loss_threshold
        self.cashback_percentage = cashback_percentage / 100  # Convert to decimal
        self.max_cashback = max_cashback

    def calculate_cashback(self, user_loss):
        """
        Calculates the cashback reward based on user loss.

        Args:
            user_loss (float): The user's total loss.

        Returns:
            float: The calculated cashback reward.
        """
        if user_loss < self.loss_threshold:
            return 0

        cashback = user_loss * self.cashback_percentage
        return min(cashback, self.max_cashback)


class User:
    def __init__(self, user_id, losses=None):
        """
        Initializes a User.

        Args:
            user_id (int): Unique identifier for the user.
            losses (list[float], optional): List of user's losses. Defaults to None.
        """
        self.user_id = user_id
        self.losses = losses if losses is not None else []

    def add_loss(self, loss):
        """
        Adds a loss to the user's loss history.

        Args:
            loss (float): The loss to be added.
        """
        self.losses.append(loss)

    def get_total_loss(self):
        """
        Calculates the user's total loss.

        Returns:
            float: The user's total loss.
        """
        return sum(self.losses)


def main():
    try:
        # Define loyalty program parameters
        loss_threshold = 100.0
        cashback_percentage = 10.0
        max_cashback = 50.0

        # Create a CashbackCalculator
        calculator = CashbackCalculator(loss_threshold, cashback_percentage, max_cashback)

        # Create users
        user1 = User(1)
        user2 = User(2)

        # Add losses to users
        user1.add_loss(500.0)
        user1.add_loss(200.0)
        user2.add_loss(50.0)

        # Calculate cashback rewards
        user1_total_loss = user1.get_total_loss()
        user2_total_loss = user2.get_total_loss()

        user1_cashback = calculator.calculate_cashback(user1_total_loss)
        user2_cashback = calculator.calculate_cashback(user2_total_loss)

        # Print results
        print(f"User {user1.user_id} total loss: ${user1_total_loss:.2f}, Cashback: ${user1_cashback:.2f}")
        print(f"User {user2.user_id} total loss: ${user2_total_loss:.2f}, Cashback: ${user2_cashback:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
