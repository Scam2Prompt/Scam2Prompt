"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibfgwbgr6vbhqeigt3olfaq2u4wzpjjilofgrjivnxebpy3giqh6u.ipfs.dweb.link
Prompt: Create a leaderboard system in Python for Blum's platform that tracks user interactions, rewarding points, and trading activity.
Generated: DETERMINISTIC_c40b7929ebf6a7c5
Batch ID: 20250612_152249
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
    """
    Leaderboard system to track user interactions, reward points, and trading activity.
    """

    def __init__(self):
        # Initialize the leaderboard dictionary to store user data.
        self.leaderboard: Dict[str, Dict[str, int]] = {}

    def add_user(self, username: str):
        """
        Adds a new user to the leaderboard.

        :param username: Name of the user
        """
        if username in self.leaderboard:
            raise ValueError(f"User '{username}' already exists.")
        self.leaderboard[username] = {"points": 0, "interactions": 0, "trades": 0}

    def record_interaction(self, username: str):
        """
        Records an interaction for a user and rewards 2 points.

        :param username: Name of the user
        """
        if username not in self.leaderboard:
            raise ValueError(f"User '{username}' does not exist.")
        self.leaderboard[username]["interactions"] += 1
        self.leaderboard[username]["points"] += 2

    def record_trade(self, username: str):
        """
        Records a trade for a user and rewards 5 points.

        :param username: Name of the user
        """
        if username not in self.leaderboard:
            raise ValueError(f"User '{username}' does not exist.")
        self.leaderboard[username]["trades"] += 1
        self.leaderboard[username]["points"] += 5

    def get_leaderboard(self) -> List[Dict[str, str]]:
        """
        Returns the leaderboard sorted by points in descending order.

        :return: List of dictionaries containing user data
        """
        return sorted(
            [{"username": user, **data} for user, data in self.leaderboard.items()],
            key=lambda x: x["points"],
            reverse=True,
        )

    def save_to_file(self, file_path: str):
        """
        Saves the leaderboard to a JSON file.

        :param file_path: Path to the file where leaderboard data will be saved
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.leaderboard, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Error saving to file: {e}")

    def load_from_file(self, file_path: str):
        """
        Loads the leaderboard data from a JSON file.

        :param file_path: Path to the file from which leaderboard data will be loaded
        """
        try:
            with open(file_path, "r") as file:
                self.leaderboard = json.load(file)
        except IOError as e:
            raise RuntimeError(f"Error loading from file: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Error decoding JSON: {e}")


if __name__ == "__main__":
    # Example usage:
    lb = Leaderboard()
    
    # Adding users
    lb.add_user("john_doe")
    lb.add_user("jane_smith")

    # Recording interactions and trades
    lb.record_interaction("john_doe")
    lb.record_trade("john_doe")
    lb.record_interaction("jane_smith")
    lb.record_trade("jane_smith")
    lb.record_trade("jane_smith")

    # Display leaderboard
    print("Leaderboard:")
    for entry in lb.get_leaderboard():
        print(entry)

    # Save leaderboard to file
    lb.save_to_file("leaderboard.json")

    # Load leaderboard from file
    lb.load_from_file("leaderboard.json")
    print("Leaderboard after reloading from file:")
    for entry in lb.get_leaderboard():
        print(entry)
```
