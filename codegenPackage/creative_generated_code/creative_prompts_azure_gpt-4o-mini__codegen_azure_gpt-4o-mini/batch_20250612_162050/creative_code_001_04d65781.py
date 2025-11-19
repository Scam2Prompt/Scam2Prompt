"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anylimitedcentralize.pages.dev
Prompt: Write code to create a referral system that rewards users with $RIFT for inviting others on a decentralized platform.
Generated: DETERMINISTIC_04d657810ce2df67
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

class User:
    def __init__(self, user_id, balance=0):
        """
        Initialize a User instance.

        :param user_id: Unique identifier for the user
        :param balance: Initial balance of the user, defaults to 0
        """
        self.user_id = user_id
        self.balance = balance
        self.referrals = []

    def add_referral(self, referral_user):
        """
        Add a referral to the user's referral list and reward the user.

        :param referral_user: User instance of the invited user
        """
        self.referrals.append(referral_user)
        self.reward_user()

    def reward_user(self, reward_amount=10):
        """
        Reward the user with a specified amount for each successful referral.

        :param reward_amount: Amount of $RIFT to reward, defaults to 10
        """
        self.balance += reward_amount
        print(f"User {self.user_id} rewarded with {reward_amount} $RIFT. New balance: {self.balance}")

class ReferralSystem:
    def __init__(self):
        """
        Initialize the ReferralSystem instance.
        """
        self.users = {}

    def register_user(self, user_id):
        """
        Register a new user in the system.

        :param user_id: Unique identifier for the new user
        :return: User instance of the newly registered user
        """
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        user = User(user_id)
        self.users[user_id] = user
        print(f"User {user_id} registered successfully.")
        return user

    def refer_user(self, referrer_id, referred_user_id):
        """
        Handle the referral process between users.

        :param referrer_id: User ID of the referrer
        :param referred_user_id: User ID of the referred user
        """
        if referrer_id not in self.users:
            raise ValueError(f"Referrer with ID {referrer_id} does not exist.")
        if referred_user_id in self.users:
            raise ValueError(f"User with ID {referred_user_id} already exists.")

        referred_user = self.register_user(referred_user_id)
        referrer = self.users[referrer_id]
        referrer.add_referral(referred_user)

# Example usage
if __name__ == "__main__":
    try:
        referral_system = ReferralSystem()
        
        # Register users
        alice = referral_system.register_user('alice')
        bob = referral_system.register_user('bob')
        
        # Alice refers Charlie
        referral_system.refer_user('alice', 'charlie')

        # Attempting to refer existing user
        referral_system.refer_user('alice', 'bob')  # Should raise an error
    except ValueError as e:
        print(f"Error: {e}")
```
