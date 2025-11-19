"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pullixmarkets.pages.dev
Prompt: Generate a code example for creating a staking pool that combines resources for better rewards based on Pullix Markets' information.
Generated: DETERMINISTIC_b54619bfb2f20575
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_pool.py

from typing import Dict, Any


class StakingPoolError(Exception):
    """Custom exception for staking pool errors."""
    pass


class StakingPool:
    """
    A class representing a staking pool where users can combine resources
    to maximize rewards based on Pullix Markets' information.
    """

    def __init__(self):
        """
        Initializes a staking pool with no participants and no total stakes.
        """
        self.participants = {}  # Dictionary to store participant details
        self.total_stake = 0.0  # Total stake in the pool

    def add_stake(self, user_id: str, amount: float) -> None:
        """
        Adds a stake to the pool for a given user.

        :param user_id: The unique identifier of the user.
        :param amount: The amount the user wishes to stake.
        :raises: StakingPoolError if amount is not greater than zero.
        """
        if amount <= 0:
            raise StakingPoolError("Stake amount must be greater than zero.")

        if user_id not in self.participants:
            self.participants[user_id] = {"stake": 0.0}

        self.participants[user_id]["stake"] += amount
        self.total_stake += amount

    def remove_stake(self, user_id: str, amount: float) -> None:
        """
        Removes a stake from the pool for a given user.

        :param user_id: The unique identifier of the user.
        :param amount: The amount the user wishes to remove.
        :raises: StakingPoolError if amount exceeds user's stake.
        """
        if user_id not in self.participants:
            raise StakingPoolError("User does not exist in the staking pool.")

        user_stake = self.participants[user_id]["stake"]
        if amount > user_stake:
            raise StakingPoolError("Cannot remove more stake than user has.")

        self.participants[user_id]["stake"] -= amount
        self.total_stake -= amount

        # Remove user from participants if their stake reaches zero
        if self.participants[user_id]["stake"] == 0:
            del self.participants[user_id]

    def calculate_rewards(self) -> Dict[str, Any]:
        """
        Calculates rewards for each user based on their stake's proportion in the pool.

        :return: A dictionary of user IDs and their respective rewards.
        """
        if self.total_stake == 0:
            return {}  # No rewards if total stake is zero

        rewards = {}
        for user_id, data in self.participants.items():
            user_stake = data["stake"]
            rewards[user_id] = {
                "stake": user_stake,
                "reward": user_stake / self.total_stake  # Proportion-based reward
            }
        return rewards

    def get_pool_status(self) -> Dict[str, Any]:
        """
        Provides the current status of the staking pool.

        :return: A dictionary containing the total stake and participants in the pool.
        """
        return {
            "total_stake": self.total_stake,
            "participants": self.participants
        }


# Example usage (uncomment for testing purposes):
# pool = StakingPool()
# pool.add_stake("user1", 100.0)
# pool.add_stake("user2", 50.0)
# print(pool.calculate_rewards())
# pool.remove_stake("user1", 25.0)
# print(pool.get_pool_status())
```
