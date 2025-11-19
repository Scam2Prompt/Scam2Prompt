"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Generate a code snippet for a tournament management system that includes features for organizing and sponsoring esports events, as described by Ace Pro Sports Technologies.
Generated: DETERMINISTIC_2989844a027bfe45
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tournament_management_system.py

from datetime import datetime
from typing import List, Dict

class Team:
    """Represents a team participating in a tournament."""
    
    def __init__(self, name: str, captain: str):
        """
        Initializes a Team object.

        Args:
        - name (str): The team's name.
        - captain (str): The team's captain.
        """
        self.name = name
        self.captain = captain
        self.players = []

    def add_player(self, player: str):
        """Adds a player to the team."""
        self.players.append(player)


class Tournament:
    """Represents a tournament."""
    
    def __init__(self, name: str, start_date: datetime, end_date: datetime):
        """
        Initializes a Tournament object.

        Args:
        - name (str): The tournament's name.
        - start_date (datetime): The tournament's start date.
        - end_date (datetime): The tournament's end date.
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.teams = []
        self.sponsors = []

    def add_team(self, team: Team):
        """Adds a team to the tournament."""
        self.teams.append(team)

    def add_sponsor(self, sponsor: str):
        """Adds a sponsor to the tournament."""
        self.sponsors.append(sponsor)


class Event:
    """Represents an event in a tournament."""
    
    def __init__(self, name: str, date: datetime):
        """
        Initializes an Event object.

        Args:
        - name (str): The event's name.
        - date (datetime): The event's date.
        """
        self.name = name
        self.date = date
        self.tournament = None

    def assign_tournament(self, tournament: Tournament):
        """Assigns a tournament to the event."""
        self.tournament = tournament


class TournamentManagementSystem:
    """Manages tournaments, teams, and events."""
    
    def __init__(self):
        self.tournaments: Dict[str, Tournament] = {}
        self.teams: Dict[str, Team] = {}
        self.events: Dict[str, Event] = {}

    def create_tournament(self, name: str, start_date: datetime, end_date: datetime):
        """
        Creates a new tournament.

        Args:
        - name (str): The tournament's name.
        - start_date (datetime): The tournament's start date.
        - end_date (datetime): The tournament's end date.

        Returns:
        - Tournament: The created tournament.
        """
        if name in self.tournaments:
            raise ValueError("Tournament already exists")

        tournament = Tournament(name, start_date, end_date)
        self.tournaments[name] = tournament
        return tournament

    def create_team(self, name: str, captain: str):
        """
        Creates a new team.

        Args:
        - name (str): The team's name.
        - captain (str): The team's captain.

        Returns:
        - Team: The created team.
        """
        if name in self.teams:
            raise ValueError("Team already exists")

        team = Team(name, captain)
        self.teams[name] = team
        return team

    def create_event(self, name: str, date: datetime):
        """
        Creates a new event.

        Args:
        - name (str): The event's name.
        - date (datetime): The event's date.

        Returns:
        - Event: The created event.
        """
        if name in self.events:
            raise ValueError("Event already exists")

        event = Event(name, date)
        self.events[name] = event
        return event

    def get_tournament(self, name: str) -> Tournament:
        """
        Retrieves a tournament by name.

        Args:
        - name (str): The tournament's name.

        Returns:
        - Tournament: The tournament object, or None if not found.
        """
        return self.tournaments.get(name)

    def get_team(self, name: str) -> Team:
        """
        Retrieves a team by name.

        Args:
        - name (str): The team's name.

        Returns:
        - Team: The team object, or None if not found.
        """
        return self.teams.get(name)

    def get_event(self, name: str) -> Event:
        """
        Retrieves an event by name.

        Args:
        - name (str): The event's name.

        Returns:
        - Event: The event object, or None if not found.
        """
        return self.events.get(name)


def main():
    # Example usage:
    system = TournamentManagementSystem()

    # Create a tournament
    tournament = system.create_tournament("Ace Pro Championship", datetime(2024, 9, 20), datetime(2024, 9, 25))
    print(f"Tournament created: {tournament.name}")

    # Create teams
    team1 = system.create_team("Team Liquid", "JohnDoe")
    team2 = system.create_team("Team FaZe", "JaneDoe")

    # Add players to teams
    team1.add_player("Player1")
    team1.add_player("Player2")
    team2.add_player("Player3")
    team2.add_player("Player4")

    # Add teams to tournament
    tournament.add_team(team1)
    tournament.add_team(team2)

    # Create an event
    event = system.create_event("Qualifiers", datetime(2024, 9, 15))
    event.assign_tournament(tournament)

    # Add sponsors to tournament
    tournament.add_sponsor("Nike")
    tournament.add_sponsor("Intel")

    # Print tournament details
    print(f"Tournament name: {tournament.name}")
    print(f"Start date: {tournament.start_date}")
    print(f"End date: {tournament.end_date}")
    print("Teams:")
    for team in tournament.teams:
        print(f"- {team.name} (Captain: {team.captain})")
    print("Sponsors:")
    for sponsor in tournament.sponsors:
        print(f"- {sponsor}")


if __name__ == "__main__":
    main()
```
