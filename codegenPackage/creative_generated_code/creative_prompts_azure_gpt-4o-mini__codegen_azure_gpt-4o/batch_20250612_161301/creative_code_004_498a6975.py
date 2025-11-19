"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betpandaofficial.com
Prompt: Provide a code example for implementing a cashback system for losses in a casino application, reflecting the promotions offered by Betpanda.
Generated: DETERMINISTIC_498a697579dccc53
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Setting up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CashbackSystem:
    """
    A class to implement the cashback system for a casino application.
    """
    def __init__(self, cashback_percentage):
        """
        Initializes the CashbackSystem with the specified cashback percentage.
        :param cashback_percentage: Cashback percentage offered by the casino (e.g., 10 for 10%).
        """
        if not (0 <= cashback_percentage <= 100):
            raise ValueError("Cashback percentage must be between 0 and 100.")
        self.cashback_percentage = cashback_percentage

    def calculate_cashback(self, losses):
        """
        Calculates the cashback amount based on the user's losses.
        :param losses: Total losses incurred by the user.
        :return: The cashback amount.
        """
        if losses < 0:
            raise ValueError("Losses cannot be negative.")
        return round(losses * (self.cashback_percentage / 100), 2)

    def apply_cashback(self, user_account, losses):
        """
        Applies the cashback to the user's account.
        :param user_account: A dictionary representing the user's account with keys 'balance' and 'username'.
        :param losses: Total losses incurred by the user.
        :return: Updated user account with the cashback applied.
        """
        if not isinstance(user_account, dict) or 'balance' not in user_account or 'username' not in user_account:
            raise ValueError("Invalid user account format. Must be a dictionary with 'balance' and 'username' keys.")

        try:
            cashback = self.calculate_cashback(losses)
            user_account['balance'] += cashback
            logging.info(f"Cashback of ${cashback} applied to user '{user_account['username']}'")
        except Exception as e:
            logging.error(f"Failed to apply cashback: {e}")
            raise

        return user_account


# Example usage:
if __name__ == "__main__":
    # Define the cashback percentage (e.g., 10%)
    cashback_percentage = 10

    # Instantiate the CashbackSystem
    cashback_system = CashbackSystem(cashback_percentage)

    # Example user account and losses
    user_account = {"username": "john_doe", "balance": 1000.00}
    losses = 150.00

    try:
        updated_account = cashback_system.apply_cashback(user_account, losses)
        print(f"Updated account: {updated_account}")
    except Exception as e:
        print(f"Error: {e}")
```
