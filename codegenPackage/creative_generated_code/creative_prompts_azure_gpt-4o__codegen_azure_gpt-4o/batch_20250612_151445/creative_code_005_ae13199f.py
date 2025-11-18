"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Write code to manage a poker tournament system with weekly and seasonal events, inspired by DominoBet's tournament structure.
Generated: DETERMINISTIC_ae13199fa9375ae4
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict


class Player:
    """
    Represents a poker player in the tournament system.
    """
    def __init__(self, player_id: int, name: str):
        self.player_id = player_id
        self.name = name
        self.score = 0

    def update_score(self, points: int):
        """
        Updates the player's score with the given points.
        :param points: Number of points to add to the player's score.
        """
        if points < 0:
            raise ValueError("Points must be a positive number.")
        self.score += points

    def __str__(self):
        return f"Player {self.name} (ID: {self.player_id}) - Score: {self.score}"


class Tournament:
    """
    Manages weekly and seasonal poker tournaments.
    """
    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.players: Dict[int, Player] = {}

    def add_player(self, player: Player):
        """
        Adds a player to the tournament.
        :param player: Player object to add.
        """
        if player.player_id in self.players:
            raise ValueError(f"Player with ID {player.player_id} is already registered.")
        self.players[player.player_id] = player

    def record_score(self, player_id: int, points: int):
        """
        Records the score for a player in the tournament.
        :param player_id: ID of the player to record the score for.
        :param points: Points to add to the player's score.
        """
        if player_id not in self.players:
            raise ValueError(f"No player found with ID {player_id}.")
        self.players[player_id].update_score(points)

    def get_leaderboard(self) -> List[Player]:
        """
        Returns the leaderboard sorted by player scores in descending order.
        """
        return sorted(self.players.values(), key=lambda p: p.score, reverse=True)

    def __str__(self):
        return f"Tournament '{self.name}' from {self.start_date} to {self.end_date}"


class PokerTournamentSystem:
    """
    Manages weekly and seasonal poker tournaments.
    """
    def __init__(self):
        self.weekly_tournaments: List[Tournament] = []
        self.seasonal_tournaments: List[Tournament] = []

    def create_tournament(self, name: str, start_date: datetime.date, end_date: datetime.date, is_weekly: bool):
        """
        Creates a new poker tournament and adds it to either weekly or seasonal tournaments.
        :param name: Name of the tournament.
        :param start_date: Start date of the tournament.
        :param end_date: End date of the tournament.
        :param is_weekly: Boolean to determine if the tournament is weekly or seasonal.
        """
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")

        tournament = Tournament(name, start_date, end_date)

        if is_weekly:
            self.weekly_tournaments.append(tournament)
        else:
            self.seasonal_tournaments.append(tournament)

    def list_tournaments(self, is_weekly: bool) -> List[Tournament]:
        """
        Lists all tournaments, either weekly or seasonal.
        :param is_weekly: Boolean to determine if weekly or seasonal tournaments are listed.
        """
        return self.weekly_tournaments if is_weekly else self.seasonal_tournaments


# Example usage:

if __name__ == "__main__":
    # Create the poker tournament system
    system = PokerTournamentSystem()

    # Create a weekly tournament
    system.create_tournament(
        name="Weekly Poker Challenge",
        start_date=datetime.date(2023, 10, 1),
        end_date=datetime.date(2023, 10, 7),
        is_weekly=True
    )

    # Create a seasonal tournament
    system.create_tournament(
        name="Fall Poker Championship",
        start_date=datetime.date(2023, 10, 1),
        end_date=datetime.date(2023, 12, 31),
        is_weekly=False
    )

    # Add players to the weekly tournament
    weekly_tournament = system.weekly_tournaments[0]

    player_1 = Player(player_id=1, name="Alice")
    player_2 = Player(player_id=2, name="Bob")

    weekly_tournament.add_player(player_1)
    weekly_tournament.add_player(player_2)

    # Record scores
    weekly_tournament.record_score(player_id=1, points=50)
    weekly_tournament.record_score(player_id=2, points=30)

    # Display leaderboard
    leaderboard = weekly_tournament.get_leaderboard()
    for player in leaderboard:
        print(player)

    # Display tournaments
    print("\nWeekly Tournaments:")
    for tournament in system.list_tournaments(is_weekly=True):
        print(tournament)

    print("\nSeasonal Tournaments:")
    for tournament in system.list_tournaments(is_weekly=False):
        print(tournament)
```
