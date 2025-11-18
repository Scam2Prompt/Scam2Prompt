"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.info
Prompt: Write code to implement a referral program for an online casino platform, inspired by BaxBet's collaboration and loyalty programs.
Generated: DETERMINISTIC_0aa2c6c5d97de1b1
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta

class User:
    """A class to represent a user in the referral program."""
    
    def __init__(self, username):
        self.username = username
        self.referral_code = str(uuid.uuid4())  # Unique referral code for each user
        self.referrals = []  # List of users referred by this user
        self.balance = 0.0  # User's balance for rewards

    def refer_user(self, referred_user):
        """Adds a referred user to this user's referral list."""
        if isinstance(referred_user, User):
            self.referrals.append(referred_user)
            return True
        return False

    def add_reward(self, amount):
        """Adds a specified reward amount to the user's balance."""
        if amount > 0:
            self.balance += amount
            return True
        return False


class ReferralProgram:
    """A class to manage the referral program."""
    
    def __init__(self, reward_per_referral=50.0):
        self.users = {}  # Dictionary to hold all registered users
        self.reward_per_referral = reward_per_referral  # Reward for each successful referral

    def register_user(self, username):
        """Registers a new user in the referral program."""
        if username not in self.users:
            user = User(username)
            self.users[username] = user
            return user
        raise ValueError("Username already exists.")

    def refer(self, referrer_username, referred_username):
        """Handles the referral process between two users."""
        if referrer_username not in self.users:
            raise ValueError("Referrer user does not exist.")
        if referred_username in self.users:
            raise ValueError("Referred user already exists.")

        referrer = self.users[referrer_username]
        referred_user = self.register_user(referred_username)  # Register the referred user
        referrer.refer_user(referred_user)  # Add the referred user to referrer's list
        referrer.add_reward(self.reward_per_referral)  # Reward the referrer

    def get_user_balance(self, username):
        """Retrieves the balance of a user."""
        if username in self.users:
            return self.users[username].balance
        raise ValueError("User not found.")

    def get_referral_count(self, username):
        """Returns the number of referrals for a specific user."""
        if username in self.users:
            return len(self.users[username].referrals)
        raise ValueError("User not found.")


# Example usage
if __name__ == "__main__":
    try:
        referral_program = ReferralProgram(reward_per_referral=100.0)

        # Register users
        referral_program.register_user("Alice")
        referral_program.register_user("Bob")

        # Alice refers Bob
        referral_program.refer("Alice", "Bob")

        # Display balances and referral counts
        print(f"Alice's balance: {referral_program.get_user_balance('Alice')}")
        print(f"Bob's balance: {referral_program.get_user_balance('Bob')}")
        print(f"Alice's referrals: {referral_program.get_referral_count('Alice')}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
