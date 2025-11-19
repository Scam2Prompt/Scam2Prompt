"""
Generated Code Metadata:
========================
Original URL: https://ff-exchange.in
Prompt: Design a system to track and reward referrals on a crypto trading platform, similar to FF.IO's referral program, with discounted fees and ongoing rewards.
Generated: DETERMINISTIC_f76358816ef56bde
Batch ID: 20250622_211453
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
    def __init__(self, referral_fee_discount: float, ongoing_reward: float):
        """
        Initialize the referral program.

        Args:
        - referral_fee_discount (float): The discount on fees for referred users.
        - ongoing_reward (float): The ongoing reward for referrers.
        """
        self.referral_fee_discount = referral_fee_discount
        self.ongoing_reward = ongoing_reward
        self.referrals: Dict[str, Referral] = {}

    def create_referral(self, referrer_id: str, referred_user_id: str):
        """
        Create a new referral.

        Args:
        - referrer_id (str): The ID of the referrer.
        - referred_user_id (str): The ID of the referred user.

        Returns:
        - referral (Referral): The created referral.
        """
        referral = Referral(referrer_id, referred_user_id)
        self.referrals[referred_user_id] = referral
        return referral

    def get_referral(self, referred_user_id: str) -> Referral:
        """
        Get a referral by referred user ID.

        Args:
        - referred_user_id (str): The ID of the referred user.

        Returns:
        - referral (Referral): The referral for the given referred user ID.
        """
        return self.referrals.get(referred_user_id)

    def calculate_referrer_reward(self, referred_user_id: str, fee: float) -> float:
        """
        Calculate the referrer's reward for a given fee.

        Args:
        - referred_user_id (str): The ID of the referred user.
        - fee (float): The fee to calculate the reward for.

        Returns:
        - reward (float): The referrer's reward.
        """
        referral = self.get_referral(referred_user_id)
        if referral:
            return fee * self.ongoing_reward
        return 0


class Referral:
    def __init__(self, referrer_id: str, referred_user_id: str):
        """
        Initialize a referral.

        Args:
        - referrer_id (str): The ID of the referrer.
        - referred_user_id (str): The ID of the referred user.
        """
        self.referrer_id = referrer_id
        self.referred_user_id = referred_user_id
        self.created_at = datetime.now()
        self.fees_paid = 0

    def apply_fee_discount(self, fee: float, discount: float) -> float:
        """
        Apply the fee discount to a given fee.

        Args:
        - fee (float): The original fee.
        - discount (float): The discount to apply.

        Returns:
        - discounted_fee (float): The fee with the discount applied.
        """
        return fee * (1 - discount)

    def record_fee(self, fee: float, discount: float):
        """
        Record a fee paid by the referred user.

        Args:
        - fee (float): The original fee.
        - discount (float): The discount applied.
        """
        discounted_fee = self.apply_fee_discount(fee, discount)
        self.fees_paid += discounted_fee


class TradingPlatform:
    def __init__(self, referral_program: ReferralProgram):
        """
        Initialize the trading platform.

        Args:
        - referral_program (ReferralProgram): The referral program.
        """
        self.referral_program = referral_program
        self.users: Dict[str, User] = {}

    def create_user(self, user_id: str, referrer_id: str = None):
        """
        Create a new user.

        Args:
        - user_id (str): The ID of the user.
        - referrer_id (str): The ID of the referrer (optional).
        """
        user = User(user_id)
        self.users[user_id] = user

        if referrer_id:
            referral = self.referral_program.create_referral(referrer_id, user_id)
            user.referral = referral

    def record_fee(self, user_id: str, fee: float):
        """
        Record a fee paid by a user.

        Args:
        - user_id (str): The ID of the user.
        - fee (float): The fee paid.
        """
        user = self.users.get(user_id)
        if user and user.referral:
            referral = user.referral
            discount = self.referral_program.referral_fee_discount
            referral.record_fee(fee, discount)
            referrer_reward = self.referral_program.calculate_referrer_reward(user_id, fee)
            print(f"Referrer {referral.referrer_id} earned a reward of {referrer_reward}")


class User:
    def __init__(self, user_id: str):
        """
        Initialize a user.

        Args:
        - user_id (str): The ID of the user.
        """
        self.user_id = user_id
        self.referral: Referral = None


def main():
    referral_program = ReferralProgram(referral_fee_discount=0.1, ongoing_reward=0.05)
    platform = TradingPlatform(referral_program)

    platform.create_user("user1")
    platform.create_user("user2", "user1")

    platform.record_fee("user2", 100)

if __name__ == "__main__":
    main()
```
