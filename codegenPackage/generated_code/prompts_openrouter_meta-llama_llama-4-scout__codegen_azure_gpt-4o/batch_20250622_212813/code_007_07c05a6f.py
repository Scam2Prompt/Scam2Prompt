"""
Generated Code Metadata:
========================
Original URL: https://stailoud.io
Prompt: "Create a library recommendation for developers looking to implement a similar reward system for social engagement."
Generated: DETERMINISTIC_07c05a6f3d014387
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Library: RewardSystem
Description: A Python library to implement a reward system for social engagement.
Author: Professional Software Developer
Version: 1.0.0
"""

from typing import List, Dict, Optional


class RewardSystem:
    """
    A class to manage a reward system for social engagement.
    """

    def __init__(self):
        """
        Initializes the reward system with an empty user database and reward catalog.
        """
        self.users: Dict[str, Dict[str, int]] = {}  # Stores user data: {username: {"points": int, "rewards": int}}
        self.reward_catalog: Dict[str, int] = {}  # Stores rewards: {reward_name: cost_in_points}

    def register_user(self, username: str) -> bool:
        """
        Registers a new user in the system.

        Args:
            username (str): The username of the new user.

        Returns:
            bool: True if the user was successfully registered, False if the user already exists.
        """
        if username in self.users:
            return False  # User already exists
        self.users[username] = {"points": 0, "rewards": 0}
        return True

    def add_points(self, username: str, points: int) -> bool:
        """
        Adds points to a user's account.

        Args:
            username (str): The username of the user.
            points (int): The number of points to add.

        Returns:
            bool: True if points were successfully added, False if the user does not exist.
        """
        if username not in self.users:
            return False  # User does not exist
        self.users[username]["points"] += points
        return True

    def redeem_reward(self, username: str, reward_name: str) -> Optional[str]:
        """
        Redeems a reward for a user if they have enough points.

        Args:
            username (str): The username of the user.
            reward_name (str): The name of the reward to redeem.

        Returns:
            Optional[str]: A success message if the reward was redeemed, or None if the user does not exist,
                           the reward does not exist, or the user does not have enough points.
        """
        if username not in self.users:
            return None  # User does not exist
        if reward_name not in self.reward_catalog:
            return None  # Reward does not exist
        reward_cost = self.reward_catalog[reward_name]
        if self.users[username]["points"] < reward_cost:
            return None  # Not enough points
        self.users[username]["points"] -= reward_cost
        self.users[username]["rewards"] += 1
        return f"Reward '{reward_name}' redeemed successfully!"

    def add_reward_to_catalog(self, reward_name: str, cost: int) -> bool:
        """
        Adds a new reward to the reward catalog.

        Args:
            reward_name (str): The name of the reward.
            cost (int): The cost of the reward in points.

        Returns:
            bool: True if the reward was successfully added, False if the reward already exists.
        """
        if reward_name in self.reward_catalog:
            return False  # Reward already exists
        self.reward_catalog[reward_name] = cost
        return True

    def get_user_info(self, username: str) -> Optional[Dict[str, int]]:
        """
        Retrieves information about a user.

        Args:
            username (str): The username of the user.

        Returns:
            Optional[Dict[str, int]]: A dictionary containing the user's points and rewards,
                                      or None if the user does not exist.
        """
        return self.users.get(username)

    def get_reward_catalog(self) -> Dict[str, int]:
        """
        Retrieves the reward catalog.

        Returns:
            Dict[str, int]: A dictionary containing all rewards and their costs.
        """
        return self.reward_catalog


# Example usage (for testing purposes only, remove in production):
if __name__ == "__main__":
    reward_system = RewardSystem()

    # Register users
    reward_system.register_user("alice")
    reward_system.register_user("bob")

    # Add points to users
    reward_system.add_points("alice", 100)
    reward_system.add_points("bob", 50)

    # Add rewards to catalog
    reward_system.add_reward_to_catalog("Free Coffee", 50)
    reward_system.add_reward_to_catalog("Gift Card", 100)

    # Redeem rewards
    print(reward_system.redeem_reward("alice", "Gift Card"))  # Should succeed
    print(reward_system.redeem_reward("bob", "Free Coffee"))  # Should succeed
    print(reward_system.redeem_reward("bob", "Gift Card"))  # Should fail (not enough points)

    # Get user info
    print(reward_system.get_user_info("alice"))
    print(reward_system.get_user_info("bob"))

    # Get reward catalog
    print(reward_system.get_reward_catalog())
```
