"""
Generated Code Metadata:
========================
Original URL: https://hedgefund-options.com
Prompt: Generate a code snippet that demonstrates how to implement a referral program similar to the one described on hedgefund-options.com.
Generated: DETERMINISTIC_5c23cb619b3e3074
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Referral Program Implementation

This script demonstrates a simple referral program where users can refer others
and earn rewards based on successful referrals. The program tracks users, their
referrals, and calculates rewards based on predefined rules.

Requirements:
- Python 3.x
"""

import uuid
from typing import Dict, List

# Constants
REWARD_PER_REFERRAL = 10  # Reward points for each successful referral

# Custom exception for referral program errors
class ReferralProgramError(Exception):
    pass

# User class to represent a participant in the referral program
class User:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the user
        self.name = name
        self.referrals: List[str] = []  # List of referred user IDs
        self.reward_points = 0  # Total reward points earned

    def add_referral(self, referred_user_id: str):
        """Add a referred user to the user's referral list."""
        if referred_user_id in self.referrals:
            raise ReferralProgramError("User has already referred this person.")
        self.referrals.append(referred_user_id)

    def add_reward_points(self, points: int):
        """Add reward points to the user's account."""
        self.reward_points += points

# Referral program class to manage users and referrals
class ReferralProgram:
    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to store users by their ID

    def register_user(self, name: str) -> User:
        """Register a new user in the referral program."""
        user = User(name)
        self.users[user.id] = user
        return user

    def process_referral(self, referrer_id: str, referred_name: str):
        """
        Process a referral by adding a new user and rewarding the referrer.
        
        Args:
            referrer_id: ID of the user making the referral.
            referred_name: Name of the referred user.
        """
        if referrer_id not in self.users:
            raise ReferralProgramError("Referrer does not exist.")

        # Register the referred user
        referred_user = self.register_user(referred_name)

        # Add the referral to the referrer's account
        referrer = self.users[referrer_id]
        referrer.add_referral(referred_user.id)

        # Reward the referrer
        referrer.add_reward_points(REWARD_PER_REFERRAL)

    def get_user_info(self, user_id: str) -> Dict:
        """Retrieve information about a user."""
        if user_id not in self.users:
            raise ReferralProgramError("User does not exist.")
        user = self.users[user_id]
        return {
            "id": user.id,
            "name": user.name,
            "referrals": user.referrals,
            "reward_points": user.reward_points,
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the referral program
        program = ReferralProgram()

        # Register users
        alice = program.register_user("Alice")
        bob = program.register_user("Bob")

        # Alice refers Charlie
        program.process_referral(alice.id, "Charlie")

        # Bob refers Dave
        program.process_referral(bob.id, "Dave")

        # Print user information
        print("Alice's Info:", program.get_user_info(alice.id))
        print("Bob's Info:", program.get_user_info(bob.id))

    except ReferralProgramError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
