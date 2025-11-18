"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalhandelssystem.com
Prompt: Develop a referral program system for a cryptocurrency investment platform that calculates and distributes a 5% referral bonus, as described on Capitalhandelssystem.
Generated: DETERMINISTIC_1f73c0ac3def3ca4
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class representing a user in the referral program."""
    
    def __init__(self, user_id, balance=0.0):
        self.user_id = user_id
        self.balance = balance
        self.referrals = []
        
    def add_referral(self, referral_user):
        """Adds a referral to the user's referral list."""
        if referral_user not in self.referrals:
            self.referrals.append(referral_user)

    def get_balance(self):
        """Returns the user's current balance."""
        return self.balance

    def update_balance(self, amount):
        """Updates the user's balance by a specified amount."""
        if amount < 0 and abs(amount) > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance += amount


class ReferralProgram:
    """Class representing the referral program."""
    
    REFERRAL_BONUS_PERCENTAGE = 0.05  # 5% referral bonus

    def __init__(self):
        self.users = {}
    
    def register_user(self, user_id):
        """Registers a new user in the referral program."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id)
    
    def refer_user(self, referrer_id, referral_id):
        """Handles the referral process between users."""
        if referrer_id not in self.users or referral_id not in self.users:
            raise ValueError("Both users must be registered to refer.")
        
        referrer = self.users[referrer_id]
        referral = self.users[referral_id]
        
        # Add referral
        referrer.add_referral(referral)
        
        # Calculate and distribute referral bonus
        bonus = self.calculate_referral_bonus(referral.get_balance())
        referrer.update_balance(bonus)

    @staticmethod
    def calculate_referral_bonus(amount):
        """Calculates the referral bonus based on the investment amount."""
        return amount * ReferralProgram.REFERRAL_BONUS_PERCENTAGE


# Example Usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    # Register users
    referral_program.register_user("user1")
    referral_program.register_user("user2")
    
    # Simulate a balance for user2 (new user)
    referral_program.users["user2"].update_balance(1000.0)  # User 2 invests $1000
    
    # User 1 refers user 2
    referral_program.refer_user("user1", "user2")

    # Output balances
    print(f"User 1 Balance: {referral_program.users['user1'].get_balance()}")
    print(f"User 2 Balance: {referral_program.users['user2'].get_balance()}")
```
