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
"""
Leaderboard System for Community Engagement

This script implements a leaderboard system where users earn points for participation 
and voting in governance activities. It includes features for adding points to users,
retrieving the leaderboard, and error handling for invalid operations.
"""

from typing import Dict, List, Tuple

class Leaderboard:
    def __init__(self):
        """
        Initialize the leaderboard with an empty dictionary to store user data.
        """
        self.user_points: Dict[str, int] = {}

    def add_points(self, user: str, points: int) -> None:
        """
        Add points to a user. Creates a new entry if the user does not exist.

        :param user: The username of the individual.
        :param points: The number of points to add (must be positive).
        :raises ValueError: If the points are not positive.
        """
        if points <= 0:
            raise ValueError("Points must be a positive integer.")
        
        if user in self.user_points:
            self.user_points[user] += points
        else:
            self.user_points[user] = points

    def get_leaderboard(self, top_n: int = 10) -> List[Tuple[str, int]]:
        """
        Retrieve the leaderboard sorted by points in descending order.

        :param top_n: The number of top users to retrieve (default is 10).
        :return: A list of tuples containing usernames and their respective points.
        """
        sorted_users = sorted(self.user_points.items(), key=lambda x: x[1], reverse=True)
        return sorted_users[:top_n]

    def get_user_points(self, user: str) -> int:
        """
        Retrieve the current points for a specific user.

        :param user: The username of the individual.
        :return: The number of points the user has.
        :raises KeyError: If the user does not exist in the leaderboard.
        """
        if user not in self.user_points:
            raise KeyError(f"User '{user}' does not exist in the leaderboard.")
        return self.user_points[user]

    def reset_points(self, user: str) -> None:
        """
        Reset the points for a specific user.

        :param user: The username of the individual.
        :raises KeyError: If the user does not exist in the leaderboard.
        """
        if user not in self.user_points:
            raise KeyError(f"User '{user}' does not exist in the leaderboard.")
        self.user_points[user] = 0

# Example usage (for testing purposes):
if __name__ == "__main__":
    leaderboard = Leaderboard()
    try:
        leaderboard.add_points("Alice", 50)
        leaderboard.add_points("Bob", 75)
        leaderboard.add_points("Charlie", 35)
        leaderboard.add_points("Alice", 25)  # Add more points to an existing user
        
        print("Leaderboard:", leaderboard.get_leaderboard())
        print("Alice's Points:", leaderboard.get_user_points("Alice"))
        
        leaderboard.reset_points("Charlie")
        print("Leaderboard After Reset:", leaderboard.get_leaderboard())
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
