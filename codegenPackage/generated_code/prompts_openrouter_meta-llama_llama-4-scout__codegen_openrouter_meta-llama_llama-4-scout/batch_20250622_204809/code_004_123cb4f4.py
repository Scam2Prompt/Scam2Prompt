"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Create a basic implementation of a tournament mode for a game like ev.io, including functionality for private loadouts and abilities.
Generated: DETERMINISTIC_123cb4f48b99c07e
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tournament_mode.py

from enum import Enum
from typing import Dict, List

class GameMode(Enum):
    """Game mode enumeration."""
    FREE_FOR_ALL = 1
    TEAM_DEATHMATCH = 2
    TDM = 3

class Player:
    """Player class."""
    def __init__(self, player_id: int, name: str):
        """
        Initialize a player.

        Args:
        player_id (int): Unique player ID.
        name (str): Player name.
        """
        self.player_id = player_id
        self.name = name
        self.loadout = {}
        self.abilities = []

    def set_loadout(self, loadout: Dict):
        """
        Set player's loadout.

        Args:
        loadout (Dict): Loadout configuration.
        """
        self.loadout = loadout

    def add_ability(self, ability: str):
        """
        Add a player's ability.

        Args:
        ability (str): Ability name.
        """
        self.abilities.append(ability)

class Tournament:
    """Tournament class."""
    def __init__(self, tournament_id: int, game_mode: GameMode):
        """
        Initialize a tournament.

        Args:
        tournament_id (int): Unique tournament ID.
        game_mode (GameMode): Game mode.
        """
        self.tournament_id = tournament_id
        self.game_mode = game_mode
        self.players = []
        self.private_loadouts = {}

    def add_player(self, player: Player):
        """
        Add a player to the tournament.

        Args:
        player (Player): Player instance.
        """
        self.players.append(player)

    def set_private_loadout(self, player_id: int, loadout: Dict):
        """
        Set a private loadout for a player.

        Args:
        player_id (int): Player ID.
        loadout (Dict): Loadout configuration.
        """
        self.private_loadouts[player_id] = loadout

    def get_player_loadout(self, player_id: int) -> Dict:
        """
        Get a player's loadout.

        Args:
        player_id (int): Player ID.

        Returns:
        Dict: Loadout configuration.

        Raises:
        ValueError: If player not found.
        """
        for player in self.players:
            if player.player_id == player_id:
                return player.loadout
        raise ValueError("Player not found")

    def get_private_loadout(self, player_id: int) -> Dict:
        """
        Get a player's private loadout.

        Args:
        player_id (int): Player ID.

        Returns:
        Dict: Loadout configuration.

        Raises:
        ValueError: If player not found or no private loadout set.
        """
        if player_id not in self.private_loadouts:
            raise ValueError("No private loadout set for player")
        return self.private_loadouts[player_id]

def main():
    # Example usage
    tournament = Tournament(1, GameMode.TDM)

    player1 = Player(1, "JohnDoe")
    player1.set_loadout({"weapon": "rifle", "armor": "light"})
    player1.add_ability("healing")

    player2 = Player(2, "JaneDoe")
    player2.set_loadout({"weapon": "shotgun", "armor": "heavy"})
    player2.add_ability("shield")

    tournament.add_player(player1)
    tournament.add_player(player2)

    tournament.set_private_loadout(1, {"weapon": "sniper", "armor": "medium"})

    print(tournament.get_player_loadout(1))  # Output: {'weapon': 'rifle', 'armor': 'light'}
    print(tournament.get_private_loadout(1))  # Output: {'weapon': 'sniper', 'armor': 'medium'}

if __name__ == "__main__":
    main()
```
