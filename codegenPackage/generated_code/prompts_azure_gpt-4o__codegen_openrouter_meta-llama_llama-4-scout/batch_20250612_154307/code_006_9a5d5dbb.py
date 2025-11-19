"""
Generated Code Metadata:
========================
Original URL: https://coinrush.bet
Prompt: Develop a referral program system in Python for a crypto casino, where users earn rewards for inviting friends, as described on Coin Rush.
Generated: DETERMINISTIC_9a5d5dbb2fba324a
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

from typing import Dict
import hashlib
import logging
import uuid

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ReferralProgram:
    def __init__(self):
        # In-memory storage for demonstration purposes.
        # Consider using a database in production.
        self.users: Dict[str, Dict] = {}
        self.referrals: Dict[str, int] = {}

    def create_user(self, user_id: str, referrer_id: str = None) -> str:
        """
        Create a new user with an optional referrer.

        Args:
        - user_id (str): Unique identifier for the user.
        - referrer_id (str): Unique identifier for the referrer.

        Returns:
        - user_id (str): Unique identifier for the created user.
        """
        if user_id in self.users:
            logger.error(f"User {user_id} already exists.")
            raise ValueError("User already exists.")

        self.users[user_id] = {
            "referrer_id": referrer_id,
            "referral_code": self.generate_referral_code(user_id),
            "reward_balance": 0,
        }

        if referrer_id:
            self.referrals[referrer_id] = self.referrals.get(referrer_id, 0) + 1
            logger.info(f"User {user_id} referred by {referrer_id}.")

        logger.info(f"User {user_id} created.")
        return user_id

    def generate_referral_code(self, user_id: str) -> str:
        """
        Generate a unique referral code for a user.

        Args:
        - user_id (str): Unique identifier for the user.

        Returns:
        - referral_code (str): Unique referral code.
        """
        return hashlib.sha256((user_id + str(uuid.uuid4())).encode()).hexdigest()[:8]

    def get_referral_code(self, user_id: str) -> str:
        """
        Get the referral code for a user.

        Args:
        - user_id (str): Unique identifier for the user.

        Returns:
        - referral_code (str): Referral code for the user.
        """
        if user_id not in self.users:
            logger.error(f"User {user_id} does not exist.")
            raise ValueError("User does not exist.")

        return self.users[user_id]["referral_code"]

    def get_reward_balance(self, user_id: str) -> int:
        """
        Get the reward balance for a user.

        Args:
        - user_id (str): Unique identifier for the user.

        Returns:
        - reward_balance (int): Reward balance for the user.
        """
        if user_id not in self.users:
            logger.error(f"User {user_id} does not exist.")
            raise ValueError("User does not exist.")

        return self.users[user_id]["reward_balance"]

    def add_reward(self, user_id: str, amount: int) -> None:
        """
        Add rewards to a user's balance.

        Args:
        - user_id (str): Unique identifier for the user.
        - amount (int): Amount of rewards to add.
        """
        if user_id not in self.users:
            logger.error(f"User {user_id} does not exist.")
            raise ValueError("User does not exist.")

        self.users[user_id]["reward_balance"] += amount
        logger.info(f"Added {amount} rewards to user {user_id}.")

def main():
    referral_program = ReferralProgram()

    # Create users
    user1_id = referral_program.create_user("user1")
    user2_id = referral_program.create_user("user2", "user1")

    # Get referral code
    referral_code = referral_program.get_referral_code("user1")
    logger.info(f"Referral code for user1: {referral_code}")

    # Add rewards
    referral_program.add_reward("user1", 100)

    # Get reward balance
    reward_balance = referral_program.get_reward_balance("user1")
    logger.info(f"Reward balance for user1: {reward_balance}")

if __name__ == "__main__":
    main()
```
