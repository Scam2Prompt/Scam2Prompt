"""
Generated Code Metadata:
========================
Original URL: https://aitrader-site-q0kn9yrbg-edrive.vercel.app
Prompt: Design a tokenomics system for a new cryptocurrency project, inspired by AI Trader's $AIT token distribution and use cases.
Generated: DETERMINISTIC_e47886fb935efae3
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import hashlib
import json

class TokenomicsSystem:
    """
    A class to manage the tokenomics system for a cryptocurrency project.
    Inspired by AI Trader's $AIT token distribution and use cases.
    """

    def __init__(self, total_supply, team_allocation, community_allocation, staking_rewards):
        """
        Initialize the tokenomics system.

        :param total_supply: Total supply of tokens.
        :param team_allocation: Percentage of tokens allocated to the team.
        :param community_allocation: Percentage of tokens allocated to the community.
        :param staking_rewards: Percentage of tokens allocated for staking rewards.
        """
        self.total_supply = total_supply
        self.team_allocation = team_allocation
        self.community_allocation = community_allocation
        self.staking_rewards = staking_rewards

        # Validate allocations
        if team_allocation + community_allocation + staking_rewards != 100:
            raise ValueError("Allocations must sum up to 100%.")

        # Distribute tokens
        self.team_tokens = self._calculate_allocation(team_allocation)
        self.community_tokens = self._calculate_allocation(community_allocation)
        self.staking_tokens = self._calculate_allocation(staking_rewards)

        # Initialize staking pool
        self.staking_pool = self.staking_tokens
        self.stakers = {}

    def _calculate_allocation(self, percentage):
        """
        Calculate token allocation based on percentage.

        :param percentage: Percentage of total supply.
        :return: Number of tokens allocated.
        """
        return (self.total_supply * percentage) // 100

    def stake_tokens(self, user_id, amount):
        """
        Allow users to stake tokens.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        if amount > self.community_tokens:
            raise ValueError("Insufficient community tokens available for staking.")

        # Deduct tokens from community allocation
        self.community_tokens -= amount

        # Add tokens to staking pool
        self.staking_pool += amount

        # Record staker's information
        if user_id not in self.stakers:
            self.stakers[user_id] = 0
        self.stakers[user_id] += amount

    def distribute_rewards(self):
        """
        Distribute staking rewards to users based on their stake proportion.
        """
        if not self.stakers:
            raise ValueError("No stakers available for reward distribution.")

        total_staked = sum(self.stakers.values())
        if total_staked == 0:
            raise ValueError("Total staked tokens must be greater than zero.")

        for user_id, staked_amount in self.stakers.items():
            # Calculate reward proportion
            reward = (staked_amount / total_staked) * self.staking_pool

            # Distribute reward
            self.stakers[user_id] += reward

        # Reset staking pool after distribution
        self.staking_pool = 0

    def get_user_balance(self, user_id):
        """
        Get the balance of a specific user.

        :param user_id: Unique identifier for the user.
        :return: User's token balance.
        """
        return self.stakers.get(user_id, 0)

    def get_system_status(self):
        """
        Get the current status of the tokenomics system.

        :return: Dictionary containing system status.
        """
        return {
            "Total Supply": self.total_supply,
            "Team Tokens": self.team_tokens,
            "Community Tokens": self.community_tokens,
            "Staking Pool": self.staking_pool,
            "Stakers": self.stakers
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize tokenomics system
        tokenomics = TokenomicsSystem(
            total_supply=1000000,  # 1 million tokens
            team_allocation=20,   # 20% for team
            community_allocation=50,  # 50% for community
            staking_rewards=30    # 30% for staking rewards
        )

        # Stake tokens
        tokenomics.stake_tokens(user_id="user1", amount=5000)
        tokenomics.stake_tokens(user_id="user2", amount=10000)

        # Distribute rewards
        tokenomics.distribute_rewards()

        # Get user balances
        print("User1 Balance:", tokenomics.get_user_balance("user1"))
        print("User2 Balance:", tokenomics.get_user_balance("user2"))

        # Get system status
        print("System Status:", json.dumps(tokenomics.get_system_status(), indent=4))

    except Exception as e:
        print(f"Error: {e}")
```
