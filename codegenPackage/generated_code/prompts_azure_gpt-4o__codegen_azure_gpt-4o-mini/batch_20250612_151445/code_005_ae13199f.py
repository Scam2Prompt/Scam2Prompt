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
import datetime
from typing import List, Optional

class Player:
    """Class representing a player in the poker tournament."""
    
    def __init__(self, name: str):
        self.name = name
        self.points = 0  # Points accumulated by the player

    def add_points(self, points: int):
        """Add points to the player's total."""
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.points += points

class Tournament:
    """Class representing a poker tournament."""
    
    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.players: List[Player] = []

    def add_player(self, player: Player):
        """Add a player to the tournament."""
        if player in self.players:
            raise ValueError(f"Player {player.name} is already registered.")
        self.players.append(player)

    def remove_player(self, player: Player):
        """Remove a player from the tournament."""
        try:
            self.players.remove(player)
        except ValueError:
            raise ValueError(f"Player {player.name} is not registered in the tournament.")

    def award_points(self, player: Player, points: int):
        """Award points to a player in the tournament."""
        if player not in self.players:
            raise ValueError(f"Player {player.name} is not registered in the tournament.")
        player.add_points(points)

class TournamentManager:
    """Class to manage multiple poker tournaments."""
    
    def __init__(self):
        self.tournaments: List[Tournament] = []

    def create_tournament(self, name: str, start_date: datetime.date, end_date: datetime.date) -> Tournament:
        """Create a new tournament and add it to the manager."""
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")
        tournament = Tournament(name, start_date, end_date)
        self.tournaments.append(tournament)
        return tournament

    def get_active_tournaments(self) -> List[Tournament]:
        """Return a list of active tournaments."""
        today = datetime.date.today()
        return [tournament for tournament in self.tournaments if tournament.start_date <= today <= tournament.end_date]

# Example usage
if __name__ == "__main__":
    manager = TournamentManager()
    
    # Create a weekly tournament
    weekly_tournament = manager.create_tournament("Weekly Poker Night", datetime.date(2023, 10, 1), datetime.date(2023, 10, 31))
    
    # Create players
    player1 = Player("Alice")
    player2 = Player("Bob")
    
    # Add players to the tournament
    weekly_tournament.add_player(player1)
    weekly_tournament.add_player(player2)
    
    # Award points to players
    weekly_tournament.award_points(player1, 10)
    weekly_tournament.award_points(player2, 5)
    
    # Display active tournaments
    active_tournaments = manager.get_active_tournaments()
    for tournament in active_tournaments:
        print(f"Active Tournament: {tournament.name}, Players: {[player.name for player in tournament.players]}")
```
