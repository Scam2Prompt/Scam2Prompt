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
import uuid
from datetime import datetime
from typing import List, Optional

class Tournament:
    """Class representing an esports tournament."""
    
    def __init__(self, name: str, date: str, location: str):
        """
        Initialize a new tournament.

        :param name: Name of the tournament
        :param date: Date of the tournament in YYYY-MM-DD format
        :param location: Location of the tournament
        """
        self.id = uuid.uuid4()  # Unique identifier for the tournament
        self.name = name
        self.date = self._validate_date(date)
        self.location = location
        self.teams = []  # List to hold participating teams
        self.sponsors = []  # List to hold sponsors

    def _validate_date(self, date: str) -> datetime:
        """Validate and convert date string to a datetime object."""
        try:
            return datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

    def add_team(self, team_name: str):
        """Add a team to the tournament."""
        if team_name not in self.teams:
            self.teams.append(team_name)
        else:
            raise ValueError(f"Team '{team_name}' is already registered.")

    def add_sponsor(self, sponsor_name: str):
        """Add a sponsor to the tournament."""
        if sponsor_name not in self.sponsors:
            self.sponsors.append(sponsor_name)
        else:
            raise ValueError(f"Sponsor '{sponsor_name}' is already added.")

    def get_details(self) -> dict:
        """Get the details of the tournament."""
        return {
            "id": str(self.id),
            "name": self.name,
            "date": self.date.strftime("%Y-%m-%d"),
            "location": self.location,
            "teams": self.teams,
            "sponsors": self.sponsors
        }

class TournamentManager:
    """Class to manage multiple tournaments."""
    
    def __init__(self):
        """Initialize the tournament manager."""
        self.tournaments: List[Tournament] = []

    def create_tournament(self, name: str, date: str, location: str) -> Tournament:
        """Create a new tournament and add it to the manager."""
        tournament = Tournament(name, date, location)
        self.tournaments.append(tournament)
        return tournament

    def find_tournament(self, tournament_id: str) -> Optional[Tournament]:
        """Find a tournament by its ID."""
        for tournament in self.tournaments:
            if str(tournament.id) == tournament_id:
                return tournament
        return None

    def list_tournaments(self) -> List[dict]:
        """List all tournaments with their details."""
        return [tournament.get_details() for tournament in self.tournaments]

# Example usage
if __name__ == "__main__":
    manager = TournamentManager()
    
    # Create a new tournament
    try:
        tournament = manager.create_tournament("Summer Championship", "2023-08-15", "Los Angeles")
        tournament.add_team("Team A")
        tournament.add_team("Team B")
        tournament.add_sponsor("Ace Pro Sports Technologies")
        
        # Print tournament details
        print(tournament.get_details())
        
        # List all tournaments
        print(manager.list_tournaments())
    except Exception as e:
        print(f"An error occurred: {e}")
```
