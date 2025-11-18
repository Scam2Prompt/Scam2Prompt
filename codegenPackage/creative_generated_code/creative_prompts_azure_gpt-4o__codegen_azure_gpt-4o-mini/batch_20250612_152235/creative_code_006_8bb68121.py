"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Develop a leaderboard system for tracking user points in the XSwap ecosystem, referencing the features mentioned on the webpage.
Generated: DETERMINISTIC_8bb68121877dbb7e
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List, Optional

class Leaderboard:
    """
    A class to represent a leaderboard for tracking user points in the XSwap ecosystem.
    """

    def __init__(self):
        """
        Initializes the leaderboard with an empty dictionary to store user points.
        """
        self.scores: Dict[str, int] = {}

    def add_user(self, username: str) -> None:
        """
        Adds a new user to the leaderboard with an initial score of 0.

        :param username: The username of the user to add
        :raises ValueError: If the username already exists
        """
        if username in self.scores:
            raise ValueError(f"User '{username}' already exists.")
        self.scores[username] = 0

    def update_points(self, username: str, points: int) -> None:
        """
        Updates the points for the specified user.

        :param username: The username of the user whose points will be updated
        :param points: The number of points to add (can be negative)
        :raises KeyError: If the user does not exist
        :raises ValueError: If points are invalid
        """
        if username not in self.scores:
            raise KeyError(f"User '{username}' does not exist.")
        if not isinstance(points, int):
            raise ValueError("Points must be an integer.")
        self.scores[username] += points

    def get_leaderboard(self) -> List[Dict[str, int]]:
        """
        Returns a sorted leaderboard of users by their scores.

        :return: A list of dictionaries containing usernames and their scores, sorted by score
        """
        return [{"username": user, "points": points} for user, points in sorted(self.scores.items(), key=lambda item: item[1], reverse=True)]

    def save_to_file(self, filename: str) -> None:
        """
        Saves the leaderboard data to a JSON file.

        :param filename: The name of the file to save leaderboard data
        :raises IOError: If there is an error writing to the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.scores, file)
        except IOError as e:
            raise IOError(f"An error occurred while saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Loads leaderboard data from a JSON file.

        :param filename: The name of the file to load leaderboard data from
        :raises IOError: If there is an error reading the file
        :raises json.JSONDecodeError: If the file does not contain valid JSON
        """
        try:
            with open(filename, 'r') as file:
                self.scores = json.load(file)
        except IOError as e:
            raise IOError(f"An error occurred while loading from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to decode JSON from the file: {e}")

# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Add users
    leaderboard.add_user("Alice")
    leaderboard.add_user("Bob")

    # Update points
    leaderboard.update_points("Alice", 10)
    leaderboard.update_points("Bob", 5)

    # Print the leaderboard
    print("Leaderboard:", leaderboard.get_leaderboard())

    # Save to file
    leaderboard.save_to_file("leaderboard.json")

    # Load from file
    new_leaderboard = Leaderboard()
    new_leaderboard.load_from_file("leaderboard.json")
    print("Loaded Leaderboard:", new_leaderboard.get_leaderboard())
```
