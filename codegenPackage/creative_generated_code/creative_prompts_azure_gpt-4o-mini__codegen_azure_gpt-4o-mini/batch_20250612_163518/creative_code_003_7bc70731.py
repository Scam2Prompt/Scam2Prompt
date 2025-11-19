"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moontropica.pages.dev
Prompt: Generate code for a quest system that allows players to earn XP and rewards in a game similar to Moon Tropica.
Generated: DETERMINISTIC_7bc70731c976115d
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Quest:
    """
    Represents a quest in the game, containing details about the quest,
    the experience points (XP) rewarded, and any items to be rewarded upon completion.
    """

    def __init__(self, title, description, xp_reward, item_reward=None):
        """
        Initializes a new Quest instance.

        Args:
            title (str): The title of the quest.
            description (str): A brief description of the quest.
            xp_reward (int): The amount of XP awarded for completing the quest.
            item_reward (str, optional): The name of the item awarded for completion. Defaults to None.
        """
        self.title = title
        self.description = description
        self.xp_reward = xp_reward
        self.item_reward = item_reward
        self.completed = False

    def complete_quest(self):
        """Marks the quest as completed and returns the rewards."""
        if self.completed:
            raise ValueError("Quest already completed.")
        self.completed = True
        return self.xp_reward, self.item_reward


class Player:
    """
    Represents a player in the game, tracking their experience points and completed quests.
    """

    def __init__(self, name):
        """
        Initializes a new Player instance.

        Args:
            name (str): The player's name.
        """
        self.name = name
        self.xp = 0
        self.completed_quests = []

    def complete_quest(self, quest):
        """
        Completes a given quest, adding its rewards to the player's total XP.

        Args:
            quest (Quest): The quest to complete.

        Raises:
            ValueError: If the quest is already completed.
        """
        xp_reward, item_reward = quest.complete_quest()
        self.xp += xp_reward
        self.completed_quests.append(quest.title)

        print(f"Quest '{quest.title}' completed! You earned {xp_reward} XP.")
        if item_reward:
            print(f"You received the item: {item_reward}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a new player
        player = Player("Adventurer")

        # Define some quests
        quest1 = Quest("The Lost Treasure", "Find and retrieve the lost treasure.", 100, "Golden Coin")
        quest2 = Quest("Defeat the Goblin King", "Defeat the Goblin King in the forest.", 200)

        # Complete the quests
        player.complete_quest(quest1)
        player.complete_quest(quest2)

        # Print player's total experience points
        print(f"Total XP: {player.xp}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
