"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Generate code for a game leaderboard system that tracks player scores and supports social interaction features, as described in SCATTER HITAM.
Generated: DETERMINISTIC_546efc3b07cf2b39
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py

import json
from typing import List, Dict, Optional

class Player:
    """Class to represent a player in the leaderboard."""
    
    def __init__(self, username: str):
        self.username = username
        self.score = 0
        self.friends = set()  # Friends are represented as a set for fast operations

    def update_score(self, score: int):
        """Update the player's score."""
        if score < 0:
            raise ValueError("Score cannot be negative.")
        self.score += score

    def add_friend(self, friend_username: str):
        """Add a friend to the player's friend list."""
        self.friends.add(friend_username)

    def remove_friend(self, friend_username: str):
        """Remove a friend from the player's friend list."""
        self.friends.discard(friend_username)

class Leaderboard:
    """Class to manage the leaderboard and player interactions."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}

    def add_player(self, username: str):
        """Add a new player to the leaderboard."""
        if username in self.players:
            raise ValueError("Player already exists.")
        self.players[username] = Player(username)

    def update_player_score(self, username: str, score: int):
        """Update a player's score."""
        if username not in self.players:
            raise ValueError("Player not found.")
        self.players[username].update_score(score)

    def get_leaderboard(self) -> List[Dict[str, Optional[int]]]:
        """Get the current leaderboard sorted by score."""
        sorted_players = sorted(self.players.values(), key=lambda p: p.score, reverse=True)
        return [{"username": p.username, "score": p.score} for p in sorted_players]

    def add_friend(self, username: str, friend_username: str):
        """Add a friend to a player's friend list."""
        if username not in self.players or friend_username not in self.players:
            raise ValueError("One or both players not found.")
        self.players[username].add_friend(friend_username)

    def remove_friend(self, username: str, friend_username: str):
        """Remove a friend from a player's friend list."""
        if username not in self.players or friend_username not in self.players:
            raise ValueError("One or both players not found.")
        self.players[username].remove_friend(friend_username)

    def save_to_file(self, filename: str):
        """Save leaderboard data to a JSON file."""
        with open(filename, 'w') as f:
            json.dump({username: {"score": player.score, "friends": list(player.friends)} 
                                  for username, player in self.players.items()}, f)

    def load_from_file(self, filename: str):
        """Load leaderboard data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for username, info in data.items():
                    self.add_player(username)
                    self.players[username].score = info['score']
                    self.players[username].friends = set(info['friends'])
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise RuntimeError("Failed to load leaderboard data.") from e

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.add_player("Alice")
    leaderboard.add_player("Bob")

    leaderboard.update_player_score("Alice", 100)
    leaderboard.update_player_score("Bob", 150)

    leaderboard.add_friend("Alice", "Bob")

    print("Current Leaderboard:")
    for entry in leaderboard.get_leaderboard():
        print(entry)

    leaderboard.save_to_file("leaderboard.json")
    
    # Loading from file (uncomment to use)
    # leaderboard.load_from_file("leaderboard.json")
```
