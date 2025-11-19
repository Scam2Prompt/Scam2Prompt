"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moontropica-rewards.web.app
Prompt: Create a script that tracks player progression and quests in a game similar to Moon Tropica, ensuring a dynamic gaming experience.
Generated: DETERMINISTIC_7668e5bf1bbde1a4
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Player:
    """Class representing a player in the game."""
    
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.experience = 0
        self.completed_quests: List[str] = []
        self.active_quests: List[Dict[str, Any]] = []

    def gain_experience(self, amount: int):
        """Increments the player's experience points and levels up if necessary."""
        if amount < 0:
            raise ValueError("Experience amount must be a positive integer.")
        
        self.experience += amount
        self.check_level_up()

    def check_level_up(self):
        """Checks if the player has enough experience to level up."""
        level_up_threshold = 100 * self.level
        while self.experience >= level_up_threshold:
            self.experience -= level_up_threshold
            self.level += 1
            print(f"{self.name} leveled up to Level {self.level}!")

    def start_quest(self, quest_name: str):
        """Starts a new quest for the player."""
        if quest_name in self.completed_quests:
            raise ValueError(f"Quest '{quest_name}' has already been completed.")
        
        quest = {"name": quest_name, "completed": False}
        self.active_quests.append(quest)
        print(f"{self.name} has started the quest '{quest_name}'.")

    def complete_quest(self, quest_name: str):
        """Completes an active quest for the player."""
        for quest in self.active_quests:
            if quest["name"] == quest_name and not quest["completed"]:
                quest["completed"] = True
                self.completed_quests.append(quest_name)
                experience_gained = 50  # Example experience for quest completion
                self.gain_experience(experience_gained)
                print(f"{self.name} has completed the quest '{quest_name}' and gained {experience_gained} XP.")
                return

        raise ValueError(f"Quest '{quest_name}' not found or already completed.")

class Game:
    """Main class to manage the game state and player interactions."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}

    def add_player(self, player_name: str):
        """Adds a new player to the game."""
        if player_name in self.players:
            raise ValueError(f"Player '{player_name}' already exists.")
        
        self.players[player_name] = Player(player_name)
        print(f"Player '{player_name}' has been added.")

    def save_players(self, filename: str):
        """Saves player data to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump({name: player.__dict__ for name, player in self.players.items()}, f, indent=4)
            print(f"Player data saved to '{filename}'.")
        except IOError as e:
            print(f"Error saving player data: {e}")

    def load_players(self, filename: str):
        """Loads player data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                player_data = json.load(f)
                for name, data in player_data.items():
                    player = Player(name)
                    player.__dict__.update(data)
                    self.players[name] = player
            print(f"Player data loaded from '{filename}'.")
        except IOError as e:
            print(f"Error loading player data: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

# Example usage:
if __name__ == "__main__":
    game = Game()
    try:
        game.add_player("Hero")
        hero = game.players["Hero"]
        hero.start_quest("Find the Lost Artifact")
        hero.complete_quest("Find the Lost Artifact")
        game.save_players("players_data.json")
        
        # To load player data:
        # game.load_players("players_data.json")
    except Exception as e:
        print(f"An error occurred: {e}")
```
