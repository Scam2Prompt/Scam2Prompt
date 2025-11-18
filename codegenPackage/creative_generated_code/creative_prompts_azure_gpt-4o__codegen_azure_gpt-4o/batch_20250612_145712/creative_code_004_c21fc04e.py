"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerinde.com
Prompt: Implement a leaderboard system in Python that tracks the top players based on their coin earnings, as described in the "Die besten Spieler" section of the TG WebApp Euro Verdienen webpage.
Generated: DETERMINISTIC_c21fc04e175e82a8
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq


class Leaderboard:
    """
    A class representing a leaderboard system based on players' coin earnings.
    """

    def __init__(self, max_size=10):
        """
        Initialize the leaderboard.

        :param max_size: The maximum number of top players to track.
        """
        self.max_size = max_size  # Maximum number of entries in the leaderboard
        self.board = []  # Min-heap to store player scores
        self.player_data = {}  # Dictionary to store all players' scores for quick lookup

    def add_player(self, player_id, coins):
        """
        Add a new player or update an existing player's coin earnings.

        :param player_id: Unique identifier for the player.
        :param coins: Number of coins the player has earned.
        """
        if coins < 0:
            raise ValueError("Coin earnings cannot be negative.")

        # Update player data
        if player_id in self.player_data:
            self.player_data[player_id] += coins
        else:
            self.player_data[player_id] = coins

        # Update the leaderboard only if the player qualifies
        self._update_leaderboard(player_id)

    def _update_leaderboard(self, player_id):
        """
        Internal method to update the leaderboard based on a player's new score.

        :param player_id: Unique identifier for the player whose score has been updated.
        """
        coins = self.player_data[player_id]

        # Check if player is already in the leaderboard
        for entry in self.board:
            if entry[1] == player_id:
                # Update the entry and rebuild the heap
                entry[0] = coins
                heapq.heapify(self.board)
                return

        # If not in leaderboard, check if they qualify
        if len(self.board) < self.max_size or coins > self.board[0][0]:
            # Add new entry to leaderboard
            heapq.heappush(self.board, [coins, player_id])

            # Maintain the max_size constraint
            if len(self.board) > self.max_size:
                heapq.heappop(self.board)

    def get_top_players(self):
        """
        Retrieve the current top players sorted by coin earnings.

        :return: List of tuples (player_id, coins) sorted by highest earnings.
        """
        # Sort leaderboard entries by coins in descending order
        return sorted([(player_id, coins) for coins, player_id in self.board], key=lambda x: x[1], reverse=True)

    def get_player_score(self, player_id):
        """
        Get the coin earnings for a specific player.

        :param player_id: Unique identifier for the player.
        :return: Number of coins the player has earned, or None if the player does not exist.
        """
        return self.player_data.get(player_id, None)


# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard(max_size=5)

    # Add players and their earnings
    leaderboard.add_player("Player1", 100)
    leaderboard.add_player("Player2", 200)
    leaderboard.add_player("Player3", 150)
    leaderboard.add_player("Player4", 250)
    leaderboard.add_player("Player5", 300)
    leaderboard.add_player("Player6", 50)

    # Get top players
    print("Leaderboard:")
    for player_id, score in leaderboard.get_top_players():
        print(f"{player_id}: {score} coins")

    # Retrieve specific player score
    player_id = "Player3"
    print(f"\nScore for {player_id}: {leaderboard.get_player_score(player_id)} coins")
```
