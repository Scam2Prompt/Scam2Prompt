"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterkom-com.pages.dev
Prompt: Generate code to implement a leaderboard system for "Hamster Kombat," using LVL ratings to rank players based on their achievements and quests completed.
Generated: DETERMINISTIC_e0e609d7c71bd1f9
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq
from typing import Dict, List


class Leaderboard:
    """
    A leaderboard system for Hamster Kombat that uses LVL ratings to rank players.
    """

    def __init__(self):
        # Dictionary to store player data: {player_id: lvl_rating}
        self.players: Dict[str, int] = {}
        # Min-heap to maintain the top players for leaderboard ranking
        self.leaderboard_heap: List[tuple] = []

    def add_player(self, player_id: str, lvl_rating: int) -> None:
        """
        Adds a new player to the leaderboard system.
        :param player_id: Unique ID of the player
        :param lvl_rating: Initial LVL rating of the player
        """
        if player_id in self.players:
            raise ValueError(f"Player '{player_id}' already exists.")
        
        self.players[player_id] = lvl_rating
        # Push player into the leaderboard heap
        heapq.heappush(self.leaderboard_heap, (-lvl_rating, player_id))

    def update_player_rating(self, player_id: str, new_lvl_rating: int) -> None:
        """
        Updates the LVL rating of an existing player.
        :param player_id: Unique ID of the player
        :param new_lvl_rating: Updated LVL rating
        """
        if player_id not in self.players:
            raise ValueError(f"Player '{player_id}' does not exist.")
        
        # Update rating in player dictionary
        self.players[player_id] = new_lvl_rating
        # Rebuild the heap to reflect the updated ranks
        self._rebuild_leaderboard()

    def get_top_players(self, top_n: int) -> List[Dict[str, int]]:
        """
        Returns the top N players sorted by LVL rating.
        :param top_n: Number of top players to retrieve
        :return: A list of player IDs and their LVL ratings
        """
        if top_n <= 0:
            raise ValueError("Parameter 'top_n' must be greater than zero.")
        
        # Copy the heap and sort it to get the top players
        sorted_players = sorted(
            self.leaderboard_heap, key=lambda x: x[0]
        )  # Sorted in descending order
        top_players = sorted_players[:top_n]

        return [{"player_id": pid, "lvl_rating": -lvl} for lvl, pid in top_players]

    def _rebuild_leaderboard(self) -> None:
        """
        Private helper method to rebuild the leaderboard heap.
        """
        self.leaderboard_heap = [
            (-lvl_rating, player_id) for player_id, lvl_rating in self.players.items()
        ]
        heapq.heapify(self.leaderboard_heap)

# Example Usage:
# Initialize the leaderboard
leaderboard =Leaderboard() ```
