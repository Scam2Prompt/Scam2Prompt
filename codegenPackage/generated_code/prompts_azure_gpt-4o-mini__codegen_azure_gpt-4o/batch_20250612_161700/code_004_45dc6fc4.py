"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Provide an example of how to implement a leaderboard feature in a game that tracks user earnings and ranks players based on their trading performance in Meme Moguls.
Generated: DETERMINISTIC_45dc6fc44d83e218
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

from typing import List, Dict, Tuple
import heapq

class Leaderboard:
    """
    A class to manage a leaderboard for tracking user earnings and ranking players
    based on their trading performance in Meme Moguls.
    """

    def __init__(self):
        # Dictionary to store user earnings: {user_id: earnings}
        self.user_earnings = {}

    def update_earnings(self, user_id: str, earnings: float) -> None:
        """
        Updates the earnings of a user. If the user does not exist, they are added to the leaderboard.

        :param user_id: The unique identifier of the user
        :param earnings: The earnings to be added to the user's total
        """
        if user_id in self.user_earnings:
            self.user_earnings[user_id] += earnings
        else:
            self.user_earnings[user_id] = earnings

    def get_top_players(self, top_n: int) -> List[Tuple[str, float]]:
        """
        Retrieves the top N players based on their earnings.

        :param top_n: The number of top players to retrieve
        :return: A list of tuples containing user_id and earnings, sorted by earnings in descending order
        """
        if top_n <= 0:
            return []

        # Use a heap to efficiently get the top N players
        top_players = heapq.nlargest(top_n, self.user_earnings.items(), key=lambda x: x[1])
        return top_players

    def get_user_rank(self, user_id: str) -> int:
        """
        Retrieves the rank of a specific user based on their earnings.

        :param user_id: The unique identifier of the user
        :return: The rank of the user (1-based), or -1 if the user is not on the leaderboard
        """
        if user_id not in self.user_earnings:
            return -1

        # Sort all users by earnings in descending order
        sorted_users = sorted(self.user_earnings.items(), key=lambda x: x[1], reverse=True)
        for rank, (uid, _) in enumerate(sorted_users, start=1):
            if uid == user_id:
                return rank

        return -1  # Should not reach here

    def reset_leaderboard(self) -> None:
        """
        Resets the leaderboard by clearing all user earnings.
        """
        self.user_earnings.clear()


# Example usage
if __name__ == "__main__":
    # Initialize the leaderboard
    leaderboard = Leaderboard()

    # Update earnings for users
    leaderboard.update_earnings("user1", 1500.0)
    leaderboard.update_earnings("user2", 3000.0)
    leaderboard.update_earnings("user3", 2000.0)
    leaderboard.update_earnings("user1", 500.0)  # Increment user1's earnings

    # Get the top 2 players
    top_players = leaderboard.get_top_players(2)
    print("Top 2 Players:", top_players)

    # Get the rank of a specific user
    user_rank = leaderboard.get_user_rank("user1")
    print("Rank of user1:", user_rank)

    # Reset the leaderboard
    leaderboard.reset_leaderboard()
    print("Leaderboard after reset:", leaderboard.user_earnings)
```
