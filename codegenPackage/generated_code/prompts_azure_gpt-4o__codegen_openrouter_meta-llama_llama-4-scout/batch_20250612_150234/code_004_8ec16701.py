"""
Generated Code Metadata:
========================
Original URL: https://bafybeihbxjh2jhzkz3ukjjcmui77y7fmp4tvvmhqzhv6csboxxwd7dcndu.ipfs.dweb.link
Prompt: Write code to implement staking rewards for $DOP tokens, ensuring users can check their current rewards allocation.
Generated: DETERMINISTIC_8ec16701efa8f208
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_rewards.py

from typing import Dict
from datetime import datetime, timedelta

class StakingRewards:
    def __init__(self, total_rewards: float, staking_duration: int, reward_rate: float):
        """
        Initialize staking rewards.

        Args:
        - total_rewards (float): Total rewards available.
        - staking_duration (int): Staking duration in days.
        - reward_rate (float): Reward rate per day.
        """
        self.total_rewards = total_rewards
        self.staking_duration = staking_duration
        self.reward_rate = reward_rate
        self.user_stakes: Dict[str, UserStake] = {}

    def add_user_stake(self, user_id: str, stake_amount: float, stake_start_time: datetime):
        """
        Add user stake.

        Args:
        - user_id (str): User ID.
        - stake_amount (float): Stake amount.
        - stake_start_time (datetime): Stake start time.
        """
        self.user_stakes[user_id] = UserStake(stake_amount, stake_start_time)

    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculate rewards for a user.

        Args:
        - user_id (str): User ID.

        Returns:
        - float: Rewards amount.
        """
        if user_id not in self.user_stakes:
            raise ValueError("User has no stake")

        user_stake = self.user_stakes[user_id]
        staking_time = (datetime.now() - user_stake.stake_start_time).days
        if staking_time < 0:
            return 0

        staking_time = min(staking_time, self.staking_duration)
        rewards = staking_time * self.reward_rate * user_stake.stake_amount / 100
        return rewards

    def get_user_rewards_allocation(self, user_id: str) -> Dict[str, float]:
        """
        Get user's rewards allocation.

        Args:
        - user_id (str): User ID.

        Returns:
        - Dict[str, float]: Rewards allocation.
        """
        rewards = self.calculate_rewards(user_id)
        return {"rewards": rewards}


class UserStake:
    def __init__(self, stake_amount: float, stake_start_time: datetime):
        """
        Initialize user stake.

        Args:
        - stake_amount (float): Stake amount.
        - stake_start_time (datetime): Stake start time.
        """
        self.stake_amount = stake_amount
        self.stake_start_time = stake_start_time


def main():
    # Initialize staking rewards
    staking_rewards = StakingRewards(
        total_rewards=10000.0,
        staking_duration=30,
        reward_rate=0.1,
    )

    # Add user stakes
    staking_rewards.add_user_stake(
        user_id="user1",
        stake_amount=1000.0,
        stake_start_time=datetime.now() - timedelta(days=15),
    )

    staking_rewards.add_user_stake(
        user_id="user2",
        stake_amount=500.0,
        stake_start_time=datetime.now() - timedelta(days=10),
    )

    # Get user rewards allocation
    try:
        user1_rewards = staking_rewards.get_user_rewards_allocation("user1")
        print(f"User 1 rewards allocation: {user1_rewards}")

        user2_rewards = staking_rewards.get_user_rewards_allocation("user2")
        print(f"User 2 rewards allocation: {user2_rewards}")

        # Test non-existent user
        staking_rewards.get_user_rewards_allocation("non_existent_user")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
