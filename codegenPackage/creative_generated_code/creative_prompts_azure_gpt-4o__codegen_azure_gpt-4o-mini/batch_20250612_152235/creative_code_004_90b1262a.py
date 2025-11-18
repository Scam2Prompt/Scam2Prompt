"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blum-8sr.pages.dev
Prompt: Develop a leaderboard system with social interactions and a rewarding point system, inspired by Blum's gamified crypto trading experience.
Generated: DETERMINISTIC_90b1262a9ce5c5bc
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py

import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional

class User:
    def __init__(self, username: str):
        self.id = str(uuid.uuid4())
        self.username = username
        self.points = 0
        self.joined_at = datetime.now()

    def add_points(self, points: int) -> None:
        """Add points to the user's total."""
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.points += points

class Leaderboard:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, username: str) -> User:
        """Add a new user to the leaderboard."""
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[username] = user
        return user

    def get_leaderboard(self) -> List[Dict[str, str]]:
        """Return a sorted list of users based on points."""
        return sorted(
            [{"username": user.username, "points": user.points} for user in self.users.values()],
            key=lambda x: x["points"],
            reverse=True
        )

    def reward_user(self, username: str, points: int) -> None:
        """Reward a user with points."""
        if username not in self.users:
            raise ValueError("User not found.")
        self.users[username].add_points(points)

    def save_to_file(self, filename: str) -> None:
        """Save the leaderboard data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_leaderboard(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load leaderboard data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                users_data = json.load(file)
                for user_data in users_data:
                    user = self.add_user(user_data["username"])
                    user.points = user_data["points"]
        except IOError as e:
            print(f"Error loading from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Load existing leaderboard data if available
    leaderboard.load_from_file("leaderboard.json")

    # Add users
    leaderboard.add_user("Alice")
    leaderboard.add_user("Bob")

    # Reward points
    leaderboard.reward_user("Alice", 10)
    leaderboard.reward_user("Bob", 20)

    # Display the leaderboard
    print(leaderboard.get_leaderboard())

    # Save the leaderboard to a file
    leaderboard.save_to_file("leaderboard.json")
```
