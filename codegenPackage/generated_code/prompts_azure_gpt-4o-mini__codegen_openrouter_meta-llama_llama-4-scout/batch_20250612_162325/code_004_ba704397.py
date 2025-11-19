"""
Generated Code Metadata:
========================
Original URL: https://monarch-game.pages.dev
Prompt: Create a code example that simulates the leveling up of a Dragon from D1 to D5 in the Monarch Dungeon based on game activity.
Generated: DETERMINISTIC_ba70439734f5c0d9
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dragon.py

class Dragon:
    """
    Represents a Dragon in the Monarch Dungeon.

    Attributes:
        level (int): The current level of the Dragon (D1 to D5).
        experience (int): The current experience points of the Dragon.
        experience_required (int): The experience points required to level up.
    """

    def __init__(self, level=1, experience=0):
        """
        Initializes a new Dragon.

        Args:
            level (int, optional): The initial level of the Dragon. Defaults to 1.
            experience (int, optional): The initial experience points of the Dragon. Defaults to 0.
        """
        self.level = level
        self.experience = experience
        self.experience_required = self.calculate_experience_required()

    def calculate_experience_required(self):
        """
        Calculates the experience points required to level up based on the current level.

        Returns:
            int: The experience points required to level up.
        """
        return self.level * 100

    def add_experience(self, amount):
        """
        Adds experience points to the Dragon.

        Args:
            amount (int): The amount of experience points to add.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Experience points cannot be negative")

        self.experience += amount
        self.check_level_up()

    def check_level_up(self):
        """
        Checks if the Dragon has enough experience points to level up.

        If the Dragon has enough experience points, levels up the Dragon and resets the experience points.
        """
        while self.experience >= self.experience_required and self.level < 5:
            self.level_up()

    def level_up(self):
        """
        Levels up the Dragon.

        Increases the level, resets the experience points, and updates the experience points required.
        """
        self.level += 1
        self.experience -= self.experience_required
        self.experience_required = self.calculate_experience_required()
        print(f"Dragon leveled up to D{self.level}")


def simulate_game_activity(dragon):
    """
    Simulates game activity by adding experience points to the Dragon.

    Args:
        dragon (Dragon): The Dragon to simulate game activity for.
    """
    # Simulate game activity (e.g., killing monsters, completing quests)
    experience_gains = [50, 75, 25, 100, 150, 200, 300, 250]
    for gain in experience_gains:
        dragon.add_experience(gain)
        print(f"Dragon experience: {dragon.experience}, Level: D{dragon.level}")


def main():
    dragon = Dragon()
    print("Initial Dragon Level:", f"D{dragon.level}")
    simulate_game_activity(dragon)
    print("Final Dragon Level:", f"D{dragon.level}")


if __name__ == "__main__":
    main()
```
