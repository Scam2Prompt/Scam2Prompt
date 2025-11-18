"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaps.us.com
Prompt: Generate code to create a leaderboard system for multiplayer games, incorporating features like "Bạn chơi chung" (play with friends) as described on 8Day Club.
Generated: DETERMINISTIC_c7e9ef35d3ce7dac
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py

from typing import List, Dict, Optional

class Player:
    """Represents a player in the leaderboard."""
    
    def __init__(self, player_id: str, name: str):
        self.player_id = player_id  # Unique identifier for the player
        self.name = name  # Player's name
        self.score = 0  # Player's score initialized to 0

    def update_score(self, points: int):
        """Updates the player's score by adding points."""
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.score += points

class Leaderboard:
    """Manages the leaderboard for the game."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}  # Player ID to Player mapping

    def add_player(self, player_id: str, name: str) -> None:
        """Adds a new player to the leaderboard."""
        if player_id in self.players:
            raise ValueError("Player ID already exists.")
        self.players[player_id] = Player(player_id, name)

    def update_player_score(self, player_id: str, points: int) -> None:
        """Updates the score of a player."""
        if player_id not in self.players:
            raise ValueError("Player not found.")
        self.players[player_id].update_score(points)

    def get_top_players(self, num_players: int) -> List[Player]:
        """Returns the top players sorted by score."""
        return sorted(self.players.values(), key=lambda p: p.score, reverse=True)[:num_players]

    def play_with_friends(self, player_id: str, friend_ids: List[str]) -> Optional[str]:
        """Simulates playing with friends and updates their scores."""
        if player_id not in self.players:
            raise ValueError("Main player not found.")
        
        # Simulate score update for friends
        for friend_id in friend_ids:
            if friend_id not in self.players:
                return f"Friend {friend_id} not found."
            self.update_player_score(friend_id, 10)  # Example of scoring 10 points
        
        return "Scores updated for friends."

# Example usage of the Leaderboard system
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding players
    leaderboard.add_player("1", "Alice")
    leaderboard.add_player("2", "Bob")
    leaderboard.add_player("3", "Charlie")

    # Updating scores
    leaderboard.update_player_score("1", 50)
    leaderboard.update_player_score("2", 75)

    # Getting top players
    top_players = leaderboard.get_top_players(2)
    print("Top Players:")
    for player in top_players:
        print(f"{player.name}: {player.score}")

    # Playing with friends
    result = leaderboard.play_with_friends("1", ["2", "3"])
    print(result)

    # Display updated scores for verification
    for player in leaderboard.players.values():
        print(f"{player.name}: {player.score}")
```
