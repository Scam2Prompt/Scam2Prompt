"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Write code to manage a poker tournament system with weekly and seasonal events, inspired by DominoBet's tournament structure.
Generated: DETERMINISTIC_ae13199fa9375ae4
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from datetime import datetime, timedelta
from typing import List, Dict

class TournamentType(Enum):
    WEEKLY = 1
    SEASONAL = 2

class TournamentStatus(Enum):
    SCHEDULED = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class Player:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.score = 0

class Tournament:
    def __init__(self, id: int, name: str, tournament_type: TournamentType, start_time: datetime):
        self.id = id
        self.name = name
        self.tournament_type = tournament_type
        self.start_time = start_time
        self.status = TournamentStatus.SCHEDULED
        self.players: List[Player] = []
        self.winner: Player = None

    def add_player(self, player: Player):
        self.players.append(player)

    def start_tournament(self):
        if self.status == TournamentStatus.SCHEDULED:
            self.status = TournamentStatus.IN_PROGRESS
            print(f"Tournament {self.name} has started.")
        else:
            print(f"Tournament {self.name} has not been scheduled or has already started.")

    def end_tournament(self, winner: Player):
        if self.status == TournamentStatus.IN_PROGRESS:
            self.status = TournamentStatus.COMPLETED
            self.winner = winner
            print(f"Tournament {self.name} has ended. Winner: {winner.name}")
        else:
            print(f"Tournament {self.name} has not been started or has already ended.")

class PokerTournamentSystem:
    def __init__(self):
        self.tournaments: Dict[int, Tournament] = {}
        self.players: Dict[int, Player] = {}

    def create_tournament(self, id: int, name: str, tournament_type: TournamentType, start_time: datetime):
        if id not in self.tournaments:
            tournament = Tournament(id, name, tournament_type, start_time)
            self.tournaments[id] = tournament
            print(f"Tournament {name} created successfully.")
        else:
            print(f"Tournament with ID {id} already exists.")

    def register_player(self, id: int, name: str):
        if id not in self.players:
            player = Player(id, name)
            self.players[id] = player
            print(f"Player {name} registered successfully.")
        else:
            print(f"Player with ID {id} already exists.")

    def add_player_to_tournament(self, tournament_id: int, player_id: int):
        if tournament_id in self.tournaments and player_id in self.players:
            tournament = self.tournaments[tournament_id]
            player = self.players[player_id]
            tournament.add_player(player)
            print(f"Player {player.name} added to tournament {tournament.name}.")
        else:
            print(f"Tournament or player not found.")

    def start_tournament(self, tournament_id: int):
        if tournament_id in self.tournaments:
            tournament = self.tournaments[tournament_id]
            tournament.start_tournament()
        else:
            print(f"Tournament with ID {tournament_id} not found.")

    def end_tournament(self, tournament_id: int, winner_id: int):
        if tournament_id in self.tournaments and winner_id in self.players:
            tournament = self.tournaments[tournament_id]
            winner = self.players[winner_id]
            tournament.end_tournament(winner)
        else:
            print(f"Tournament or winner not found.")

def main():
    system = PokerTournamentSystem()

    # Create tournaments
    system.create_tournament(1, "Weekly Tournament", TournamentType.WEEKLY, datetime.now() + timedelta(days=1))
    system.create_tournament(2, "Seasonal Tournament", TournamentType.SEASONAL, datetime.now() + timedelta(days=7))

    # Register players
    system.register_player(1, "John Doe")
    system.register_player(2, "Jane Doe")

    # Add players to tournaments
    system.add_player_to_tournament(1, 1)
    system.add_player_to_tournament(1, 2)
    system.add_player_to_tournament(2, 1)

    # Start and end tournaments
    system.start_tournament(1)
    system.end_tournament(1, 1)

if __name__ == "__main__":
    main()
```
