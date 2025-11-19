"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-aixcbcapital.pages.dev
Prompt: Explain how the community-driven venture capital model works in the context of aixCB Staking.
Generated: DETERMINISTIC_ef84bbeda616d72f
Batch ID: 20250612_155846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script explains how a community-driven venture capital model works in the context of aixCB staking.
It simulates the staking, reward distribution, and community-driven investment model for a decentralized platform.
"""

from typing import Dict, List

class AixCBStaking:
    """
    A class to represent the AixCB Staking mechanism.
    """
    def __init__(self):
        """
        Initialize staking pool, users, and community fund.
        """
        self.staking_pool: Dict[str, float] = {}  # Stores user stakes in key-value pairs {user: stake_amount}
        self.community_fund: float = 0.0         # Community-driven fund for investments
        self.total_staked: float = 0.0           # Total stake in the pool

    def stake(self, user: str, amount: float) -> None:
        """
        Allows a user to stake their tokens into the staking pool.

        Parameters:
        user (str): The user's identifier.
        amount (float): The amount of tokens the user wants to stake.

        Raises:
        ValueError: If the staking amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        if user in self.staking_pool:
            self.staking_pool[user] += amount
        else:
            self.staking_pool[user] = amount

        self.total_staked += amount
        print(f"{user} staked {amount} tokens. Total staked: {self.total_staked}.")

    def unstake(self, user: str, amount: float) -> None:
        """
        Allows a user to unstake their tokens from the staking pool.

        Parameters:
        user (str): The user's identifier.
        amount (float): The amount of tokens the user wants to unstake.

        Raises:
        ValueError: If the unstaking amount is invalid.
        """
        if user not in self.staking_pool or amount <= 0:
            raise ValueError("Invalid unstake request. Check user and amount.")

        if self.staking_pool[user] < amount:
            raise ValueError("User does not have enough staked tokens to unstake.")

        self.staking_pool[user] -= amount
        self.total_staked -= amount

        if self.staking_pool[user] == 0:
            del self.staking_pool[user]  # Remove user from pool if no tokens remain

        print(f"{user} unstaked {amount} tokens. Total staked: {self.total_staked}.")

    def distribute_rewards(self, rewards: float) -> None:
        """
        Distributes staking rewards based on stake proportion.

        Parameters:
        rewards (float): The total reward amount to be distributed.

        Raises:
        ValueError: If the rewards amount is invalid.
        """
        if rewards <= 0:
            raise ValueError("Rewards must be greater than zero.")

        print(f"Distributing {rewards} tokens among stakeholders.")
        for user, stake in self.staking_pool.items():
            proportion = stake / self.total_staked
            reward = rewards * proportion
            print(f"{user} receives {reward:.2f} tokens as reward.")

    def allocate_to_community_fund(self, percentage: float) -> None:
        """
        Allocates a percentage of the total staked tokens to the community fund.

        Parameters:
        percentage (float): The percentage of the total stake to allocate.

        Raises:
        ValueError: If the allocation percentage is invalid.
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")

        allocation = self.total_staked * (percentage / 100)
        self.community_fund += allocation
        print(f"{allocation:.2f} tokens allocated to the community fund. Total community fund: {self.community_fund:.2f}.")

    def invest_community_fund(self, project_name: str, amount: float) -> None:
        """
        Invests tokens from the community fund into a specified project.

        Parameters:
        project_name (str): The name of the project.
        amount (float): The amount to be invested.

        Raises:
        ValueError: If the investment amount is invalid.
        """
        if amount <= 0 or amount > self.community_fund:
            raise ValueError("Invalid investment amount.")

        self.community_fund -= amount
        print(f"Invested {amount:.2f} tokens from the community fund into project '{project_name}'. Remaining community fund: {self.community_fund:.2f}.")

# Usage Example
if __name__ == "__main__":
    staking_system = AixCBStaking()
    
    # Users staking tokens
    staking_system.stake("Alice", 100)
    staking_system.stake("Bob", 200)
    staking_system.stake("Charlie", 300)

    # Distributing rewards
    staking_system.distribute_rewards(60)

    # Allocating funds to community
    staking_system.allocate_to_community_fund(10)

    # Investing community fund into a project
    staking_system.invest_community_fund("Green Energy Initiative", 50)
```
