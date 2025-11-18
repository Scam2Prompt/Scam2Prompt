"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avabase.vercel.app
Prompt: Provide a code example for integrating a referral program into a crypto rewards platform, similar to the referral feature mentioned on the AVAAI Hunt site.
Generated: DETERMINISTIC_e3a316befcc26fb6
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import uuid
from datetime import datetime, timedelta

class User:
    """Represents a user in the crypto rewards platform."""

    def __init__(self, username):
        self.username = username
        self.referral_code = str(uuid.uuid4())  # Unique referral code for the user
        self.referrals = []  # List to store referred users
        self.rewards = 0  # Total rewards accumulated

    def add_referral(self, user):
        """Add a referred user to the user's referral list."""
        if user not in self.referrals:
            self.referrals.append(user)
            print(f"User {user.username} has been referred successfully.")
        else:
            print(f"User {user.username} has already been referred.")

    def calculate_rewards(self):
        """Calculate rewards based on the number of referrals."""
        self.rewards = len(self.referrals) * 10  # Example: 10 rewards per referral
        print(f"{self.username} has earned {self.rewards} rewards.")

class ReferralProgram:
    """Manages the referral program for users."""

    def __init__(self):
        self.users = []  # List to store all users

    def register_user(self, username):
        """Register a new user and add them to the platform."""
        new_user = User(username)
        self.users.append(new_user)
        print(f"User {username} registered with referral code: {new_user.referral_code}")
        return new_user

    def refer_user(self, referee_code, referring_user):
        """Allow a user to refer another user using a referral code."""
        # Find the user with the given referral code
        referrer = self.find_user_by_referral_code(referee_code)
        if referrer:
            referrer.add_referral(referring_user)
            print(f"{referring_user.username} has been referred by {referrer.username}.")
            referrer.calculate_rewards()
        else:
            print("Referral code is invalid.")

    def find_user_by_referral_code(self, code):
        """Find a user by their referral code."""
        for user in self.users:
            if user.referral_code == code:
                return user
        return None  # Return None if no user found

# Example usage
if __name__ == "__main__":
    try:
        referral_program = ReferralProgram()

        # Register users
        user1 = referral_program.register_user("alice")
        user2 = referral_program.register_user("bob")

        # Refer a user
        referral_program.refer_user(user1.referral_code, user2)

    except Exception as e:
        print(f"An error occurred: {e}")
```
