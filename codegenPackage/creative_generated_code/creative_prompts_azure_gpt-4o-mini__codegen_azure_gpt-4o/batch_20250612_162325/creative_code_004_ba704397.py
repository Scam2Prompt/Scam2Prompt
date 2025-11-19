"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monarch-game.pages.dev
Prompt: Create a code example that simulates the leveling up of a Dragon from D1 to D5 in the Monarch Dungeon based on game activity.
Generated: DETERMINISTIC_ba70439734f5c0d9
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Dragon:
    """
    Represents a Dragon in the Monarch Dungeon game.
    A Dragon can level up from D1 to D5 based on activity points earned.
    """
    
    def __init__(self, name):
        """
        Initialize a new Dragon with a name, starting level (D1), 
        and zero activity points.
        """
        self.name = name
        self.level = "D1"
        self.activity_points = 0

        # Level thresholds
        self.level_thresholds = {
            "D2": 50,
            "D3": 150,
            "D4": 300,
            "D5": 500
        }

    def earn_activity_points(self):
        """
        Simulates earning random activity points during gameplay.
        """
        points_earned = random.randint(10, 50)
        self.activity_points += points_earned
        print(f"{self.name} earned {points_earned} activity points! Total: {self.activity_points}")
        self.check_level_up()

    def check_level_up(self):
        """
        Checks if the Dragon qualifies for a level-up based on activity points.
        Updates the Dragon's level if conditions are met.
        """
        for level, threshold in self.level_thresholds.items():
            if self.activity_points >= threshold and self.level != level:
                self.level = level
                print(f"Congratulations! {self.name} leveled up to {self.level}!")

    def display_status(self):
        """
        Displays the current status of the Dragon.
        """
        print(f"Dragon Name: {self.name}")
        print(f"Current Level: {self.level}")
        print(f"Activity Points: {self.activity_points}")


# Game Simulation
if __name__ == "__main__":
    # Create a new Dragon
    dragon = Dragon("Drako")

    print("Welcome to the Monarch Dungeon!")
    dragon.display_status()

    try:
        # Simulate earning activity points and leveling up
        for _ in range(15):  # Simulates 15 rounds of activity
            dragon.earn_activity_points()
            dragon.display_status()

    except Exception as e:
        # Properly handle any unexpected errors
        print(f"An error occurred during gameplay: {e}")
```
