"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tarileague.pages.dev
Prompt: How can I implement a Tari airdrop game using quests to earn gems and rewards, as described on the Tari League website?
Generated: DETERMINISTIC_e48c03025fe8aee8
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Quest:
    """
    Class representing a quest in the Tari airdrop game.
    Each quest has a title, description, and a reward in gems.
    """

    def __init__(self, title: str, description: str, reward: int):
        self.title = title
        self.description = description
        self.reward = reward

    def __str__(self):
        return f"{self.title}: {self.description} (Reward: {self.reward} gems)"


class Player:
    """
    Class representing a player in the Tari airdrop game.
    The player has a name and a gem balance.
    """

    def __init__(self, name: str):
        self.name = name
        self.gems = 0

    def complete_quest(self, quest: Quest):
        """
        Method for the player to complete a quest and earn gems.
        
        :param quest: The quest to be completed.
        """
        self.gems += quest.reward
        print(f"{self.name} completed '{quest.title}' and earned {quest.reward} gems! Total gems: {self.gems}")


class Game:
    """
    Class representing the Tari airdrop game.
    It manages players and quests.
    """

    def __init__(self):
        self.players = {}
        self.quests = []

    def add_player(self, player_name: str):
        """
        Add a new player to the game.
        
        :param player_name: Name of the player to add.
        """
        if player_name in self.players:
            print(f"Player '{player_name}' already exists.")
            return

        self.players[player_name] = Player(player_name)
        print(f"Player '{player_name}' added to the game.")

    def add_quest(self, title: str, description: str, reward: int):
        """
        Add a new quest to the game.
        
        :param title: Title of the quest.
        :param description: Description of the quest.
        :param reward: Reward in gems for completing the quest.
        """
        if reward < 0:
            raise ValueError("Reward cannot be negative.")

        quest = Quest(title, description, reward)
        self.quests.append(quest)
        print(f"Quest '{title}' added to the game.")

    def complete_quest(self, player_name: str, quest_title: str):
        """
        Allow a player to complete a quest.
        
        :param player_name: Name of the player completing the quest.
        :param quest_title: Title of the quest to complete.
        """
        if player_name not in self.players:
            print(f"Player '{player_name}' does not exist.")
            return
        
        quest = next((q for q in self.quests if q.title == quest_title), None)
        if quest is None:
            print(f"Quest '{quest_title}' not found.")
            return
        
        self.players[player_name].complete_quest(quest)


if __name__ == "__main__":
    # Create a game instance
    game = Game()

    # Add some quests
    game.add_quest("Quest 1", "Collect 10 flowers", 100)
    game.add_quest("Quest 2", "Defeat 5 monsters", 150)

    # Add players
    game.add_player("Alice")
    game.add_player("Bob")

    # Players complete quests
    game.complete_quest("Alice", "Quest 1")
    game.complete_quest("Bob", "Quest 2")
    
    # Attempt to complete a non-existing quest
    game.complete_quest("Alice", "Quest 3")
```
