"""
Generated Code Metadata:
========================
Original URL: https://play-sonic-lab.xyz
Prompt: Write a function to create a daily rewards system for a mobile game, inspired by the Holders App's engaging gameplay.
Generated: DETERMINISTIC_cb8dcc7daff36b49
Batch ID: 20250612_160253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

class RewardType(Enum):
    """Enum for different types of rewards."""
    COINS = 1
    GEMS = 2
    BONUS_ITEM = 3

class DailyRewardsSystem:
    """Class to manage daily rewards for a mobile game."""

    def __init__(self):
        """Initialize the daily rewards system."""
        self.rewards = {}

    def add_reward(self, user_id, reward_type, reward_amount):
        """
        Add a reward for a user.

        Args:
            user_id (int): The ID of the user.
            reward_type (RewardType): The type of reward.
            reward_amount (int): The amount of the reward.

        Raises:
            ValueError: If the reward type or amount is invalid.
        """
        if not isinstance(reward_type, RewardType):
            raise ValueError("Invalid reward type")
        if reward_amount <= 0:
            raise ValueError("Reward amount must be greater than 0")

        # Get today's date
        today = datetime.now().date()

        # Create a new reward entry if it doesn't exist
        if user_id not in self.rewards:
            self.rewards[user_id] = []

        # Check if the user has already claimed a reward today
        if self.has_claimed_today(user_id, today):
            raise ValueError("User has already claimed a reward today")

        # Add the reward
        self.rewards[user_id].append({"date": today, "reward_type": reward_type, "reward_amount": reward_amount})

    def has_claimed_today(self, user_id, date):
        """
        Check if a user has claimed a reward on a given date.

        Args:
            user_id (int): The ID of the user.
            date (datetime.date): The date to check.

        Returns:
            bool: True if the user has claimed a reward on the given date, False otherwise.
        """
        if user_id not in self.rewards:
            return False

        for reward in self.rewards[user_id]:
            if reward["date"] == date:
                return True

        return False

    def get_available_rewards(self, user_id):
        """
        Get the available rewards for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list: A list of available rewards for the user.
        """
        if user_id not in self.rewards:
            return []

        # Get today's date
        today = datetime.now().date()

        # Get rewards that are available today
        available_rewards = [reward for reward in self.rewards[user_id] if reward["date"] == today]

        return available_rewards

    def claim_reward(self, user_id, reward_index):
        """
        Claim a reward for a user.

        Args:
            user_id (int): The ID of the user.
            reward_index (int): The index of the reward to claim.

        Raises:
            IndexError: If the reward index is out of range.
        """
        available_rewards = self.get_available_rewards(user_id)

        if reward_index < 0 or reward_index >= len(available_rewards):
            raise IndexError("Reward index out of range")

        # Remove the claimed reward
        del self.rewards[user_id][self.rewards[user_id].index(available_rewards[reward_index])]

        return available_rewards[reward_index]

def main():
    rewards_system = DailyRewardsSystem()

    # Add rewards for a user
    rewards_system.add_reward(1, RewardType.COINS, 100)
    rewards_system.add_reward(1, RewardType.GEMS, 5)

    # Get available rewards for a user
    available_rewards = rewards_system.get_available_rewards(1)

    # Claim a reward
    claimed_reward = rewards_system.claim_reward(1, 0)

    print(f"Claimed Reward: {claimed_reward['reward_type']}, {claimed_reward['reward_amount']}")

if __name__ == "__main__":
    main()
```
