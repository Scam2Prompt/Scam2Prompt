"""
Generated Code Metadata:
========================
Original URL: https://nft-stores.web.app
Prompt: Write code to implement dynamic rewards based on user level status, similar to the "Sign In to see your level status" functionality described on the site.
Generated: DETERMINISTIC_e6a81d5bf2c78378
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_level_rewards.py

class UserLevelRewards:
    """
    A class to manage dynamic rewards based on user level status.
    """

    def __init__(self, levels):
        """
        Initialize the UserLevelRewards class.

        Args:
            levels (list): A list of dictionaries containing level information.
                Each dictionary should have the following keys:
                    - 'level' (int): The level number.
                    - 'min_xp' (int): The minimum XP required for the level.
                    - 'max_xp' (int): The maximum XP required for the level.
                    - 'reward' (int): The reward for the level.
        """
        self.levels = levels

    def get_user_level(self, user_xp):
        """
        Get the user's level based on their XP.

        Args:
            user_xp (int): The user's current XP.

        Returns:
            dict: The user's level information, or None if not found.
        """
        for level in self.levels:
            if level['min_xp'] <= user_xp <= level['max_xp']:
                return level
        return None

    def get_user_reward(self, user_xp):
        """
        Get the user's reward based on their XP.

        Args:
            user_xp (int): The user's current XP.

        Returns:
            int: The user's reward, or 0 if not found.
        """
        user_level = self.get_user_level(user_xp)
        if user_level:
            return user_level['reward']
        return 0

    def update_user_xp(self, user_xp, new_xp):
        """
        Update the user's XP and return their new level and reward.

        Args:
            user_xp (int): The user's current XP.
            new_xp (int): The user's new XP.

        Returns:
            tuple: A tuple containing the user's new level and reward.
        """
        if new_xp < 0:
            raise ValueError("XP cannot be negative")

        new_level = self.get_user_level(new_xp)
        new_reward = self.get_user_reward(new_xp)

        return new_level, new_reward


# Example usage:
if __name__ == "__main__":
    levels = [
        {'level': 1, 'min_xp': 0, 'max_xp': 100, 'reward': 10},
        {'level': 2, 'min_xp': 101, 'max_xp': 500, 'reward': 50},
        {'level': 3, 'min_xp': 501, 'max_xp': 1000, 'reward': 100},
    ]

    rewards = UserLevelRewards(levels)

    user_xp = 250
    user_level = rewards.get_user_level(user_xp)
    user_reward = rewards.get_user_reward(user_xp)

    print(f"User Level: {user_level['level']}")
    print(f"User Reward: {user_reward}")

    new_xp = 750
    new_level, new_reward = rewards.update_user_xp(user_xp, new_xp)

    print(f"New User Level: {new_level['level']}")
    print(f"New User Reward: {new_reward}")
```
