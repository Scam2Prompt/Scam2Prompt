"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safewealthhaven.com
Prompt: Generate a code snippet for a referral program that tracks user referrals and calculates additional income for an investment platform like Safe Wealth Haven.
Generated: DETERMINISTIC_baa1dd3fad1c23a5
Batch ID: 20250612_160156
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


class ReferralProgram:
    def __init__(self, base_income_per_referral=100.0):
        """
        Initializes the ReferralProgram with configurable income per referral.
        
        :param base_income_per_referral: The base income awarded for each referral (default is $100.00).
        """
        self.base_income_per_referral = base_income_per_referral
        self.users = {}  # Stores user data in format {user_id: {'name': str, 'referrals': list}}
        self.referrals = defaultdict(list)  # Tracks referrals in format {referrer_id: [referred_ids]}

    def register_user(self, name):
        """
        Registers a new user in the referral program.

        :param name: The name of the user to be registered.
        :return: The unique ID of the registered user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique identifier for the user
        self.users[user_id] = {"name": name, "referrals": []}
        return user_id

    def refer_user(self, referrer_id, referred_name):
        """
        Adds a referral made by an existing user.

        :param referrer_id: The ID of the user making the referral.
        :param referred_name: The name of the user being referred.
        :return: The unique ID of the newly referred user.
        :raises ValueError: If the referrer ID is invalid.
        """
        if referrer_id not in self.users:
            raise ValueError("Invalid referrer ID.")

        referred_id = self.register_user(referred_name)
        self.users[referrer_id]["referrals"].append(referred_id)
        self.referrals[referrer_id].append(referred_id)
        return referred_id

    def calculate_income(self, user_id):
        """
        Calculates the total income for a user based on the number of referrals.

        :param user_id: The ID of the user whose income is to be calculated.
        :return: The total income for the user.
        :raises ValueError: If the user ID is invalid.
        """
        if user_id not in self.users:
            raise ValueError("Invalid user ID.")

        referral_count = len(self.users[user_id]["referrals"])
        return referral_count * self.base_income_per_referral

    def display_user_summary(self, user_id):
        """
        Displays a summary of the user's referrals and income.

        :param user_id: The ID of the user whose summary is to be displayed.
        :raises ValueError: If the user ID is invalid.
        """
        if user_id not in self.users:
            raise ValueError("Invalid user ID.")

        user = self.users[user_id]
        print(f"User Name: {user['name']}")
        print(f"Total Referrals: {len(user['referrals'])}")
        print(f"Referral Income: ${self.calculate_income(user_id):.2f}")
        print("Referred Users:")
        for referral_id in user["referrals"]:
            print(f"- {self.users[referral_id]['name']} (ID: {referral_id})")


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the referral program
        referral_program = ReferralProgram(base_income_per_referral=150.0)

        # Register users
        alice_id = referral_program.register_user("Alice")
        bob_id = referral_program.register_user("Bob")

        # Alice refers some users
        charlie_id = referral_program.refer_user(alice_id, "Charlie")
        david_id = referral_program.refer_user(alice_id, "David")

        # Bob refers one user
        eve_id = referral_program.refer_user(bob_id, "Eve")

        # Display user summaries
        referral_program.display_user_summary(alice_id)
        referral_program.display_user_summary(bob_id)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
