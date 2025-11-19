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
import json
from collections import defaultdict
from typing import Dict, List, Tuple
import os
import time

class Leaderboard:
    """
    A class to manage a points-based leaderboard system.
    Supports adding points, retrieving top players, and saving/loading data.
    """
    
    def __init__(self, storage_file: str = "leaderboard.json"):
        """
        Initialize the leaderboard with optional file storage.
        
        Args:
            storage_file: Path to JSON file for persistent storage
        """
        self.storage_file = storage_file
        self.leaderboard: Dict[str, int] = defaultdict(int)
        self._load_data()

    def add_points(self, player_id: str, points: int) -> None:
        """
        Add points to a player's total.
        
        Args:
            player_id: Unique identifier for the player
            points: Points to add (can be negative)
        """
        if not isinstance(points, int):
            raise ValueError("Points must be an integer")
            
        self.leaderboard[player_id] += points
        self._save_data()

    def get_top_players(self, limit: int = 10) -> List[Tuple[str, int]]:
        """
        Get the top players by points.
        
        Args:
            limit: Number of top players to return
            
        Returns:
            List of tuples (player_id, points) sorted descending by points
        """
        if limit <= 0:
            return []
            
        sorted_players = sorted(
            self.leaderboard.items(),
            key=lambda item: item[1],
            reverse=True
        )
        return sorted_players[:limit]

    def get_player_rank(self, player_id: str) -> int:
        """
        Get a player's rank (1-based index).
        
        Args:
            player_id: Player to check
            
        Returns:
            Rank (1 = first place) or -1 if player not found
        """
        if player_id not in self.leaderboard:
            return -1
            
        sorted_players = sorted(
            self.leaderboard.items(),
            key=lambda item: item[1],
            reverse=True
        )
        
        for rank, (pid, _) in enumerate(sorted_players, 1):
            if pid == player_id:
                return rank
        return -1

    def reset_leaderboard(self) -> None:
        """Reset all player points to zero."""
        self.leaderboard.clear()
        self._save_data()

    def _save_data(self) -> None:
        """Save leaderboard data to file."""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(dict(self.leaderboard), f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error saving leaderboard: {e}")

    def _load_data(self) -> None:
        """Load leaderboard data from file."""
        if not os.path.exists(self.storage_file):
            return
            
        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                self.leaderboard.update(data)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading leaderboard: {e}")

    def __str__(self) -> str:
        """String representation of top 10 players."""
        top_players = self.get_top_players(10)
        output = ["Leaderboard:"]
        for rank, (player, points) in enumerate(top_players, 1):
            output.append(f"{rank}. {player}: {points} points")
        return "\n".join(output)


# Example usage
if __name__ == "__main__":
    lb = Leaderboard()
    
    # Add some test data
    lb.add_points("player1", 100)
    lb.add_points("player2", 200)
    lb.add_points("player3", 150)
    lb.add_points("player1", 50)  # player1 now has 150
    
    # Display leaderboard
    print(lb)
    
    # Get specific player rank
    print(f"Player1 rank: {lb.get_player_rank('player1')}")
```
