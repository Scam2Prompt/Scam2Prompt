"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Write a Python script to manage esports tournament data, including team and player information, match schedules, and scores, inspired by Ace Pro Sports Technologies' operations in Kenya.
Generated: DETERMINISTIC_019c2ede139d2c54
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class Player:
    """Class to represent a player in the esports tournament."""
    
    def __init__(self, player_id: int, name: str, team: str):
        self.player_id = player_id
        self.name = name
        self.team = team

    def to_dict(self) -> Dict:
        """Convert player information to a dictionary."""
        return {
            "player_id": self.player_id,
            "name": self.name,
            "team": self.team
        }

class Team:
    """Class to represent a team in the esports tournament."""
    
    def __init__(self, team_id: int, name: str):
        self.team_id = team_id
        self.name = name
        self.players: List[Player] = []

    def add_player(self, player: Player):
        """Add a player to the team."""
        self.players.append(player)

    def to_dict(self) -> Dict:
        """Convert team information to a dictionary."""
        return {
            "team_id": self.team_id,
            "name": self.name,
            "players": [player.to_dict() for player in self.players]
        }

class Match:
    """Class to represent a match in the esports tournament."""
    
    def __init__(self, match_id: int, team_a: Team, team_b: Team, match_time: datetime):
        self.match_id = match_id
        self.team_a = team_a
        self.team_b = team_b
        self.match_time = match_time
        self.score_a: Optional[int] = None
        self.score_b: Optional[int] = None

    def set_scores(self, score_a: int, score_b: int):
        """Set the scores for the match."""
        self.score_a = score_a
        self.score_b = score_b

    def to_dict(self) -> Dict:
        """Convert match information to a dictionary."""
        return {
            "match_id": self.match_id,
            "team_a": self.team_a.to_dict(),
            "team_b": self.team_b.to_dict(),
            "match_time": self.match_time.isoformat(),
            "score_a": self.score_a,
            "score_b": self.score_b
        }

class Tournament:
    """Class to manage the esports tournament data."""
    
    def __init__(self, name: str):
        self.name = name
        self.teams: List[Team] = []
        self.matches: List[Match] = []

    def add_team(self, team: Team):
        """Add a team to the tournament."""
        self.teams.append(team)

    def schedule_match(self, match: Match):
        """Schedule a match in the tournament."""
        self.matches.append(match)

    def save_to_file(self, filename: str):
        """Save tournament data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({
                    "tournament_name": self.name,
                    "teams": [team.to_dict() for team in self.teams],
                    "matches": [match.to_dict() for match in self.matches]
                }, file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """Load tournament data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.name = data["tournament_name"]
                self.teams = [Team(**team) for team in data["teams"]]
                self.matches = [Match(**match) for match in data["matches"]]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    # Create tournament
    tournament = Tournament("Kenya Esports Championship")

    # Create teams
    team1 = Team(1, "Team Alpha")
    team2 = Team(2, "Team Beta")

    # Add players to teams
    team1.add_player(Player(1, "Alice", "Team Alpha"))
    team1.add_player(Player(2, "Bob", "Team Alpha"))
    team2.add_player(Player(3, "Charlie", "Team Beta"))
    team2.add_player(Player(4, "David", "Team Beta"))

    # Add teams to tournament
    tournament.add_team(team1)
    tournament.add_team(team2)

    # Schedule a match
    match_time = datetime(2023, 10, 15, 18, 0)
    match = Match(1, team1, team2, match_time)
    tournament.schedule_match(match)

    # Save tournament data to a file
    tournament.save_to_file("tournament_data.json")

    # Load tournament data from a file
    tournament.load_from_file("tournament_data.json")
```
