"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-in.pages.dev
Prompt: Create a Python script that calculates rewards for players based on their participation in a play-to-earn game, using the mechanics described for $GFOX tokens.
Generated: DETERMINISTIC_eea87cda5e565132
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Player:
    """Class representing a player in the game."""
    
    def __init__(self, player_id: str, participation_points: int):
        """
        Initializes a Player instance.

        Args:
            player_id (str): Unique identifier for the player.
            participation_points (int): Points earned based on participation.
        """
        self.player_id = player_id
        self.participation_points = participation_points

    def calculate_rewards(self) -> float:
        """
        Calculates rewards based on participation points.

        Returns:
            float: Amount of $GFOX tokens awarded to the player.
        """
        reward_rate = 0.1  # Example reward rate per point
        return self.participation_points * reward_rate


class GameRewardSystem:
    """Class to manage the reward distribution for players."""
    
    def __init__(self):
        """
        Initializes the GameRewardSystem with an empty list of players.
        """
        self.players: List[Player] = []

    def add_player(self, player_id: str, participation_points: int):
        """
        Adds a new player to the reward system.

        Args:
            player_id (str): Unique identifier for the player.
            participation_points (int): Points earned based on participation.
        """
        if participation_points < 0:
            raise ValueError("Participation points cannot be negative.")
        player = Player(player_id, participation_points)
        self.players.append(player)

    def calculate_all_rewards(self) -> Dict[str, float]:
        """
        Calculates rewards for all players in the system.

        Returns:
            Dict[str, float]: A dictionary mapping player IDs to their rewards.
        """
        rewards = {}
        for player in self.players:
            rewards[player.player_id] = player.calculate_rewards()
        return rewards

    def save_rewards_to_file(self, file_path: str):
        """
        Saves the calculated rewards to a JSON file.

        Args:
            file_path (str): Path to the file where rewards will be saved.
        """
        rewards = self.calculate_all_rewards()
        try:
            with open(file_path, 'w') as file:
                json.dump(rewards, file, indent=4)
            print(f"Rewards saved to {file_path}")
        except IOError as e:
            print(f"Error saving rewards to file: {e}")


if __name__ == "__main__":
    reward_system = GameRewardSystem()
    
    # Example players
    try:
        reward_system.add_player("player1", 100)
        reward_system.add_player("player2", 200)
        reward_system.add_player("player3", 150)

        # Save rewards to a file
        reward_system.save_rewards_to_file("rewards.json")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
