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
import random

class Quest:
    """
    Represents a single quest in the game.
    """
    def __init__(self, name, description, xp_reward, item_reward):
        self.name = name
        self.description = description
        self.xp_reward = xp_reward
        self.item_reward = item_reward
        self.is_completed = False

    def complete_quest(self):
        """
        Marks the quest as completed and returns the rewards.
        """
        if self.is_completed:
            raise Exception("Quest already completed!")
        self.is_completed = True
        return self.xp_reward, self.item_reward


class Player:
    """
    Represents a player in the game.
    """
    def __init__(self, name):
        self.name = name
        self.xp = 0
        self.inventory = []

    def earn_rewards(self, xp_reward, item_reward):
        """
        Adds XP and item rewards to the player's stats.
        """
        self.xp += xp_reward
        self.inventory.append(item_reward)

    def __str__(self):
        """
        Returns player's stats as a string.
        """
        return f"Player: {self.name}\nXP: {self.xp}\nInventory: {self.inventory}"


class QuestSystem:
    """
    Manages quests for players in the game.
    """
    def __init__(self):
        self.available_quests = []

    def add_quest(self, quest):
        """
        Adds a new quest to the quest pool.
        """
        if not isinstance(quest, Quest):
            raise TypeError("Only instances of Quest can be added.")
        self.available_quests.append(quest)

    def list_quests(self):
        """
        Lists all available quests.
        """
        return [quest for quest in self.available_quests if not quest.is_completed]


# Example usage
if __name__ == "__main__":
    # Create a player
    player = Player("Alex")

    # Initialize a quest system
    quest_system = QuestSystem()

    # Add some quests
    quest_system.add_quest(Quest("Treasure Hunt", "Find the hidden treasure.", 100, "Golden Sword"))
    quest_system.add_quest(Quest("Monster Slayer", "Defeat 5 monsters.", 150, "Shield of Valor"))

    # List available quests
    print("Available Quests:")
    for idx, quest in enumerate(quest_system.list_quests(), start=1):
        print(f"{idx}. {quest.name} - {quest.description} (XP: {quest.xp_reward}, Reward: {quest.item_reward})")

    # Simulate completing a quest
    print("\nCompleting a quest...")
    selected_quest = quest_system.list_quests()[0]  # Select the first quest
    xp, item = selected_quest.complete_quest()
    player.earn_rewards(xp, item)

    # Display player stats
    print("\nPlayer Stats:")
    print(player)

    # List remaining quests
    print("\nRemaining Quests:")
    for idx, quest in enumerate(quest_system.list_quests(), start=1):
        print(f"{idx}. {quest.name} - {quest.description} (XP: {quest.xp_reward}, Reward: {quest.item_reward})")
```
