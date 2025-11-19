"""
Generated Code Metadata:
========================
Original URL: https://pablo-defi.pages.dev
Prompt: Write a Python script to simulate gameplay mechanics for Narcos Land, including territory control, alliances, and NFT rewards, based on the Pablo ecosystem description.
Generated: DETERMINISTIC_2c058385a46c371a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional

class Territory:
    """Class representing a territory in the game."""
    
    def __init__(self, name: str):
        self.name = name
        self.controlled_by: Optional[str] = None  # Player controlling the territory
        self.alliances: List[str] = []  # List of players in alliance for this territory

    def control_territory(self, player_name: str):
        """Control the territory by a player."""
        self.controlled_by = player_name
        print(f"{player_name} now controls {self.name}.")

    def form_alliance(self, player_name: str):
        """Form an alliance for the territory."""
        if player_name not in self.alliances:
            self.alliances.append(player_name)
            print(f"{player_name} has formed an alliance in {self.name}.")

    def reward_nft(self) -> str:
        """Reward an NFT to the controlling player."""
        if self.controlled_by:
            return f"{self.controlled_by} has received an NFT for controlling {self.name}!"
        return "No player controls this territory to receive an NFT."


class Player:
    """Class representing a player in the game."""
    
    def __init__(self, name: str):
        self.name = name
        self.territories: List[Territory] = []  # Territories controlled by the player

    def take_control(self, territory: Territory):
        """Player takes control of a territory."""
        territory.control_territory(self.name)
        self.territories.append(territory)

    def form_alliance(self, territory: Territory):
        """Player forms an alliance in a territory."""
        territory.form_alliance(self.name)

    def claim_nft(self, territory: Territory) -> Optional[str]:
        """Player claims NFT reward for a territory."""
        if territory.controlled_by == self.name:
            return territory.reward_nft()
        return f"{self.name} cannot claim NFT for {territory.name}."


class Game:
    """Class to manage the game mechanics."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}
        self.territories: List[Territory] = []

    def add_player(self, player_name: str):
        """Add a new player to the game."""
        if player_name not in self.players:
            self.players[player_name] = Player(player_name)
            print(f"Player {player_name} has joined the game.")
        else:
            print(f"Player {player_name} already exists.")

    def add_territory(self, territory_name: str):
        """Add a new territory to the game."""
        territory = Territory(territory_name)
        self.territories.append(territory)
        print(f"Territory {territory_name} has been added to the game.")

    def simulate_gameplay(self):
        """Simulate gameplay mechanics."""
        for territory in self.territories:
            if random.choice([True, False]):  # Randomly decide if a player takes control
                player_name = random.choice(list(self.players.keys()))
                self.players[player_name].take_control(territory)

            if territory.controlled_by:
                # Randomly decide if the player forms an alliance
                if random.choice([True, False]):
                    self.players[territory.controlled_by].form_alliance(territory)

                # Randomly decide if the player claims an NFT
                if random.choice([True, False]):
                    print(self.players[territory.controlled_by].claim_nft(territory))


# Example usage
if __name__ == "__main__":
    game = Game()
    
    # Adding players
    game.add_player("Pablo")
    game.add_player("Gustavo")
    
    # Adding territories
    game.add_territory("Medellin")
    game.add_territory("Cali")
    
    # Simulate gameplay
    game.simulate_gameplay()
```
