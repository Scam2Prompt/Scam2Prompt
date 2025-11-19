"""
Generated Code Metadata:
========================
Original URL: https://vatanplatform.bet
Prompt: Write code to implement a referral program for an online casino platform, including tracking referrals and calculating rewards, inspired by BaxBet's collaboration programs.
Generated: DETERMINISTIC_ad5a55ac3bd08b21
Batch ID: 20250612_145919
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
from typing import Dict, List

class ReferralProgram:
    def __init__(self):
        # Initialize referral program data store
        self.referrals: Dict[str, Referral] = {}
        self.rewards: Dict[str, float] = {
            'signup': 10.0,  # $10 for signing up
            'deposit': 50.0,  # $50 for making a deposit
            'loss': 0.05,  # 5% refund on losses
        }

    def create_referral(self, referrer_id: str, referral_id: str) -> None:
        """
        Create a new referral link between two users.

        Args:
        - referrer_id (str): The ID of the user referring others
        - referral_id (str): The ID of the new user
        """
        if referral_id in self.referrals:
            raise ValueError("Referral already exists")

        self.referrals[referral_id] = Referral(referrer_id, referral_id)

    def track_signup(self, referral_id: str) -> None:
        """
        Track a new signup and award the referrer.

        Args:
        - referral_id (str): The ID of the new user
        """
        if referral_id not in self.referrals:
            raise ValueError("Referral not found")

        referral = self.referrals[referral_id]
        referral.signup_date = datetime.now()
        referral.signup_rewarded = True

        self.award_referrer(referral, 'signup')

    def track_deposit(self, referral_id: str, amount: float) -> None:
        """
        Track a deposit made by a referred user and award the referrer.

        Args:
        - referral_id (str): The ID of the user who made the deposit
        - amount (float): The amount deposited
        """
        if referral_id not in self.referrals:
            raise ValueError("Referral not found")

        referral = self.referrals[referral_id]
        referral.deposit_date = datetime.now()
        referral.deposit_amount = amount
        referral.deposit_rewarded = True

        self.award_referrer(referral, 'deposit')

    def track_loss(self, referral_id: str, amount: float) -> None:
        """
        Track losses made by a referred user and award the referrer.

        Args:
        - referral_id (str): The ID of the user who incurred losses
        - amount (float): The amount lost
        """
        if referral_id not in self.referrals:
            raise ValueError("Referral not found")

        referral = self.referrals[referral_id]
        referral.loss_amount += amount

        self.award_referrer(referral, 'loss', amount)

    def award_referrer(self, referral: 'Referral', reward_type: str, amount: float = 0.0) -> None:
        """
        Award the referrer based on the referral's actions.

        Args:
        - referral (Referral): The referral object
        - reward_type (str): The type of reward to award
        - amount (float): The amount related to the reward (e.g., loss amount)
        """
        referrer_id = referral.referrer_id
        reward_amount = self.rewards[reward_type]

        if reward_type == 'loss':
            reward_amount *= amount

        # Simulate awarding the referrer (e.g., update their balance)
        print(f"Awarding ${reward_amount:.2f} to referrer {referrer_id} for {reward_type}")


class Referral:
    def __init__(self, referrer_id: str, referral_id: str):
        self.referrer_id = referrer_id
        self.referral_id = referral_id
        self.signup_date: datetime = None
        self.signup_rewarded = False
        self.deposit_date: datetime = None
        self.deposit_amount: float = 0.0
        self.deposit_rewarded = False
        self.loss_amount: float = 0.0


def main():
    referral_program = ReferralProgram()

    # Create referrals
    referral_program.create_referral('referrer1', 'newuser1')
    referral_program.create_referral('referrer2', 'newuser2')

    # Track signups
    referral_program.track_signup('newuser1')
    referral_program.track_signup('newuser2')

    # Track deposits
    referral_program.track_deposit('newuser1', 100.0)
    referral_program.track_deposit('newuser2', 50.0)

    # Track losses
    referral_program.track_loss('newuser1', 20.0)
    referral_program.track_loss('newuser2', 10.0)


if __name__ == '__main__':
    main()
```
