"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starltoken.com
Prompt: Generate code to implement a promotional system for a cryptocurrency casino, including features like "free spins," "welcome bonuses," and "daily rebates," as described on the STARL Token site.
Generated: DETERMINISTIC_63aa5ecb86039b05
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import Dict, List

class PromotionalSystem:
    """
    A promotional system for a cryptocurrency casino including features like 
    free spins, welcome bonuses, and daily rebates.
    """

    def __init__(self):
        # Store user data and promotions
        self.users: Dict[str, Dict] = {}
        self.promotions: Dict[str, Dict] = {
            "welcome_bonus": {"amount": 100, "conditions": "First deposit only"},
            "free_spins": {"count": 10, "conditions": "Available once daily"},
            "daily_rebate": {"rate": 0.05, "conditions": "5% rebate on daily losses"},
        }

    def register_user(self, user_id: str):
        """
        Registers a new user into the system.
        """
        if user_id in self.users:
            raise ValueError("User already registered.")
        
        self.users[user_id] = {
            "balance": 0,
            "last_claimed_spins": None,
            "daily_loss": 0,
            "received_welcome_bonus": False
        }

    def apply_welcome_bonus(self, user_id: str):
        """
        Applies a welcome bonus to a user's account upon their first deposit.
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")
        
        if self.users[user_id]["received_welcome_bonus"]:
            raise ValueError("Welcome bonus already claimed.")
        
        self.users[user_id]["balance"] += self.promotions["welcome_bonus"]["amount"]
        self.users[user_id]["received_welcome_bonus"] = True

    def claim_free_spins(self, user_id: str):
        """
        Allows a user to claim free spins once per day.
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")
        
        today = datetime.now().date()
        last_claimed = self.users[user_id]["last_claimed_spins"]

        if last_claimed is not None and last_claimed == today:
            raise ValueError("Free spins already claimed today.")
        
        self.users[user_id]["last_claimed_spins"] = today
        return self.promotions["free_spins"]["count"]

    def record_daily_loss(self, user_id: str, amount: float):
        """
        Records a user's daily losses to calculate rebates.
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")
        
        if amount < 0:
            raise ValueError("Loss amount cannot be negative.")
        
        self.users[user_id]["daily_loss"] += amount

    def apply_daily_rebate(self, user_id: str):
        """
        Applies a daily rebate to a user's account based on their losses.
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")
        
        daily_loss = self.users[user_id]["daily_loss"]
        rebate_rate = self.promotions["daily_rebate"]["rate"]
        rebate_amount = daily_loss * rebate_rate

        self.users[user_id]["balance"] += rebate_amount
        self.users[user_id]["daily_loss"] = 0  # Reset daily loss after rebate
        return rebate_amount

    def get_user_info(self, user_id: str) -> Dict:
        """
        Retrieves user information.
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")
        
        return self.users[user_id]

# Example usage:
if __name__ == "__main__":
    # Initialize the promotional system
    promo_system = PromotionalSystem()

    # Register a user
    user_id = "user123"
    promo_system.register_user(user_id)

    # Apply welcome bonus
    promo_system.apply_welcome_bonus(user_id)

    # Claim free spins
    free_spins = promo_system.claim_free_spins(user_id)
    print(f"User {user_id} claimed {free_spins} free spins.")

    # Record daily loss
    promo_system.record_daily_loss(user_id, 200.0)

    # Apply daily rebate
    rebate = promo_system.apply_daily_rebate(user_id)
    print(f"User {user_id} received a rebate of {rebate}.")

    # Get user info
    user_info = promo_system.get_user_info(user_id)
    print(f"User Info: {user_info}")
```
