"""
Generated Code Metadata:
========================
Original URL: https://memecoin-cks.pages.dev
Prompt: Generate code to implement a seasonal reward system, where users can harvest rewards at the end of each season.
Generated: DETERMINISTIC_f8d4cfaf541c9a3a
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from datetime import datetime, timedelta

class Season(Enum):
    """Enum representing the different seasons."""
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

class Reward:
    """Class representing a reward."""
    def __init__(self, name, description, value):
        """
        Initialize a Reward object.

        Args:
            name (str): The name of the reward.
            description (str): The description of the reward.
            value (int): The value of the reward.
        """
        self.name = name
        self.description = description
        self.value = value

class User:
    """Class representing a user."""
    def __init__(self, user_id):
        """
        Initialize a User object.

        Args:
            user_id (int): The ID of the user.
        """
        self.user_id = user_id
        self.rewards = []

    def add_reward(self, reward):
        """
        Add a reward to the user's rewards list.

        Args:
            reward (Reward): The reward to add.
        """
        self.rewards.append(reward)

class SeasonalRewardSystem:
    """Class representing the seasonal reward system."""
    def __init__(self):
        """
        Initialize a SeasonalRewardSystem object.
        """
        self.users = {}
        self.seasonal_rewards = {
            Season.SPRING: Reward("Spring Reward", "Reward for spring season", 100),
            Season.SUMMER: Reward("Summer Reward", "Reward for summer season", 150),
            Season.AUTUMN: Reward("Autumn Reward", "Reward for autumn season", 120),
            Season.WINTER: Reward("Winter Reward", "Reward for winter season", 180)
        }

    def add_user(self, user_id):
        """
        Add a user to the system.

        Args:
            user_id (int): The ID of the user.
        """
        if user_id not in self.users:
            self.users[user_id] = User(user_id)

    def harvest_reward(self, user_id, season):
        """
        Harvest a reward for a user at the end of a season.

        Args:
            user_id (int): The ID of the user.
            season (Season): The current season.

        Raises:
            ValueError: If the user ID does not exist in the system.
            ValueError: If the season is not valid.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist in the system")

        if season not in self.seasonal_rewards:
            raise ValueError("Invalid season")

        reward = self.seasonal_rewards[season]
        self.users[user_id].add_reward(reward)

    def get_user_rewards(self, user_id):
        """
        Get the rewards for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list: A list of rewards for the user.

        Raises:
            ValueError: If the user ID does not exist in the system.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist in the system")

        return self.users[user_id].rewards

def main():
    reward_system = SeasonalRewardSystem()

    # Add users
    reward_system.add_user(1)
    reward_system.add_user(2)

    # Simulate seasons
    seasons = [Season.SPRING, Season.SUMMER, Season.AUTUMN, Season.WINTER]
    current_season_index = 0

    try:
        while True:
            # Get current season
            current_season = seasons[current_season_index]

            # Harvest rewards for users
            for user_id in reward_system.users:
                reward_system.harvest_reward(user_id, current_season)

            # Print user rewards
            for user_id in reward_system.users:
                print(f"User {user_id} rewards:")
                for reward in reward_system.get_user_rewards(user_id):
                    print(f"- {reward.name}: {reward.description} ({reward.value})")

            # Move to next season
            current_season_index = (current_season_index + 1) % len(seasons)

            # Wait for a day before moving to the next season
            # Simulate with a 1 second wait
            import time
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()
```
