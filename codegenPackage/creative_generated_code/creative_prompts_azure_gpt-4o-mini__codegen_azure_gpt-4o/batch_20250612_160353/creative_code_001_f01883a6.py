"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://247signalfxtrade.com
Prompt: How can I implement a referral program similar to the one offered by 247signalfxtrade, allowing users to earn income by referring others?
Generated: DETERMINISTIC_f01883a6cc26cf52
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Referral Program Implementation
# Language: Python
# Author: Expert Developer
# Description: This script implements a referral program where users can earn income by referring others.

import uuid
from typing import Dict, List


class User:
    """
    Represents a user in the referral system.
    """
    def __init__(self, name: str):
        self.user_id = str(uuid.uuid4())  # Generate a unique ID for the user
        self.name = name  # User's name
        self.referral_code = self.user_id[:8]  # Generate a referral code based on user ID
        self.referred_users = []  # List to store referred user IDs
        self.earnings = 0.0  # Earnings from referrals

    def add_referred_user(self, referred_user_id: str):
        """
        Adds a referred user ID to the list of referred users.
        """
        self.referred_users.append(referred_user_id)

    def add_earning(self, amount: float):
        """
        Adds earnings to the user's account.
        """
        self.earnings += amount


class ReferralProgram:
    """
    Referral program to manage users and their referrals.
    """
    def __init__(self, referral_bonus: float):
        self.users: Dict[str, User] = {}  # Dictionary to store users by user ID
        self.referral_bonus = referral_bonus  # Bonus amount for each successful referral

    def register_user(self, name: str) -> User:
        """
        Registers a new user in the referral program.
        """
        user = User(name)
        self.users[user.user_id] = user
        return user

    def process_referral(self, referee_name: str, referral_code: str) -> None:
        """
        Processes a referral by linking the referee to the referrer.
        """
        # Find the user associated with the referral code
        referrer = next((user for user in self.users.values() if user.referral_code == referral_code), None)
        if not referrer:
            raise ValueError("Invalid referral code.")

        # Register the referee as a new user
        referee = self.register_user(referee_name)
        referrer.add_referred_user(referee.user_id)
        referrer.add_earning(self.referral_bonus)

    def get_user_info(self, user_id: str) -> Dict:
        """
        Fetches information about a user.
        """
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User not found.")
        return {
            "Name": user.name,
            "Referral Code": user.referral_code,
            "Referred Users": user.referred_users,
            "Earnings": user.earnings,
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the referral program with a referral bonus of $10
        referral_program = ReferralProgram(referral_bonus=10.0)

        # Register a user as the referrer
        referrer = referral_program.register_user("John Doe")
        print(f"Referrer registered. Referral Code: {referrer.referral_code}")

        # Referrer shares their referral code with others
        referral_program.process_referral("Jane Smith", referrer.referral_code)
        referral_program.process_referral("Alice Brown", referrer.referral_code)

        # Fetch referrer's information
        referrer_info = referral_program.get_user_info(referrer.user_id)
        print(f"Referrer Info: {referrer_info}")

    except Exception as e:
        print(f"Error: {e}")
```
