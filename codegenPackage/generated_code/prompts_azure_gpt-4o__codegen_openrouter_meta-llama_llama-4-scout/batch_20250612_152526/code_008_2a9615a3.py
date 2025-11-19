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
# promotional_campaign_system.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class PromotionType(str, Enum):
    """Type of promotion."""
    BONUS = "bonus"
    CASHBACK = "cashback"

class Promotion:
    """Represents a promotional campaign."""

    def __init__(self, 
                 promotion_id: int, 
                 promotion_type: PromotionType, 
                 name: str, 
                 description: str, 
                 start_date: datetime, 
                 end_date: datetime, 
                 bonus_amount: float = 0.0, 
                 cashback_percentage: float = 0.0):
        """
        Initializes a Promotion.

        Args:
        - promotion_id (int): Unique identifier for the promotion.
        - promotion_type (PromotionType): Type of promotion (bonus or cashback).
        - name (str): Name of the promotion.
        - description (str): Description of the promotion.
        - start_date (datetime): Start date of the promotion.
        - end_date (datetime): End date of the promotion.
        - bonus_amount (float): Bonus amount for bonus promotions (default is 0.0).
        - cashback_percentage (float): Cashback percentage for cashback promotions (default is 0.0).
        """
        self.promotion_id = promotion_id
        self.promotion_type = promotion_type
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.bonus_amount = bonus_amount
        self.cashback_percentage = cashback_percentage

    def is_active(self) -> bool:
        """Checks if the promotion is active."""
        return self.start_date <= datetime.now() <= self.end_date

class User:
    """Represents a user."""

    def __init__(self, user_id: int):
        """
        Initializes a User.

        Args:
        - user_id (int): Unique identifier for the user.
        """
        self.user_id = user_id
        self.promotions: Dict[int, Promotion] = {}
        self.bonus_balance: float = 0.0
        self.cashback_balance: float = 0.0

    def add_promotion(self, promotion: Promotion):
        """Adds a promotion to the user's promotions."""
        self.promotions[promotion.promotion_id] = promotion

    def remove_promotion(self, promotion_id: int):
        """Removes a promotion from the user's promotions."""
        if promotion_id in self.promotions:
            del self.promotions[promotion_id]

class PromotionalCampaignSystem:
    """Manages promotional campaigns."""

    def __init__(self):
        self.promotions: Dict[int, Promotion] = {}
        self.users: Dict[int, User] = {}

    def add_promotion(self, promotion: Promotion):
        """Adds a promotion to the system."""
        self.promotions[promotion.promotion_id] = promotion

    def remove_promotion(self, promotion_id: int):
        """Removes a promotion from the system."""
        if promotion_id in self.promotions:
            del self.promotions[promotion_id]

    def add_user(self, user: User):
        """Adds a user to the system."""
        self.users[user.user_id] = user

    def remove_user(self, user_id: int):
        """Removes a user from the system."""
        if user_id in self.users:
            del self.users[user_id]

    def claim_bonus(self, user_id: int, promotion_id: int):
        """
        Claims a bonus for a user.

        Args:
        - user_id (int): ID of the user.
        - promotion_id (int): ID of the promotion.

        Returns:
        - bool: Whether the claim was successful.
        """
        if user_id not in self.users or promotion_id not in self.promotions:
            return False

        user = self.users[user_id]
        promotion = self.promotions[promotion_id]

        if promotion.promotion_type != PromotionType.BONUS or not promotion.is_active():
            return False

        user.bonus_balance += promotion.bonus_amount
        return True

    def claim_cashback(self, user_id: int, promotion_id: int, amount: float):
        """
        Claims cashback for a user.

        Args:
        - user_id (int): ID of the user.
        - promotion_id (int): ID of the promotion.
        - amount (float): Amount to claim cashback for.

        Returns:
        - bool: Whether the claim was successful.
        """
        if user_id not in self.users or promotion_id not in self.promotions:
            return False

        user = self.users[user_id]
        promotion = self.promotions[promotion_id]

        if promotion.promotion_type != PromotionType.CASHBACK or not promotion.is_active():
            return False

        cashback_amount = amount * promotion.cashback_percentage / 100
        user.cashback_balance += cashback_amount
        return True

def main():
    system = PromotionalCampaignSystem()

    # Create promotions
    promotion1 = Promotion(1, PromotionType.BONUS, "Welcome Bonus", "10% bonus on first deposit", 
                           datetime.now() - timedelta(days=1), datetime.now() + timedelta(days=1), 
                           bonus_amount=10.0)
    promotion2 = Promotion(2, PromotionType.CASHBACK, "Cashback Offer", "5% cashback on all bets", 
                           datetime.now() - timedelta(days=1), datetime.now() + timedelta(days=1), 
                           cashback_percentage=5.0)

    # Add promotions to the system
    system.add_promotion(promotion1)
    system.add_promotion(promotion2)

    # Create a user
    user = User(1)

    # Add the user to the system
    system.add_user(user)

    # Add promotions to the user
    user.add_promotion(promotion1)
    user.add_promotion(promotion2)

    # Claim bonus
    system.claim_bonus(1, 1)
    print(f"User 1 bonus balance: {user.bonus_balance}")

    # Claim cashback
    system.claim_cashback(1, 2, 100.0)
    print(f"User 1 cashback balance: {user.cashback_balance}")

if __name__ == "__main__":
    main()
```
