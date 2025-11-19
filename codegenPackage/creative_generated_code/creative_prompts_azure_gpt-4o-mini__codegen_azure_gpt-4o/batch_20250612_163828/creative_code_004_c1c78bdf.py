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

Here's a production-ready implementation in Python for setting up a tournament lobby with player matchmaking and team assignments:

```python
import random
from typing import List, Dict, Tuple


class Player:
    """
    Represents a player in the tournament.
    """
    def __init__(self, player_id: str, skill_level: int):
        self.player_id = player_id
        self.skill_level = skill_level


class Lobby:
    """
    Represents the tournament lobby, responsible for matchmaking and team assignments.
    """
    def __init__(self, max_players: int, team_count: int = 2):
        """
        Initialize a lobby with the given maximum players and team count.
        :param max_players: Maximum number of players allowed in the lobby.
        :param team_count: Number of teams to assign players to.
        """
        if team_count < 2:
            raise ValueError("There must be at least two teams.")
        self.max_players = max_players
        self.team_count = team_count
        self.players = []

    def add_player(self, player: Player) -> None:
        """
        Add a player to the lobby.
        :param player: The player to add.
        """
        if len(self.players) >= self.max_players:
            raise ValueError("Lobby is full. Cannot add more players.")
        self.players.append(player)

    def matchmaking(self) -> List[Tuple[Player, Player]]:
        """
        Pair players based on their skill levels for matchmaking.
        :return: List of tuples representing matched player pairs.
        """
        # Sort players by skill level
        sorted_players = sorted(self.players, key=lambda p: p.skill_level)
        matched_pairs = []

        # Create pairs (top skill paired with bottom skill to balance)
        while len(sorted_players) >= 2:
            high_skill_player = sorted_players.pop()
            low_skill_player = sorted_players.pop(0)
            matched_pairs.append((high_skill_player, low_skill_player))

        # Return matched pairs
        return matched_pairs

    def assign_teams(self) -> Dict[int, List[Player]]:
        """
        Assign players to teams randomly.
        :return: A dictionary mapping team numbers to lists of players.
        """
        random.shuffle(self.players)  # Shuffle players for random assignment
        teams = {i: [] for i in range(1, self.team_count + 1)}

        # Distribute players across teams
        for i, player in enumerate(self.players):
            team_number = (i % self.team_count) + 1
            teams[team_number].append(player)

        return teams


# Example usage
def main():
    try:
        # Create a lobby with a maximum of 10 players and 2 teams
        lobby = Lobby(max_players=10, team_count=2)

        # Add players to the lobby
        lobby.add_player(Player("Player1", 85))
        lobby.add_player(Player("Player2", 70))
        lobby.add_player(Player("Player3", 90))
        lobby.add_player(Player("Player4", 60))
        lobby.add_player(Player("Player5", 75))
        lobby.add_player(Player("Player6", 80))

        # Perform matchmaking
        print("Matchmaking results:")
        matches = lobby.matchmaking()
        for pair in matches:
            print(f"{pair[0].player_id} (Skill {pair[0].skill_level}) vs {pair[1].player_id} (Skill {pair[1].skill_level})")

        # Assign teams
        print("\nTeam assignments:")
        teams = lobby.assign_teams()
        for team_number, players in teams.items():
            print(f"Team {team_number}: {[player.player_id for player in players]}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
