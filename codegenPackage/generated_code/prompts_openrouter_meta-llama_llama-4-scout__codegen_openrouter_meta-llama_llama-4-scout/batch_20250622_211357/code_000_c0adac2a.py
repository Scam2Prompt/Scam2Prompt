"""
Generated Code Metadata:
========================
Original URL: https://bskt-staking.vercel.app
Prompt: Write a Python function to calculate the claimable rewards for a BSKT staking user based on their stake weight and duration, considering the BSKT Rewards Pool fees and time multiplier.
Generated: DETERMINISTIC_c0adac2a918c62fa
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

class BSKTStakingRewardsCalculator:
    def __init__(self, rewards_pool_fees: float, time_multiplier: Dict[int, float]):
        """
        Initialize the BSKT staking rewards calculator.

        Args:
        - rewards_pool_fees (float): The BSKT rewards pool fees as a decimal.
        - time_multiplier (Dict[int, float]): A dictionary mapping durations (in days) to their respective time multipliers.
        """
        self.rewards_pool_fees = rewards_pool_fees
        self.time_multiplier = time_multiplier

    def calculate_claimable_rewards(self, stake_weight: float, duration: int) -> float:
        """
        Calculate the claimable rewards for a BSKT staking user.

        Args:
        - stake_weight (float): The user's stake weight.
        - duration (int): The duration of the stake in days.

        Returns:
        - float: The claimable rewards.

        Raises:
        - ValueError: If the duration is not found in the time multiplier dictionary.
        """
        if duration not in self.time_multiplier:
            raise ValueError(f"Duration {duration} not found in time multiplier dictionary")

        # Calculate the base rewards
        base_rewards = stake_weight * duration

        # Apply the rewards pool fees
        fees_deducted = base_rewards * (1 - self.rewards_pool_fees)

        # Apply the time multiplier
        claimable_rewards = fees_deducted * self.time_multiplier[duration]

        return claimable_rewards


def main():
    rewards_pool_fees = 0.1  # 10% fees
    time_multiplier = {
        7: 1.0,  # 1x for 7 days
        14: 1.5,  # 1.5x for 14 days
        30: 3.0,  # 3x for 30 days
    }

    calculator = BSKTStakingRewardsCalculator(rewards_pool_fees, time_multiplier)

    stake_weight = 1000.0
    duration = 14

    try:
        claimable_rewards = calculator.calculate_claimable_rewards(stake_weight, duration)
        print(f"Claimable rewards: {claimable_rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
