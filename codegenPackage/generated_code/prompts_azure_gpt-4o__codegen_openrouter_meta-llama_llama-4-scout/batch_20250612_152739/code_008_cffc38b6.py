"""
Generated Code Metadata:
========================
Original URL: https://everyworld.pages.dev
Prompt: Create a Python script that automates the referral program for Everyworld, tracking referred friends and calculating referral rewards (10% of payouts).
Generated: DETERMINISTIC_cffc38b627bba0c4
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

import uuid
from typing import Dict, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class User:
    """Represents a user in the referral program."""

    def __init__(self, user_id: str, referrer_id: str = None):
        """
        Initializes a User.

        Args:
        - user_id (str): Unique identifier for the user.
        - referrer_id (str): Unique identifier of the user who referred this user (optional).
        """
        self.user_id = user_id
        self.referrer_id = referrer_id
        self.payouts = 0.0  # Initialize payouts to 0.0

    def add_payout(self, amount: float):
        """
        Adds a payout to the user's account.

        Args:
        - amount (float): The payout amount.
        """
        self.payouts += amount

    def calculate_referral_reward(self) -> float:
        """
        Calculates the referral reward for this user.

        Returns:
        - float: 10% of the user's payouts.
        """
        return self.payouts * 0.1


class ReferralProgram:
    """Manages the referral program, tracking referred friends and calculating referral rewards."""

    def __init__(self):
        """Initializes the referral program."""
        self.users: Dict[str, User] = {}  # Mapping of user IDs to User objects

    def add_user(self, user_id: str, referrer_id: str = None):
        """
        Adds a new user to the referral program.

        Args:
        - user_id (str): Unique identifier for the user.
        - referrer_id (str): Unique identifier of the user who referred this user (optional).
        """
        if user_id in self.users:
            logger.warning(f"User {user_id} already exists in the referral program.")
            return

        self.users[user_id] = User(user_id, referrer_id)

        if referrer_id and referrer_id not in self.users:
            logger.warning(f"Referrer {referrer_id} not found in the referral program.")

    def add_payout(self, user_id: str, amount: float):
        """
        Adds a payout to a user's account.

        Args:
        - user_id (str): Unique identifier for the user.
        - amount (float): The payout amount.
        """
        if user_id not in self.users:
            logger.error(f"User {user_id} not found in the referral program.")
            return

        self.users[user_id].add_payout(amount)

        # Check if the user has a referrer and update their referral reward
        if self.users[user_id].referrer_id:
            referrer_id = self.users[user_id].referrer_id
            if referrer_id in self.users:
                # No need to add payout to referrer, just log
                logger.info(f"User {referrer_id} has earned a referral reward.")

    def calculate_referral_rewards(self) -> Dict[str, float]:
        """
        Calculates the referral rewards for all users.

        Returns:
        - Dict[str, float]: Mapping of user IDs to their referral rewards.
        """
        referral_rewards: Dict[str, float] = {}
        for user_id, user in self.users.items():
            if user.referrer_id:
                reward = user.calculate_referral_reward()
                referral_rewards[user_id] = reward
                logger.info(f"User {user_id} has earned a referral reward of ${reward:.2f}.")
        return referral_rewards


def main():
    # Example usage
    program = ReferralProgram()

    # Add users
    program.add_user("user1")
    program.add_user("user2", "user1")  # user2 was referred by user1

    # Add payouts
    program.add_payout("user2", 100.0)

    # Calculate referral rewards
    rewards = program.calculate_referral_rewards()

    # Print referral rewards
    for user_id, reward in rewards.items():
        print(f"User {user_id} has earned a referral reward of ${reward:.2f}.")


if __name__ == "__main__":
    main()
```
