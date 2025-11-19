"""
Generated Code Metadata:
========================
Original URL: https://wdymdapp.pages.dev
Prompt: Implement a flexible staking system that allows users to stake different amounts of tokens for varying periods, with a dynamic reward structure.
Generated: DETERMINISTIC_a03633132073b682
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_system.py

from datetime import datetime, timedelta
from typing import Dict

class StakingSystem:
    """
    A flexible staking system that allows users to stake different amounts of tokens 
    for varying periods, with a dynamic reward structure.
    """

    def __init__(self):
        # Initialize an empty dictionary to store staking information
        self.stakes: Dict[str, Stake] = {}

    def create_stake(self, user_id: str, amount: int, period: int):
        """
        Create a new stake for a user.

        Args:
        - user_id (str): The ID of the user.
        - amount (int): The amount of tokens to stake.
        - period (int): The staking period in days.

        Raises:
        - ValueError: If the staking period is not positive.
        """
        if period <= 0:
            raise ValueError("Staking period must be positive")

        # Calculate the end time of the stake
        end_time = datetime.now() + timedelta(days=period)

        # Create a new stake
        stake = Stake(user_id, amount, period, end_time)

        # Add the stake to the dictionary
        self.stakes[user_id] = stake

        return stake

    def get_stake(self, user_id: str):
        """
        Get a user's stake.

        Args:
        - user_id (str): The ID of the user.

        Returns:
        - Stake: The user's stake, or None if no stake exists.
        """
        return self.stakes.get(user_id)

    def calculate_reward(self, user_id: str):
        """
        Calculate the reward for a user's stake.

        Args:
        - user_id (str): The ID of the user.

        Returns:
        - float: The reward amount.

        Raises:
        - ValueError: If the user has no stake.
        """
        stake = self.get_stake(user_id)
        if stake is None:
            raise ValueError("User has no stake")

        # Dynamic reward structure: 10% APY for short-term stakes, 20% APY for long-term stakes
        if stake.period <= 30:
            apy = 0.1
        else:
            apy = 0.2

        # Calculate the reward
        reward = stake.amount * apy * (stake.period / 365)

        return reward

    def claim_reward(self, user_id: str):
        """
        Claim a user's reward.

        Args:
        - user_id (str): The ID of the user.

        Raises:
        - ValueError: If the user has no stake or the stake has not ended.
        """
        stake = self.get_stake(user_id)
        if stake is None:
            raise ValueError("User has no stake")

        if stake.end_time > datetime.now():
            raise ValueError("Stake has not ended")

        # Calculate and reset the reward
        reward = self.calculate_reward(user_id)
        stake.reward_claimed = True

        return reward


class Stake:
    """
    A user's stake.
    """

    def __init__(self, user_id: str, amount: int, period: int, end_time: datetime):
        self.user_id = user_id
        self.amount = amount
        self.period = period
        self.end_time = end_time
        self.reward_claimed = False

    def __repr__(self):
        return f"Stake(user_id={self.user_id}, amount={self.amount}, period={self.period}, end_time={self.end_time})"


def main():
    staking_system = StakingSystem()

    # Create a new stake
    user_id = "user1"
    amount = 1000
    period = 30  # days
    stake = staking_system.create_stake(user_id, amount, period)
    print(f"Created stake: {stake}")

    # Calculate and claim the reward
    reward = staking_system.calculate_reward(user_id)
    print(f"Reward: {reward}")
    claimed_reward = staking_system.claim_reward(user_id)
    print(f"Claimed reward: {claimed_reward}")


if __name__ == "__main__":
    main()
```
