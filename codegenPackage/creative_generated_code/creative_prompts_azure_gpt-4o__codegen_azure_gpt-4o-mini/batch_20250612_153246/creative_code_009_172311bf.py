"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blogdotrabalhadordigital.com
Prompt: Write code to implement a promotional system where users can claim discounts or bonuses, as seen on Pelangi189, based on their gameplay activity.
Generated: DETERMINISTIC_172311bfd156b68f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import Dict, List, Optional

class User:
    """A class to represent a user in the promotional system."""
    
    def __init__(self, user_id: str, gameplay_activity: int):
        self.user_id = user_id
        self.gameplay_activity = gameplay_activity

class Promotion:
    """A class to represent a promotional discount or bonus."""
    
    def __init__(self, promo_id: str, discount_percentage: float, min_activity: int):
        self.promo_id = promo_id
        self.discount_percentage = discount_percentage
        self.min_activity = min_activity

class PromotionalSystem:
    """A class to manage the promotional system."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.promotions: List[Promotion] = []

    def add_user(self, user_id: str, gameplay_activity: int) -> None:
        """Add a user to the promotional system."""
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        self.users[user_id] = User(user_id, gameplay_activity)

    def add_promotion(self, promo_id: str, discount_percentage: float, min_activity: int) -> None:
        """Add a promotion to the system."""
        if discount_percentage <= 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 1 and 100.")
        self.promotions.append(Promotion(promo_id, discount_percentage, min_activity))

    def claim_promotion(self, user_id: str, promo_id: str) -> Optional[float]:
        """Claim a promotion based on user gameplay activity."""
        user = self.users.get(user_id)
        
        if user is None:
            raise ValueError(f"User with ID {user_id} does not exist.")
        
        promotion = next((promo for promo in self.promotions if promo.promo_id == promo_id), None)
        
        if promotion is None:
            raise ValueError(f"Promotion with ID {promo_id} does not exist.")

        if user.gameplay_activity < promotion.min_activity:
            raise ValueError(f"User does not meet the minimum activity requirement of {promotion.min_activity}.")

        # Calculate the discount value
        discount_value = user.gameplay_activity * (promotion.discount_percentage / 100)
        return discount_value

# Example usage
if __name__ == "__main__":
    promo_system = PromotionalSystem()
    
    try:
        promo_system.add_user("user123", 250)
        promo_system.add_promotion("promo001", 20.0, 200)
        
        discount = promo_system.claim_promotion("user123", "promo001")
        print(f"Discount claimed: ${discount:.2f}")
        
    except ValueError as e:
        print(f"An error occurred: {e}")
```
