"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jups.io
Prompt: How can I implement a referral system for a crypto casino website, inspired by the promotions mentioned on Jups.io?
Generated: DETERMINISTIC_2377f6c3e70868bf
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

import uuid
from datetime import datetime

class ReferralSystem:
    """
    A class to manage the referral system for a crypto casino website.
    """

    def __init__(self):
        # Dictionary to store user data. In production, replace with a proper database.
        self.users = {}
        self.referral_codes = {}
        self.referrals = {}

    def generate_referral_code(self, user_id):
        """
        Generate a unique referral code for a given user.

        :param user_id: ID of the user for whom the referral code will be generated.
        :return: Generated referral code (string).
        """
        if user_id in self.referral_codes:
            return self.referral_codes[user_id]

        referral_code = str(uuid.uuid4())[:8]  # Generate an 8-character unique code
        self.referral_codes[user_id] = referral_code
        return referral_code

    def register_user(self, username, referral_code=None):
        """
        Register a new user. Optionally, attach them to a referrer via the referral code.

        :param username: Username for the new user.
        :param referral_code: Referral code provided during registration (optional).
        :return: User ID of the newly registered user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        if username in self.users:
            raise ValueError(f"Username '{username}' is already taken.")

        self.users[user_id] = {
            "username": username,
            "referral_code": self.generate_referral_code(user_id),
            "registered_at": datetime.utcnow(),
            "referrer_id": None,
            "referee_count": 0,
        }

        if referral_code:
            # Associate the referrer if a valid referral code is provided
            referrer_id = self.get_user_by_referral_code(referral_code)
            if not referrer_id:
                raise ValueError(f"Invalid referral code: {referral_code}")
            self.users[user_id]["referrer_id"] = referrer_id
            self.users[referrer_id]["referee_count"] += 1

            # Log the referral relation
            self.referrals.setdefault(referrer_id, []).append(user_id)

        return user_id

    def get_user_by_referral_code(self, referral_code):
        """
        Retrieve the user ID associated with a given referral code.

        :param referral_code: Referral code to look up.
        :return: User ID of the referrer (or None if not found).
        """
        for user_id, user_code in self.referral_codes.items():
            if user_code == referral_code:
                return user_id
        return None

    def get_referral_summary(self, user_id):
        """
        Get a summary of a user's referral activity.

        :param user_id: ID of the user to retrieve the referral summary for.
        :return: Dictionary containing the referral summary.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID '{user_id}' does not exist.")

        user_data = self.users[user_id]
        return {
            "username": user_data["username"],
            "referral_code": user_data["referral_code"],
            "referee_count": user_data["referee_count"],
            "referees": [
                self.users[referee_id]["username"]
                for referee_id in self.referrals.get(user_id, [])
            ],
        }

# Example usage
if __name__ == "__main__":
    # Instantiate the referral system
    referral_system = ReferralSystem()

    # Register users
    user1 = referral_system.register_user("Alice")
    user2 = referral_system.register_user("Bob", referral_code=referral_system.users[user1]["referral_code"])
    user3 = referral_system.register_user("Charlie", referral_code=referral_system.users[user1]["referral_code"])

    # Get referral summary for Alice
    alice_summary = referral_system.get_referral_summary(user1)
    print("Alice's Referral Summary:")
    print(alice_summary)

    # Get referral summary for Bob
    bob_summary = referral_system.get_referral_summary(user2)
    print("\nBob's Referral Summary:")
    print(bob_summary)
```

This Python script implements a referral system for a crypto casino website. To adapt this code for production, it would need integration with a database for data persistence and additional security measures such as input validation and rate-limiting to prevent abuse.
