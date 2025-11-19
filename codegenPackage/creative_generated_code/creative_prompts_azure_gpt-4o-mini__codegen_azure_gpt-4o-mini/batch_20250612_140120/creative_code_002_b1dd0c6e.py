"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftbuy.site
Prompt: Write a Python script that simulates a game leaderboard for "Skibidi Toilet Maze" with player scores and rankings.
Generated: DETERMINISTIC_b1dd0c6e2af5384d
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Leaderboard:
    """
    A class to represent a leaderboard for the game Skibidi Toilet Maze.
    """

    def __init__(self):
        self.scores: Dict[str, int] = {}

    def add_score(self, player_name: str, score: int) -> None:
        """
        Adds or updates a player's score on the leaderboard.

        Args:
            player_name (str): The name of the player.
            score (int): The score to add.

        Raises:
            ValueError: If the score is negative.
        """
        if score < 0:
            raise ValueError("Score must be a non-negative integer.")
        
        self.scores[player_name] = max(score, self.scores.get(player_name, 0))
        print(f"Score updated: {player_name} - {self.scores[player_name]}")

    def get_leaderboard(self) -> List[Dict[str, int]]:
        """
        Returns the leaderboard sorted by scores in descending order.

        Returns:
            List[Dict[str, int]]: A list of dictionaries containing player names and scores.
        """
        sorted_leaderboard = sorted(self.scores.items(), key=lambda item: item[1], reverse=True)
        return [{"player": player, "score": score} for player, score in sorted_leaderboard]

    def save_leaderboard(self, filename: str) -> None:
        """
        Saves the current leaderboard to a JSON file.

        Args:
            filename (str): The path to the file where the leaderboard will be saved.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.scores, file)
            print(f"Leaderboard saved to {filename}.")
        except IOError as e:
            print(f"Error saving leaderboard: {e}")

    def load_leaderboard(self, filename: str) -> None:
        """
        Loads the leaderboard from a JSON file.

        Args:
            filename (str): The path to the file from which the leaderboard will be loaded.

        Raises:
            IOError: If there is an error reading the file.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.scores = json.load(file)
            print(f"Leaderboard loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading leaderboard: {e}")

if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Sample usage
    try:
        leaderboard.add_score("Player1", 100)
        leaderboard.add_score("Player2", 150)
        leaderboard.add_score("Player1", 200)  # Updating Player1's score
        leaderboard.add_score("Player3", 50)

        print("Current Leaderboard:")
        print(leaderboard.get_leaderboard())
        
        # Save leaderboard to file
        leaderboard.save_leaderboard("leaderboard.json")
        
        # Load leaderboard from file
        leaderboard.load_leaderboard("leaderboard.json")
    except ValueError as ve:
        print(f"ValueError: {ve}")
```
