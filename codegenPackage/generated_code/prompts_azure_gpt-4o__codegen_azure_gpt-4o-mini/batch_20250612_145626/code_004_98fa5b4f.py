"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Suggest an API or library for managing player profiles and performance metrics, tailored for basketball training programs like those offered by L-Zero, including skill refinement and game IQ tracking.
Generated: DETERMINISTIC_98fa5b4f7a5c90c9
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# basketball_profile_manager.py

import json
from typing import List, Dict, Any

class PlayerProfile:
    """
    A class to represent a basketball player's profile and performance metrics.
    """

    def __init__(self, player_id: str, name: str):
        """
        Initializes a new player profile.

        :param player_id: Unique identifier for the player
        :param name: Name of the player
        """
        self.player_id = player_id
        self.name = name
        self.skills = {}
        self.performance_metrics = {}

    def update_skill(self, skill_name: str, skill_level: int):
        """
        Updates the skill level of the player.

        :param skill_name: Name of the skill
        :param skill_level: Level of the skill (1-10)
        """
        if not (1 <= skill_level <= 10):
            raise ValueError("Skill level must be between 1 and 10.")
        self.skills[skill_name] = skill_level

    def record_performance(self, game_id: str, metrics: Dict[str, Any]):
        """
        Records performance metrics for a specific game.

        :param game_id: Unique identifier for the game
        :param metrics: Dictionary containing performance metrics
        """
        self.performance_metrics[game_id] = metrics

    def get_profile(self) -> Dict[str, Any]:
        """
        Returns the player's profile as a dictionary.

        :return: Dictionary containing player profile information
        """
        return {
            "player_id": self.player_id,
            "name": self.name,
            "skills": self.skills,
            "performance_metrics": self.performance_metrics
        }

class PlayerProfileManager:
    """
    A class to manage multiple player profiles.
    """

    def __init__(self):
        """
        Initializes the player profile manager.
        """
        self.profiles = {}

    def add_profile(self, player_id: str, name: str):
        """
        Adds a new player profile.

        :param player_id: Unique identifier for the player
        :param name: Name of the player
        """
        if player_id in self.profiles:
            raise ValueError("Player ID already exists.")
        self.profiles[player_id] = PlayerProfile(player_id, name)

    def get_profile(self, player_id: str) -> Dict[str, Any]:
        """
        Retrieves a player's profile.

        :param player_id: Unique identifier for the player
        :return: Player profile information
        """
        if player_id not in self.profiles:
            raise ValueError("Player ID not found.")
        return self.profiles[player_id].get_profile()

    def save_profiles_to_file(self, filename: str):
        """
        Saves all player profiles to a JSON file.

        :param filename: Name of the file to save profiles
        """
        try:
            with open(filename, 'w') as file:
                json.dump({pid: profile.get_profile() for pid, profile in self.profiles.items()}, file, indent=4)
        except IOError as e:
            raise Exception(f"An error occurred while saving profiles: {e}")

    def load_profiles_from_file(self, filename: str):
        """
        Loads player profiles from a JSON file.

        :param filename: Name of the file to load profiles from
        """
        try:
            with open(filename, 'r') as file:
                profiles_data = json.load(file)
                for player_id, data in profiles_data.items():
                    self.add_profile(player_id, data['name'])
                    for skill, level in data['skills'].items():
                        self.profiles[player_id].update_skill(skill, level)
                    for game_id, metrics in data['performance_metrics'].items():
                        self.profiles[player_id].record_performance(game_id, metrics)
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"An error occurred while loading profiles: {e}")

# Example usage
if __name__ == "__main__":
    manager = PlayerProfileManager()
    manager.add_profile("001", "John Doe")
    manager.profiles["001"].update_skill("Shooting", 8)
    manager.profiles["001"].record_performance("game_001", {"points": 20, "assists": 5})

    print(manager.get_profile("001"))
    manager.save_profiles_to_file("player_profiles.json")
```
