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
import json
from typing import List, Dict, Optional

class Player:
    """Class to represent a basketball player."""
    
    def __init__(self, name: str, age: int, skill_level: str):
        self.name = name
        self.age = age
        self.skill_level = skill_level

    def to_dict(self) -> Dict:
        """Convert player information to a dictionary."""
        return {
            "name": self.name,
            "age": self.age,
            "skill_level": self.skill_level
        }

class Team:
    """Class to represent a basketball team."""
    
    def __init__(self, team_name: str):
        self.team_name = team_name
        self.players: List[Player] = []

    def add_player(self, player: Player) -> None:
        """Add a player to the team."""
        self.players.append(player)

    def to_dict(self) -> Dict:
        """Convert team information to a dictionary."""
        return {
            "team_name": self.team_name,
            "players": [player.to_dict() for player in self.players]
        }

class League:
    """Class to manage the basketball league."""
    
    def __init__(self):
        self.teams: List[Team] = []

    def create_team(self, team_name: str) -> None:
        """Create a new team in the league."""
        team = Team(team_name)
        self.teams.append(team)

    def sign_up_player(self, team_name: str, player: Player) -> Optional[str]:
        """Sign up a player to a specific team."""
        for team in self.teams:
            if team.team_name == team_name:
                team.add_player(player)
                return None
        return f"Team '{team_name}' not found."

    def save_to_file(self, filename: str) -> None:
        """Save league data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([team.to_dict() for team in self.teams], file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load league data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                teams_data = json.load(file)
                for team_data in teams_data:
                    team = Team(team_data['team_name'])
                    for player_data in team_data['players']:
                        player = Player(player_data['name'], player_data['age'], player_data['skill_level'])
                        team.add_player(player)
                    self.teams.append(team)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

def main():
    """Main function to manage league sign-ups."""
    league = League()
    
    # Example usage
    league.create_team("Warriors")
    league.create_team("Lakers")

    player1 = Player("John Doe", 25, "Intermediate")
    player2 = Player("Jane Smith", 22, "Beginner")

    error = league.sign_up_player("Warriors", player1)
    if error:
        print(error)

    error = league.sign_up_player("Lakers", player2)
    if error:
        print(error)

    # Save league data to a file
    league.save_to_file("league_data.json")

    # Load league data from a file
    league.load_from_file("league_data.json")

if __name__ == "__main__":
    main()
```
