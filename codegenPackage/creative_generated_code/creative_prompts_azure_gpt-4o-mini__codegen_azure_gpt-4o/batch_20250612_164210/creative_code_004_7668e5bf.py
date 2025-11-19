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


class Game:
    """Main game class to manage player progression and quests."""

    def __init__(self, player_name: str):
        """
        Initialize the game instance with player details.

        Args:
            player_name (str): Name of the player.
        """
        self.player_name = player_name
        self.level = 1
        self.experience = 0
        self.quests = []
        self.completed_quests = []
        self.load_game()

    def save_game(self):
        """Save the player's progression and quests to a file."""
        try:
            data = {
                "player_name": self.player_name,
                "level": self.level,
                "experience": self.experience,
                "quests": self.quests,
                "completed_quests": self.completed_quests
            }
            with open("game_data.json", "w") as file:
                json.dump(data, file, indent=4)
        except IOError:
            print("Error saving game data.")

    def load_game(self):
        """Load the player's progression and quests from a file."""
        try:
            with open("game_data.json", "r") as file:
                data = json.load(file)
                self.player_name = data["player_name"]
                self.level = data["level"]
                self.experience = data["experience"]
                self.quests = data["quests"]
                self.completed_quests = data["completed_quests"]
        except (IOError, json.JSONDecodeError):
            print("No previous data found. Starting fresh.")

    def add_quest(self, quest_name: str, description: str, reward: int):
        """
        Add a new quest to the active quests list.

        Args:
            quest_name (str): Name of the quest.
            description (str): Description of the quest.
            reward (int): Reward for completing the quest.
        """
        new_quest = {"name": quest_name, "description": description, "reward": reward}
        self.quests.append(new_quest)
        print(f"Quest '{quest_name}' added.")

    def complete_quest(self, quest_name: str):
        """
        Mark a quest as completed and update player's progression.

        Args:
            quest_name (str): Name of the quest to complete.
        """
        for quest in self.quests:
            if quest["name"] == quest_name:
                self.quests.remove(quest)
                self.completed_quests.append(quest)
                self.experience += quest["reward"]
                print(f"Quest '{quest_name}' completed! Reward: {quest['reward']} experience points.")
                self.level_up()
                self.save_game()
                return
        print(f"Quest '{quest_name}' not found in active quests.")

    def level_up(self):
        """Check if player qualifies for a level-up based on experience."""
        while self.experience >= self.level * 100:  # Level-up threshold
            self.experience -= self.level * 100
            self.level += 1
            print(f"Congratulations! You leveled up to Level {self.level}!")

    def show_progression(self):
        """Display the player's current progression."""
        print(f"Player: {self.player_name}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}")
        print(f"Active Quests: {[quest['name'] for quest in self.quests]}")
        print(f"Completed Quests: {[quest['name'] for quest in self.completed_quests]}")


# Example usage
if __name__ == "__main__":
    # Initialize game with player name
    player_game = Game(player_name="Hero")

    # Add quests dynamically
    player_game.add_quest("Find the Hidden Treasure", "Locate the hidden treasure in the forest.", 150)
    player_game.add_quest("Defeat the Bandit Leader", "Defeat the leader of the bandits terrorizing the village.", 200)

    # Show current progression
    player_game.show_progression()

    # Complete a quest
    player_game.complete_quest("Find the Hidden Treasure")

    # Show updated progression
    player_game.show_progression()
```
