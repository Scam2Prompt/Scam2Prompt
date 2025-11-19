"""
Generated Code Metadata:
========================
Original URL: https://rentsy.pro
Prompt: Generate code to implement a referral program for a subscription-based platform, including tracking and rewards, inspired by Rentsy.
Generated: DETERMINISTIC_1542b2d2ef9c5b76
Batch ID: 20250612_145815
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

from datetime import datetime, timedelta
from typing import Dict

class ReferralProgram:
    def __init__(self, referral_reward: int, expiration_days: int):
        """
        Initialize the referral program.

        Args:
        - referral_reward (int): The reward for a successful referral.
        - expiration_days (int): The number of days the referral link is valid.
        """
        self.referral_reward = referral_reward
        self.expiration_days = expiration_days
        self.referrals: Dict[str, Referral] = {}

    def generate_referral_link(self, user_id: str) -> str:
        """
        Generate a unique referral link for a user.

        Args:
        - user_id (str): The ID of the user.

        Returns:
        - str: A unique referral link.
        """
        referral = Referral(user_id, self.referral_reward, self.expiration_days)
        self.referrals[referral.link] = referral
        return referral.link

    def track_referral(self, referral_link: str, new_user_id: str) -> bool:
        """
        Track a referral and reward the referrer if the referral is successful.

        Args:
        - referral_link (str): The referral link used by the new user.
        - new_user_id (str): The ID of the new user.

        Returns:
        - bool: True if the referral is successful, False otherwise.
        """
        if referral_link in self.referrals:
            referral = self.referrals[referral_link]
            if referral.is_valid():
                referral.referral_count += 1
                # Reward the referrer
                self.reward_referrer(referral.user_id)
                return True
        return False

    def reward_referrer(self, user_id: str):
        """
        Reward the referrer with the referral reward.

        Args:
        - user_id (str): The ID of the referrer.
        """
        # Implement the logic to reward the referrer
        print(f"Rewarding user {user_id} with {self.referral_reward}")


class Referral:
    def __init__(self, user_id: str, referral_reward: int, expiration_days: int):
        """
        Initialize a referral.

        Args:
        - user_id (str): The ID of the user who generated the referral link.
        - referral_reward (int): The reward for a successful referral.
        - expiration_days (int): The number of days the referral link is valid.
        """
        self.user_id = user_id
        self.referral_reward = referral_reward
        self.expiration_days = expiration_days
        self.link = self.generate_link()
        self.creation_date = datetime.now()
        self.referral_count = 0

    def generate_link(self) -> str:
        """
        Generate a unique referral link.

        Returns:
        - str: A unique referral link.
        """
        import uuid
        return str(uuid.uuid4())

    def is_valid(self) -> bool:
        """
        Check if the referral link is still valid.

        Returns:
        - bool: True if the referral link is valid, False otherwise.
        """
        expiration_date = self.creation_date + timedelta(days=self.expiration_days)
        return datetime.now() < expiration_date


def main():
    referral_program = ReferralProgram(referral_reward=10, expiration_days=30)
    user_id = "user123"
    referral_link = referral_program.generate_referral_link(user_id)
    print(f"Referral link: {referral_link}")
    new_user_id = "new_user456"
    if referral_program.track_referral(referral_link, new_user_id):
        print("Referral tracked successfully")
    else:
        print("Invalid referral link")


if __name__ == "__main__":
    main()
```
