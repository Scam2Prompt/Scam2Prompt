"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Write a Python script to simulate the resource collection and leveling-up mechanics described in the SIMemes game, specifically focusing on collecting "poop" as currency and defending resources.
Generated: DETERMINISTIC_91e72474e438dabe
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class SIMemesGame:
    """
    A class to simulate SIMemes game mechanics involving resource collection (poop) 
    and leveling-up features with defense functionality.
    """

    def __init__(self):
        """
        Initialize the game with default values.
        """
        self.poop_collected = 0  # Poop currency collected
        self.level = 1  # Initial player level
        self.defense_level = 1  # Initial defense level
        self.collection_rate = 1  # Poop collected per tick
        self.attack_probability = 0.1  # Probability of an attack occurring (10%)

    def collect_poop(self):
        """
        Simulate resource collection. The player collects poop based on their collection rate.
        """
        self.poop_collected += self.collection_rate
        print(f"[INFO] Collected {self.collection_rate} poop. Total poop: {self.poop_collected}")

    def level_up(self):
        """
        Simulate leveling up. Costs increase at higher levels.
        """
        level_up_cost = self.level ** 2 * 10  # Example: Leveling up cost scales quadratically
        if self.poop_collected >= level_up_cost:
            self.poop_collected -= level_up_cost
            self.level += 1
            self.collection_rate += 1  # Increase collection rate with level
            print(f"[INFO] Level up! New level: {self.level}. Collection rate: {self.collection_rate}")
        else:
            print(f"[WARNING] Not enough poop to level up. Needed: {level_up_cost}, Available: {self.poop_collected}")

    def upgrade_defense(self):
        """
        Simulate upgrading defense. Defense cost scales with level.
        """
        defense_upgrade_cost = self.defense_level ** 2 * 15  # Example: Defense upgrade cost scales quadratically
        if self.poop_collected >= defense_upgrade_cost:
            self.poop_collected -= defense_upgrade_cost
            self.defense_level += 1
            print(f"[INFO] Defense upgraded! New defense level: {self.defense_level}")
        else:
            print(f"[WARNING] Not enough poop to upgrade defense. Needed: {defense_upgrade_cost}, Available: {self.poop_collected}")

    def defend_resources(self):
        """
        Simulate defending resources against an attack. Success depends on defense level.
        """
        if random.random() < self.attack_probability:  # Attack occurs with some probability
            print("[ALERT] Attack! Defending...")
            if random.random() < self.defense_level / (self.defense_level + 5):  # Defense success chance
                print("[SUCCESS] Defense successful! No poop lost.")
            else:
                loss = self.poop_collected // 2  # Lose half of the poop if defense fails
                self.poop_collected -= loss
                print(f"[FAILURE] Defense failed! Lost {loss} poop. Remaining poop: {self.poop_collected}")
        else:
            print("[INFO] No attack occurred.")

    def play_turn(self):
        """
        Simulate a single turn in the game.
        """
        print("\n[TURN START]")
        self.collect_poop()
        self.defend_resources()

        # Provide options to the player for actions
        print("[OPTIONS] Choose an action:")
        print("1. Level up")
        print("2. Upgrade defense")
        print("3. Skip")
        action = input("Enter the number of your action: ")

        if action == '1':
            self.level_up()
        elif action == '2':
            self.upgrade_defense()
        elif action == '3':
            print("[INFO] Turn skipped.")
        else:
            print("[ERROR] Invalid action. Skipping turn.")

    def start_game(self):
        """
        Start the game loop.
        """
        print("Welcome to SIMemes Game!")
        print("[INFO] Collect poop, level up, and defend your resources.")

        try:
            while True:
                self.play_turn()
                time.sleep(1)  # Pause for a short duration between turns
        except KeyboardInterrupt:
            print("\n[INFO] Game ended. Thanks for playing!")
        except Exception as e:
            print(f"[ERROR] An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    game = SIMemesGame()
    game.start_game()
```
