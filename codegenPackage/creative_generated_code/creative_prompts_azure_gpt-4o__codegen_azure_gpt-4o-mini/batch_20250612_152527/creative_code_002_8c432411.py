"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubaswap.com
Prompt: Generate code to implement a bonus system for new users, daily cashback, and promotional offers, as described on the MESIN128 platform.
Generated: DETERMINISTIC_8c4324117db5f3ec
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import random

class User:
    """Class to represent a user in the system."""
    
    def __init__(self, user_id, registration_date):
        self.user_id = user_id
        self.registration_date = registration_date
        self.bonus_balance = 0
        self.cashback_balance = 0

class BonusSystem:
    """Class to handle bonus, cashback, and promotional offers for users."""
    
    def __init__(self):
        self.users = {}

    def register_user(self, user_id):
        """Register a new user and initialize their bonus system."""
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists.")
        
        registration_date = datetime.now()
        self.users[user_id] = User(user_id, registration_date)
        self.apply_new_user_bonus(user_id)
        print(f"User {user_id} registered successfully.")

    def apply_new_user_bonus(self, user_id):
        """Apply a welcome bonus for new users."""
        bonus_amount = 100  # Fixed bonus amount for new users
        user = self.users[user_id]
        user.bonus_balance += bonus_amount
        print(f"Applied a new user bonus of {bonus_amount} to user {user_id}.")

    def apply_daily_cashback(self, user_id, purchase_amount):
        """Calculate and apply daily cashback for a user's purchase."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found.")
        
        cashback_percentage = 0.05  # 5% cashback
        cashback_amount = purchase_amount * cashback_percentage
        user = self.users[user_id]
        user.cashback_balance += cashback_amount
        print(f"Applied a cashback of {cashback_amount} to user {user_id} for a purchase of {purchase_amount}.")

    def apply_promotional_offer(self, user_id, offer_amount):
        """Apply a promotional offer to a user's account."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found.")
        
        user = self.users[user_id]
        user.bonus_balance += offer_amount
        print(f"Applied a promotional offer of {offer_amount} to user {user_id}.")

    def get_user_balances(self, user_id):
        """Retrieve the current bonus and cashback balances for a user."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found.")
        
        user = self.users[user_id]
        return {
            "bonus_balance": user.bonus_balance,
            "cashback_balance": user.cashback_balance
        }

# Example usage:
if __name__ == "__main__":
    bonus_system = BonusSystem()

    try:
        # Register new users
        bonus_system.register_user("user1")
        bonus_system.register_user("user2")

        # Apply daily cashback
        bonus_system.apply_daily_cashback("user1", 200)
        
        # Apply a promotional offer
        bonus_system.apply_promotional_offer("user2", 50)

        # Print user balances
        print(bonus_system.get_user_balances("user1"))
        print(bonus_system.get_user_balances("user2"))

    except ValueError as e:
        print(f"Error: {e}")
```
