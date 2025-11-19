"""
Generated Code Metadata:
========================
Original URL: https://jups.io
Prompt: Develop a leaderboard system for tracking top players in a crypto-based casino platform, inspired by the leaderboard functionality on Jups.io.
Generated: DETERMINISTIC_61ec3948bf055cc4
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime, timedelta
import json

@dataclass
class Player:
    """Represents a player in the leaderboard."""
    id: int
    username: str
    balance: float

class Leaderboard:
    """Manages the leaderboard for the crypto-based casino platform."""

    def __init__(self, max_players: int = 100):
        """
        Initializes the leaderboard.

        Args:
        - max_players (int): The maximum number of players to display on the leaderboard.
        """
        self.max_players = max_players
        self.players: Dict[int, Player] = {}
        self.leaderboard: List[Player] = []

    def add_player(self, player: Player):
        """
        Adds a player to the leaderboard.

        Args:
        - player (Player): The player to add.
        """
        self.players[player.id] = player
        self._update_leaderboard()

    def update_player_balance(self, player_id: int, new_balance: float):
        """
        Updates a player's balance on the leaderboard.

        Args:
        - player_id (int): The ID of the player to update.
        - new_balance (float): The new balance of the player.

        Raises:
        - ValueError: If the player ID does not exist on the leaderboard.
        """
        if player_id not in self.players:
            raise ValueError("Player ID does not exist on the leaderboard.")
        self.players[player_id].balance = new_balance
        self._update_leaderboard()

    def remove_player(self, player_id: int):
        """
        Removes a player from the leaderboard.

        Args:
        - player_id (int): The ID of the player to remove.

        Raises:
        - ValueError: If the player ID does not exist on the leaderboard.
        """
        if player_id not in self.players:
            raise ValueError("Player ID does not exist on the leaderboard.")
        del self.players[player_id]
        self._update_leaderboard()

    def _update_leaderboard(self):
        """Updates the leaderboard by sorting players by balance in descending order."""
        self.leaderboard = sorted(self.players.values(), key=lambda player: player.balance, reverse=True)
        self.leaderboard = self.leaderboard[:self.max_players]

    def get_leaderboard(self) -> List[Player]:
        """
        Retrieves the current leaderboard.

        Returns:
        - List[Player]: The current leaderboard.
        """
        return self.leaderboard

    def to_json(self) -> str:
        """
        Converts the leaderboard to a JSON string.

        Returns:
        - str: The leaderboard as a JSON string.
        """
        leaderboard_json = []
        for i, player in enumerate(self.leaderboard):
            leaderboard_json.append({
                "rank": i + 1,
                "id": player.id,
                "username": player.username,
                "balance": player.balance
            })
        return json.dumps(leaderboard_json)

def main():
    leaderboard = Leaderboard()

    # Create some example players
    player1 = Player(1, "Player 1", 1000.0)
    player2 = Player(2, "Player 2", 500.0)
    player3 = Player(3, "Player 3", 2000.0)

    # Add players to the leaderboard
    leaderboard.add_player(player1)
    leaderboard.add_player(player2)
    leaderboard.add_player(player3)

    # Print the leaderboard
    print(leaderboard.to_json())

    # Update a player's balance
    leaderboard.update_player_balance(1, 1500.0)
    print(leaderboard.to_json())

    # Remove a player
    leaderboard.remove_player(2)
    print(leaderboard.to_json())

if __name__ == "__main__":
    main()
```
