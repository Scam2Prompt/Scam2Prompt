"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: Develop a system for rewarding players with XP progression, quests, and challenges in a game like Moon Tropica.
Generated: DETERMINISTIC_b6bcb55d4b9df0cc
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Player:
    """
    A class to represent a player in the game.

    Attributes:
        name (str): The name of the player.
        xp (int): The experience points of the player.
        level (int): The current level of the player.
        quests (list): A list of quests assigned to the player.
    """

    def __init__(self, name):
        """
        Initializes a new player with a name, 0 XP, and level 1.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.xp = 0
        self.level = 1
        self.quests = []

    def add_xp(self, amount):
        """
        Adds experience points to the player and checks for level up.

        Args:
            amount (int): The amount of XP to add.
        """
        if amount < 0:
            raise ValueError("XP amount must be non-negative.")
        
        self.xp += amount
        self.check_level_up()

    def check_level_up(self):
        """
        Checks if the player has enough XP to level up.
        Levels up the player if the required XP threshold is met.
        """
        required_xp = self.level * 100  # Example threshold for leveling up
        while self.xp >= required_xp:
            self.xp -= required_xp
            self.level += 1
            print(f"{self.name} leveled up to level {self.level}!")

    def add_quest(self, quest):
        """
        Adds a quest to the player's quest list.

        Args:
            quest (str): The quest to be added.
        """
        self.quests.append(quest)

    def complete_quest(self, quest):
        """
        Completes a quest and rewards XP.

        Args:
            quest (str): The quest to be completed.

        Raises:
            ValueError: If the quest is not found in the player's quest list.
        """
        if quest not in self.quests:
            raise ValueError(f"Quest '{quest}' not found in player's quest list.")
        
        self.quests.remove(quest)
        xp_reward = 50  # Example XP reward for completing a quest
        self.add_xp(xp_reward)
        print(f"{self.name} completed quest: {quest} and earned {xp_reward} XP!")

class Quest:
    """
    A class to represent a quest in the game.

    Attributes:
        title (str): The title of the quest.
        description (str): A brief description of the quest.
        xp_reward (int): The amount of XP awarded for completing the quest.
    """

    def __init__(self, title, description, xp_reward):
        """
        Initializes a new quest.

        Args:
            title (str): The title of the quest.
            description (str): A brief description of the quest.
            xp_reward (int): The amount of XP awarded for completing the quest.
        """
        self.title = title
        self.description = description
        self.xp_reward = xp_reward

def main():
    """
    Main function to demonstrate the player XP progression system.
    """
    # Create a new player
    player = Player("Hero")

    # Create some quests
    quest1 = Quest("Defeat the Goblin", "Eliminate the goblin in the forest.", 50)
    quest2 = Quest("Collect Herbs", "Gather 10 healing herbs.", 30)

    # Add quests to the player
    player.add_quest(quest1.title)
    player.add_quest(quest2.title)

    # Complete quests and gain XP
    player.complete_quest(quest1.title)
    player.complete_quest(quest2.title)

if __name__ == "__main__":
    main()
```
