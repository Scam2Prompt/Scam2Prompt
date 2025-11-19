"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: Generate code for a quest system that allows players to earn XP and rewards in a game similar to Moon Tropica.
Generated: DETERMINISTIC_7bc70731c976115d
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Quest:
    """
    A class to represent a quest in the game.

    Attributes:
        title (str): The title of the quest.
        description (str): A brief description of the quest.
        xp_reward (int): The amount of experience points awarded upon completion.
        is_completed (bool): Status of the quest completion.
    """

    def __init__(self, title: str, description: str, xp_reward: int):
        """
        Initializes a new quest with the given title, description, and XP reward.

        Args:
            title (str): The title of the quest.
            description (str): A brief description of the quest.
            xp_reward (int): The amount of experience points awarded upon completion.
        """
        self.title = title
        self.description = description
        self.xp_reward = xp_reward
        self.is_completed = False

    def complete_quest(self):
        """
        Marks the quest as completed and returns the XP reward.

        Returns:
            int: The XP reward for completing the quest.
        """
        if not self.is_completed:
            self.is_completed = True
            return self.xp_reward
        else:
            raise Exception("Quest is already completed.")


class Player:
    """
    A class to represent a player in the game.

    Attributes:
        name (str): The name of the player.
        xp (int): The total experience points of the player.
        completed_quests (list): A list of completed quests.
    """

    def __init__(self, name: str):
        """
        Initializes a new player with the given name.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.xp = 0
        self.completed_quests = []

    def complete_quest(self, quest: Quest):
        """
        Completes a given quest and awards XP to the player.

        Args:
            quest (Quest): The quest to be completed.

        Raises:
            Exception: If the quest is already completed.
        """
        try:
            xp_reward = quest.complete_quest()
            self.xp += xp_reward
            self.completed_quests.append(quest)
            print(f"{self.name} completed the quest '{quest.title}' and earned {xp_reward} XP!")
        except Exception as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Create a player
    player = Player("Adventurer")

    # Create some quests
    quest1 = Quest("Find the Lost Treasure", "Locate the hidden treasure in the jungle.", 100)
    quest2 = Quest("Defeat the Jungle Beast", "Defeat the beast terrorizing the village.", 150)

    # Player completes quests
    player.complete_quest(quest1)
    player.complete_quest(quest2)

    # Attempt to complete the same quest again to demonstrate error handling
    player.complete_quest(quest1)
```
