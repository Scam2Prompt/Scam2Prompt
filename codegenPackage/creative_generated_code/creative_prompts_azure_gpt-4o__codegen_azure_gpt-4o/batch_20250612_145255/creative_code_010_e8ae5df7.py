"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivebrokers.fo
Prompt: Write code to implement a tournament system for an online casino, allowing users to compete for prizes, similar to the tournaments hosted by 1Win.
Generated: DETERMINISTIC_e8ae5df7a70de928
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class Tournament:
    """
    Class to represent a tournament.
    """
    def __init__(self, name: str, prize_pool: float, start_time: datetime, end_time: datetime):
        self.id = uuid.uuid4()  # Generate unique ID for each tournament
        self.name = name
        self.prize_pool = prize_pool
        self.start_time = start_time
        self.end_time = end_time
        self.players: Dict[str, float] = {}  # Store players and their scores

    def register_player(self, player_id: str):
        """
        Register a player for the tournament.
        """
        if player_id in self.players:
            raise ValueError(f"Player {player_id} is already registered.")
        self.players[player_id] = 0.0  # Initialize player score to 0

    def update_score(self, player_id: str, score: float):
        """
        Update a player's score during the tournament.
        """
        if player_id not in self.players:
            raise ValueError(f"Player {player_id} is not registered in this tournament.")
        self.players[player_id] += score  # Add to the existing score

    def get_leaderboard(self) -> List[Dict[str, float]]:
        """
        Get the leaderboard, sorted by scores in descending order.
        """
        return sorted(self.players.items(), key=lambda x: x[1], reverse=True)

    def is_active(self) -> bool:
        """
        Check if the tournament is currently active.
        """
        now = datetime.now()
        return self.start_time <= now <= self.end_time

    def distribute_prizes(self) -> Dict[str, float]:
        """
        Distribute the prize pool to the top players after the tournament ends.
        """
        if datetime.now() <= self.end_time:
            raise ValueError("Tournament has not ended yet.")
        
        leaderboard = self.get_leaderboard()
        total_players = len(leaderboard)
        if total_players == 0:
            return {}  # No players participated
        
        # Simple prize distribution: 50%, 30%, 20% for top 3 players
        prize_distribution = [0.5, 0.3, 0.2]
        prizes = {}
        
        for idx, (player_id, _) in enumerate(leaderboard[:3]):  # Top 3 players
            prizes[player_id] = self.prize_pool * prize_distribution[idx]
        
        return prizes


class CasinoTournamentSystem:
    """
    Class to manage multiple tournaments in the online casino.
    """
    def __init__(self):
        self.tournaments: Dict[uuid.UUID, Tournament] = {}

    def create_tournament(self, name: str, prize_pool: float, start_time: datetime, end_time: datetime) -> uuid.UUID:
        """
        Create a new tournament and return its ID.
        """
        if start_time >= end_time:
            raise ValueError("Start time must be before end time.")
        
        tournament = Tournament(name, prize_pool, start_time, end_time)
        self.tournaments[tournament.id] = tournament
        return tournament.id

    def register_player(self, tournament_id: uuid.UUID, player_id: str):
        """
        Register a player for a specific tournament.
        """
        tournament = self._get_tournament(tournament_id)
        if not tournament.is_active():
            raise ValueError("Cannot register for a tournament that is not active.")
        tournament.register_player(player_id)

    def update_player_score(self, tournament_id: uuid.UUID, player_id: str, score: float):
        """
        Update a player's score in a specific tournament.
        """
        tournament = self._get_tournament(tournament_id)
        if not tournament.is_active():
            raise ValueError("Cannot update score for a tournament that is not active.")
        tournament.update_score(player_id, score)

    def get_leaderboard(self, tournament_id: uuid.UUID) -> List[Dict[str, float]]:
        """
        Get the leaderboard for a specific tournament.
        """
        tournament = self._get_tournament(tournament_id)
        return tournament.get_leaderboard()

    def distribute_prizes(self, tournament_id: uuid.UUID) -> Dict[str, float]:
        """
        Distribute prizes for a specific tournament after it ends.
        """
        tournament = self._get_tournament(tournament_id)
        return tournament.distribute_prizes()

    def _get_tournament(self, tournament_id: uuid.UUID) -> Tournament:
        """
        Helper function to retrieve a tournament by its ID.
        """
        if tournament_id not in self.tournaments:
            raise ValueError(f"Tournament with ID {tournament_id} does not exist.")
        return self.tournaments[tournament_id]


# Example usage:
if __name__ == "__main__":
    casino_system = CasinoTournamentSystem()

    # Create a new tournament
    start = datetime.now()
    end = start + timedelta(hours=1)
    tournament_id = casino_system.create_tournament("Poker Championship", 10000.0, start, end)

    # Register players
    casino_system.register_player(tournament_id, "player1")
    casino_system.register_player(tournament_id, "player2")

    # Update scores
    casino_system.update_player_score(tournament_id, "player1", 150.0)
    casino_system.update_player_score(tournament_id, "player2", 200.0)

    # Get leaderboard
    print(casino_system.get_leaderboard(tournament_id))

    # Distribute prizes (after the tournament ends)
    # Uncomment the following lines after the tournament duration has passed
    # prizes = casino_system.distribute_prizes(tournament_id)
    # print(prizes)
```
