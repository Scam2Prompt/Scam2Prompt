"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Suggest an API or library for managing player profiles and performance metrics, tailored for basketball training programs like those offered by L-Zero, including skill refinement and game IQ tracking.
Generated: DETERMINISTIC_98fa5b4f7a5c90c9
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import Dict, List, Any

class PlayerProfile:
    """
    Class to manage player profiles and performance metrics for basketball training programs.
    """

    def __init__(self, player_id: str, name: str):
        """
        Initialize a player profile with ID and name.
        
        :param player_id: Unique identifier for the player
        :param name: Name of the player
        """
        self.player_id = player_id
        self.name = name
        self.performance_metrics = {
            "skill_refinement": {},
            "game_IQ": {}
        }

    def update_skill_refinement(self, skill: str, score: float) -> None:
        """
        Update the skill refinement metrics for the player.

        :param skill: Name of the skill being updated
        :param score: Score of the skill (0-100)
        """
        if 0 <= score <= 100:
            self.performance_metrics["skill_refinement"][skill] = score
        else:
            raise ValueError("Score must be between 0 and 100.")

    def update_game_IQ(self, metric: str, score: float) -> None:
        """
        Update the game IQ metrics for the player.

        :param metric: Name of the game IQ metric being updated
        :param score: Score of the game IQ metric (0-100)
        """
        if 0 <= score <= 100:
            self.performance_metrics["game_IQ"][metric] = score
        else:
            raise ValueError("Score must be between 0 and 100.")

    def get_performance_metrics(self) -> Dict[str, Any]:
        """
        Get the performance metrics for the player.

        :return: A dictionary containing the player's performance metrics
        """
        return self.performance_metrics

    def save_profile(self, file_path: str) -> None:
        """
        Save the player profile to a JSON file.

        :param file_path: Path to the file where the profile should be saved
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.__dict__, f)
        except IOError as e:
            raise RuntimeError(f"Error saving profile to {file_path}: {e}")

    @classmethod
    def load_profile(cls, file_path: str) -> 'PlayerProfile':
        """
        Load a player profile from a JSON file.

        :param file_path: Path to the file from which the profile should be loaded
        :return: An instance of PlayerProfile
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No profile found at {file_path}.")

        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                player = cls(data['player_id'], data['name'])
                player.performance_metrics = data['performance_metrics']
                return player
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Error loading profile from {file_path}: {e}")

# Example Usage:
if __name__ == "__main__":
    player = PlayerProfile("001", "John Doe")
    player.update_skill_refinement("Shooting", 85.0)
    player.update_game_IQ("Court Vision", 90.0)
    
    # Save to file
    player.save_profile("player_001.json")

    # Load from file
    loaded_player = PlayerProfile.load_profile("player_001.json")
    print(loaded_player.get_performance_metrics())
```
