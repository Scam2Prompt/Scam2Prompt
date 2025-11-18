"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ttrumpwallet.com
Prompt: Write a Python script to calculate and distribute referral rewards in a cryptocurrency system, similar to the $TRUMP Wallet promotion rules.
Generated: DETERMINISTIC_3fe1459ad313dbb5
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from decimal import Decimal, InvalidOperation

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReferralSystem:
    def __init__(self, total_rewards: Decimal, referrer_percentage: Decimal, direct_referral_percentage: Decimal):
        """
        Initializes the referral system with total rewards and distribution percentages.

        :param total_rewards: Total amount of rewards to distribute
        :param referrer_percentage: Percentage of total rewards allocated to the referrer
        :param direct_referral_percentage: Percentage allocated for direct referrals
        """
        self.total_rewards = total_rewards
        self.referrer_percentage = referrer_percentage
        self.direct_referral_percentage = direct_referral_percentage

    def calculate_rewards(self, referrer_count: int) -> dict:
        """
        Calculates the rewards for referrers and their direct referrals.

        :param referrer_count: Number of direct referrals made by the user
        :return: A dictionary containing rewards for referrer and direct referrals
        """
        if referrer_count < 0:
            logging.error("Referrer count cannot be negative")
            raise ValueError("Referrer count cannot be negative")

        # Calculate rewards for referrer
        referrer_reward = (self.total_rewards * self.referrer_percentage) / Decimal(100)

        # Calculate rewards for direct referrals
        direct_referral_reward = (self.total_rewards * self.direct_referral_percentage) / Decimal(100)
        total_direct_referral_reward = direct_referral_reward * referrer_count

        return {
            "referrer_reward": referrer_reward,
            "total_direct_referral_reward": total_direct_referral_reward
        }

def main():
    try:
        # Initialize the referral system with example values
        total_rewards = Decimal('1000.00')  # Total rewards to distribute
        referrer_percentage = Decimal('30.0')  # 30% to the referrer
        direct_referral_percentage = Decimal('10.0')  # 10% for each direct referral

        referral_system = ReferralSystem(total_rewards, referrer_percentage, direct_referral_percentage)

        # Example: Calculate rewards for a user with 5 direct referrals
        referrer_count = 5
        rewards = referral_system.calculate_rewards(referrer_count)

        # Display the calculated rewards
        logging.info(f"Referrer Reward: {rewards['referrer_reward']}, Total Direct Referral Reward: {rewards['total_direct_referral_reward']}")

    except (InvalidOperation, ValueError) as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
