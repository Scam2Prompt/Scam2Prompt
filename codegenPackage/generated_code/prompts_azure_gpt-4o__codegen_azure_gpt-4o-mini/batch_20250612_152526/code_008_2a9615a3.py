"""
Generated Code Metadata:
========================
Original URL: https://betpandaofficial.com
Prompt: Develop a promotional campaign system in code that tracks bonuses and cashback offers, inspired by Betpanda's generous promotions.
Generated: DETERMINISTIC_2a9615a3ca8f99ba
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Promotion:
    """Class to represent a promotional campaign."""
    
    def __init__(self, name: str, bonus_amount: float, cashback_percentage: float, duration_days: int):
        self.id = uuid.uuid4()  # Unique identifier for the promotion
        self.name = name  # Name of the promotion
        self.bonus_amount = bonus_amount  # Fixed bonus amount
        self.cashback_percentage = cashback_percentage  # Percentage for cashback
        self.start_date = datetime.now()  # Start date of the promotion
        self.end_date = self.start_date + timedelta(days=duration_days)  # End date of the promotion

    def is_active(self) -> bool:
        """Check if the promotion is currently active."""
        return self.start_date <= datetime.now() <= self.end_date

class User:
    """Class to represent a user in the promotional system."""
    
    def __init__(self, username: str):
        self.username = username  # Username of the user
        self.bonuses: List[float] = []  # List to track bonuses received
        self.cashbacks: List[float] = []  # List to track cashback received

    def add_bonus(self, amount: float):
        """Add a bonus to the user's account."""
        if amount < 0:
            raise ValueError("Bonus amount must be non-negative.")
        self.bonuses.append(amount)

    def add_cashback(self, amount: float):
        """Add cashback to the user's account."""
        if amount < 0:
            raise ValueError("Cashback amount must be non-negative.")
        self.cashbacks.append(amount)

    def total_bonuses(self) -> float:
        """Calculate the total bonuses received by the user."""
        return sum(self.bonuses)

    def total_cashbacks(self) -> float:
        """Calculate the total cashbacks received by the user."""
        return sum(self.cashbacks)

class PromotionSystem:
    """Class to manage promotions and user interactions."""
    
    def __init__(self):
        self.promotions: Dict[uuid.UUID, Promotion] = {}  # Dictionary to store active promotions
        self.users: Dict[str, User] = {}  # Dictionary to store users

    def create_promotion(self, name: str, bonus_amount: float, cashback_percentage: float, duration_days: int) -> Promotion:
        """Create a new promotion and add it to the system."""
        promotion = Promotion(name, bonus_amount, cashback_percentage, duration_days)
        self.promotions[promotion.id] = promotion
        return promotion

    def register_user(self, username: str) -> User:
        """Register a new user in the system."""
        if username in self.users:
            raise ValueError("User already exists.")
        user = User(username)
        self.users[username] = user
        return user

    def apply_promotion(self, username: str, promotion_id: uuid.UUID) -> Optional[str]:
        """Apply a promotion to a user if the promotion is active."""
        user = self.users.get(username)
        promotion = self.promotions.get(promotion_id)

        if not user:
            return "User not found."
        if not promotion:
            return "Promotion not found."
        if not promotion.is_active():
            return "Promotion is not active."

        # Apply bonus and cashback
        user.add_bonus(promotion.bonus_amount)
        cashback_amount = promotion.bonus_amount * (promotion.cashback_percentage / 100)
        user.add_cashback(cashback_amount)

        return f"Promotion applied: {promotion.name}. Bonus: {promotion.bonus_amount}, Cashback: {cashback_amount}"

# Example usage
if __name__ == "__main__":
    try:
        system = PromotionSystem()
        user = system.register_user("john_doe")
        promotion = system.create_promotion("Spring Sale", 50.0, 10.0, 30)

        result = system.apply_promotion("john_doe", promotion.id)
        print(result)

        print(f"Total Bonuses: {user.total_bonuses()}")
        print(f"Total Cashbacks: {user.total_cashbacks()}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
