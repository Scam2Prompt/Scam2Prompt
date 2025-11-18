"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundaktion.org
Prompt: Write code to implement a leaderboard system for community engagement, where users earn points for voting and participation in governance, inspired by the Ondo DAO.
Generated: DETERMINISTIC_f7f9a5a62be6358a
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py

from typing import Dict, List, Optional

class User:
    """
    Represents a user in the leaderboard system.
    """
    def __init__(self, username: str):
        self.username = username
        self.points = 0

    def add_points(self, points: int) -> None:
        """
        Adds points to the user.
        
        :param points: The number of points to add.
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.points += points

    def __str__(self) -> str:
        return f"{self.username}: {self.points} points"


class Leaderboard:
    """
    Manages the leaderboard for community engagement.
    """
    def __init__(self):
        self.users: Dict[str, User] = {}

    def register_user(self, username: str) -> None:
        """
        Registers a new user in the leaderboard.

        :param username: The username of the new user.
        :raises ValueError: If the username already exists.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username)

    def record_participation(self, username: str, points: int) -> None:
        """
        Records a user's participation and awards points.

        :param username: The username of the user.
        :param points: The number of points to award.
        :raises ValueError: If the user does not exist or points are negative.
        """
        if username not in self.users:
            raise ValueError("User not found.")
        self.users[username].add_points(points)

    def get_leaderboard(self) -> List[str]:
        """
        Returns the leaderboard sorted by points in descending order.

        :return: A list of strings representing the leaderboard.
        """
        sorted_users = sorted(self.users.values(), key=lambda user: user.points, reverse=True)
        return [str(user) for user in sorted_users]

    def reset_points(self) -> None:
        """
        Resets points for all users to zero.
        """
        for user in self.users.values():
            user.points = 0


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Register users
    try:
        leaderboard.register_user("Alice")
        leaderboard.register_user("Bob")
        leaderboard.register_user("Charlie")
        
        # Record participation
        leaderboard.record_participation("Alice", 10)
        leaderboard.record_participation("Bob", 5)
        leaderboard.record_participation("Charlie", 8)
        
        # Print leaderboard
        print("Current Leaderboard:")
        print("\n".join(leaderboard.get_leaderboard()))
        
        # Reset points for a new round
        leaderboard.reset_points()
    except ValueError as e:
        print(f"Error: {e}")
```
This code implements a basic leaderboard system for a community engagement application, allowing users to earn points for their participation. It includes error handling for common edge cases, such as duplicate usernames and negative point values.
