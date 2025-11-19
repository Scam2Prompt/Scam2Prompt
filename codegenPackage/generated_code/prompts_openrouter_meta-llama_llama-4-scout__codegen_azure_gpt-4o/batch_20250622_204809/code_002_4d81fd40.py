"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Generate code for a basic leaderboard system that tracks player XP and performance metrics, as seen in ev.io.
Generated: DETERMINISTIC_4d81fd4082eaed15
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Leaderboard:
    """
    A class to represent a leaderboard system for tracking player XP and performance metrics.
    """

    def __init__(self):
        """
        Initializes an empty leaderboard.
        """
        self.players = {}  # Dictionary to store player data: {player_id: {"name": str, "xp": int, "metrics": dict}}

    def add_player(self, player_id: str, name: str):
        """
        Adds a new player to the leaderboard.

        :param player_id: Unique identifier for the player.
        :param name: Name of the player.
        """
        if player_id in self.players:
            raise ValueError(f"Player with ID {player_id} already exists.")
        self.players[player_id] = {"name": name, "xp": 0, "metrics": {}}

    def update_xp(self, player_id: str, xp: int):
        """
        Updates the XP of a player.

        :param player_id: Unique identifier for the player.
        :param xp: XP to add to the player's current XP.
        """
        if player_id not in self.players:
            raise ValueError(f"Player with ID {player_id} does not exist.")
        if xp < 0:
            raise ValueError("XP cannot be negative.")
        self.players[player_id]["xp"] += xp

    def update_metrics(self, player_id: str, metric_name: str, value: int):
        """
        Updates a specific performance metric for a player.

        :param player_id: Unique identifier for the player.
        :param metric_name: Name of the metric to update.
        :param value: Value to set for the metric.
        """
        if player_id not in self.players:
            raise ValueError(f"Player with ID {player_id} does not exist.")
        self.players[player_id]["metrics"][metric_name] = value

    def get_leaderboard(self) -> List[Dict]:
        """
        Retrieves the leaderboard sorted by XP in descending order.

        :return: List of players sorted by XP.
        """
        return sorted(
            [{"player_id": pid, "name": pdata["name"], "xp": pdata["xp"], "metrics": pdata["metrics"]}
             for pid, pdata in self.players.items()],
            key=lambda x: x["xp"],
            reverse=True
        )

    def save_to_file(self, filename: str):
        """
        Saves the leaderboard data to a JSON file.

        :param filename: Name of the file to save the data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.players, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save leaderboard to file: {e}")

    def load_from_file(self, filename: str):
        """
        Loads leaderboard data from a JSON file.

        :param filename: Name of the file to load the data from.
        """
        try:
            with open(filename, 'r') as file:
                self.players = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load leaderboard from file: {e}")


# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Add players
    leaderboard.add_player("player1", "Alice")
    leaderboard.add_player("player2", "Bob")

    # Update XP and metrics
    leaderboard.update_xp("player1", 150)
    leaderboard.update_xp("player2", 200)
    leaderboard.update_metrics("player1", "kills", 10)
    leaderboard.update_metrics("player2", "kills", 15)

    # Display leaderboard
    print("Leaderboard:")
    for player in leaderboard.get_leaderboard():
        print(player)

    # Save and load leaderboard
    leaderboard.save_to_file("leaderboard.json")
    leaderboard.load_from_file("leaderboard.json")
```
