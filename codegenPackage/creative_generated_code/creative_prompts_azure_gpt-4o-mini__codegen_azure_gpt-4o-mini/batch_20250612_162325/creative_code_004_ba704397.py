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
class Dragon:
    """
    A class to represent a Dragon in the Monarch Dungeon game.

    Attributes:
        name (str): The name of the dragon.
        level (int): The current level of the dragon (from 1 to 5).
        experience (int): The total experience points the dragon has earned.
    """

    def __init__(self, name: str):
        """
        Initializes a new instance of the Dragon class.

        Args:
            name (str): The name of the dragon.
        """
        self.name = name
        self.level = 1
        self.experience = 0

    def gain_experience(self, points: int):
        """
        Increases the dragon's experience points and levels up if necessary.

        Args:
            points (int): Experience points to be added.

        Raises:
            ValueError: If points is negative.
        """
        if points < 0:
            raise ValueError("Experience points cannot be negative.")
        self.experience += points
        print(f"{self.name} gained {points} experience points!")

        # Check for level up
        self.check_level_up()

    def check_level_up(self):
        """
        Checks if the dragon can level up based on its experience points.
        Levels are defined as follows:
            Level 1: 0 - 99 XP
            Level 2: 100 - 199 XP
            Level 3: 200 - 299 XP
            Level 4: 300 - 399 XP
            Level 5: 400+ XP
        """
        if self.level < 5 and self.experience >= self.level * 100:
            self.level += 1
            print(f"{self.name} leveled up to Level {self.level}!")

    def __str__(self):
        """
        Returns a string representation of the dragon's current state.

        Returns:
            str: Information about the dragon.
        """
        return f"{self.name} - Level: {self.level}, Experience: {self.experience}"


# Example usage
if __name__ == "__main__":
    # Create a new dragon
    my_dragon = Dragon(name="Fury")

    # Simulate gaining experience
    try:
        experience_points = [50, 70, 120, 80, 150]  # Example experience points to gain
        for points in experience_points:
            my_dragon.gain_experience(points)
            print(my_dragon)

    except ValueError as e:
        print(f"Error: {e}")
```
