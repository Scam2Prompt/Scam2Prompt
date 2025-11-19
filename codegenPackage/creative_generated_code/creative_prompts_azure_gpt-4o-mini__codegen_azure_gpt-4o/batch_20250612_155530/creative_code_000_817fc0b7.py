"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayen.pages.dev
Prompt: How can I implement a points system for a gaming platform similar to KAYEN League, where users complete missions and earn rewards?
Generated: DETERMINISTIC_817fc0b7711ba647
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Points System for a Gaming Platform
# Language: Python

import json


class PointsSystem:
    """
    A class to manage the points system for a gaming platform.
    Users can complete missions, earn rewards, and track their points.
    """

    def __init__(self):
        """
        Initializes the points system with an empty user data dictionary.
        """
        self.user_data = {}

    def add_user(self, user_id: str):
        """
        Adds a new user to the system.

        Args:
            user_id (str): Unique identifier for the user.

        Raises:
            ValueError: If the user already exists.
        """
        if user_id in self.user_data:
            raise ValueError("User already exists.")
        self.user_data[user_id] = {"points": 0, "completed_missions": []}

    def complete_mission(self, user_id: str, mission_name: str, mission_points: int):
        """
        Updates user data when a mission is completed.

        Args:
            user_id (str): Unique identifier for the user.
            mission_name (str): Name of the completed mission.
            mission_points (int): Points earned from the mission.

        Raises:
            ValueError: If the user does not exist or the mission was already completed.
        """
        if user_id not in self.user_data:
            raise ValueError("User not found.")
        if mission_name in self.user_data[user_id]["completed_missions"]:
            raise ValueError("Mission already completed.")

        # Update user points and completed missions
        self.user_data[user_id]["points"] += mission_points
        self.user_data[user_id]["completed_missions"].append(mission_name)

    def get_user_points(self, user_id: str) -> int:
        """
        Retrieves the total points of a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            int: Total points of the user.

        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.user_data:
            raise ValueError("User not found.")
        return self.user_data[user_id]["points"]

    def save_data(self, filepath: str):
        """
        Saves the user data to a file in JSON format.

        Args:
            filepath (str): Path to the file where data will be saved.
        """
        with open(filepath, "w") as file:
            json.dump(self.user_data, file, indent=4)

    def load_data(self, filepath: str):
        """
        Loads user data from a JSON file.

        Args:
            filepath (str): Path to the file from which data will be loaded.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        try:
            with open(filepath, "r") as file:
                self.user_data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Data file not found.")

    def __str__(self):
        """
        Returns a string representation of the user data for debugging purposes.

        Returns:
            str: User data in JSON format.
        """
        return json.dumps(self.user_data, indent=4)


# Example Usage (Commented Out For Production)
# Uncomment to run in testing environments.

# points_system = PointsSystem()
# points_system.add_user("user123")
# points_system.complete_mission("user123", "Mission 1", 100)
# print(points_system.get_user_points("user123"))  # Output: 100
# points_system.save_data("user_data.json")
# points_system.load_data("user_data.json")
# print(points_system)
```
