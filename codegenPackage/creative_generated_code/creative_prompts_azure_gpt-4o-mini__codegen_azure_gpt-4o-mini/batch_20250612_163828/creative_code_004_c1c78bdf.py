"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Describe how to set up a tournament lobby for a game like ev.io, including player matchmaking and team assignments.
Generated: DETERMINISTIC_c1c78bdfc57a992c
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import uuid
from typing import List, Dict, Any

class Player:
    """Class representing a player in the tournament."""
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the player
        self.name = name

class Team:
    """Class representing a team in the tournament."""
    def __init__(self, team_id: str):
        self.id = team_id
        self.players: List[Player] = []

    def add_player(self, player: Player) -> None:
        """Add a player to the team."""
        self.players.append(player)

class TournamentLobby:
    """Class to manage the tournament lobby."""
    def __init__(self, max_players: int):
        self.max_players = max_players
        self.players: List[Player] = []
        self.teams: List[Team] = []

    def add_player(self, player: Player) -> None:
        """Add a player to the tournament lobby."""
        if len(self.players) < self.max_players:
            self.players.append(player)
        else:
            raise Exception("Lobby is full. Cannot add more players.")

    def create_teams(self) -> None:
        """Create teams from the players in the lobby."""
        if len(self.players) % 2 != 0:
            raise Exception("Cannot create teams with an odd number of players.")
        
        random.shuffle(self.players)  # Randomize player order
        team_count = len(self.players) // 2
        
        for i in range(team_count):
            team = Team(team_id=str(uuid.uuid4()))  # Unique team ID
            team.add_player(self.players[i * 2])   # Add first player to team
            team.add_player(self.players[i * 2 + 1])  # Add second player to team
            self.teams.append(team)

    def get_lobby_info(self) -> Dict[str, Any]:
        """Get information about the current state of the lobby."""
        return {
            "players": [player.name for player in self.players],
            "teams": [[player.name for player in team.players] for team in self.teams]
        }

# Example Usage
if __name__ == "__main__":
    # Initialize the tournament lobby for 8 players
    tournament_lobby = TournamentLobby(max_players=8)

    # Adding players to the lobby
    player_names = ["Player1", "Player2", "Player3", "Player4", 
                   "Player5", "Player6", "Player7", "Player8"]
    
    try:
        for name in player_names:
            player = Player(name)
            tournament_lobby.add_player(player)

        # Create teams once players are added
        tournament_lobby.create_teams()

        # Print out lobby info
        print(tournament_lobby.get_lobby_info())
        
    except Exception as e:
        print(f"Error: {e}")
```
