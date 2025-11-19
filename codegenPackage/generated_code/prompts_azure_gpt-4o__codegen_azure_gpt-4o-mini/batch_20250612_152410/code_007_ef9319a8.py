"""
Generated Code Metadata:
========================
Original URL: https://newshungama.com
Prompt: Write code to create a leaderboard system for color prediction games, incorporating ideas from "How Colour Prediction Game Changes the User Mindset" on Newshungama.com.
Generated: DETERMINISTIC_ef9319a8e98155ec
Batch ID: 20250612_152410
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
    def __init__(self):
        """Initialize the leaderboard with an empty list of players."""
        self.players: List[Dict[str, Any]] = []

    def add_player(self, name: str, score: int) -> None:
        """
        Add a player to the leaderboard.

        Args:
            name (str): The name of the player.
            score (int): The score of the player.

        Raises:
            ValueError: If the score is negative.
        """
        if score < 0:
            raise ValueError("Score cannot be negative.")
        
        player = {
            'name': name,
            'score': score
        }
        self.players.append(player)
        self.players.sort(key=lambda x: x['score'], reverse=True)  # Sort players by score in descending order

    def get_top_players(self, top_n: int = 10) -> List[Dict[str, Any]]:
        """
        Retrieve the top N players from the leaderboard.

        Args:
            top_n (int): The number of top players to retrieve.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing player names and scores.
        """
        return self.players[:top_n]

    def save_leaderboard(self, filename: str) -> None:
        """
        Save the leaderboard to a JSON file.

        Args:
            filename (str): The name of the file to save the leaderboard to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.players, file)
        except IOError as e:
            print(f"Error saving leaderboard to {filename}: {e}")

    def load_leaderboard(self, filename: str) -> None:
        """
        Load the leaderboard from a JSON file.

        Args:
            filename (str): The name of the file to load the leaderboard from.
        """
        try:
            with open(filename, 'r') as file:
                self.players = json.load(file)
                self.players.sort(key=lambda x: x['score'], reverse=True)  # Sort after loading
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading leaderboard from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding players
    leaderboard.add_player("Alice", 150)
    leaderboard.add_player("Bob", 200)
    leaderboard.add_player("Charlie", 100)

    # Display top players
    print("Top Players:", leaderboard.get_top_players())

    # Save leaderboard to a file
    leaderboard.save_leaderboard("leaderboard.json")

    # Load leaderboard from a file
    new_leaderboard = Leaderboard()
    new_leaderboard.load_leaderboard("leaderboard.json")
    print("Loaded Players:", new_leaderboard.get_top_players())
```
