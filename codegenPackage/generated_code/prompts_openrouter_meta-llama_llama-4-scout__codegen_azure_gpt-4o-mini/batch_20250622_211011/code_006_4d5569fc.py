"""
Generated Code Metadata:
========================
Original URL: https://etherfi.vercel.app
Prompt: Design a library for tracking and calculating staking rewards and community allocations for projects like Ether.fi, with documentation similar to the information on their website.
Generated: DETERMINISTIC_4d5569fc86fceca8
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
staking_rewards.py

A library for tracking and calculating staking rewards and community allocations for projects like Ether.fi.

This module provides functionality to calculate staking rewards based on user contributions, staking duration,
and community allocation percentages. It includes error handling to ensure robust operations.

Usage:
    from staking_rewards import StakingRewards

    # Initialize the StakingRewards object
    staking = StakingRewards(total_supply=1000000, reward_rate=0.05)

    # Add a user stake
    staking.add_stake(user_id='user1', amount=1000, duration=30)

    # Calculate rewards for a user
    rewards = staking.calculate_rewards(user_id='user1')
    print(f"User rewards: {rewards}")

    # Get community allocation
    allocation = staking.get_community_allocation()
    print(f"Community allocation: {allocation}")
"""

class StakingRewards:
    def __init__(self, total_supply: float, reward_rate: float):
        """
        Initializes the StakingRewards object.

        Args:
            total_supply (float): The total supply of tokens available for staking.
            reward_rate (float): The rate at which rewards are generated (as a decimal).

        Raises:
            ValueError: If total_supply or reward_rate is not positive.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        if reward_rate <= 0:
            raise ValueError("Reward rate must be a positive number.")

        self.total_supply = total_supply
        self.reward_rate = reward_rate
        self.stakes = {}

    def add_stake(self, user_id: str, amount: float, duration: int):
        """
        Adds a stake for a user.

        Args:
            user_id (str): The unique identifier for the user.
            amount (float): The amount of tokens staked by the user.
            duration (int): The duration of the stake in days.

        Raises:
            ValueError: If amount is not positive or duration is not positive.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be a positive number.")
        if duration <= 0:
            raise ValueError("Stake duration must be a positive number.")

        self.stakes[user_id] = {
            'amount': amount,
            'duration': duration
        }

    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculates the staking rewards for a user.

        Args:
            user_id (str): The unique identifier for the user.

        Returns:
            float: The calculated rewards for the user.

        Raises:
            KeyError: If the user_id does not exist in stakes.
        """
        if user_id not in self.stakes:
            raise KeyError(f"No stake found for user: {user_id}")

        stake_info = self.stakes[user_id]
        amount = stake_info['amount']
        duration = stake_info['duration']

        # Calculate rewards based on the formula: rewards = amount * reward_rate * duration
        rewards = amount * self.reward_rate * duration
        return rewards

    def get_community_allocation(self) -> float:
        """
        Calculates the total community allocation based on the total supply and reward rate.

        Returns:
            float: The total community allocation.
        """
        # Community allocation is a percentage of the total supply based on the reward rate
        community_allocation = self.total_supply * self.reward_rate
        return community_allocation

# Example usage (uncomment to run):
# if __name__ == "__main__":
#     staking = StakingRewards(total_supply=1000000, reward_rate=0.05)
#     staking.add_stake(user_id='user1', amount=1000, duration=30)
#     rewards = staking.calculate_rewards(user_id='user1')
#     print(f"User rewards: {rewards}")
#     allocation = staking.get_community_allocation()
#     print(f"Community allocation: {allocation}")
```
