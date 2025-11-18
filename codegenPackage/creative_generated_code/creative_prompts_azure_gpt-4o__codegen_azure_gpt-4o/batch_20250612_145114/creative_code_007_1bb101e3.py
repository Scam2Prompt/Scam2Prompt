"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shoppiday.site
Prompt: Implement a feature to track user purchases and link them to cashback rewards, inspired by Shoppiday's tools for earning money with purchases.
Generated: DETERMINISTIC_1bb101e382a7fd02
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Feature: Track user purchases and link them to cashback rewards.
Language: Python
Description: This module enables users to earn cashback rewards based on their purchases.
"""

import uuid
from datetime import datetime
from typing import List, Dict


# Custom exception for invalid operations
class CashbackError(Exception):
    pass


# User class to represent a user in the system
class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.purchases: List[Purchase] = []
        self.cashback_balance: float = 0.0

    def add_purchase(self, purchase):
        """Link a purchase to the user and calculate cashback."""
        if not isinstance(purchase, Purchase):
            raise CashbackError("Invalid purchase object.")
        self.purchases.append(purchase)
        self.cashback_balance += purchase.calculate_cashback()

    def get_cashback_balance(self) -> float:
        """Retrieve the user's current cashback balance."""
        return round(self.cashback_balance, 2)

    def get_purchase_history(self) -> List[Dict]:
        """Retrieve all purchases made by the user."""
        return [purchase.to_dict() for purchase in self.purchases]


# Purchase class to represent a purchase transaction
class Purchase:
    def __init__(self, amount: float, category: str, cashback_rate: float = 0.02):
        """
        Initialize a purchase object.
        :param amount: The monetary value of the purchase.
        :param category: Category of the purchase.
        :param cashback_rate: Percentage of cashback (default: 2%).
        """
        if amount <= 0:
            raise CashbackError("Purchase amount must be greater than zero.")
        if not (0 <= cashback_rate <= 1):
            raise CashbackError("Cashback rate must be between 0 and 1.")

        self.purchase_id = str(uuid.uuid4())
        self.amount = amount
        self.category = category
        self.cashback_rate = cashback_rate
        self.date = datetime.now()

    def calculate_cashback(self) -> float:
        """Calculate the cashback amount for the purchase."""
        return self.amount * self.cashback_rate

    def to_dict(self) -> Dict:
        """Convert the purchase object to a dictionary for easy display."""
        return {
            "purchase_id": self.purchase_id,
            "amount": round(self.amount, 2),
            "category": self.category,
            "cashback_rate": self.cashback_rate,
            "cashback_amount": round(self.calculate_cashback(), 2),
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
        }


# Example of usage
if __name__ == "__main__":
    try:
        # Create a user object
        user = User(user_id="U123", name="Alice Doe", email="alice@example.com")

        # Simulate purchases and add them to the user
        purchase1 = Purchase(amount=100.00, category="Groceries")
        user.add_purchase(purchase1)

        purchase2 = Purchase(amount=250.50, category="Electronics", cashback_rate=0.05)
        user.add_purchase(purchase2)

        purchase3 = Purchase(amount=50.00, category="Books")
        user.add_purchase(purchase3)

        # Display user's cashback balance and purchase history
        print(f"Cashback Balance: ${user.get_cashback_balance()}")
        print("Purchase History:")
        for purchase in user.get_purchase_history():
            print(purchase)

    except CashbackError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
