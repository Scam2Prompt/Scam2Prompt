"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimunstake-prosper.pages.dev
Prompt: Generate code to calculate BTC rewards for PROS token holders based on staking participation, factoring in the unbonding period and wrapped BTC rewards as described on the Prosper platform.
Generated: DETERMINISTIC_9d5191bc0c997bec
Batch ID: 20250612_145450
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from decimal import Decimal, InvalidOperation
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StakingRewardCalculator:
    def __init__(self, total_staked: Decimal, user_staked: Decimal, 
                 btc_reward_per_staked: Decimal, unbonding_period_days: int):
        """
        Initialize the StakingRewardCalculator with necessary parameters.

        :param total_staked: Total amount of PROS tokens staked on the platform
        :param user_staked: Amount of PROS tokens staked by the user
        :param btc_reward_per_staked: BTC reward per staked PROS token
        :param unbonding_period_days: Number of days for the unbonding period
        """
        self.total_staked = total_staked
        self.user_staked = user_staked
        self.btc_reward_per_staked = btc_reward_per_staked
        self.unbonding_period_days = unbonding_period_days

    def calculate_rewards(self) -> Decimal:
        """
        Calculate the BTC rewards for the user based on their staking participation.

        :return: The total BTC rewards the user is entitled to
        """
        if self.total_staked <= 0:
            logging.error("Total staked amount must be greater than zero.")
            raise ValueError("Total staked amount must be greater than zero.")

        if self.user_staked < 0:
            logging.error("User staked amount cannot be negative.")
            raise ValueError("User staked amount cannot be negative.")

        # Calculate user share of the total staked
        user_share = self.user_staked / self.total_staked
        # Calculate BTC rewards based on user's share
        btc_rewards = user_share * self.btc_reward_per_staked * self.user_staked

        logging.info(f"User share: {user_share}, BTC Rewards: {btc_rewards}")
        return btc_rewards

    def is_unbonding_period_over(self, days_since_unbond: int) -> bool:
        """
        Check if the unbonding period has passed for the user.

        :param days_since_unbond: Days since the user initiated the unbonding process
        :return: True if the unbonding period is over, False otherwise
        """
        if days_since_unbond < 0:
            logging.error("Days since unbond cannot be negative.")
            raise ValueError("Days since unbond cannot be negative.")
        
        return days_since_unbond >= self.unbonding_period_days

# Example usage
if __name__ == "__main__":
    try:
        # Sample data
        total_staked = Decimal('1000.0')  # Total PROS staked
        user_staked = Decimal('100.0')     # User's staked PROS
        btc_reward_per_staked = Decimal('0.002')  # BTC reward per staked PROS token
        unbonding_period_days = 14          # Unbonding period in days

        # Instantiate the reward calculator
        calculator = StakingRewardCalculator(total_staked, user_staked, btc_reward_per_staked, unbonding_period_days)
        
        # Calculate rewards
        btc_rewards = calculator.calculate_rewards()
        logging.info(f"Calculated BTC rewards: {btc_rewards}")

        # Check unbonding status
        days_since_unbond = 15  # Assume 15 days have passed since unbonding
        if calculator.is_unbonding_period_over(days_since_unbond):
            logging.info("Unbonding period is over. User can withdraw rewards.")
        else:
            logging.info("Unbonding period is still ongoing.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
