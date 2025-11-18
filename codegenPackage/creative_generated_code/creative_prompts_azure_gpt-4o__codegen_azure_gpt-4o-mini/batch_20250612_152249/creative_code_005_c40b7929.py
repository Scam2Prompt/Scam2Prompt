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
from typing import Dict, List, Optional

class User:
    """Represents a user in the leaderboard system."""
    
    def __init__(self, username: str):
        self.username = username
        self.points = 0
        self.trading_activity = 0

    def add_points(self, points: int):
        """Add points to the user's score."""
        if points < 0:
            raise ValueError("Points must be non-negative.")
        self.points += points

    def add_trading_activity(self):
        """Increment the trading activity count for the user."""
        self.trading_activity += 1

    def to_dict(self) -> Dict[str, int]:
        """Return the user data as a dictionary."""
        return {
            "username": self.username,
            "points": self.points,
            "trading_activity": self.trading_activity
        }


class Leaderboard:
    """Manages the leaderboard for tracking user interactions and trading activity."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, username: str):
        """Add a new user to the leaderboard."""
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        self.users[username] = User(username)

    def record_interaction(self, username: str, points: int):
        """Record a user interaction and update points."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        self.users[username].add_points(points)

    def record_trading_activity(self, username: str):
        """Record trading activity for a user."""
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        self.users[username].add_trading_activity()

    def get_leaderboard(self) -> List[Dict[str, int]]:
        """Return the leaderboard sorted by points."""
        return sorted(
            (user.to_dict() for user in self.users.values()),
            key=lambda x: x['points'],
            reverse=True
        )

    def save_leaderboard(self, filename: str):
        """Save the current leaderboard to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_leaderboard(), f, indent=4)
        except IOError as e:
            raise Exception(f"Failed to save leaderboard: {e}")

    def load_leaderboard(self, filename: str):
        """Load the leaderboard from a JSON file."""
        try:
            with open(filename, 'r') as f:
                users_data = json.load(f)
                for user_data in users_data:
                    self.add_user(user_data['username'])
                    self.users[user_data['username']].points = user_data['points']
                    self.users[user_data['username']].trading_activity = user_data['trading_activity']
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Failed to load leaderboard: {e}")

# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Add users and record interactions
    leaderboard.add_user("Alice")
    leaderboard.record_interaction("Alice", 10)
    leaderboard.record_trading_activity("Alice")

    leaderboard.add_user("Bob")
    leaderboard.record_interaction("Bob", 20)
    leaderboard.record_trading_activity("Bob")

    # Display leaderboard
    print(leaderboard.get_leaderboard())

    # Save to file
    leaderboard.save_leaderboard("leaderboard.json")

    # Load from file
    new_leaderboard = Leaderboard()
    new_leaderboard.load_leaderboard("leaderboard.json")
    print(new_leaderboard.get_leaderboard())
```
