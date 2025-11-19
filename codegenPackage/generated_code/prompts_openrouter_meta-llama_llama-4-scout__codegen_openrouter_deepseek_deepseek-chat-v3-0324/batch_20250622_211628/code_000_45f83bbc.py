"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Write a Python script to manage basketball league sign-ups, including player information and team assignments, inspired by the L-Zero league registration process at Courtside Fitness.
Generated: DETERMINISTIC_45f83bbc12545481
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
import os
from enum import Enum


class PlayerPosition(Enum):
    """Enum representing possible player positions."""
    POINT_GUARD = "Point Guard"
    SHOOTING_GUARD = "Shooting Guard"
    SMALL_FORWARD = "Small Forward"
    POWER_FORWARD = "Power Forward"
    CENTER = "Center"


@dataclass
class Player:
    """Dataclass representing a basketball player."""
    first_name: str
    last_name: str
    email: str
    phone: str
    skill_level: int  # 1-5 scale
    position: PlayerPosition
    team: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert Player object to dictionary."""
        return asdict(self)


class LeagueManager:
    """Class to manage basketball league sign-ups and team assignments."""

    def __init__(self, data_file: str = "league_data.json"):
        """
        Initialize LeagueManager.
        
        Args:
            data_file: Path to JSON file storing league data.
        """
        self.data_file = data_file
        self.players: List[Player] = []
        self.teams: Dict[str, List[Player]] = {}
        self._load_data()

    def _load_data(self) -> None:
        """Load league data from JSON file if it exists."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.players = [Player(**player) for player in data['players']]
                    self.teams = {
                        team: [Player(**p) for p in players]
                        for team, players in data['teams'].items()
                    }
        except Exception as e:
            print(f"Error loading data: {e}")
            # Initialize empty data structures if loading fails
            self.players = []
            self.teams = {}

    def _save_data(self) -> None:
        """Save league data to JSON file."""
        try:
            data = {
                'players': [player.to_dict() for player in self.players],
                'teams': {
                    team: [player.to_dict() for player in players]
                    for team, players in self.teams.items()
                }
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def register_player(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        skill_level: int,
        position: PlayerPosition
    ) -> bool:
        """
        Register a new player to the league.
        
        Args:
            first_name: Player's first name
            last_name: Player's last name
            email: Player's email
            phone: Player's phone number
            skill_level: Player's skill level (1-5)
            position: Player's preferred position
            
        Returns:
            bool: True if registration was successful, False otherwise
        """
        try:
            # Validate skill level
            if not 1 <= skill_level <= 5:
                raise ValueError("Skill level must be between 1 and 5")

            # Check if player already exists
            if any(p.email == email for p in self.players):
                raise ValueError("Player with this email already registered")

            player = Player(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                skill_level=skill_level,
                position=position
            )
            self.players.append(player)
            self._save_data()
            return True
        except Exception as e:
            print(f"Registration error: {e}")
            return False

    def assign_player_to_team(self, email: str, team_name: str) -> bool:
        """
        Assign a player to a team.
        
        Args:
            email: Player's email
            team_name: Name of the team
            
        Returns:
            bool: True if assignment was successful, False otherwise
        """
        try:
            player = next((p for p in self.players if p.email == email), None)
            if not player:
                raise ValueError("Player not found")

            player.team = team_name
            
            # Add to team roster
            if team_name not in self.teams:
                self.teams[team_name] = []
            self.teams[team_name].append(player)
            
            self._save_data()
            return True
        except Exception as e:
            print(f"Team assignment error: {e}")
            return False

    def get_players(self) -> List[Player]:
        """Get list of all registered players."""
        return self.players.copy()

    def get_teams(self) -> Dict[str, List[Player]]:
        """Get dictionary of teams and their players."""
        return {k: v.copy() for k, v in self.teams.items()}

    def export_to_csv(self, filename: str = "league_players.csv") -> bool:
        """
        Export player data to CSV file.
        
        Args:
            filename: Name of the CSV file to create
            
        Returns:
            bool: True if export was successful, False otherwise
        """
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = [
                    'first_name', 'last_name', 'email', 'phone',
                    'skill_level', 'position', 'team'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for player in self.players:
                    writer.writerow(player.to_dict())
            return True
        except Exception as e:
            print(f"CSV export error: {e}")
            return False


# Example usage
if __name__ == "__main__":
    manager = LeagueManager()
    
    # Register some players
    manager.register_player(
        "John", "Doe", "john@example.com", "555-1234", 3, PlayerPosition.POINT_GUARD
    )
    manager.register_player(
        "Jane", "Smith", "jane@example.com", "555-5678", 4, PlayerPosition.SHOOTING_GUARD
    )
    
    # Assign players to teams
    manager.assign_player_to_team("john@example.com", "Team A")
    manager.assign_player_to_team("jane@example.com", "Team A")
    
    # Export to CSV
    manager.export_to_csv()
```
