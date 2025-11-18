"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betpandaofficial.com
Prompt: Develop a promotional campaign system in code that tracks bonuses and cashback offers, inspired by Betpanda's generous promotions.
Generated: DETERMINISTIC_2a9615a3ca8f99ba
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta

class Promotion:
    """Class to represent a promotional campaign with bonuses and cashback offers."""
    
    def __init__(self, name, bonus_amount, cashback_percentage, valid_days):
        """
        Initialize a new promotion.

        :param name: Name of the promotion.
        :param bonus_amount: Fixed bonus amount for the promotion.
        :param cashback_percentage: Percentage of cashback offered.
        :param valid_days: Duration the promotion is valid (in days).
        """
        self.id = uuid.uuid4()  # Unique identifier for the promotion
        self.name = name
        self.bonus_amount = bonus_amount
        self.cashback_percentage = cashback_percentage
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=valid_days)
    
    def is_active(self):
        """Check if the promotion is currently active."""
        return self.start_date <= datetime.now() <= self.end_date


class User:
    """Class to represent a user in the promotional system."""
    
    def __init__(self, username):
        """
        Initialize a new user.

        :param username: Unique username for the user.
        """
        self.username = username
        self.bonus_balance = 0.0
        self.cashback_balance = 0.0
        self.promotions_applied = []

    def apply_promotion(self, promotion):
        """
        Apply a promotion to the user's account if it's active.

        :param promotion: The Promotion object to apply.
        :raises ValueError: If the promotion is not active.
        """
        if not promotion.is_active():
            raise ValueError(f"Promotion '{promotion.name}' is not active.")

        self.bonus_balance += promotion.bonus_amount
        self.promotions_applied.append(promotion)
        print(f"Applied promotion '{promotion.name}'. Bonus added: {promotion.bonus_amount}")

    def calculate_cashback(self, purchase_amount):
        """
        Calculate cashback for a given purchase amount based on active promotions.

        :param purchase_amount: The total amount of the purchase.
        :return: Cash back earned.
        """
        cashback = 0.0
        for promotion in self.promotions_applied:
            if promotion.is_active():
                cashback += purchase_amount * (promotion.cashback_percentage / 100)
        self.cashback_balance += cashback
        return cashback


# Example usage
if __name__ == "__main__":
    try:
        # Create a user
        user = User(username="john_doe")

        # Create a promotion
        promotion1 = Promotion(name="Summer Bonus", bonus_amount=50.0, cashback_percentage=10, valid_days=30)

        # Apply the promotion
        user.apply_promotion(promotion1)

        # Simulate a purchase and calculate cashback
        purchase_amount = 200.0
        cashback_earned = user.calculate_cashback(purchase_amount)
        print(f"Cashback earned on a purchase of {purchase_amount}: {cashback_earned}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
