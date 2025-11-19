"""
Generated Code Metadata:
========================
Original URL: https://rheapratas.com
Prompt: Develop a system for tracking and rewarding player loyalty, similar to the programs described on this webpage, and provide a detailed explanation of the system's features and benefits.
Generated: DETERMINISTIC_e1d48cf2afa32d95
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_program.py

from datetime import datetime, timedelta
from typing import Dict

class Player:
    """Represents a player in the loyalty program."""

    def __init__(self, player_id: int, name: str):
        """
        Initializes a new player.

        Args:
            player_id (int): Unique identifier for the player.
            name (str): Player's name.
        """
        self.player_id = player_id
        self.name = name
        self.visits = 0
        self.rewards = []
        self.last_visit = None

class LoyaltyProgram:
    """Manages player loyalty and rewards."""

    def __init__(self):
        """
        Initializes a new loyalty program.
        """
        self.players: Dict[int, Player] = {}
        self.rewards = {
            5: "Bronze Badge",
            10: "Silver Badge",
            20: "Gold Badge"
        }

    def add_player(self, player_id: int, name: str):
        """
        Adds a new player to the loyalty program.

        Args:
            player_id (int): Unique identifier for the player.
            name (str): Player's name.

        Raises:
            ValueError: If a player with the same ID already exists.
        """
        if player_id in self.players:
            raise ValueError("Player already exists")
        self.players[player_id] = Player(player_id, name)

    def log_visit(self, player_id: int):
        """
        Logs a visit for the specified player.

        Args:
            player_id (int): Unique identifier for the player.

        Raises:
            ValueError: If the player does not exist.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist")
        player = self.players[player_id]
        player.visits += 1
        player.last_visit = datetime.now()
        self.check_rewards(player)

    def check_rewards(self, player: Player):
        """
        Checks if the player has earned any rewards.

        Args:
            player (Player): The player to check.
        """
        for visit_threshold, reward in self.rewards.items():
            if player.visits >= visit_threshold and reward not in [r["reward"] for r in player.rewards]:
                player.rewards.append({"visit_threshold": visit_threshold, "reward": reward, "earned_at": datetime.now()})

    def get_player_info(self, player_id: int):
        """
        Retrieves information about a player.

        Args:
            player_id (int): Unique identifier for the player.

        Returns:
            Dict: Player information.

        Raises:
            ValueError: If the player does not exist.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist")
        player = self.players[player_id]
        return {
            "player_id": player.player_id,
            "name": player.name,
            "visits": player.visits,
            "rewards": player.rewards,
            "last_visit": player.last_visit
        }

def main():
    loyalty_program = LoyaltyProgram()

    # Add players
    loyalty_program.add_player(1, "John Doe")
    loyalty_program.add_player(2, "Jane Doe")

    # Log visits
    loyalty_program.log_visit(1)
    loyalty_program.log_visit(1)
    loyalty_program.log_visit(1)
    loyalty_program.log_visit(1)
    loyalty_program.log_visit(1)  # Earns Bronze Badge

    loyalty_program.log_visit(2)
    loyalty_program.log_visit(2)
    loyalty_program.log_visit(2)
    loyalty_program.log_visit(2)
    loyalty_program.log_visit(2)
    loyalty_program.log_visit(2)
    loyalty_program.log_visit(2)
    loyalty_program.log_visit(2)
    loyalty_program.log_visit(2)
    loyalty_program.log_visit(2)
    loyalty_program.log_visit(2)  # Earns Bronze Badge

    loyalty_program.log_visit(1)
    loyalty_program.log_visit(1)
    loyalty_program.log_visit(1)
    loyalty_program.log_visit(1)
    loyalty_program.log_visit(1)  # Earns Silver Badge

    # Get player info
    print(loyalty_program.get_player_info(1))
    print(loyalty_program.get_player_info(2))

if __name__ == "__main__":
    main()
```
