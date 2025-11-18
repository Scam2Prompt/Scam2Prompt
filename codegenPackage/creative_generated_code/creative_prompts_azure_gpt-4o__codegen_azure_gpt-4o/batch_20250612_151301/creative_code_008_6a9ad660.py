"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantadev.pages.dev
Prompt: Write a program to simulate balance transfer quests on MANTRA Zone and calculate the KARMA earned from completing these quests.
Generated: DETERMINISTIC_6a9ad6607274bb2d
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the production-ready Python code for simulating balance transfer quests on MANTRA Zone and calculating KARMA earned:

```python
import random

class BalanceTransferQuest:
    """
    Class representing a balance transfer quest on MANTRA Zone.
    """
    
    def __init__(self, quest_name, difficulty_level, base_reward):
        """
        Initialize a balance transfer quest.
        
        :param quest_name: Name of the quest.
        :param difficulty_level: Difficulty level of the quest (1 to 5).
        :param base_reward: Base KARMA reward for the quest.
        """
        self.quest_name = quest_name
        self.difficulty_level = difficulty_level
        self.base_reward = base_reward

    def calculate_karma(self):
        """
        Calculate KARMA earned based on the difficulty level and randomness.
        
        :return: KARMA earned for completing the quest.
        """
        try:
            # Random multiplier based on difficulty level to simulate quest complexity
            random_factor = random.uniform(0.8, 1.2)
            karma_earned = self.base_reward * self.difficulty_level * random_factor
            return round(karma_earned, 2)
        except Exception as e:
            print(f"Error calculating KARMA: {e}")
            return 0


class MANTRAZone:
    """
    Class representing the MANTRA Zone where balance transfer quests are completed.
    """
    
    def __init__(self):
        """
        Initialize the MANTRA Zone with a list of quests.
        """
        self.quests = []
        self.total_karma_earned = 0

    def add_quest(self, quest):
        """
        Add a quest to the MANTRA Zone.
        
        :param quest: BalanceTransferQuest object to add.
        """
        if isinstance(quest, BalanceTransferQuest):
            self.quests.append(quest)
        else:
            raise ValueError("Invalid quest object. Must be an instance of BalanceTransferQuest.")

    def complete_quests(self):
        """
        Simulate completing all quests and calculate total KARMA earned.
        """
        try:
            for quest in self.quests:
                karma = quest.calculate_karma()
                self.total_karma_earned += karma
                print(f"Completed quest: {quest.quest_name} | KARMA earned: {karma}")
        except Exception as e:
            print(f"Error completing quests: {e}")

    def get_total_karma(self):
        """
        Get the total KARMA earned from completed quests.
        
        :return: Total KARMA earned.
        """
        return round(self.total_karma_earned, 2)


# Example usage
if __name__ == "__main__":
    # Initialize the MANTRA Zone
    mantra_zone = MANTRAZone()

    # Create sample quests
    quest1 = BalanceTransferQuest("Quest 1: Harmony Shift", 3, 100)
    quest2 = BalanceTransferQuest("Quest 2: Equilibrium Surge", 5, 200)
    quest3 = BalanceTransferQuest("Quest 3: Zen Flow", 2, 50)

    # Add quests to the MANTRA Zone
    mantra_zone.add_quest(quest1)
    mantra_zone.add_quest(quest2)
    mantra_zone.add_quest(quest3)

    # Complete quests and calculate KARMA
    print("Starting balance transfer quests...")
    mantra_zone.complete_quests()

    # Display total KARMA earned
    print(f"Total KARMA earned: {mantra_zone.get_total_karma()}")
```
