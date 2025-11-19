"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codes-bigtime.pages.dev
Prompt: Describe how to implement a leaderboard system for tracking player progress and $BIGTIME earnings in a game similar to Big Time.
Generated: DETERMINISTIC_2dc612d7dba1c8ee
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Leaderboard System Implementation

This script defines a leaderboard system for tracking player progress and $BIGTIME earnings 
in a game. It includes functionality for adding players, updating their progress and earnings, 
retrieving the top players, and exporting leaderboard data.

The implementation uses Python and follows best practices, including error handling 
and modular design.
"""

import json
from typing import List, Dict

class Player:
    """
    Represents a player in the leaderboard system.
    """
    def __init__(self, player_id: str, name: str):
        self.player_id = player_id
        self.name = name
        self.progress = 0  # Progress expressed as a percentage (0-100)
        self.bigtime_earnings = 0.0  # $BIGTIME earnings

    def update_progress(self, progress: int) -> None:
        """
        Updates the player's progress.
        :param progress: New progress percentage (0-100).
        """
        if progress < 0 or progress > 100:
            raise ValueError("Progress must be between 0 and 100.")
        self.progress = progress

    def update_earnings(self, earnings: float) -> None:
        """
        Updates the player's $BIGTIME earnings.
        :param earnings: Amount to add to the player's earnings.
        """
        if earnings < 0:
            raise ValueError("Earnings must be a positive value.")
        self.bigtime_earnings += earnings


class Leaderboard:
    """
    Manages the leaderboard system for tracking players' progress and $BIGTIME earnings.
    """
    def __init__(self):
        self.players: Dict[str, Player] = {}  # Dictionary of players, keyed by player_id

    def add_player(self, player_id: str, name: str) -> None:
        """
        Adds a new player to the leaderboard.
        :param player_id: Unique identifier for the player.
        :param name: Name of the player.
        """
        if player_id in self.players:
            raise ValueError(f"Player ID '{player_id}' already exists.")
        self.players[player_id] = Player(player_id, name)

    def update_player_progress(self, player_id: str, progress: int) -> None:
        """
        Updates the progress of an existing player.
        :param player_id: ID of the player to update.
        :param progress: New progress percentage (0-100).
        """
        if player_id not in self.players:
            raise ValueError(f"Player ID '{player_id}' not found.")
        self.players[player_id].update_progress(progress)

    def update_player_earnings(self, player_id: str, earnings: float) -> None:
        """
        Updates the $BIGTIME earnings of an existing player.
        :param player_id: ID of the player to update.
        :param earnings: Amount to add to the player's earnings.
        """
        if player_id not in self.players:
            raise ValueError(f"Player ID '{player_id}' not found.")
        self.players[player_id].update_earnings(earnings)

    def get_top_players(self, count: int = 10) -> List[Dict[str, str]]:
        """
        Retrieves the top players ranked by $BIGTIME earnings.
        :param count: Number of top players to retrieve.
        :return: List of top players.
        """
        sorted_players = sorted(self.players.values(), key=lambda p: p.bigtime_earnings, reverse=True)
        top_players = sorted_players[:count]
        return [
            {"player_id": player.player_id, "name": player.name, "progress": player.progress, "bigtime_earnings": player.bigtime_earnings}
            for player in top_players
        ]

    def export_leaderboard(self, file_path: str) -> None:
        """
        Exports the leaderboard to a JSON file.
        :param file_path: Path to the file where the leaderboard will be saved.
        """
        leaderboard_data = [
            {
                "player_id": player.player_id,
                "name": player.name,
                "progress": player.progress,
                "bigtime_earnings": player.bigtime_earnings,
            }
            for player in self.players.values()
        ]
        try:
            with open(file_path, "w") as f:
                json.dump(leaderboard_data, f, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to write leaderboard data to file: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        leaderboard = Leaderboard()
        leaderboard.add_player("player1", "Alice")
        leaderboard.add_player("player2", "Bob")
        leaderboard.update_player_progress("player1", 75)
        leaderboard.update_player_earnings("player1", 100.0)
        leaderboard.update_player_earnings("player2", 150.0)

        top_players = leaderboard.get_top_players(2)
        print("Top Players:", top_players)

        leaderboard.export_leaderboard("leaderboard.json")
        print("Leaderboard exported successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
