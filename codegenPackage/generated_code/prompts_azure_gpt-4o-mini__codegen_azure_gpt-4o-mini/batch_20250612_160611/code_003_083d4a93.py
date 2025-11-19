"""
Generated Code Metadata:
========================
Original URL: https://metacade-web.pages.dev
Prompt: Generate a script for a tournament feature that allows users to compete in games and track their performance on a platform like Metacade.
Generated: DETERMINISTIC_083d4a939a5a6f0a
Batch ID: 20250612_160611
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

class Player:
    """Class representing a player in the tournament."""
    
    def __init__(self, username: str):
        self.username = username
        self.score = 0

    def update_score(self, points: int):
        """Update the player's score by adding points."""
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.score += points

class Tournament:
    """Class representing a tournament."""
    
    def __init__(self, name: str):
        self.name = name
        self.players: Dict[str, Player] = {}
        self.results: List[Dict[str, Any]] = []

    def add_player(self, username: str):
        """Add a player to the tournament."""
        if username in self.players:
            raise ValueError(f"Player {username} is already in the tournament.")
        self.players[username] = Player(username)

    def record_score(self, username: str, points: int):
        """Record the score for a player."""
        if username not in self.players:
            raise ValueError(f"Player {username} not found in the tournament.")
        self.players[username].update_score(points)
        self.results.append({"username": username, "score": self.players[username].score})

    def get_leaderboard(self) -> List[Dict[str, Any]]:
        """Get the current leaderboard sorted by score."""
        leaderboard = [{"username": player.username, "score": player.score} for player in self.players.values()]
        return sorted(leaderboard, key=lambda x: x['score'], reverse=True)

    def save_results(self, filename: str):
        """Save tournament results to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.results, file)
        except IOError as e:
            print(f"Error saving results: {e}")

    def load_results(self, filename: str):
        """Load tournament results from a JSON file."""
        try:
            with open(filename, 'r') as file:
                self.results = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading results: {e}")

# Example usage
if __name__ == "__main__":
    tournament = Tournament("Metacade Championship")
    
    # Adding players
    tournament.add_player("Player1")
    tournament.add_player("Player2")
    
    # Recording scores
    tournament.record_score("Player1", 10)
    tournament.record_score("Player2", 15)
    
    # Displaying leaderboard
    leaderboard = tournament.get_leaderboard()
    print("Current Leaderboard:")
    for entry in leaderboard:
        print(f"{entry['username']}: {entry['score']} points")
    
    # Saving results
    tournament.save_results("tournament_results.json")
    
    # Loading results
    tournament.load_results("tournament_results.json")
```
