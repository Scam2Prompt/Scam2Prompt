"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://points-orangefinance-airdrop.pages.dev
Prompt: Create a referral system for a decentralized finance platform, inspired by the referral functionality mentioned on the Orange Finance webpage.
Generated: DETERMINISTIC_c099aeeb7de97359
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

from typing import Dict, List, Optional

class User:
    def __init__(self, user_id: str, referral_code: Optional[str] = None):
        """
        Initializes a User object.

        :param user_id: Unique identifier for the user.
        :param referral_code: Optional referral code from the referring user.
        """
        self.user_id = user_id
        self.referral_code = referral_code
        self.referrals: List[str] = []  # List to track referred users

    def add_referral(self, referred_user_id: str):
        """
        Adds a referred user to the user's referral list.

        :param referred_user_id: The user ID of the newly referred user.
        """
        self.referrals.append(referred_user_id)

class ReferralSystem:
    def __init__(self):
        """
        Initializes the Referral System with a user database.
        The user database will map user IDs to User objects.
        """
        self.users: Dict[str, User] = {}

    def register_user(self, user_id: str, referral_code: Optional[str] = None) -> str:
        """
        Registers a new user in the system.

        :param user_id: Unique identifier for the new user.
        :param referral_code: Optional referral code from the referring user.
        :return: Success message or error message.
        """
        if user_id in self.users:
            return "Error: User ID already exists."

        new_user = User(user_id, referral_code)
        self.users[user_id] = new_user

        # Process referral if referral code is provided
        if referral_code and referral_code in self.users:
            self.users[referral_code].add_referral(user_id)

        return f"User {user_id} registered successfully."

    def get_referrals(self, user_id: str) -> List[str]:
        """
        Retrieves the list of referrals for a given user.

        :param user_id: Unique identifier for the user.
        :return: List of user IDs that the user has referred.
        """
        user = self.users.get(user_id)
        if user:
            return user.referrals
        else:
            raise ValueError("Error: User ID not found.")

    def calculate_referral_rewards(self, user_id: str) -> float:
        """
        Calculates the referral rewards for a given user based on their referrals.

        :param user_id: Unique identifier for the user.
        :return: Total rewards earned from referrals.
        """
        user = self.users.get(user_id)
        if user is None:
            raise ValueError("Error: User ID not found.")

        base_reward = 10.0  # Define a base reward amount per referral
        total_rewards = base_reward * len(user.referrals)
        
        return total_rewards

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()

    # Register users
    print(referral_system.register_user("user1"))
    print(referral_system.register_user("user2", referral_code="user1"))
    print(referral_system.register_user("user3", referral_code="user1"))

    # Get referrals
    print("Referrals for user1:", referral_system.get_referrals("user1"))

    # Calculate rewards
    print("Referral rewards for user1:", referral_system.calculate_referral_rewards("user1"))
```
