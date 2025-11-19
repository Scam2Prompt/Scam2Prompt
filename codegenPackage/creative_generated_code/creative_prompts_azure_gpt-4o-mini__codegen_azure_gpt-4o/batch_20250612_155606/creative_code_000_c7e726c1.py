"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayenferno.pages.dev
Prompt: How can I implement a leaderboard system for the KAYEN League that tracks user points and ranks based on mission completions?
Generated: DETERMINISTIC_c7e726c1f1d43b8d
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Leaderboard:
    def __init__(self):
        """
        Initialize the leaderboard with an empty data structure.
        The data structure stores user_id, name, and points.
        """
        self.leaderboard_data: List[Dict] = []

    def add_user(self, user_id: str, name: str):
        """
        Add a new user to the leaderboard.
        :param user_id: Unique identifier for the user.
        :param name: Name of the user.
        """
        # Check if user already exists
        if any(user['user_id'] == user_id for user in self.leaderboard_data):
            raise ValueError(f"User with ID {user_id} already exists.")

        # Add new user with default 0 points
        self.leaderboard_data.append({
            'user_id': user_id,
            'name': name,
            'points': 0
        })

    def update_points(self, user_id: str, points: int):
        """
        Update the points for a specific user.
        :param user_id: Unique identifier for the user.
        :param points: Points to be added (can be positive or negative).
        """
        for user in self.leaderboard_data:
            if user['user_id'] == user_id:
                user['points'] += points
                return

        raise ValueError(f"User with ID {user_id} not found.")

    def get_rankings(self) -> List[Dict]:
        """
        Retrieve the leaderboard rankings sorted by points in descending order.
        :return: List of users sorted by rank.
        """
        # Sort users by points, descending
        return sorted(self.leaderboard_data, key=lambda x: x['points'], reverse=True)

    def save_to_file(self, file_path: str):
        """
        Save the leaderboard data to a file in JSON format.
        :param file_path: Path to the file where data will be stored.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.leaderboard_data, file, indent=4)
        except Exception as e:
            raise IOError(f"Error saving to file: {e}")

    def load_from_file(self, file_path: str):
        """
        Load leaderboard data from a JSON file.
        :param file_path: Path to the file to be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.leaderboard_data = json.load(file)
                # Validate that loaded data is in correct format
                if not all(isinstance(user, dict) and 'user_id' in user and 'name' in user and 'points' in user
                           for user in self.leaderboard_data):
                    raise ValueError("Invalid data format in file.")
        except Exception as e:
            raise IOError(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        leaderboard = Leaderboard()
        leaderboard.add_user("u1", "Alice")
        leaderboard.add_user("u2", "Bob")
        leaderboard.update_points("u1", 50)
        leaderboard.update_points("u2", 30)
        leaderboard.update_points("u1", 20)

        print("Current Rankings:")
        for rank, user in enumerate(leaderboard.get_rankings(), start=1):
            print(f"Rank {rank}: {user['name']} - {user['points']} points")

        # Save and reload leaderboard data
        leaderboard.save_to_file("leaderboard.json")
        leaderboard.load_from_file("leaderboard.json")
    except Exception as e:
        print(f"Error: {e}")
```
