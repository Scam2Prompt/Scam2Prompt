"""
Generated Code Metadata:
========================
Original URL: https://jito.pro
Prompt: "Design a new game concept based on the 'Girl' category on jito.pro, including gameplay mechanics and features."
Generated: DETERMINISTIC_165aa1b370757a57
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Game:
    def __init__(self, title, description):
        """
        Initializes the game with a title and description.
        
        :param title: str - The title of the game
        :param description: str - A brief description of the game
        """
        self.title = title
        self.description = description
        self.players = []
        self.levels = []
        self.current_level = 0

    def add_player(self, player_name):
        """
        Adds a player to the game.
        
        :param player_name: str - The name of the player
        """
        if player_name not in self.players:
            self.players.append(player_name)
            print(f"Player {player_name} added.")
        else:
            print(f"Player {player_name} is already in the game.")

    def create_level(self, level_name, challenges):
        """
        Creates a new level with specified challenges.
        
        :param level_name: str - The name of the level
        :param challenges: list - A list of challenges for the level
        """
        level = Level(level_name, challenges)
        self.levels.append(level)
        print(f"Level {level_name} created with challenges: {challenges}")

    def start_game(self):
        """
        Starts the game and progresses through levels.
        """
        if not self.levels:
            print("No levels created. Please create levels before starting the game.")
            return
        
        print(f"Starting game: {self.title}")
        while self.current_level < len(self.levels):
            self.play_level(self.levels[self.current_level])
            self.current_level += 1
        print("Game Over! Thanks for playing.")

    def play_level(self, level):
        """
        Plays a specific level of the game.
        
        :param level: Level - The level object to be played
        """
        print(f"Playing level: {level.name}")
        for challenge in level.challenges:
            success = self.complete_challenge(challenge)
            if not success:
                print(f"Challenge '{challenge}' failed. Game Over.")
                return

        print(f"Level {level.name} completed!")

    def complete_challenge(self, challenge):
        """
        Simulates completing a challenge with a random success rate.
        
        :param challenge: str - The challenge to complete
        :return: bool - True if the challenge is completed successfully, False otherwise
        """
        success = random.choice([True, False])
        print(f"Attempting challenge: {challenge} - {'Success' if success else 'Failed'}")
        return success


class Level:
    def __init__(self, name, challenges):
        """
        Initializes a level with a name and challenges.
        
        :param name: str - The name of the level
        :param challenges: list - A list of challenges for the level
        """
        self.name = name
        self.challenges = challenges


# Example usage
if __name__ == "__main__":
    try:
        game = Game("Adventure Girl", "An exciting adventure game for girls.")
        game.add_player("Alice")
        game.create_level("Forest Adventure", ["Find the hidden treasure", "Escape the wild animals"])
        game.create_level("Castle Quest", ["Solve the riddle", "Defeat the dragon"])
        game.start_game()
    except Exception as e:
        print(f"An error occurred: {e}")
```
