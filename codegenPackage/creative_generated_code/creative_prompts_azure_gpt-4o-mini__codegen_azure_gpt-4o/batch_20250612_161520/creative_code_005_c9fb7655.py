"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoindapp.pages.dev
Prompt: Provide an example of a staking strategy that leverages the unique features of Green Bitcoin's gamified rewards system.
Generated: DETERMINISTIC_c9fb76554a9780c3
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import Dict, List

class StakingStrategy:
    """
    Class representing a staking strategy leveraging Green Bitcoin's gamified rewards system.
    """

    def __init__(self, user_wallet: str, reward_tiers: Dict[int, float], reward_decay_factor: float):
        """
        Initialize the staking strategy.

        :param user_wallet: User's wallet address for staking.
        :param reward_tiers: Mapping of staking time (in days) to reward percentages.
        :param reward_decay_factor: Factor to adjust rewards over time for gamification.
        """
        self.user_wallet = user_wallet
        self.reward_tiers = reward_tiers
        self.reward_decay_factor = reward_decay_factor
        self.staked_amount = 0.0
        self.start_time = None
        self.rewards_earned = 0.0

    def stake(self, amount: float) -> None:
        """
        Stake a specific amount into the strategy.

        :param amount: Amount to stake.
        :raises ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        self.staked_amount += amount
        self.start_time = time.time()  # Save the start time for reward calculation
        print(f"Successfully staked {amount} Green Bitcoin. Total staked: {self.staked_amount}")

    def calculate_rewards(self) -> float:
        """
        Calculate the rewards based on the staking duration and gamified reward tiers.

        :return: Total rewards earned.
        """
        if self.staked_amount == 0 or self.start_time is None:
            return 0.0

        elapsed_time_in_days = (time.time() - self.start_time) / (60 * 60 * 24)

        # Determine reward percentage based on elapsed time
        applicable_reward_percentage = 0.0
        for days, percentage in self.reward_tiers.items():
            if elapsed_time_in_days >= days:
                applicable_reward_percentage = percentage

        # Apply reward decay factor for gamification
        adjusted_reward_percentage = (
            applicable_reward_percentage * (1 - self.reward_decay_factor)
        )

        # Calculate rewards earned
        rewards = self.staked_amount * (adjusted_reward_percentage / 100)
        self.rewards_earned += rewards
        return rewards

    def claim_rewards(self) -> float:
        """
        Claim the rewards earned so far and reset the reward calculation.

        :return: Claimed rewards amount.
        """
        claimed_rewards = self.calculate_rewards()

        # Reset the staking start time for the next round
        self.start_time = time.time()
        print(f"Rewards claimed: {claimed_rewards:.2f} Green Bitcoin")
        return claimed_rewards


# Example usage:
if __name__ == "__main__":
    # Define reward tiers (days: reward percentage)
    reward_tiers = {
        1: 2.0,  # 2% for staking 1 day
        7: 5.0,  # 5% for staking 7 days
        30: 10.0, # 10% for staking 30 days
    }

    # Instantiate the staking strategy with decay factor of 0.1 (10%)
    staking_strategy = StakingStrategy(
        user_wallet="0x12345abcde",
        reward_tiers=reward_tiers,
        reward_decay_factor=0.1
    )

    # Stake some Green Bitcoin
    staking_strategy.stake(100)  # Stake 100 Green Bitcoin

    # Simulate staking period
    time.sleep(2)  # Wait for 2 seconds (illustration purposes)

    # Calculate rewards
    rewards = staking_strategy.calculate_rewards()
    print(f"Rewards earned: {rewards:.2f} Green Bitcoin")

    # Claim rewards
    staking_strategy.claim_rewards()
```
