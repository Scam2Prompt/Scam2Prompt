"""
Generated Code Metadata:
========================
Original URL: https://pioneerparticle-sigma.vercel.app
Prompt: Create a leaderboard implementation for a points-based system similar to Particle Pioneer's Points Booster Leaderboard.
Generated: DETERMINISTIC_07a8271d52822003
Batch ID: 20250622_211048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

import heapq
from typing import List, Dict, Tuple

class Leaderboard:
    """
    A class to manage a points-based leaderboard system.
    """

    def __init__(self):
        """
        Initializes the leaderboard with an empty dictionary to store user points.
        """
        self.scores = {}  # Dictionary to store user scores {user_id: points}

    def add_points(self, user_id: str, points: int) -> None:
        """
        Adds points to a user's total score. If the user does not exist, they are added to the leaderboard.

        :param user_id: The unique identifier for the user.
        :param points: The number of points to add to the user's score.
        """
        if user_id in self.scores:
            self.scores[user_id] += points
        else:
            self.scores[user_id] = points

    def reset_points(self, user_id: str) -> None:
        """
        Resets a user's points to zero. If the user does not exist, no action is taken.

        :param user_id: The unique identifier for the user.
        """
        if user_id in self.scores:
            self.scores[user_id] = 0

    def get_top_users(self, n: int) -> List[Tuple[str, int]]:
        """
        Retrieves the top N users based on their scores.

        :param n: The number of top users to retrieve.
        :return: A list of tuples containing user IDs and their scores, sorted in descending order.
        """
        # Use a heap to efficiently get the top N users
        return heapq.nlargest(n, self.scores.items(), key=lambda x: x[1])

    def get_user_score(self, user_id: str) -> int:
        """
        Retrieves the score of a specific user.

        :param user_id: The unique identifier for the user.
        :return: The user's score. Returns 0 if the user does not exist.
        """
        return self.scores.get(user_id, 0)

# Example usage
if __name__ == "__main__":
    try:
        leaderboard = Leaderboard()

        # Adding points to users
        leaderboard.add_points("user1", 100)
        leaderboard.add_points("user2", 200)
        leaderboard.add_points("user3", 150)

        # Resetting points for a user
        leaderboard.reset_points("user1")

        # Fetching top users
        top_users = leaderboard.get_top_users(2)
        print("Top Users:", top_users)

        # Fetching individual user score
        user_score = leaderboard.get_user_score("user2")
        print("User2 Score:", user_score)

    except Exception as e:
        print(f"An error occurred: {e}")
```
