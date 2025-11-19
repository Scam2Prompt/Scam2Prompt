"""
Generated Code Metadata:
========================
Original URL: https://stellar-datagrid.xyz
Prompt: Illustrate how to implement a leaderboard feature for poker tournaments in a casino app, drawing on the competitive elements highlighted in the Royal Joker experience.
Generated: DETERMINISTIC_c3ceddb538c4153e
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

from typing import List, Dict, Any
import json

class Player:
    """Class representing a player in the poker tournament."""
    
    def __init__(self, player_id: str, name: str):
        self.player_id = player_id
        self.name = name
        self.score = 0  # Initialize score to zero

    def update_score(self, points: int):
        """Update the player's score by adding points."""
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.score += points

    def to_dict(self) -> Dict[str, Any]:
        """Convert player information to a dictionary."""
        return {
            "player_id": self.player_id,
            "name": self.name,
            "score": self.score
        }

class Leaderboard:
    """Class to manage the leaderboard for the poker tournament."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}

    def add_player(self, player_id: str, name: str):
        """Add a new player to the leaderboard."""
        if player_id in self.players:
            raise ValueError("Player ID already exists.")
        self.players[player_id] = Player(player_id, name)

    def update_player_score(self, player_id: str, points: int):
        """Update the score of a player."""
        if player_id not in self.players:
            raise ValueError("Player not found.")
        self.players[player_id].update_score(points)

    def get_leaderboard(self) -> List[Dict[str, Any]]:
        """Get the current leaderboard sorted by score in descending order."""
        return sorted(
            (player.to_dict() for player in self.players.values()),
            key=lambda x: x['score'],
            reverse=True
        )

    def save_leaderboard(self, filename: str):
        """Save the leaderboard to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_leaderboard(), file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save leaderboard: {e}")

    def load_leaderboard(self, filename: str):
        """Load the leaderboard from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for player_data in data:
                    self.add_player(player_data['player_id'], player_data['name'])
                    self.players[player_data['player_id']].score = player_data['score']
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load leaderboard: {e}")

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding players
    leaderboard.add_player("1", "Alice")
    leaderboard.add_player("2", "Bob")
    
    # Updating scores
    leaderboard.update_player_score("1", 10)
    leaderboard.update_player_score("2", 20)
    
    # Displaying the leaderboard
    print("Current Leaderboard:")
    for player in leaderboard.get_leaderboard():
        print(player)
    
    # Saving the leaderboard to a file
    leaderboard.save_leaderboard("leaderboard.json")
    
    # Loading the leaderboard from a file
    new_leaderboard = Leaderboard()
    new_leaderboard.load_leaderboard("leaderboard.json")
    print("Loaded Leaderboard:")
    for player in new_leaderboard.get_leaderboard():
        print(player)
```
