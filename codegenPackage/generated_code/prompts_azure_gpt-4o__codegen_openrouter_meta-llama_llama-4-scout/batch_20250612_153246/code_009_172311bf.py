"""
Generated Code Metadata:
========================
Original URL: https://blogdotrabalhadordigital.com
Prompt: Write code to implement a promotional system where users can claim discounts or bonuses, as seen on Pelangi189, based on their gameplay activity.
Generated: DETERMINISTIC_172311bfd156b68f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# promotional_system.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class PromotionType(Enum):
    """Enum for promotion types."""
    DISCOUNT = 1
    BONUS = 2

class User:
    """Class representing a user."""
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.gameplay_activity = {
            'login_count': 0,
            'play_count': 0,
            'last_login': None
        }
        self.promotions = []

class Promotion:
    """Class representing a promotion."""
    def __init__(self, promotion_id: int, promotion_type: PromotionType, 
                 discount_percentage: float = 0, bonus_amount: float = 0):
        self.promotion_id = promotion_id
        self.promotion_type = promotion_type
        self.discount_percentage = discount_percentage
        self.bonus_amount = bonus_amount
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(days=7)

class PromotionalSystem:
    """Class representing the promotional system."""
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.promotions: Dict[int, Promotion] = {}

    def add_user(self, user_id: int):
        """Add a new user to the system."""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)

    def add_promotion(self, promotion_id: int, promotion_type: PromotionType, 
                      discount_percentage: float = 0, bonus_amount: float = 0):
        """Add a new promotion to the system."""
        if promotion_id not in self.promotions:
            self.promotions[promotion_id] = Promotion(promotion_id, promotion_type, 
                                                       discount_percentage, bonus_amount)

    def claim_promotion(self, user_id: int, promotion_id: int):
        """Claim a promotion for a user."""
        if user_id in self.users and promotion_id in self.promotions:
            user = self.users[user_id]
            promotion = self.promotions[promotion_id]
            if promotion.start_time <= datetime.now() <= promotion.end_time:
                user.promotions.append(promotion)
                print(f"Promotion {promotion_id} claimed for user {user_id}")
            else:
                print(f"Promotion {promotion_id} is not available")
        else:
            print(f"User {user_id} or promotion {promotion_id} does not exist")

    def update_gameplay_activity(self, user_id: int):
        """Update the gameplay activity for a user."""
        if user_id in self.users:
            user = self.users[user_id]
            user.gameplay_activity['login_count'] += 1
            user.gameplay_activity['last_login'] = datetime.now()
            print(f"Gameplay activity updated for user {user_id}")
        else:
            print(f"User {user_id} does not exist")

    def check_eligibility(self, user_id: int):
        """Check if a user is eligible for promotions."""
        if user_id in self.users:
            user = self.users[user_id]
            if user.gameplay_activity['login_count'] >= 5:
                print(f"User {user_id} is eligible for promotions")
                return True
            else:
                print(f"User {user_id} is not eligible for promotions")
                return False
        else:
            print(f"User {user_id} does not exist")
            return False

def main():
    promotional_system = PromotionalSystem()

    # Add users
    promotional_system.add_user(1)
    promotional_system.add_user(2)

    # Add promotions
    promotional_system.add_promotion(1, PromotionType.DISCOUNT, discount_percentage=10)
    promotional_system.add_promotion(2, PromotionType.BONUS, bonus_amount=100)

    # Update gameplay activity
    promotional_system.update_gameplay_activity(1)
    promotional_system.update_gameplay_activity(1)
    promotional_system.update_gameplay_activity(1)
    promotional_system.update_gameplay_activity(1)
    promotional_system.update_gameplay_activity(1)

    # Check eligibility
    promotional_system.check_eligibility(1)

    # Claim promotion
    promotional_system.claim_promotion(1, 1)

if __name__ == "__main__":
    main()
```
