"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daos-world-wl.pages.dev
Prompt: Explain how to design a farm-style rewards system for DAOs, similar to the "Farms 🧑‍🌾" feature on daos.world.
Generated: DETERMINISTIC_2b9b0ae5fb99e54c
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict, Any
import datetime

class RewardFarm:
    """
    A class to represent a reward farm for a DAO (Decentralized Autonomous Organization).
    This system allows users to stake tokens and earn rewards over time.
    """

    def __init__(self):
        # Initialize an empty dictionary to store user stakes and rewards
        self.user_stakes: Dict[str, float] = {}
        self.reward_rate: float = 0.1  # Reward rate per day
        self.last_updated: datetime.datetime = datetime.datetime.now()

    def stake_tokens(self, user_id: str, amount: float) -> None:
        """
        Allow a user to stake a specified amount of tokens.

        :param user_id: The unique identifier for the user
        :param amount: The amount of tokens to stake
        :raises ValueError: If the stake amount is non-positive
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")
        
        if user_id in self.user_stakes:
            self.user_stakes[user_id] += amount
        else:
            self.user_stakes[user_id] = amount
        
        # Update last_updated time
        self.last_updated = datetime.datetime.now()

    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculate the rewards for a user based on their stake and the time elapsed since last update.

        :param user_id: The unique identifier for the user
        :return: The total rewards calculated
        :raises KeyError: If the user has not staked any tokens
        """
        if user_id not in self.user_stakes:
            raise KeyError("User has not staked any tokens.")
        
        # Calculate the number of days since the last update
        days_passed = (datetime.datetime.now() - self.last_updated).days
        rewards = self.user_stakes[user_id] * self.reward_rate * days_passed
        
        return rewards

    def claim_rewards(self, user_id: str) -> float:
        """
        Allow a user to claim their rewards.

        :param user_id: The unique identifier for the user
        :return: The amount of rewards claimed
        :raises KeyError: If the user has not staked any tokens
        """
        rewards = self.calculate_rewards(user_id)
        
        # Reset user's stake to reflect claiming rewards
        self.user_stakes[user_id] = 0  # Reset the stake amount
        self.last_updated = datetime.datetime.now()  # Reset the last updated time
        
        return rewards

    def get_user_stake(self, user_id: str) -> float:
        """
        Retrieve the current stake amount for a user.

        :param user_id: The unique identifier for the user
        :return: The current stake amount
        :raises KeyError: If the user has not staked any tokens
        """
        if user_id not in self.user_stakes:
            raise KeyError("User has not staked any tokens.")
        
        return self.user_stakes[user_id]

# Example usage
if __name__ == "__main__":
    farm = RewardFarm()
    farm.stake_tokens("user123", 100)
    print("User stake:", farm.get_user_stake("user123"))
    print("User rewards:", farm.calculate_rewards("user123"))
    print("Claimed rewards:", farm.claim_rewards("user123"))
```
