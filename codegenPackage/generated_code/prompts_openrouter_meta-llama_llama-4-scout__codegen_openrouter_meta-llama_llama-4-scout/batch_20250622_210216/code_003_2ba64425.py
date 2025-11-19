"""
Generated Code Metadata:
========================
Original URL: https://scottyweb.pages.dev
Prompt: Design a staking system that allows users to withdraw their staked tokens and claimable rewards, taking into account the 3-year reward period and dynamic rewards rate.
Generated: DETERMINISTIC_2ba64425a6b74fb0
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict

class StakingSystem:
    def __init__(self):
        # Initialize an empty dictionary to store user staking information
        self.user_stakes: Dict[str, Dict] = {}

    def stake(self, user_id: str, amount: int):
        """
        Stake tokens for a user.

        Args:
        - user_id (str): The ID of the user staking tokens.
        - amount (int): The amount of tokens to stake.

        Raises:
        - ValueError: If the user has already staked tokens.
        """
        if user_id in self.user_stakes:
            raise ValueError("User has already staked tokens.")

        # Initialize the stake information for the user
        self.user_stakes[user_id] = {
            "staked_amount": amount,
            "staked_at": datetime.datetime.now(),
            "reward_rate": 0.05,  # Initial reward rate (5%)
            "reward_claimed": 0,
            "reward_period": datetime.timedelta(days=1095),  # 3 years
        }

    def unstake(self, user_id: str):
        """
        Unstake tokens for a user.

        Args:
        - user_id (str): The ID of the user unstaking tokens.

        Raises:
        - ValueError: If the user has not staked tokens.
        """
        if user_id not in self.user_stakes:
            raise ValueError("User has not staked tokens.")

        # Calculate the claimable rewards
        claimable_rewards = self.calculate_rewards(user_id)

        # Update the user's stake information
        self.user_stakes[user_id]["staked_amount"] = 0
        self.user_stakes[user_id]["reward_claimed"] += claimable_rewards

        return claimable_rewards

    def claim_rewards(self, user_id: str):
        """
        Claim rewards for a user.

        Args:
        - user_id (str): The ID of the user claiming rewards.

        Raises:
        - ValueError: If the user has not staked tokens or has already claimed all rewards.
        """
        if user_id not in self.user_stakes:
            raise ValueError("User has not staked tokens.")

        # Calculate the claimable rewards
        claimable_rewards = self.calculate_rewards(user_id)

        # Update the user's stake information
        self.user_stakes[user_id]["reward_claimed"] += claimable_rewards

        return claimable_rewards

    def calculate_rewards(self, user_id: str):
        """
        Calculate the claimable rewards for a user.

        Args:
        - user_id (str): The ID of the user.

        Returns:
        - int: The claimable rewards.
        """
        stake_info = self.user_stakes[user_id]
        staked_at = stake_info["staked_at"]
        reward_period = stake_info["reward_period"]
        reward_rate = stake_info["reward_rate"]
        staked_amount = stake_info["staked_amount"]
        reward_claimed = stake_info["reward_claimed"]

        # Calculate the time elapsed since staking
        time_elapsed = datetime.datetime.now() - staked_at

        # Check if the reward period has passed
        if time_elapsed > reward_period:
            # Calculate the claimable rewards
            claimable_rewards = staked_amount * reward_rate * (time_elapsed / reward_period)
            claimable_rewards -= reward_claimed
            return claimable_rewards
        else:
            # Calculate the claimable rewards based on the elapsed time
            claimable_rewards = staked_amount * reward_rate * (time_elapsed / reward_period)
            return claimable_rewards

    def update_reward_rate(self, new_reward_rate: float):
        """
        Update the reward rate for all users.

        Args:
        - new_reward_rate (float): The new reward rate.

        Raises:
        - ValueError: If the new reward rate is not valid.
        """
        if new_reward_rate < 0:
            raise ValueError("Invalid reward rate.")

        # Update the reward rate for all users
        for user_id, stake_info in self.user_stakes.items():
            self.user_stakes[user_id]["reward_rate"] = new_reward_rate


def main():
    staking_system = StakingSystem()

    try:
        staking_system.stake("user1", 1000)
        print("Staked 1000 tokens for user1.")

        # Wait for some time to pass...
        # For demonstration purposes, we'll simulate the passage of time
        stake_info = staking_system.user_stakes["user1"]
        stake_info["staked_at"] = datetime.datetime.now() - datetime.timedelta(days=365)

        claimable_rewards = staking_system.claim_rewards("user1")
        print(f"Claimed {claimable_rewards} rewards for user1.")

        claimable_rewards = staking_system.unstake("user1")
        print(f"Unstaked and claimed {claimable_rewards} rewards for user1.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
