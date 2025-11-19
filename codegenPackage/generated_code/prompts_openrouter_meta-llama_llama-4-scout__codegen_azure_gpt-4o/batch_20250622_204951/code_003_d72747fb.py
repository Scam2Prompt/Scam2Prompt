"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Design a system to manage poker tournament brackets and standings, including features for player registration and prize distribution.
Generated: DETERMINISTIC_d72747fbcb6ee953
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from typing import List, Dict, Optional


class Player:
    """
    Represents a player in the poker tournament.
    """
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the player
        self.name = name
        self.points = 0  # Points earned in the tournament

    def __repr__(self):
        return f"Player(id={self.id}, name={self.name}, points={self.points})"


class Tournament:
    """
    Represents a poker tournament, including player registration, brackets, and prize distribution.
    """
    def __init__(self, name: str, prize_pool: float):
        self.name = name
        self.prize_pool = prize_pool
        self.players: Dict[str, Player] = {}  # Registered players
        self.brackets: List[List[str]] = []  # Tournament brackets (list of player IDs)

    def register_player(self, name: str) -> str:
        """
        Registers a new player in the tournament.
        :param name: Name of the player
        :return: Player ID
        """
        if name in [player.name for player in self.players.values()]:
            raise ValueError(f"Player with name '{name}' is already registered.")
        player = Player(name)
        self.players[player.id] = player
        return player.id

    def create_brackets(self):
        """
        Creates tournament brackets based on registered players.
        """
        if len(self.players) < 2:
            raise ValueError("At least two players are required to create brackets.")
        player_ids = list(self.players.keys())
        self.brackets = [player_ids[i:i + 2] for i in range(0, len(player_ids), 2)]

    def record_match_result(self, winner_id: str, loser_id: str):
        """
        Records the result of a match and updates player points.
        :param winner_id: ID of the winning player
        :param loser_id: ID of the losing player
        """
        if winner_id not in self.players or loser_id not in self.players:
            raise ValueError("Invalid player ID(s).")
        if winner_id == loser_id:
            raise ValueError("Winner and loser cannot be the same player.")
        self.players[winner_id].points += 3  # Award 3 points to the winner
        self.players[loser_id].points += 1  # Award 1 point to the loser

    def distribute_prizes(self) -> Dict[str, float]:
        """
        Distributes the prize pool among the top players based on their standings.
        :return: Dictionary of player IDs and their prize amounts
        """
        if not self.players:
            raise ValueError("No players registered in the tournament.")
        sorted_players = sorted(self.players.values(), key=lambda p: p.points, reverse=True)
        top_players = sorted_players[:3]  # Top 3 players
        prize_distribution = {
            1: 0.5,  # 50% of the prize pool for the 1st place
            2: 0.3,  # 30% of the prize pool for the 2nd place
            3: 0.2   # 20% of the prize pool for the 3rd place
        }
        prizes = {}
        for rank, player in enumerate(top_players, start=1):
            prizes[player.id] = self.prize_pool * prize_distribution[rank]
        return prizes

    def get_standings(self) -> List[Dict[str, Optional[str]]]:
        """
        Returns the current standings of players in the tournament.
        :return: List of dictionaries containing player standings
        """
        standings = sorted(self.players.values(), key=lambda p: p.points, reverse=True)
        return [{"id": player.id, "name": player.name, "points": player.points} for player in standings]


# Example usage:
if __name__ == "__main__":
    try:
        # Create a tournament
        tournament = Tournament(name="Poker Championship", prize_pool=10000.0)

        # Register players
        player1_id = tournament.register_player("Alice")
        player2_id = tournament.register_player("Bob")
        player3_id = tournament.register_player("Charlie")
        player4_id = tournament.register_player("Diana")

        # Create brackets
        tournament.create_brackets()
        print("Brackets:", tournament.brackets)

        # Record match results
        tournament.record_match_result(winner_id=player1_id, loser_id=player2_id)
        tournament.record_match_result(winner_id=player3_id, loser_id=player4_id)

        # Get standings
        standings = tournament.get_standings()
        print("Standings:", standings)

        # Distribute prizes
        prizes = tournament.distribute_prizes()
        print("Prize Distribution:", prizes)

    except Exception as e:
        print(f"Error: {e}")
```
