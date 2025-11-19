"""
Generated Code Metadata:
========================
Original URL: https://vatanbet.info
Prompt: Generate code for a loyalty program system that calculates cashback on losses for users, inspired by BaxBet's cashback feature.
Generated: DETERMINISTIC_fba5bd14293ffd0c
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LoyaltyProgram:
    """
    A class to represent a loyalty program that calculates cashback on losses for users.
    """

    def __init__(self, cashback_percentage: float):
        """
        Initializes the LoyaltyProgram with a specified cashback percentage.

        :param cashback_percentage: The percentage of cashback to be awarded on losses.
        """
        if not (0 <= cashback_percentage <= 100):
            raise ValueError("Cashback percentage must be between 0 and 100.")
        self.cashback_percentage = cashback_percentage / 100  # Convert to decimal

    def calculate_cashback(self, losses: float) -> float:
        """
        Calculates the cashback amount based on the user's losses.

        :param losses: The total losses incurred by the user.
        :return: The cashback amount to be awarded.
        """
        if losses < 0:
            raise ValueError("Losses cannot be negative.")
        cashback = losses * self.cashback_percentage
        return round(cashback, 2)  # Round to two decimal places for currency

    def apply_cashback(self, user_balance: float, cashback: float) -> float:
        """
        Applies the calculated cashback to the user's balance.

        :param user_balance: The current balance of the user.
        :param cashback: The cashback amount to be applied.
        :return: The new balance after applying cashback.
        """
        if user_balance < 0:
            raise ValueError("User balance cannot be negative.")
        new_balance = user_balance + cashback
        return round(new_balance, 2)  # Round to two decimal places for currency


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the loyalty program with a 10% cashback on losses
        loyalty_program = LoyaltyProgram(cashback_percentage=10)

        # Example losses incurred by the user
        user_losses = 150.00  # User lost $150
        user_balance = 200.00  # User's current balance is $200

        # Calculate cashback based on losses
        cashback_amount = loyalty_program.calculate_cashback(losses=user_losses)
        print(f"Cashback amount: ${cashback_amount}")

        # Apply cashback to the user's balance
        new_balance = loyalty_program.apply_cashback(user_balance=user_balance, cashback=cashback_amount)
        print(f"New user balance: ${new_balance}")

    except ValueError as e:
        print(f"Error: {e}")
```
