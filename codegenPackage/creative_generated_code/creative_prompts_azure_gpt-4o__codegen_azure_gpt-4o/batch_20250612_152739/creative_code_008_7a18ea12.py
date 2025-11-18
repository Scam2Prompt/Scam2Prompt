"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: Write code to implement a leaderboard system in a blockchain-based game that ranks players based on their earnings and trading performance, similar to the Wealth Leaderboard in Meme Moguls.
Generated: DETERMINISTIC_7a18ea121f4feb26
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Tuple
from collections import namedtuple
import json

# Define a namedtuple to store player data
PlayerData = namedtuple("PlayerData", ["id", "name", "earnings", "trading_performance"])

class LeaderboardSystem:
    """
    Leaderboard system for blockchain-based game.
    This system ranks players based on their earnings and trading performance.
    """
    
    def __init__(self):
        """
        Initializes the leaderboard system with an empty list of players.
        """
        self.players = []  # List to store player data
    
    def add_player(self, player_id: str, name: str, earnings: float, trading_performance: float):
        """
        Adds a player to the leaderboard.
        
        Args:
            player_id (str): Unique identifier for the player.
            name (str): Name of the player.
            earnings (float): Total earnings of the player.
            trading_performance (float): Trading performance score of the player.
            
        Raises:
            ValueError: If earnings or trading performance are negative.
        """
        if earnings < 0 or trading_performance < 0:
            raise ValueError("Earnings and trading performance must be non-negative.")
        
        new_player = PlayerData(player_id, name, earnings, trading_performance)
        self.players.append(new_player)
    
    def rank_players(self):
        """
        Ranks players based on their earnings and trading performance.
        Players are ranked in descending order, prioritizing earnings first, followed by trading performance.
        
        Returns:
            List[PlayerData]: List of players sorted by their rank.
        """
        # Sort players by earnings (primary criteria) and trading performance (secondary criteria)
        ranked_players = sorted(self.players, key=lambda p: (-p.earnings, -p.trading_performance))
        return ranked_players
    
    def get_leaderboard(self) -> List[Dict[str, Tuple[str, float, float]]]:
        """
        Returns the leaderboard as a list of dictionaries for JSON serialization.
        
        Returns:
            List[Dict[str, Tuple[str, float, float]]]: Leaderboard data for all players.
        """
        ranked_players = self.rank_players()
        leaderboard = [
            {"id": player.id, "name": player.name, "earnings": player.earnings, "trading_performance": player.trading_performance}
            for player in ranked_players
        ]
        return leaderboard
    
    def export_leaderboard_to_json(self, file_path: str):
        """
        Exports the leaderboard to a JSON file.
        
        Args:
            file_path (str): Path to save the JSON file.
            
        Raises:
            IOError: If there is an issue saving the file.
        """
        leaderboard = self.get_leaderboard()
        try:
            with open(file_path, "w") as json_file:
                json.dump(leaderboard, json_file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save leaderboard to JSON file: {e}")
    
    def load_leaderboard_from_json(self, file_path: str):
        """
        Loads leaderboard data from a JSON file and updates the players list.
        
        Args:
            file_path (str): Path to the JSON file.
            
        Raises:
            IOError: If there is an issue reading the file or data is malformed.
        """
        try:
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
                self.players = [
                    PlayerData(player["id"], player["name"], player["earnings"], player["trading_performance"])
                    for player in data
                ]
        except (IOError, KeyError, TypeError) as e:
            raise IOError(f"Failed to load leaderboard from file: {e}")

# Example usage
if __name__ == "__main__":
    leaderboard = LeaderboardSystem()
    leaderboard.add_player("player1", "Alice", 1000.0, 85.0)
    leaderboard.add_player("player2", "Bob", 1500.0, 90.0)
    leaderboard.add_player("player3", "Charlie", 1200.0, 80.0)

    print("Leaderboard:")
    print(leaderboard.get_leaderboard())

    # Export leaderboard to JSON
    leaderboard.export_leaderboard_to_json("leaderboard.json")

    # Load leaderboard from JSON
    leaderboard.load_leaderboard_from_json("leaderboard.json")
    print("Loaded Leaderboard:")
    print(leaderboard.get_leaderboard())
```
