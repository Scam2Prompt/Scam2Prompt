"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-en.pages.dev
Prompt: Implement a leaderboard system in Python that tracks and ranks Meme Moguls players based on their earnings and trading activity, using the wealth leaderboard feature described on the site.
Generated: DETERMINISTIC_9d96a26a40996936
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq
from typing import List, Tuple

class Leaderboard:
    """
    A class to manage and track the leaderboard for Meme Moguls players
    based on their earnings and trading activity.
    """
    
    def __init__(self):
        """
        Initializes the leaderboard with an empty list for players.
        Uses a min-heap for efficient ranking.
        """
        self.players = []  # Min-heap to store players as tuples (-earnings, player_name)

    def add_player(self, player_name: str, earnings: float):
        """
        Adds a new player to the leaderboard with their current earnings.

        :param player_name: Name of the player.
        :param earnings: Player's earnings (positive number).
        """
        if earnings < 0:
            raise ValueError("Earnings must be a positive number.")
        heapq.heappush(self.players, (-earnings, player_name))  # Use negative earnings to simulate max-heap

    def update_earnings(self, player_name: str, new_earnings: float):
        """
        Updates the earnings for an existing player.
        If the player doesn't exist, raises a ValueError.

        :param player_name: Name of the player.
        :param new_earnings: Updated earnings (positive number).
        """
        if new_earnings < 0:
            raise ValueError("New earnings must be a positive number.")
        
        # Find and update the player's earnings
        found = False
        for i, (neg_earnings, name) in enumerate(self.players):
            if name == player_name:
                found = True
                self.players[i] = (-new_earnings, player_name)
                break
        
        if not found:
            raise ValueError(f"Player '{player_name}' not found in the leaderboard.")
        
        # Re-heapify after updating
        heapq.heapify(self.players)

    def get_top_players(self, top_n: int) -> List[Tuple[str, float]]:
        """
        Retrieves the top N players sorted by their earnings.

        :param top_n: Number of top players to retrieve.
        :return: List of tuples containing player names and their earnings.
        """
        if top_n <= 0:
            raise ValueError("The number of top players must be greater than zero.")
        
        # Get the top N players using heapq.nlargest
        top_players = heapq.nlargest(top_n, self.players)
        return [(name, -neg_earnings) for neg_earnings, name in top_players]

    def remove_player(self, player_name: str):
        """
        Removes a player from the leaderboard. If the player doesn't exist, raises a ValueError.

        :param player_name: Name of the player to remove.
        """
        found = False
        for i, (neg_earnings, name) in enumerate(self.players):
            if name == player_name:
                found = True
                del self.players[i]
                break
        
        if not found:
            raise ValueError(f"Player '{player_name}' not found in the leaderboard.")
        
        # Re-heapify after removing a player
        heapq.heapify(self.players)

    def display_leaderboard(self) -> List[Tuple[str, float]]:
        """
        Displays the leaderboard sorted by player earnings.

        :return: List of tuples containing player names and their earnings.
        """
        # Sort by earnings in descending order
        return sorted([(name, -neg_earnings) for neg_earnings, name in self.players], key=lambda x: x[1], reverse=True)

# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Add players
    leaderboard.add_player("Alice", 5000)
    leaderboard.add_player("Bob", 3000)
    leaderboard.add_player("Charlie", 7000)

    # Display leaderboard
    print("Leaderboard:", leaderboard.display_leaderboard())

    # Update earnings
    leaderboard.update_earnings("Bob", 8000)

    # Get top 2 players
    print("Top 2 Players:", leaderboard.get_top_players(2))

    # Remove a player
    leaderboard.remove_player("Alice")

    # Display updated leaderboard
    print("Updated Leaderboard:", leaderboard.display_leaderboard())
```
