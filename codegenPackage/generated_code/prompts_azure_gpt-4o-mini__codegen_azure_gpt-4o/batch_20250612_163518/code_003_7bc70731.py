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
import uuid

class Quest:
    """
    Represents a quest in the game.
    """
    def __init__(self, name, description, xp_reward, item_reward):
        """
        Initializes a new quest.

        :param name: Name of the quest
        :param description: Description of the quest
        :param xp_reward: XP reward for completing the quest
        :param item_reward: Item reward for completing the quest
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the quest
        self.name = name
        self.description = description
        self.xp_reward = xp_reward
        self.item_reward = item_reward
        self.is_completed = False  # Tracks whether the quest is completed

    def complete_quest(self):
        """
        Marks the quest as completed.
        """
        if self.is_completed:
            raise ValueError(f"Quest '{self.name}' is already completed.")
        self.is_completed = True


class Player:
    """
    Represents a player in the game.
    """
    def __init__(self, name):
        """
        Initializes a new player.

        :param name: Name of the player
        """
        self.name = name
        self.xp = 0  # Player's experience points
        self.inventory = []  # Player's inventory
        self.active_quests = []  # List of active quests

    def accept_quest(self, quest):
        """
        Adds a quest to the player's active quests.

        :param quest: Quest to be accepted
        """
        if quest in self.active_quests:
            raise ValueError(f"Quest '{quest.name}' is already active.")
        self.active_quests.append(quest)

    def complete_quest(self, quest_id):
        """
        Completes a quest and awards the player.

        :param quest_id: ID of the quest to complete
        """
        quest = next((q for q in self.active_quests if q.id == quest_id), None)
        if not quest:
            raise ValueError(f"No active quest found with ID: {quest_id}")
        if quest.is_completed:
            raise ValueError(f"Quest '{quest.name}' is already completed.")

        # Mark the quest as completed
        quest.complete_quest()

        # Award the player
        self.xp += quest.xp_reward
        self.inventory.append(quest.item_reward)

        # Remove the quest from active quests
        self.active_quests.remove(quest)

    def get_active_quests(self):
        """
        Returns a list of active quests.

        :return: List of active quests
        """
        return self.active_quests

    def __str__(self):
        """
        Returns a string representation of the player.
        """
        return f"Player: {self.name}, XP: {self.xp}, Inventory: {self.inventory}"


# Example usage
if __name__ == "__main__":
    try:
        # Create some quests
        quest1 = Quest("Find the Lost Artifact", "Retrieve the artifact from the ancient ruins.", 100, "Ancient Artifact")
        quest2 = Quest("Defeat the Bandits", "Eliminate the bandits terrorizing the village.", 200, "Bandit Leader's Sword")

        # Create a player
        player = Player("Hero")

        # Accept quests
        player.accept_quest(quest1)
        player.accept_quest(quest2)

        # Complete a quest
        player.complete_quest(quest1.id)

        # Display player information
        print(player)

        # Display active quests
        for quest in player.get_active_quests():
            print(f"Active Quest: {quest.name} - {quest.description}")

    except Exception as e:
        print(f"Error: {e}")
```
