"""
Generated Code Metadata:
========================
Original URL: https://sophan.xyz
Prompt: Generate code for staking SOPH tokens and calculating rewards for Sophon Node operators and Guardians.
Generated: DETERMINISTIC_347e0874516c2ee5
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_rewards_calculator.py

import math
from datetime import datetime, timedelta

class StakingRewardsCalculator:
    """
    Calculates staking rewards for Sophon Node operators and Guardians.
    """

    def __init__(self, total_supply, circulating_supply, staking_rate, reward_rate, 
                 node_operator_share, guardian_share, epoch_duration):
        """
        Initializes the calculator with the given parameters.

        Args:
        - total_supply (float): Total supply of SOPH tokens.
        - circulating_supply (float): Circulating supply of SOPH tokens.
        - staking_rate (float): Staking rate of SOPH tokens.
        - reward_rate (float): Reward rate for staked SOPH tokens.
        - node_operator_share (float): Share of rewards for node operators.
        - guardian_share (float): Share of rewards for guardians.
        - epoch_duration (int): Duration of an epoch in seconds.
        """
        self.total_supply = total_supply
        self.circulating_supply = circulating_supply
        self.staking_rate = staking_rate
        self.reward_rate = reward_rate
        self.node_operator_share = node_operator_share
        self.guardian_share = guardian_share
        self.epoch_duration = epoch_duration

    def calculate_staking_rewards(self, staked_amount, epoch):
        """
        Calculates the staking rewards for the given staked amount and epoch.

        Args:
        - staked_amount (float): Amount of SOPH tokens staked.
        - epoch (int): Current epoch.

        Returns:
        - float: Staking rewards for the given staked amount and epoch.
        """
        # Calculate the total rewards for the epoch
        total_rewards = self.calculate_total_rewards(epoch)

        # Calculate the staking rewards for the given staked amount
        staking_rewards = (staked_amount / self.circulating_supply) * total_rewards

        return staking_rewards

    def calculate_total_rewards(self, epoch):
        """
        Calculates the total rewards for the given epoch.

        Args:
        - epoch (int): Current epoch.

        Returns:
        - float: Total rewards for the given epoch.
        """
        # Calculate the total staking amount
        total_staking_amount = self.circulating_supply * self.staking_rate

        # Calculate the total rewards for the epoch
        total_rewards = total_staking_amount * self.reward_rate * self.epoch_duration

        return total_rewards

    def calculate_node_operator_rewards(self, staking_rewards):
        """
        Calculates the node operator rewards for the given staking rewards.

        Args:
        - staking_rewards (float): Staking rewards.

        Returns:
        - float: Node operator rewards.
        """
        return staking_rewards * self.node_operator_share

    def calculate_guardian_rewards(self, staking_rewards):
        """
        Calculates the guardian rewards for the given staking rewards.

        Args:
        - staking_rewards (float): Staking rewards.

        Returns:
        - float: Guardian rewards.
        """
        return staking_rewards * self.guardian_share


def main():
    try:
        # Initialize the calculator with example parameters
        calculator = StakingRewardsCalculator(
            total_supply=1000000,
            circulating_supply=500000,
            staking_rate=0.2,
            reward_rate=0.05,
            node_operator_share=0.6,
            guardian_share=0.4,
            epoch_duration=86400  # 1 day in seconds
        )

        # Example usage
        staked_amount = 10000
        epoch = 1
        staking_rewards = calculator.calculate_staking_rewards(staked_amount, epoch)
        node_operator_rewards = calculator.calculate_node_operator_rewards(staking_rewards)
        guardian_rewards = calculator.calculate_guardian_rewards(staking_rewards)

        print(f"Staking Rewards: {staking_rewards}")
        print(f"Node Operator Rewards: {node_operator_rewards}")
        print(f"Guardian Rewards: {guardian_rewards}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
