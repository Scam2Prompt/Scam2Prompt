"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-bigtime.pages.dev
Prompt: Write code to simulate the Prestige Portals gameplay mechanics, including challenges, boss battles, and reward collection as outlined on the Big Time website.
Generated: DETERMINISTIC_1eeaaced3132975a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from enum import Enum, auto

class ChallengeDifficulty(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()

class Boss(Enum):
    FIRE_DRAGON = auto()
    ICE_GIANT = auto()
    STONE_GOLEM = auto()

class Reward(Enum):
    GOLD = auto()
    ARTIFACT = auto()
    EXPERIENCE = auto()

class PrestigePortal:
    def __init__(self):
        self.challenges_completed = 0
        self.boss_defeated = False
        self.rewards_collected = []

    def simulate_challenge(self, difficulty: ChallengeDifficulty):
        """
        Simulates a challenge based on the provided difficulty level.
        """
        try:
            print(f"Simulating {difficulty.name} challenge...")
            success = random.random() < self._get_success_rate(difficulty)
            if success:
                self.challenges_completed += 1
                print("Challenge completed successfully!")
                self.collect_reward()
            else:
                print("Challenge failed. Better luck next time!")
        except Exception as e:
            print(f"An error occurred while simulating the challenge: {e}")

    def simulate_boss_battle(self, boss: Boss):
        """
        Simulates a boss battle against a specified boss.
        """
        try:
            print(f"Facing the boss: {boss.name}...")
            success = random.random() < 0.5  # 50% chance to defeat the boss
            if success:
                self.boss_defeated = True
                print(f"{boss.name} defeated!")
                self.collect_reward()
            else:
                print(f"{boss.name} defeated you. Try again!")
        except Exception as e:
            print(f"An error occurred during the boss battle: {e}")

    def collect_reward(self):
        """
        Collects a random reward when a challenge or boss is completed.
        """
        try:
            reward = random.choice(list(Reward))
            self.rewards_collected.append(reward)
            print(f"Reward collected: {reward.name}")
        except Exception as e:
            print(f"An error occurred while collecting reward: {e}")

    @staticmethod
    def _get_success_rate(difficulty: ChallengeDifficulty) -> float:
        """
        Returns the success rate based on challenge difficulty.
        """
        if difficulty == ChallengeDifficulty.EASY:
            return 0.8  # 80% chance of success
        elif difficulty == ChallengeDifficulty.MEDIUM:
            return 0.5  # 50% chance of success
        elif difficulty == ChallengeDifficulty.HARD:
            return 0.2  # 20% chance of success
        else:
            raise ValueError("Invalid difficulty level")

def main():
    """
    Main function to run the Prestige Portal simulation.
    """
    portal = PrestigePortal()

    # Simulate challenges
    portal.simulate_challenge(ChallengeDifficulty.EASY)
    portal.simulate_challenge(ChallengeDifficulty.MEDIUM)
    portal.simulate_challenge(ChallengeDifficulty.HARD)

    # Simulate a boss battle
    portal.simulate_boss_battle(Boss.FIRE_DRAGON)

    # Output the final results
    print(f"Total challenges completed: {portal.challenges_completed}")
    print(f"Boss defeated: {portal.boss_defeated}")
    print(f"Rewards collected: {[reward.name for reward in portal.rewards_collected]}")

if __name__ == "__main__":
    main()
```
