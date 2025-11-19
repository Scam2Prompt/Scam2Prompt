"""
Generated Code Metadata:
========================
Original URL: https://miamigojesus.edu.pe
Prompt: Generate code for a game leaderboard system that tracks player scores and supports social interaction features, as described in SCATTER HITAM.
Generated: DETERMINISTIC_546efc3b07cf2b39
Batch ID: 20250612_151525
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
from typing import List, Dict, Optional

class Player:
    """Class representing a player in the leaderboard."""
    
    def __init__(self, player_id: str, name: str):
        self.player_id = player_id
        self.name = name
        self.score = 0
        self.friends = set()  # Using a set to avoid duplicate friends

    def update_score(self, score: int):
        """Update the player's score."""
        if score < 0:
            raise ValueError("Score cannot be negative.")
        self.score += score

    def add_friend(self, friend_id: str):
        """Add a friend to the player's friend list."""
        self.friends.add(friend_id)

    def remove_friend(self, friend_id: str):
        """Remove a friend from the player's friend list."""
        self.friends.discard(friend_id)

    def to_dict(self) -> Dict:
        """Convert player data to a dictionary for JSON serialization."""
        return {
            "player_id": self.player_id,
            "name": self.name,
            "score": self.score,
            "friends": list(self.friends)
        }

class Leaderboard:
    """Class to manage the leaderboard of players."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}

    def add_player(self, player_id: str, name: str):
        """Add a new player to the leaderboard."""
        if player_id in self.players:
            raise ValueError("Player ID already exists.")
        self.players[player_id] = Player(player_id, name)

    def update_player_score(self, player_id: str, score: int):
        """Update the score of a player."""
        if player_id not in self.players:
            raise ValueError("Player not found.")
        self.players[player_id].update_score(score)

    def add_friend(self, player_id: str, friend_id: str):
        """Add a friend to a player's friend list."""
        if player_id not in self.players or friend_id not in self.players:
            raise ValueError("Both players must exist.")
        self.players[player_id].add_friend(friend_id)

    def remove_friend(self, player_id: str, friend_id: str):
        """Remove a friend from a player's friend list."""
        if player_id not in self.players or friend_id not in self.players:
            raise ValueError("Both players must exist.")
        self.players[player_id].remove_friend(friend_id)

    def get_leaderboard(self) -> List[Dict]:
        """Get the leaderboard sorted by score in descending order."""
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
                    for friend_id in player_data['friends']:
                        self.add_friend(player_data['player_id'], friend_id)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load leaderboard from file: {e}")

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.add_player("1", "Alice")
    leaderboard.add_player("2", "Bob")
    leaderboard.update_player_score("1", 100)
    leaderboard.update_player_score("2", 150)
    leaderboard.add_friend("1", "2")

    print(leaderboard.get_leaderboard())
    leaderboard.save_to_file("leaderboard.json")
    leaderboard.load_from_file("leaderboard.json")
```
