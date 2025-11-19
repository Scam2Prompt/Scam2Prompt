"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftgoldcoin.com
Prompt: How can I implement a referral program similar to swiftgoldcoin.com in my application, including tiered commission structures?
Generated: DETERMINISTIC_1a0f00210b61257a
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    def __init__(self, user_id, referral_code=None):
        self.user_id = user_id
        self.referral_code = referral_code
        self.referrals = []
        self.commission_earned = 0.0

    def add_referral(self, referral_user):
        """Add a referral user to the user's referral list."""
        self.referrals.append(referral_user)

    def calculate_commission(self, amount):
        """Calculate commission based on the amount of the referral's transaction."""
        tiered_commission_structure = {
            'tier_1': 0.10,  # 10% commission for direct referrals
            'tier_2': 0.05,  # 5% commission for second-tier referrals
            'tier_3': 0.02   # 2% commission for third-tier referrals
        }
        
        # Commission for direct referrals
        self.commission_earned += amount * tiered_commission_structure['tier_1']
        
        # Calculate commissions for second-tier referrals
        for referral in self.referrals:
            self.commission_earned += referral.calculate_second_tier_commission(amount)

    def calculate_second_tier_commission(self, amount):
        """Calculate second-tier commission for referrals made by this user."""
        return amount * 0.05  # 5% commission for second-tier referrals


class ReferralProgram:
    def __init__(self):
        self.users = {}

    def register_user(self, user_id, referral_code=None):
        """Register a new user in the referral program."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        
        user = User(user_id, referral_code)
        self.users[user_id] = user
        
        if referral_code and referral_code in self.users:
            self.users[referral_code].add_referral(user)
        
        return user

    def make_transaction(self, user_id, amount):
        """Record a transaction made by a user and calculate their commission."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        user = self.users[user_id]
        user.calculate_commission(amount)

    def get_user_commission(self, user_id):
        """Get the total commission earned by a user."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        return self.users[user_id].commission_earned


# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    # Register users
    user1 = referral_program.register_user("user1")
    user2 = referral_program.register_user("user2", referral_code="user1")
    user3 = referral_program.register_user("user3", referral_code="user2")
    
    # User2 makes a transaction
    referral_program.make_transaction("user2", 100.0)  # User2 earns commission from their transaction
    referral_program.make_transaction("user1", 50.0)   # User1 earns commission from user2's transaction
    referral_program.make_transaction("user2", 200.0)  # User2 makes another transaction
    
    # Get commissions
    print("User1 Commission:", referral_program.get_user_commission("user1"))  # Expected commission from user2's transactions
    print("User2 Commission:", referral_program.get_user_commission("user2"))  # Expected commission from own transactions
    print("User3 Commission:", referral_program.get_user_commission("user3"))  # Expected to be 0.0
```
