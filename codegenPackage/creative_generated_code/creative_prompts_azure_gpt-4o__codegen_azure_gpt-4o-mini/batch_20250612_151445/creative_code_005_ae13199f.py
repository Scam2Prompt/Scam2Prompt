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
from typing import List, Optional

class Tournament:
    """
    A class to represent a poker tournament.
    """
    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date, buy_in: float):
        """
        Initialize a new Tournament instance.

        :param name: The name of the tournament.
        :param start_date: The start date of the tournament.
        :param end_date: The end date of the tournament.
        :param buy_in: The buy-in amount for the tournament.
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.buy_in = buy_in
        self.participants: List[str] = []

    def add_participant(self, player_name: str) -> None:
        """
        Add a participant to the tournament.

        :param player_name: The name of the player to add.
        :raises ValueError: If the player is already registered or the tournament is over.
        """
        if player_name in self.participants:
            raise ValueError(f"Player {player_name} is already registered.")
        if datetime.date.today() > self.end_date:
            raise ValueError("Cannot add participant: Tournament has already ended.")
        self.participants.append(player_name)

    def remove_participant(self, player_name: str) -> None:
        """
        Remove a participant from the tournament.

        :param player_name: The name of the player to remove.
        :raises ValueError: If the player is not registered.
        """
        if player_name not in self.participants:
            raise ValueError(f"Player {player_name} is not registered.")
        self.participants.remove(player_name)

    def get_details(self) -> str:
        """
        Get the details of the tournament.

        :return: A formatted string with tournament details.
        """
        return (f"Tournament: {self.name}\n"
                f"Dates: {self.start_date} to {self.end_date}\n"
                f"Buy-in: ${self.buy_in}\n"
                f"Participants: {len(self.participants)}")

class TournamentManager:
    """
    A class to manage multiple poker tournaments.
    """
    def __init__(self):
        """
        Initialize the TournamentManager with an empty list of tournaments.
        """
        self.tournaments: List[Tournament] = []

    def add_tournament(self, tournament: Tournament) -> None:
        """
        Add a new tournament to the manager.

        :param tournament: A Tournament instance to add.
        :raises ValueError: If the tournament's dates are invalid.
        """
        if tournament.start_date >= tournament.end_date:
            raise ValueError("Tournament start date must be before the end date.")
        self.tournaments.append(tournament)

    def get_tournaments(self) -> List[str]:
        """
        Get a list of all tournament details.

        :return: A list of formatted strings with tournament details.
        """
        return [tournament.get_details() for tournament in self.tournaments]

    def find_tournament(self, name: str) -> Optional[Tournament]:
        """
        Find a tournament by name.

        :param name: The name of the tournament to find.
        :return: The Tournament instance if found, else None.
        """
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament
        return None

# Example Usage
if __name__ == "__main__":
    # Create a TournamentManager instance
    manager = TournamentManager()

    # Create a new tournament
    tournament1 = Tournament("Weekly Poker Night", datetime.date(2023, 10, 1), datetime.date(2023, 10, 7), 50.0)

    # Add tournament to manager
    try:
        manager.add_tournament(tournament1)
    except ValueError as e:
        print(f"Error adding tournament: {e}")

    # Register participants
    try:
        tournament1.add_participant("Alice")
        tournament1.add_participant("Bob")
        tournament1.add_participant("Alice")  # This line will raise an error
    except ValueError as e:
        print(f"Error adding participant: {e}")

    # Display tournament details
    for details in manager.get_tournaments():
        print(details)

    # Remove participant
    try:
        tournament1.remove_participant("Bob")
    except ValueError as e:
        print(f"Error removing participant: {e}")

    # Display updated tournament details
    print("\nUpdated Tournament Details:")
    for details in manager.get_tournaments():
        print(details)
```
