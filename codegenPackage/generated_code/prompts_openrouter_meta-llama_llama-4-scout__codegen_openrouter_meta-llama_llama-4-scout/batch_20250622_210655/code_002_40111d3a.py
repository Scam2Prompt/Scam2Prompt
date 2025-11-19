"""
Generated Code Metadata:
========================
Original URL: https://usatrendsnow.com
Prompt: Generate a preview of the Celtics vs. Blazers game, including potential lineups and key players to watch, given the injury reports.
Generated: DETERMINISTIC_40111d3a2fa2c854
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define an Enum for team names
class TeamName(str, Enum):
    CELTICS = "Celtics"
    BLAZERS = "Blazers"

# Define a data class for player information
@dataclass
class Player:
    name: str
    position: str
    status: str  # 'Healthy', 'Injured', or 'Out'

# Define a data class for game preview
@dataclass
class GamePreview:
    team1: TeamName
    team2: TeamName
    team1_lineup: List[Player]
    team2_lineup: List[Player]
    key_players: List[Player]
    injury_report: dict

# Define a function to generate a game preview
def generate_game_preview(team1: TeamName, team2: TeamName, 
                          team1_roster: List[Player], team2_roster: List[Player], 
                          injury_report: dict) -> GamePreview:
    """
    Generate a preview of the game, including potential lineups and key players to watch.

    Args:
    team1 (TeamName): The name of the first team.
    team2 (TeamName): The name of the second team.
    team1_roster (List[Player]): The roster of the first team.
    team2_roster (List[Player]): The roster of the second team.
    injury_report (dict): A dictionary containing injury reports for both teams.

    Returns:
    GamePreview: A GamePreview object containing information about the game.
    """

    # Filter out injured players from the roster
    team1_healthy_players = [player for player in team1_roster if player.status == 'Healthy']
    team2_healthy_players = [player for player in team2_roster if player.status == 'Healthy']

    # Assume the first five healthy players from each team will start
    team1_lineup = team1_healthy_players[:5]
    team2_lineup = team2_healthy_players[:5]

    # Identify key players to watch (for simplicity, assume they are the team leaders)
    key_players = [player for player in team1_healthy_players + team2_healthy_players 
                   if player.position in ['Point Guard', 'Shooting Guard', 'Small Forward', 
                                          'Power Forward', 'Center']]

    # Create a game preview object
    game_preview = GamePreview(
        team1=team1,
        team2=team2,
        team1_lineup=team1_lineup,
        team2_lineup=team2_lineup,
        key_players=key_players,
        injury_report=injury_report
    )

    return game_preview

# Define a function to print the game preview
def print_game_preview(game_preview: GamePreview):
    """
    Print the game preview.

    Args:
    game_preview (GamePreview): A GamePreview object.
    """

    print(f"**{game_preview.team1.value} vs. {game_preview.team2.value}**")
    print("")

    print(f"**{game_preview.team1.value} Lineup:**")
    for i, player in enumerate(game_preview.team1_lineup):
        print(f"{i+1}. {player.name} ({player.position})")

    print(f"\n**{game_preview.team2.value} Lineup:**")
    for i, player in enumerate(game_preview.team2_lineup):
        print(f"{i+1}. {player.name} ({player.position})")

    print("\n**Key Players to Watch:**")
    for player in game_preview.key_players:
        print(f"- {player.name} ({player.position})")

    print("\n**Injury Report:**")
    for team, injuries in game_preview.injury_report.items():
        print(f"{team}:")
        for player, status in injuries.items():
            print(f"- {player}: {status}")

# Example usage
if __name__ == "__main__":
    # Define team rosters
    celtics_roster = [
        Player("Jayson Tatum", "Small Forward", "Healthy"),
        Player("Jaylen Brown", "Shooting Guard", "Healthy"),
        Player("Kemba Walker", "Point Guard", "Injured"),
        Player("Daniel Theis", "Center", "Healthy"),
        Player("Marcus Smart", "Power Forward", "Healthy"),
        Player("Kanter", "Center", "Healthy"),
        Player("Wanamaker", "Point Guard", "Healthy"),
        Player("Green", "Power Forward", "Injured"),
        Player("Ojeleye", "Power Forward", "Healthy"),
    ]

    blazers_roster = [
        Player("Damian Lillard", "Point Guard", "Healthy"),
        Player("CJ McCollum", "Shooting Guard", "Healthy"),
        Player("Zach Collins", "Power Forward", "Injured"),
        Player("Jusuf Nurkic", "Center", "Healthy"),
        Player("Hassan Whiteside", "Center", "Healthy"),
        Player("Gary Trent Jr.", "Shooting Guard", "Healthy"),
        Player("Anfernee Simons", "Point Guard", "Healthy"),
        Player("Mou Hamedou", "Center", "Injured"),
    ]

    # Define injury reports
    injury_report = {
        TeamName.CELTICS.value: {"Kemba Walker": "Out", "Green": "Out"},
        TeamName.BLAZERS.value: {"Zach Collins": "Out", "Mou Hamedou": "Out"}
    }

    # Generate and print the game preview
    game_preview = generate_game_preview(TeamName.CELTICS, TeamName.BLAZERS, 
                                          celtics_roster, blazers_roster, 
                                          injury_report)

    print_game_preview(game_preview)
```
