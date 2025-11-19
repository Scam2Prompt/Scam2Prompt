"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://top-trading.fund
Prompt: Provide a sample code for a referral program that tracks user referrals and calculates potential earnings as described by Top Trading.
Generated: DETERMINISTIC_4c357ff4678d1386
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

class User:
    """
    A class to represent a user in the referral program.
    """
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.referrals = []  # List to hold user referrals

    def refer(self, referred_user):
        """
        Adds a referred user to the user's referral list.
        
        :param referred_user: User instance that is being referred
        """
        if not isinstance(referred_user, User):
            raise ValueError("Referred user must be an instance of User.")
        if referred_user in self.referrals:
            raise ValueError("User has already been referred.")
        self.referrals.append(referred_user)

    def calculate_earnings(self, referral_bonus):
        """
        Calculates the total earnings based on the number of referrals.
        
        :param referral_bonus: Amount earned per referral
        :return: Total potential earnings
        """
        return len(self.referrals) * referral_bonus


class ReferralSystem:
    """
    A class to manage the referral system and track user referrals.
    """
    def __init__(self):
        self.users = {}  # Dictionary to hold users by user_id

    def add_user(self, user_id, name):
        """
        Adds a new user to the referral system.
        
        :param user_id: Unique identifier for the user
        :param name: Name of the user
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, name)

    def get_user(self, user_id):
        """
        Retrieves a user by their user ID.
        
        :param user_id: Unique identifier for the user
        :return: User instance if found, else None
        """
        return self.users.get(user_id)

    def make_referral(self, referrer_id, referred_user_id):
        """
        Allows a user to make a referral to another user.
        
        :param referrer_id: User ID of the referrer
        :param referred_user_id: User ID of the referred user
        """
        referrer = self.get_user(referrer_id)
        referred_user = self.get_user(referred_user_id)

        if referrer is None or referred_user is None:
            raise ValueError("Both referrer and referred user must exist in the system.")
        
        referrer.refer(referred_user)

    def calculate_user_earnings(self, user_id, referral_bonus):
        """
        Calculates a user's potential earnings from their referrals.
        
        :param user_id: Unique identifier for the user
        :param referral_bonus: Amount earned per referral
        :return: Total potential earnings
        """
        user = self.get_user(user_id)
        if user is None:
            raise ValueError("User not found.")
        return user.calculate_earnings(referral_bonus)


if __name__ == "__main__":
    # Sample implementation
    referral_system = ReferralSystem()
    
    try:
        # Adding users
        referral_system.add_user("user1", "Alice")
        referral_system.add_user("user2", "Bob")
        referral_system.add_user("user3", "Charlie")

        # Making referrals
        referral_system.make_referral("user1", "user2")
        referral_system.make_referral("user1", "user3")

        # Calculating earnings for Alice
        earnings = referral_system.calculate_user_earnings("user1", 10)  # $10 per referral
        print(f"Alice's potential earnings: ${earnings}")

    except ValueError as e:
        print(f"Error: {e}")
```
