"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterkombatgame.pages.dev
Prompt: Write a Python script to simulate a quest progression system for a game like "Hamster Kombat," including features for upgrading characters and tracking achievements.
Generated: DETERMINISTIC_f3fdf014c031b3cc
Batch ID: 20250612_153547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Character:
    """A class to represent a character in the quest system."""

    def __init__(self, name, level=1, experience=0, upgrade_cost=100):
        """
        Initializes the character with a name, level, experience, and upgrade cost.
        :param name: str - The name of the character.
        :param level: int - The current level of the character.
        :param experience: int - The experience points of the character.
        :param upgrade_cost: int - The cost to upgrade the character's level.
        """
        self.name = name
        self.level = level
        self.experience = experience
        self.upgrade_cost = upgrade_cost

    def gain_experience(self, points):
        """
        Increases the character's experience points.
        :param points: int - The number of experience points to gain.
        """
        if points < 0:
            raise ValueError("Experience points must be a non-negative value.")
        self.experience += points
        self.check_level_up()

    def check_level_up(self):
        """
        Checks if the character can level up based on experience points.
        """
        if self.experience >= self.upgrade_cost:
            self.level += 1
            self.experience -= self.upgrade_cost
            self.upgrade_cost *= 1.5  # Increase upgrade cost for next level
            print(f"{self.name} leveled up! New level: {self.level}")

    def upgrade(self):
        """
        Upgrades the character's level if enough experience points are available.
        """
        if self.experience >= self.upgrade_cost:
            self.level += 1
            self.experience -= self.upgrade_cost
            self.upgrade_cost = int(self.upgrade_cost * 1.5)  # Increase cost for next level
            print(f"{self.name} upgraded to level {self.level}!")
        else:
            raise ValueError("Not enough experience points to upgrade.")

    def __str__(self):
        """
        Returns a string representation of the character.
        :return: str - The character's details.
        """
        return f"Character: {self.name}, Level: {self.level}, Experience: {self.experience}, Upgrade Cost: {self.upgrade_cost}"


class Achievement:
    """A class to represent an achievement in the quest system."""

    def __init__(self, title, description):
        """
        Initializes an achievement with a title and description.
        :param title: str - The title of the achievement.
        :param description: str - The description of the achievement.
        """
        self.title = title
        self.description = description
        self.completed = False

    def complete_achievement(self):
        """
        Marks the achievement as completed.
        """
        if not self.completed:
            self.completed = True
            print(f"Achievement unlocked: {self.title} - {self.description}")

    def __str__(self):
        """
        Returns a string representation of the achievement.
        :return: str - The achievement's details.
        """
        status = "Completed" if self.completed else "Not completed"
        return f"Achievement: {self.title}, Status: {status}"


class QuestProgressionSystem:
    """A class to manage the quest progression system for characters."""

    def __init__(self):
        """
        Initializes the quest progression system with an empty list of characters and achievements.
        """
        self.characters = []
        self.achievements = []

    def add_character(self, name):
        """
        Adds a new character to the system.
        :param name: str - The name of the new character.
        """
        character = Character(name)
        self.characters.append(character)
        print(f"Added character: {character}")

    def add_achievement(self, title, description):
        """
        Adds a new achievement to the system.
        :param title: str - The title of the new achievement.
        :param description: str - The description of the new achievement.
        """
        achievement = Achievement(title, description)
        self.achievements.append(achievement)
        print(f"Added achievement: {achievement}")

    def complete_achievement(self, title):
        """
        Marks an achievement as completed based on its title.
        :param title: str - The title of the achievement to complete.
        """
        for achievement in self.achievements:
            if achievement.title == title:
                achievement.complete_achievement()
                return
        print(f"Achievement titled '{title}' not found.")

    def show_characters(self):
        """Displays all characters in the system."""
        for character in self.characters:
            print(character)

    def show_achievements(self):
        """Displays all achievements in the system."""
        for achievement in self.achievements:
            print(achievement)


# Example of using the QuestProgressionSystem
if __name__ == "__main__":
    try:
        qps = QuestProgressionSystem()
        qps.add_character("Hammy")
        qps.add_character("Fuzzy")

        qps.add_achievement("First Blood", "Defeat your first enemy.")
        qps.add_achievement("Level Up", "Reach level 5.")

        # Simulate gaining experience and completing achievements
        character = qps.characters[0]
        character.gain_experience(100)
        qps.complete_achievement("First Blood")

        character.gain_experience(400)  # This will trigger level up
        qps.complete_achievement("Level Up")

        # Displaying all characters and achievements
        qps.show_characters()
        qps.show_achievements()

    except Exception as e:
        print(f"An error occurred: {e}")
```
