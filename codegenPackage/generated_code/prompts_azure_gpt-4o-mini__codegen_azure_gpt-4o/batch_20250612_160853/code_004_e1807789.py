"""
Generated Code Metadata:
========================
Original URL: https://bafybeigxwcw7uni73ly72bulz2bdagorb5yw5fvcytvcs7fe4kpuc5nzla.ipfs.dweb.link
Prompt: Illustrate how to implement a rewards system for users in the Pudgy Penguins virtual home using a specific programming language.
Generated: DETERMINISTIC_e1807789c583e1ac
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Rewards System for Pudgy Penguins Virtual Home

This script implements a rewards system for users in the Pudgy Penguins virtual home.
Users can earn points based on their activities, and redeem rewards when they reach certain thresholds.
"""

import json

class RewardsSystem:
    def __init__(self):
        """
        Initialize the rewards system with an empty user database and predefined rewards.
        """
        self.users = {}  # Dictionary to store user data
        self.rewards = {
            100: "Bronze Badge",
            500: "Silver Badge",
            1000: "Gold Badge",
            5000: "Platinum Badge"
        }  # Predefined rewards based on points

    def add_user(self, user_id, username):
        """
        Add a new user to the rewards system.

        :param user_id: Unique identifier for the user
        :param username: Username of the user
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = {"username": username, "points": 0, "rewards": []}

    def add_points(self, user_id, points):
        """
        Add points to a user's account.

        :param user_id: Unique identifier for the user
        :param points: Number of points to add
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        if points < 0:
            raise ValueError("Points must be a positive value.")
        
        self.users[user_id]["points"] += points
        self._check_rewards(user_id)

    def _check_rewards(self, user_id):
        """
        Check if the user qualifies for any new rewards based on their points.

        :param user_id: Unique identifier for the user
        """
        user_points = self.users[user_id]["points"]
        for threshold, reward in self.rewards.items():
            if user_points >= threshold and reward not in self.users[user_id]["rewards"]:
                self.users[user_id]["rewards"].append(reward)

    def get_user_info(self, user_id):
        """
        Retrieve information about a user.

        :param user_id: Unique identifier for the user
        :return: Dictionary containing user information
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        return self.users[user_id]

    def save_data(self, file_path):
        """
        Save the user data to a JSON file.

        :param file_path: Path to the file where data will be saved
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.users, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save data: {e}")

    def load_data(self, file_path):
        """
        Load user data from a JSON file.

        :param file_path: Path to the file from which data will be loaded
        """
        try:
            with open(file_path, "r") as file:
                self.users = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load data: {e}")


# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()

    # Add users
    rewards_system.add_user(user_id=1, username="PenguinLover")
    rewards_system.add_user(user_id=2, username="IceExplorer")

    # Add points
    rewards_system.add_points(user_id=1, points=150)
    rewards_system.add_points(user_id=2, points=600)

    # Get user info
    print(rewards_system.get_user_info(user_id=1))
    print(rewards_system.get_user_info(user_id=2))

    # Save and load data
    rewards_system.save_data("rewards_data.json")
    rewards_system.load_data("rewards_data.json")
```
