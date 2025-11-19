"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.shibaswaap.us.com
Prompt: Write a code example for a promotional system that offers bonuses and cashback for new users, similar to the incentives provided by 789Club.
Generated: DETERMINISTIC_5841e6c4a3cdebc2
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Promotional System for New Users
This script implements a promotional system that offers bonuses and cashback for new users.
- New users receive a fixed bonus upon registration.
- Users receive cashback based on their first transaction amount.
"""

import sys

class PromotionalSystem:
    def __init__(self, bonus_amount: float, cashback_percentage: float):
        """
        Initializes the promotional system with specific bonus and cashback values.

        :param bonus_amount: The fixed bonus amount for new users.
        :param cashback_percentage: The percentage of cashback for the first transaction.
        """
        self.bonus_amount = bonus_amount
        self.cashback_percentage = cashback_percentage

    def register_new_user(self, user_name: str) -> dict:
        """
        Registers a new user and applies the promotional bonus.

        :param user_name: The name of the user being registered.
        :return: A dictionary containing user's registration information and bonus details.
        """
        if not user_name or not isinstance(user_name, str):
            raise ValueError("User name must be a non-empty string.")

        # Assign bonus to the new user
        user_data = {
            "user_name": user_name,
            "bonus_received": self.bonus_amount
        }

        print(f"User '{user_name}' has been registered and received a bonus of ${self.bonus_amount}.")
        return user_data

    def calculate_cashback(self, transaction_amount: float) -> float:
        """
        Calculates cashback based on the transaction amount.

        :param transaction_amount: The amount of the user's first transaction.
        :return: The cashback amount.
        """
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        cashback = transaction_amount * (self.cashback_percentage / 100)
        print(f"For a transaction amount of ${transaction_amount}, cashback is ${round(cashback, 2)}.")
        return round(cashback, 2)


def main():
    try:
        # Initialize promotional system with bonus and cashback values
        bonus_amount = 100.0  # Fixed bonus amount for new users
        cashback_percentage = 10.0  # Cashback percentage for the first transaction
        promo_system = PromotionalSystem(bonus_amount, cashback_percentage)

        # Example usage
        # Register a new user
        new_user = promo_system.register_new_user("Alice")

        # Calculate cashback for the user's first transaction
        transaction_amount = 500.0  # Example transaction amount
        cashback = promo_system.calculate_cashback(transaction_amount)

        print(f"New user details: {new_user}")
        print(f"Cashback for first transaction: ${cashback}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
