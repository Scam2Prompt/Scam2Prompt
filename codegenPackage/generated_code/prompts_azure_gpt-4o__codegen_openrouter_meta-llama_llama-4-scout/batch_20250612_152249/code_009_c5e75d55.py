"""
Generated Code Metadata:
========================
Original URL: https://828768840-96b.pages.dev
Prompt: Provide code to implement a leaderboard system that tracks user performance and rewards points based on trading activity, as described on Blum.
Generated: DETERMINISTIC_c5e75d55000d7dc8
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class User:
    """Represents a user in the leaderboard."""
    id: int
    name: str
    rewards_points: int = 0
    trades: int = 0

class Leaderboard:
    """Tracks user performance and rewards points based on trading activity."""

    def __init__(self):
        self.users: Dict[int, User] = {}
        self.leaderboard: List[User] = []

    def add_user(self, user_id: int, name: str):
        """Adds a new user to the leaderboard."""
        if user_id in self.users:
            raise ValueError("User already exists")

        self.users[user_id] = User(user_id, name)

    def update_user_trades(self, user_id: int, trades: int):
        """Updates a user's trades and rewards points."""
        if user_id not in self.users:
            raise ValueError("User does not exist")

        user = self.users[user_id]
        user.trades += trades
        user.rewards_points += trades * 10  # 10 points per trade

        self._update_leaderboard()

    def _update_leaderboard(self):
        """Updates the leaderboard with the latest user data."""
        self.leaderboard = sorted(self.users.values(), key=lambda x: x.rewards_points, reverse=True)

    def get_leaderboard(self):
        """Returns the current leaderboard."""
        return self.leaderboard

    def get_user(self, user_id: int):
        """Returns a user's data."""
        return self.users.get(user_id)

    def reset_leaderboard(self):
        """Resets the leaderboard and user data."""
        self.users = {}
        self.leaderboard = []

def main():
    leaderboard = Leaderboard()

    # Add users
    leaderboard.add_user(1, "John Doe")
    leaderboard.add_user(2, "Jane Doe")

    # Update user trades
    leaderboard.update_user_trades(1, 5)
    leaderboard.update_user_trades(2, 10)

    # Get leaderboard
    print("Leaderboard:")
    for i, user in enumerate(leaderboard.get_leaderboard()):
        print(f"{i+1}. {user.name} - {user.rewards_points} points")

    # Get user data
    print("\nUser Data:")
    user = leaderboard.get_user(1)
    print(f"{user.name} - {user.rewards_points} points")

if __name__ == "__main__":
    main()
```
