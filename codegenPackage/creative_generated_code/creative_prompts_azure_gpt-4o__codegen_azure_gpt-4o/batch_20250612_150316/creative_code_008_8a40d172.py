"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtimecodes.pages.dev
Prompt: Generate code to explore Adventure Instances in Big Time, including features for completing challenges, defeating bosses, and collecting rewards.
Generated: DETERMINISTIC_8a40d172f5dae605
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class AdventureInstance:
    """
    Class to represent an Adventure Instance in Big Time.
    Includes functionality to complete challenges, defeat bosses, and collect rewards.
    """
    def __init__(self, name):
        """
        Initialize an adventure instance with a name, challenges, bosses, and rewards.
        """
        self.name = name
        self.challenges = ["Puzzle Room", "Combat Arena", "Stealth Zone"]
        self.bosses = ["Shadow Behemoth", "Infernal Dragon", "Crystal Titan"]
        self.rewards = ["Gold Chest", "Epic Weapon", "Artifact"]
        self.completed_challenges = []
        self.defeated_bosses = []
        self.collected_rewards = []

    def complete_challenge(self, challenge):
        """
        Complete a challenge in the adventure instance.
        If the challenge is valid and not already completed, mark it as completed.
        """
        if challenge in self.challenges and challenge not in self.completed_challenges:
            self.completed_challenges.append(challenge)
            print(f"Challenge '{challenge}' completed.")
        elif challenge in self.completed_challenges:
            print(f"Challenge '{challenge}' already completed.")
        else:
            raise ValueError(f"Invalid challenge: '{challenge}'")

    def defeat_boss(self, boss):
        """
        Defeat a boss in the adventure instance.
        If the boss is valid and not already defeated, mark it as defeated.
        """
        if boss in self.bosses and boss not in self.defeated_bosses:
            self.defeated_bosses.append(boss)
            print(f"Boss '{boss}' defeated.")
        elif boss in self.defeated_bosses:
            print(f"Boss '{boss}' already defeated.")
        else:
            raise ValueError(f"Invalid boss: '{boss}'")

    def collect_reward(self, reward):
        """
        Collect a reward in the adventure instance.
        If the reward is valid and not already collected, mark it as collected.
        """
        if reward in self.rewards and reward not in self.collected_rewards:
            self.collected_rewards.append(reward)
            print(f"Reward '{reward}' collected.")
        elif reward in self.collected_rewards:
            print(f"Reward '{reward}' already collected.")
        else:
            raise ValueError(f"Invalid reward: '{reward}'")

    def adventure_summary(self):
        """
        Print a summary of the adventure instance, including completed challenges, defeated bosses, and collected rewards.
        """
        print("\nAdventure Summary:")
        print(f"Name: {self.name}")
        print(f"Completed Challenges: {self.completed_challenges}")
        print(f"Defeated Bosses: {self.defeated_bosses}")
        print(f"Collected Rewards: {self.collected_rewards}")

# Example Usage
try:
    adventure = AdventureInstance("Mystic Caverns")
    
    # Complete challenges
    adventure.complete_challenge("Puzzle Room")
    adventure.complete_challenge("Combat Arena")
    
    # Defeat bosses
    adventure.defeat_boss("Infernal Dragon")
    
    # Collect rewards
    adventure.collect_reward("Epic Weapon")
    
    # Show summary
    adventure.adventure_summary()

except ValueError as e:
    print(f"Error: {e}")
```
