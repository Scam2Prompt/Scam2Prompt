"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Generate a code snippet that demonstrates how to create a leaderboard for players in SIMemes, tracking their poop collection and resource management.
Generated: DETERMINISTIC_bcc5c3af22bcf092
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

import json
from typing import List, Dict

class Player:
    """
    Represents a player in SIMemes with their stats.
    """
    def __init__(self, player_id: int, name: str):
        self.player_id = player_id
        self.name = name
        self.poop_collected = 0
        self.resources_managed = 0

    def update_stats(self, poop_collected: int, resources_managed: int):
        """
        Updates the player's stats.
        :param poop_collected: Amount of poop collected to add.
        :param resources_managed: Amount of resources managed to add.
        """
        if poop_collected < 0 or resources_managed < 0:
            raise ValueError("Stats cannot be negative.")
        self.poop_collected += poop_collected
        self.resources_managed += resources_managed

    def to_dict(self) -> Dict:
        """
        Converts the player's data to a dictionary for serialization.
        :return: Dictionary representation of the player.
        """
        return {
            "player_id": self.player_id,
            "name": self.name,
            "poop_collected": self.poop_collected,
            "resources_managed": self.resources_managed
        }


class Leaderboard:
    """
    Represents the leaderboard for SIMemes players.
    """
    def __init__(self):
        self.players = {}

    def add_player(self, player: Player):
        """
        Adds a player to the leaderboard.
        :param player: Player object to add.
        """
        if player.player_id in self.players:
            raise ValueError(f"Player with ID {player.player_id} already exists.")
        self.players[player.player_id] = player

    def update_player_stats(self, player_id: int, poop_collected: int, resources_managed: int):
        """
        Updates the stats of a player in the leaderboard.
        :param player_id: ID of the player to update.
        :param poop_collected: Amount of poop collected to add.
        :param resources_managed: Amount of resources managed to add.
        """
        if player_id not in self.players:
            raise ValueError(f"Player with ID {player_id} does not exist.")
        self.players[player_id].update_stats(poop_collected, resources_managed)

    def get_top_players(self, top_n: int = 10) -> List[Dict]:
        """
        Retrieves the top players based on poop collection and resource management.
        :param top_n: Number of top players to retrieve.
        :return: List of top players sorted by their stats.
        """
        sorted_players = sorted(
            self.players.values(),
            key=lambda p: (p.poop_collected, p.resources_managed),
            reverse=True
        )
        return [player.to_dict() for player in sorted_players[:top_n]]

    def save_to_file(self, file_path: str):
        """
        Saves the leaderboard data to a JSON file.
        :param file_path: Path to the file where data will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([player.to_dict() for player in self.players.values()], file, indent=4)
        except IOError as e:
            print(f"Error saving leaderboard to file: {e}")

    def load_from_file(self, file_path: str):
        """
        Loads leaderboard data from a JSON file.
        :param file_path: Path to the file to load data from.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.players = {player['player_id']: Player(**player) for player in data}
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading leaderboard from file: {e}")


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Add players
    leaderboard.add_player(Player(1, "PlayerOne"))
    leaderboard.add_player(Player(2, "PlayerTwo"))

    # Update stats
    leaderboard.update_player_stats(1, poop_collected=50, resources_managed=30)
    leaderboard.update_player_stats(2, poop_collected=70, resources_managed=20)

    # Get top players
    top_players = leaderboard.get_top_players(top_n=2)
    print("Top Players:", top_players)

    # Save leaderboard to file
    leaderboard.save_to_file("leaderboard.json")

    # Load leaderboard from file
    leaderboard.load_from_file("leaderboard.json")
    print("Leaderboard loaded from file:", leaderboard.get_top_players())
```
