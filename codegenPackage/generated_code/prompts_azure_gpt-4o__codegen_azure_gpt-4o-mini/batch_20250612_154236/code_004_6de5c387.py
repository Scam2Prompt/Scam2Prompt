"""
Generated Code Metadata:
========================
Original URL: https://centraltraderz.com
Prompt: Write code to implement a referral system similar to the affiliate program described on the Centraltraderz website, including multi-level commission percentages.
Generated: DETERMINISTIC_6de5c387690127ff
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """Class representing a user in the referral system."""
    
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.referrals = []  # List to store referred users
        self.referrer = None  # User who referred this user

    def add_referral(self, referral_user):
        """Add a referral to the user's list of referrals."""
        self.referrals.append(referral_user)
        referral_user.referrer = self


class ReferralSystem:
    """Class to manage the referral system and calculate commissions."""
    
    def __init__(self):
        self.users = {}  # Dictionary to store users by user_id
        self.commission_structure = [0.1, 0.05, 0.02]  # Commission percentages for levels 1, 2, and 3

    def add_user(self, user_id, name, referrer_id=None):
        """Add a new user to the system, optionally linking to a referrer."""
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        
        new_user = User(user_id, name)
        self.users[user_id] = new_user
        
        if referrer_id and referrer_id in self.users:
            referrer = self.users[referrer_id]
            referrer.add_referral(new_user)

    def calculate_commission(self, user_id, amount):
        """Calculate total commission for a user based on their referrals."""
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} not found.")
        
        total_commission = 0.0
        user = self.users[user_id]
        
        # Traverse the referral tree up to 3 levels
        current_user = user
        level = 0
        
        while current_user and level < len(self.commission_structure):
            commission = amount * self.commission_structure[level]
            total_commission += commission
            current_user = current_user.referrer
            level += 1
        
        return total_commission

    def get_user_referrals(self, user_id):
        """Get a list of referrals for a given user."""
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} not found.")
        
        return [referral.name for referral in self.users[user_id].referrals]


# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Adding users
    referral_system.add_user("1", "Alice")
    referral_system.add_user("2", "Bob", referrer_id="1")
    referral_system.add_user("3", "Charlie", referrer_id="1")
    referral_system.add_user("4", "David", referrer_id="2")
    
    # Calculate commission for Alice based on a sale of $100
    commission = referral_system.calculate_commission("1", 100)
    print(f"Alice's total commission: ${commission:.2f}")
    
    # Get referrals for Bob
    bob_referrals = referral_system.get_user_referrals("2")
    print(f"Bob's referrals: {bob_referrals}")
```
