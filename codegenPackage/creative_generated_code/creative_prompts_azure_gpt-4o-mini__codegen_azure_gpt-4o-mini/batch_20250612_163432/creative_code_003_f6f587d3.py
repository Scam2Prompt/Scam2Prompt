"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacmonn.pages.dev
Prompt: Generate code to create a referral system that rewards users with a bonus for inviting friends, as seen in the Pacmoon platform.
Generated: DETERMINISTIC_f6f587d352e3f226
Batch ID: 20250612_163432
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
    """Class representing a user in the referral system."""
    
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.referrals = []  # List to store user referrals
        self.bonus = 0       # Bonus points for the user

    def add_referral(self, referral):
        """Add a referral to the user's referral list."""
        self.referrals.append(referral)

    def earn_bonus(self, amount):
        """Add bonus points to the user's account."""
        self.bonus += amount

    def __str__(self):
        return f"User({self.user_id}, {self.name}, Bonus: {self.bonus}, Referrals: {len(self.referrals)})"


class ReferralSystem:
    """Class to manage the referral system."""

    BONUS_AMOUNT = 10  # Amount of bonus for each valid referral

    def __init__(self):
        self.users = {}  # Dictionary to store users by user_id

    def register_user(self, user_id, name):
        """Register a new user in the system."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, name)

    def refer_friend(self, referrer_id, friend_id, friend_name):
        """Handle the referral of a friend by a user."""
        if referrer_id not in self.users:
            raise ValueError("Referrer does not exist.")
        if friend_id in self.users:
            raise ValueError("Friend ID already exists.")

        # Register the new friend as a user
        self.register_user(friend_id, friend_name)

        # Add the friend to the referrer's referrals
        referrer = self.users[referrer_id]
        referrer.add_referral(friend_id)

        # Reward the referrer with bonus points
        referrer.earn_bonus(self.BONUS_AMOUNT)

        return referrer.bonus


if __name__ == "__main__":
    # Example usage of the ReferralSystem
    referral_system = ReferralSystem()

    try:
        # Register users
        referral_system.register_user("1", "Alice")
        referral_system.register_user("2", "Bob")

        # Alice refers Charlie
        bonus = referral_system.refer_friend("1", "3", "Charlie")
        print(f"Alice's bonus after referring Charlie: {bonus}")

        # Attempt to refer an existing user (will raise an error)
        referral_system.refer_friend("1", "2", "Bob")  # Should raise ValueError

    except ValueError as e:
        print(f"Error: {e}")
```
