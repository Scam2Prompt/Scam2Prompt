"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacade-co.pages.dev
Prompt: Write code to create a leaderboard system for gaming tournaments, ensuring compatibility with a platform like Metacade that supports competitive gameplay.
Generated: DETERMINISTIC_d2b2fe211cdf5738
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional, Any
import json

# Define a class to represent a Player in the leaderboard
class Player:
    def __init__(self, player_id: str, name: str, score: int = 0):
        """
        Initialize a Player with an ID, name, and optional score.
        
        :param player_id: Unique identifier for the player
        :param name: Name of the player
        :param score: Current score of the player, default is 0
        """
        self.player_id = player_id
        self.name = name
        self.score = score

    def update_score(self, new_score: int):
        """
        Update the player's score.
        
        :param new_score: New score to be assigned to the player
        """
        if new_score < 0:
            raise ValueError("Score cannot be negative.")
        self.score = new_score

# Define a class to manage the leaderboard
class Leaderboard:
    def __init__(self):
        """
        Initialize an empty leaderboard.
        """
        self.players: Dict[str, Player] = {}

    def add_player(self, player_id: str, name: str):
        """
        Add a new player to the leaderboard.
        
        :param player_id: Unique identifier for the player
        :param name: Name of the player
        """
        if player_id in self.players:
            raise ValueError("Player with this ID already exists.")
        self.players[player_id] = Player(player_id, name)

    def update_player_score(self, player_id: str, new_score: int):
        """
        Update the score of a player.
        
        :param player_id: Unique identifier for the player
        :param new_score: New score to assign
        """
        if player_id not in self.players:
            raise ValueError("Player not found.")
        self.players[player_id].update_score(new_score)

    def get_leaderboard(self) -> List[Dict[str, Any]]:
        """
        Get the leaderboard sorted by score in descending order.
        
        :return: List of players sorted by their scores
        """
        return sorted(
            [{"player_id": player.player_id, "name": player.name, "score": player.score}
             for player in self.players.values()],
            key=lambda x: x["score"],
            reverse=True
        )

    def to_json(self) -> str:
        """
        Serialize the leaderboard to a JSON string.
        
        :return: JSON representation of the leaderboard
        """
        return json.dumps(self.get_leaderboard())

# Example Usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding players to the leaderboard
    try:
        leaderboard.add_player("1", "Alice")
        leaderboard.add_player("2", "Bob")
        
        # Updating scores
        leaderboard.update_player_score("1", 150)
        leaderboard.update_player_score("2", 200)

        # Displaying the leaderboard
        print(leaderboard.to_json())
    except ValueError as e:
        print(f"Error: {e}")
```
