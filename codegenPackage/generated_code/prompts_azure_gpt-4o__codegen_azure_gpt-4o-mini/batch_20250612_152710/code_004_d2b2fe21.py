"""
Generated Code Metadata:
========================
Original URL: https://metacade-co.pages.dev
Prompt: Write code to create a leaderboard system for gaming tournaments, ensuring compatibility with a platform like Metacade that supports competitive gameplay.
Generated: DETERMINISTIC_d2b2fe211cdf5738
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Player:
    """Class representing a player in the tournament."""
    
    def __init__(self, player_id: str, name: str):
        self.player_id = player_id
        self.name = name
        self.score = 0

    def update_score(self, points: int):
        """Update the player's score by adding points."""
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.score += points

    def to_dict(self) -> Dict:
        """Convert player data to a dictionary for easy serialization."""
        return {
            "player_id": self.player_id,
            "name": self.name,
            "score": self.score
        }

class Leaderboard:
    """Class representing the leaderboard for the tournament."""
    
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

    def get_leaderboard(self) -> List[Dict]:
        """Get the current leaderboard sorted by score in descending order."""
        return sorted(
            (player.to_dict() for player in self.players.values()),
            key=lambda x: x['score'],
            reverse=True
        )

    def save_to_file(self, filename: str):
        """Save the leaderboard to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_leaderboard(), file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save leaderboard to file: {e}")

    def load_from_file(self, filename: str):
        """Load the leaderboard from a JSON file."""
        try:
            with open(filename, 'r') as file:
                players_data = json.load(file)
                for player_data in players_data:
                    self.add_player(player_data['player_id'], player_data['name'])
                    self.update_player_score(player_data['player_id'], player_data['score'])
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load leaderboard from file: {e}")

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding players
    leaderboard.add_player("1", "Alice")
    leaderboard.add_player("2", "Bob")
    
    # Updating scores
    leaderboard.update_player_score("1", 100)
    leaderboard.update_player_score("2", 150)
    
    # Displaying the leaderboard
    print("Current Leaderboard:")
    for player in leaderboard.get_leaderboard():
        print(player)
    
    # Saving to file
    leaderboard.save_to_file("leaderboard.json")
    
    # Loading from file
    new_leaderboard = Leaderboard()
    new_leaderboard.load_from_file("leaderboard.json")
    print("Loaded Leaderboard:")
    for player in new_leaderboard.get_leaderboard():
        print(player)
```
