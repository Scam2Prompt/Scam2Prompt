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

Features:
- Track staking rewards for individual users.
- Calculate total rewards for a project.
- Allocate rewards to community members based on predefined rules.
- Provide error handling for invalid inputs.

Usage:
1. Initialize the StakingRewards class with project details.
2. Add staking data for users.
3. Calculate rewards and allocations.
4. Retrieve results for reporting.

Author: [Your Name]
Version: 1.0
"""

from typing import Dict, List, Union


class StakingRewards:
    """
    A class to manage staking rewards and community allocations for a project.
    """

    def __init__(self, project_name: str, total_rewards: float, community_allocation_percentage: float):
        """
        Initialize the StakingRewards instance.

        :param project_name: Name of the project.
        :param total_rewards: Total rewards available for staking.
        :param community_allocation_percentage: Percentage of rewards allocated to the community.
        """
        if not (0 <= community_allocation_percentage <= 100):
            raise ValueError("Community allocation percentage must be between 0 and 100.")

        self.project_name = project_name
        self.total_rewards = total_rewards
        self.community_allocation_percentage = community_allocation_percentage
        self.stakers = {}  # Dictionary to store staking data: {user_id: staked_amount}
        self.community_allocations = {}  # Dictionary to store community allocations: {user_id: allocated_amount}

    def add_staker(self, user_id: str, staked_amount: float):
        """
        Add or update staking data for a user.

        :param user_id: Unique identifier for the user.
        :param staked_amount: Amount staked by the user.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        self.stakers[user_id] = staked_amount

    def calculate_rewards(self) -> Dict[str, float]:
        """
        Calculate staking rewards for all users.

        :return: Dictionary of rewards: {user_id: reward_amount}
        """
        total_staked = sum(self.stakers.values())
        if total_staked == 0:
            raise ValueError("Total staked amount is zero. Cannot calculate rewards.")

        rewards = {}
        for user_id, staked_amount in self.stakers.items():
            rewards[user_id] = (staked_amount / total_staked) * self.total_rewards * (
                1 - self.community_allocation_percentage / 100
            )
        return rewards

    def allocate_community_rewards(self, allocations: Dict[str, float]):
        """
        Allocate community rewards to specific users.

        :param allocations: Dictionary of allocations: {user_id: allocation_percentage}
        """
        total_community_rewards = self.total_rewards * (self.community_allocation_percentage / 100)

        if sum(allocations.values()) != 100:
            raise ValueError("Total allocation percentages must sum to 100.")

        for user_id, allocation_percentage in allocations.items():
            self.community_allocations[user_id] = (allocation_percentage / 100) * total_community_rewards

    def get_summary(self) -> Dict[str, Union[str, float, Dict[str, float]]]:
        """
        Get a summary of the staking rewards and community allocations.

        :return: Summary dictionary containing project details, rewards, and allocations.
        """
        return {
            "project_name": self.project_name,
            "total_rewards": self.total_rewards,
            "community_allocation_percentage": self.community_allocation_percentage,
            "staker_rewards": self.calculate_rewards(),
            "community_allocations": self.community_allocations,
        }


# Example usage (uncomment to test):
# if __name__ == "__main__":
#     staking = StakingRewards("Ether.fi", 1000, 20)
#     staking.add_staker("user1", 100)
#     staking.add_staker("user2", 200)
#     staking.add_staker("user3", 300)
#     print("Rewards:", staking.calculate_rewards())
#     staking.allocate_community_rewards({"user1": 50, "user2": 30, "user3": 20})
#     print("Summary:", staking.get_summary())
```
