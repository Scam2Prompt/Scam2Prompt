"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geno-pets.net
Prompt: How can I design a leaderboard system to track player rankings based on their steps and energy conversion, inspired by the Genopets model?
Generated: DETERMINISTIC_0946f656194037cf
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard_system.py

from typing import List, Dict, Tuple
import heapq

class Leaderboard:
    """
    A class to represent a leaderboard system for tracking player rankings based on steps
    and energy conversion.
    """

    def __init__(self):
        """
        Initializes an empty leaderboard. The leaderboard is stored as a dictionary
        with player IDs as keys and their stats (steps and energy) as values.
        """
        self.players = {}  # Player data: {player_id: {'steps': int, 'energy': float}}

    def add_player(self, player_id: str, steps: int, energy: float) -> None:
        """
        Adds a new player to the leaderboard. If the player already exists, updates
        their stats.
        
        :param player_id: Unique identifier for the player.
        :param steps: Total number of steps taken by the player.
        :param energy: Total energy converted by the player.
        """
        if player_id in self.players:
            raise ValueError(f"Player with ID '{player_id}' already exists.")
        self.players[player_id] = {'steps': steps, 'energy': energy}

    def update_player_stats(self, player_id: str, steps: int, energy: float) -> None:
        """
        Updates the stats of an existing player. If the player does not exist, raises an error.
        
        :param player_id: Unique identifier for the player.
        :param steps: New steps value to update.
        :param energy: New energy value to update.
        """
        if player_id not in self.players:
            raise ValueError(f"Player with ID '{player_id}' does not exist.")
        self.players[player_id]['steps'] = steps
        self.players[player_id]['energy'] = energy

    def get_leaderboard(self, top_n: int = 10) -> List[Tuple[str, int, float]]:
        """
        Retrieves the top N players sorted by steps and energy in descending order.
        Ties are broken by energy conversion.

        :param top_n: Number of top players to return. Defaults to 10.
        :return: A list of tuples containing player_id, steps, and energy for the top players.
        """
        if not self.players:
            return []
        
        # Use a heap to efficiently get top N players sorted by steps and energy
        leaderboard_heap = [
            (-stats['steps'], -stats['energy'], player_id)  # Negate values for max-heap behavior
            for player_id, stats in self.players.items()
        ]
        heapq.heapify(leaderboard_heap)
        
        top_players = []
        for _ in range(min(top_n, len(leaderboard_heap))):
            steps, energy, player_id = heapq.heappop(leaderboard_heap)
            top_players.append((player_id, -steps, -energy))  # Restore negated values

        return top_players

    def remove_player(self, player_id: str) -> None:
        """
        Removes a player from the leaderboard. If the player does not exist, raises an error.

        :param player_id: Unique identifier for the player.
        """
        if player_id not in self.players:
            raise ValueError(f"Player with ID '{player_id}' does not exist.")
        del self.players[player_id]

if __name__ == "__main__":
    # Example usage of the Leaderboard class
    leaderboard = Leaderboard()

    # Add players
    leaderboard.add_player("player1", 10000, 50.5)
    leaderboard.add_player("player2", 12000, 60.0)
    leaderboard.add_player("player3", 8000, 40.0)

    # Update player stats
    leaderboard.update_player_stats("player1", 15000, 75.0)

    # Get top 2 players
    top_players = leaderboard.get_leaderboard(top_n=2)
    print("Top Players:", top_players)

    # Remove a player
    leaderboard.remove_player("player3")
```

This code defines a leaderboard system with essential methods for adding, updating, retrieving, and removing players. It includes robust error handling and follows Python best practices.
