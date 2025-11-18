"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changelly.shop
Prompt: Develop a referral program system in Python that tracks user referrals and calculates earnings based on exchanges, similar to Changelly's referral program.
Generated: DETERMINISTIC_c64d33fdac83389a
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from collections import defaultdict

class User:
    """Class to represent a user in the referral program."""
    
    def __init__(self, username):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.referrals = []  # List of User instances
        self.earnings = 0.0  # Total earnings from referrals

    def add_referral(self, user):
        """Add a new referral to the user's referral list."""
        self.referrals.append(user)

    def calculate_earnings(self, exchange_amount):
        """Calculate earnings based on the amount exchanged."""
        # Assuming a fixed referral commission rate of 10%
        commission_rate = 0.10
        earnings = exchange_amount * commission_rate
        self.earnings += earnings

class ReferralProgram:
    """Class to manage the referral program for users."""
    
    def __init__(self):
        self.users = {}
        
    def add_user(self, username):
        """Add a new user to the program."""
        if username in self.users:
            raise ValueError("Username already exists.")
        new_user = User(username)
        self.users[username] = new_user
        return new_user

    def refer_user(self, referrer_username, referred_username):
        """Create a referral relationship between users."""
        if referrer_username not in self.users:
            raise ValueError("Referrer not found.")
        if referred_username in self.users:
            raise ValueError("Referred user already exists.")

        referrer = self.users[referrer_username]
        referred_user = self.add_user(referred_username)
        referrer.add_referral(referred_user)

    def process_exchange(self, username, exchange_amount):
        """Process an exchange for a user and distribute earnings to referrals."""
        if username not in self.users:
            raise ValueError("User not found.")
            
        user = self.users[username]
        user.calculate_earnings(exchange_amount)

        # Distribute earnings to each referral
        for referral in user.referrals:
            referral.calculate_earnings(exchange_amount)

    def get_user_info(self, username):
        """Retrieve user information including earnings and referrals."""
        if username not in self.users:
            raise ValueError("User not found.")
        
        user = self.users[username]
        return {
            "username": user.username,
            "user_id": user.user_id,
            "earnings": user.earnings,
            "referrals": [ref.username for ref in user.referrals]
        }

# Example usage of the ReferralProgram
if __name__ == "__main__":
    try:
        referral_program = ReferralProgram()

        # Adding users
        referral_program.add_user("Alice")
        referral_program.add_user("Bob")

        # Creating referral relationship
        referral_program.refer_user("Alice", "Charlie")

        # Processing an exchange
        referral_program.process_exchange("Alice", 100.0)

        # Get user information
        print(referral_program.get_user_info("Alice"))
        print(referral_program.get_user_info("Charlie"))

    except ValueError as e:
        print(f"Error: {e}")
```
