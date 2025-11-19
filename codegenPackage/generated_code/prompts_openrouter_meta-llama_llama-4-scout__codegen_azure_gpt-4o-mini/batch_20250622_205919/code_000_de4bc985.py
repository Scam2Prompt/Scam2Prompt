"""
Generated Code Metadata:
========================
Original URL: https://memefi-club.pages.dev
Prompt: "Write a Python script to implement a leaderboard system for a meme-themed game like MemeFi, where players can earn MemeFi coins and climb the ranks."
Generated: DETERMINISTIC_de4bc985bfcbf787
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Leaderboard:
    def __init__(self, filename: str):
        """
        Initializes the Leaderboard with a given filename to store player data.
        
        :param filename: The name of the file where leaderboard data will be stored.
        """
        self.filename = filename
        self.players = self.load_leaderboard()

    def load_leaderboard(self) -> Dict[str, int]:
        """
        Loads the leaderboard from a JSON file.
        
        :return: A dictionary of player names and their corresponding scores.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}  # Return an empty leaderboard if file not found or invalid JSON

    def save_leaderboard(self) -> None:
        """
        Saves the current leaderboard to a JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.players, file, indent=4)

    def add_player(self, player_name: str, score: int) -> None:
        """
        Adds a player to the leaderboard or updates their score if they already exist.
        
        :param player_name: The name of the player.
        :param score: The score to add to the player's total.
        """
        if player_name in self.players:
            self.players[player_name] += score
        else:
            self.players[player_name] = score
        self.save_leaderboard()

    def get_top_players(self, top_n: int) -> List[Dict[str, Any]]:
        """
        Retrieves the top N players from the leaderboard.
        
        :param top_n: The number of top players to retrieve.
        :return: A list of dictionaries containing player names and scores.
        """
        sorted_players = sorted(self.players.items(), key=lambda item: item[1], reverse=True)
        return [{"player": player, "score": score} for player, score in sorted_players[:top_n]]

    def display_leaderboard(self, top_n: int) -> None:
        """
        Displays the leaderboard in a readable format.
        
        :param top_n: The number of top players to display.
        """
        top_players = self.get_top_players(top_n)
        print("Leaderboard:")
        for rank, player in enumerate(top_players, start=1):
            print(f"{rank}. {player['player']} - {player['score']} MemeFi Coins")

if __name__ == "__main__":
    leaderboard = Leaderboard("leaderboard.json")

    # Example usage
    leaderboard.add_player("Player1", 100)
    leaderboard.add_player("Player2", 150)
    leaderboard.add_player("Player1", 50)  # Player1 earns more coins

    leaderboard.display_leaderboard(5)  # Display top 5 players
```
