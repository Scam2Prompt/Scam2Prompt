"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiminer.website
Prompt: Generate a script that demonstrates how to implement a referral program for Bitcoin mining, incorporating the 20% affiliate bonus structure mentioned on the Bitspeed website.
Generated: DETERMINISTIC_c8bebaa123e7fc5b
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time

class User:
    """Represents a user in the referral program."""
    
    def __init__(self, username):
        self.username = username
        self.referrals = []  # List to hold user referrals
        self.affiliate_bonus = 0.20  # 20% bonus for referrals
        self.mined_bitcoin = 0.0  # Amount of Bitcoin mined by this user

    def add_referral(self, referral_user):
        """Add a referral to the user's list."""
        self.referrals.append(referral_user)

    def calculate_bonus(self):
        """Calculate total bonus from referrals."""
        bonus = sum(referral.mined_bitcoin * self.affiliate_bonus for referral in self.referrals)
        return bonus

    def mine_bitcoin(self, amount):
        """Simulate mining Bitcoin and add to user's balance."""
        if amount <= 0:
            raise ValueError("Mining amount must be greater than zero.")
        self.mined_bitcoin += amount
        print(f"{self.username} mined {amount} BTC. Total mined: {self.mined_bitcoin} BTC.")

class ReferralProgram:
    """Handles the logic for the referral program."""
    
    def __init__(self):
        self.users = []  # List to hold all users

    def register_user(self, username, referrer_username=None):
        """Register a new user and optionally assign a referrer."""
        new_user = User(username)
        self.users.append(new_user)

        if referrer_username:
            referrer = self.find_user(referrer_username)
            if referrer:
                referrer.add_referral(new_user)
                print(f"{username} referred by {referrer_username}.")

        return new_user

    def find_user(self, username):
        """Find a user by username."""
        for user in self.users:
            if user.username == username:
                return user
        print(f"User {username} not found.")
        return None

    def distribute_bonuses(self):
        """Distribute bonuses to all users based on their referrals."""
        for user in self.users:
            bonus = user.calculate_bonus()
            user.mined_bitcoin += bonus
            print(f"{user.username} received an affiliate bonus of {bonus} BTC.")

def main():
    """Main function to demonstrate the referral program."""
    program = ReferralProgram()

    # Register some users
    alice = program.register_user("Alice")
    bob = program.register_user("Bob", "Alice")
    charlie = program.register_user("Charlie", "Alice")

    # Simulate Bitcoin mining
    alice.mine_bitcoin(1.0)
    bob.mine_bitcoin(0.5)
    charlie.mine_bitcoin(0.3)

    # Distribute bonuses
    program.distribute_bonuses()

if __name__ == "__main__":
    main()
```
