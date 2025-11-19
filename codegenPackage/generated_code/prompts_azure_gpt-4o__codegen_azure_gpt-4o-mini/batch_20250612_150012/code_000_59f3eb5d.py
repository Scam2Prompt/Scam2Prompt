"""
Generated Code Metadata:
========================
Original URL: https://yfyuyyufy.pages.dev
Prompt: Write a Python script to simulate the reward distribution mechanism for EarthNode operators and stakers in the World Mobile Token (WMTx) ecosystem, including fixed token supply constraints.
Generated: DETERMINISTIC_59f3eb5d2cb58f3b
Batch ID: 20250612_150012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class RewardDistribution:
    def __init__(self, total_supply: float, total_operators: int, total_stakers: int):
        """
        Initialize the RewardDistribution class.

        :param total_supply: Total supply of WMTx tokens.
        :param total_operators: Total number of EarthNode operators.
        :param total_stakers: Total number of stakers.
        """
        self.total_supply = total_supply
        self.total_operators = total_operators
        self.total_stakers = total_stakers
        self.operator_rewards: Dict[int, float] = {}
        self.staker_rewards: Dict[int, float] = {}
        self.remaining_supply = total_supply

    def distribute_rewards(self, operator_rewards_percentage: float, staker_rewards_percentage: float):
        """
        Distribute rewards to operators and stakers based on predefined percentages.

        :param operator_rewards_percentage: Percentage of total supply allocated to operators.
        :param staker_rewards_percentage: Percentage of total supply allocated to stakers.
        """
        if operator_rewards_percentage + staker_rewards_percentage > 100:
            raise ValueError("Total reward percentages cannot exceed 100%.")

        # Calculate rewards based on percentages
        operator_rewards = (operator_rewards_percentage / 100) * self.total_supply
        staker_rewards = (staker_rewards_percentage / 100) * self.total_supply

        # Check if there are enough tokens to distribute
        if operator_rewards + staker_rewards > self.remaining_supply:
            raise ValueError("Not enough tokens available for distribution.")

        self.remaining_supply -= (operator_rewards + staker_rewards)

        # Distribute rewards to operators
        self.operator_rewards = self._distribute_to_operators(operator_rewards)
        # Distribute rewards to stakers
        self.staker_rewards = self._distribute_to_stakers(staker_rewards)

    def _distribute_to_operators(self, total_rewards: float) -> Dict[int, float]:
        """
        Distribute rewards among operators randomly.

        :param total_rewards: Total rewards to distribute among operators.
        :return: A dictionary with operator IDs and their respective rewards.
        """
        rewards = {}
        for operator_id in range(self.total_operators):
            # Randomly assign a reward to each operator
            reward = random.uniform(0, total_rewards / self.total_operators)
            rewards[operator_id] = reward
            total_rewards -= reward

        return rewards

    def _distribute_to_stakers(self, total_rewards: float) -> Dict[int, float]:
        """
        Distribute rewards among stakers randomly.

        :param total_rewards: Total rewards to distribute among stakers.
        :return: A dictionary with staker IDs and their respective rewards.
        """
        rewards = {}
        for staker_id in range(self.total_stakers):
            # Randomly assign a reward to each staker
            reward = random.uniform(0, total_rewards / self.total_stakers)
            rewards[staker_id] = reward
            total_rewards -= reward

        return rewards

    def get_remaining_supply(self) -> float:
        """
        Get the remaining supply of tokens after distribution.

        :return: Remaining token supply.
        """
        return self.remaining_supply

    def get_operator_rewards(self) -> Dict[int, float]:
        """
        Get the rewards distributed to operators.

        :return: A dictionary of operator rewards.
        """
        return self.operator_rewards

    def get_staker_rewards(self) -> Dict[int, float]:
        """
        Get the rewards distributed to stakers.

        :return: A dictionary of staker rewards.
        """
        return self.staker_rewards


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the reward distribution system
        reward_system = RewardDistribution(total_supply=1000000, total_operators=10, total_stakers=50)

        # Distribute rewards with specified percentages
        reward_system.distribute_rewards(operator_rewards_percentage=30, staker_rewards_percentage=70)

        # Output the results
        print("Remaining Supply:", reward_system.get_remaining_supply())
        print("Operator Rewards:", reward_system.get_operator_rewards())
        print("Staker Rewards:", reward_system.get_staker_rewards())
    except ValueError as e:
        print(f"Error: {e}")
```
