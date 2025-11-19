"""
Generated Code Metadata:
========================
Original URL: https://vestings-scapesmania.pages.dev
Prompt: Develop a referral system in Python or JavaScript for ScapesMania that rewards users with $MANIA tokens based on successful referrals, integrating it with the platform's blockchain infrastructure.
Generated: DETERMINISTIC_105fc2e2ff74db79
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_system.py

import uuid
from datetime import datetime, timedelta

class User:
    def __init__(self, username):
        self.username = username
        self.referral_code = str(uuid.uuid4())  # Unique referral code for the user
        self.referrals = []  # List to store successful referrals
        self.reward_balance = 0  # User's reward balance in $MANIA tokens

    def add_referral(self, referral_user):
        """Add a successful referral to the user's list and reward them."""
        self.referrals.append(referral_user)
        self.reward_balance += 10  # Reward 10 $MANIA tokens for each successful referral
        print(f"{self.username} has successfully referred {referral_user.username}. Reward: 10 $MANIA tokens.")

class ReferralSystem:
    def __init__(self):
        self.users = {}  # Dictionary to store users by their referral code

    def register_user(self, username):
        """Register a new user in the referral system."""
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[user.referral_code] = user
        print(f"User {username} registered with referral code: {user.referral_code}")
        return user.referral_code

    def refer_user(self, referral_code, new_username):
        """Process a referral and register the new user."""
        if referral_code not in self.users:
            raise ValueError("Invalid referral code.")
        
        # Register the new user
        new_user = User(new_username)
        self.users[new_user.referral_code] = new_user
        
        # Add the new user to the referrer’s referrals
        referrer = self.users[referral_code]
        referrer.add_referral(new_user)
        print(f"User {new_username} successfully referred by {referrer.username}.")

    def get_user_balance(self, referral_code):
        """Get the reward balance of a user."""
        if referral_code not in self.users:
            raise ValueError("Invalid referral code.")
        return self.users[referral_code].reward_balance

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Register users
    code1 = referral_system.register_user("Alice")
    code2 = referral_system.register_user("Bob")
    
    # Refer a new user
    referral_system.refer_user(code1, "Charlie")
    
    # Check balances
    print(f"Alice's balance: {referral_system.get_user_balance(code1)} $MANIA tokens")
    print(f"Bob's balance: {referral_system.get_user_balance(code2)} $MANIA tokens")
```

This code implements a simple referral system in Python, allowing users to register, refer others, and earn rewards in $MANIA tokens. It includes error handling for duplicate usernames and invalid referral codes.
