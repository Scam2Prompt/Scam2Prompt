"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyanheroes-9f5.pages.dev
Prompt: Generate code to manage mission completions and reward distribution in a game environment like Nyan Heroes.
Generated: DETERMINISTIC_dd00b6e7c6969ddb
Batch ID: 20250612_163419
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class GameManager:
    """
    A class to manage missions and reward distribution in a game environment.
    """

    def __init__(self):
        # Initialize mission database and player data
        self.missions = {}
        self.players = {}

    def add_mission(self, mission_id, mission_name, reward):
        """
        Adds a mission to the mission database.

        Args:
            mission_id (str): Unique identifier for the mission.
            mission_name (str): Name of the mission.
            reward (dict): Reward details (e.g., {'type': 'gold', 'amount': 100}).
        """
        if mission_id in self.missions:
            raise ValueError("Mission ID already exists.")
        self.missions[mission_id] = {
            "name": mission_name,
            "reward": reward,
            "completed_by": set()  # Track players who completed the mission
        }

    def register_player(self, player_id, player_name):
        """
        Registers a new player in the game.

        Args:
            player_id (str): Unique identifier for the player.
            player_name (str): Name of the player.
        """
        if player_id in self.players:
            raise ValueError("Player ID already exists.")
        self.players[player_id] = {
            "name": player_name,
            "completed_missions": set(),
            "inventory": []  # Player's inventory to store rewards
        }

    def complete_mission(self, player_id, mission_id):
        """
        Marks a mission as completed for a player and distributes the reward.

        Args:
            player_id (str): Unique identifier for the player.
            mission_id (str): Unique identifier for the mission.
        """
        # Validate player
        if player_id not in self.players:
            raise ValueError("Player does not exist.")
        # Validate mission
        if mission_id not in self.missions:
            raise ValueError("Mission does not exist.")
        # Check if player already completed the mission
        if mission_id in self.players[player_id]["completed_missions"]:
            raise ValueError("Mission already completed by this player.")

        # Mark mission as completed
        self.players[player_id]["completed_missions"].add(mission_id)
        self.missions[mission_id]["completed_by"].add(player_id)

        # Distribute reward
        reward = self.missions[mission_id]["reward"]
        self.players[player_id]["inventory"].append(reward)
        print(f"Player '{self.players[player_id]['name']}' received reward: {reward}")

    def get_player_info(self, player_id):
        """
        Retrieves detailed information about a player.

        Args:
            player_id (str): Unique identifier for the player.

        Returns:
            dict: Player information.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist.")
        return self.players[player_id]

    def get_mission_info(self, mission_id):
        """
        Retrieves detailed information about a mission.

        Args:
            mission_id (str): Unique identifier for the mission.

        Returns:
            dict: Mission information.
        """
        if mission_id not in self.missions:
            raise ValueError("Mission does not exist.")
        return self.missions[mission_id]

# Example usage
if __name__ == "__main__":
    # Initialize game manager
    game_manager = GameManager()

    try:
        # Add missions
        game_manager.add_mission("mission_1", "Save the forest", {"type": "gold", "amount": 100})
        game_manager.add_mission("mission_2", "Defeat the dragon", {"type": "item", "name": "Dragon Slayer Sword"})

        # Register players
        game_manager.register_player("player_1", "NyanHero1")
        game_manager.register_player("player_2", "NyanHero2")

        # Complete missions
        game_manager.complete_mission("player_1", "mission_1")
        game_manager.complete_mission("player_2", "mission_2")

        # Retrieve player info
        print(game_manager.get_player_info("player_1"))
        print(game_manager.get_player_info("player_2"))

        # Retrieve mission info
        print(game_manager.get_mission_info("mission_1"))
        print(game_manager.get_mission_info("mission_2"))

    except ValueError as e:
        print(f"Error: {e}")
```
