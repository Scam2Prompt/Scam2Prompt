"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://247signalfxtrade.com
Prompt: Generate code for implementing a referral program, similar to the one offered by 247signalfxtrade, where users earn income by referring others.
Generated: DETERMINISTIC_aef4aa2788f4d383
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import Dict, List

# Data structure to store user information.
# In a production environment, this would likely interface with a database.
class User:
    def __init__(self, username: str):
        self.username = username
        self.referral_code = str(uuid.uuid4())  # Generate a unique referral code.
        self.referred_users: List[User] = []  # List of users referred by this user.
        self.earnings = 0.0  # Total earnings from referrals.

    def add_referred_user(self, user):
        self.referred_users.append(user)

    def add_earnings(self, amount: float):
        self.earnings += amount


class ReferralProgram:
    def __init__(self, referral_bonus: float):
        """
        Initialize the referral program with a referral bonus.
        :param referral_bonus: The amount of money earned per referral.
        """
        self.users: Dict[str, User] = {}  # Store users by their referral code.
        self.referral_bonus = referral_bonus  # Set the referral bonus.

    def register_user(self, username: str) -> User:
        """
        Register a new user to the referral program.
        :param username: The username of the new user.
        :return: The newly registered User object.
        """
        if username in self.users:
            raise ValueError(f"Username '{username}' already exists.")

        new_user = User(username)
        self.users[new_user.referral_code] = new_user
        return new_user

    def refer_user(self, referrer_code: str, new_username: str) -> User:
        """
        Register a new user using a referral code.
        :param referrer_code: The referral code of the user referring the new user.
        :param new_username: The username of the new user being referred.
        :return: The newly registered User object.
        """
        if referrer_code not in self.users:
            raise ValueError("Invalid referral code.")

        if new_username in [user.username for user in self.users.values()]:
            raise ValueError(f"Username '{new_username}' already exists.")

        # Create the new user.
        new_user = User(new_username)
        self.users[new_user.referral_code] = new_user

        # Link the new user with the referrer.
        referrer = self.users[referrer_code]
        referrer.add_referred_user(new_user)
        referrer.add_earnings(self.referral_bonus)

        return new_user

    def get_user_summary(self, username: str) -> Dict:
        """
        Get a summary of a user's referral program details.
        :param username: The username of the user.
        :return: A dictionary containing the user's summary.
        """
        user = next((u for u in self.users.values() if u.username == username), None)
        if not user:
            raise ValueError(f"User '{username}' not found.")

        return {
            "username": user.username,
            "referral_code": user.referral_code,
            "referred_users": [u.username for u in user.referred_users],
            "earnings": user.earnings,
        }


# Example usage (for testing or demonstration purposes):
if __name__ == "__main__":
    try:
        # Create a referral program instance with a $10 referral bonus.
        program = ReferralProgram(referral_bonus=10.0)

        # Register two users.
        alice = program.register_user("Alice")
        print(f"Alice registered with referral code: {alice.referral_code}")

        bob = program.refer_user(alice.referral_code, "Bob")
        print(f"Bob registered using Alice's referral code: {bob.referral_code}")

        # Get and print Alice's summary.
        alice_summary = program.get_user_summary("Alice")
        print("Alice's summary:", alice_summary)

        # Get and print Bob's summary.
        bob_summary = program.get_user_summary("Bob")
        print("Bob's summary:", bob_summary)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
