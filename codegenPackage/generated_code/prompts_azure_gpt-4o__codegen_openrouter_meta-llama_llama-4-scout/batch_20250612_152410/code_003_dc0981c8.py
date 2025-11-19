"""
Generated Code Metadata:
========================
Original URL: https://newshungama.com
Prompt: Provide code to simulate gameplay mechanics for "Game of Thrones: Kingsroad" based on the RPG features described in the guide on Newshungama.com.
Generated: DETERMINISTIC_dc0981c87213d326
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# game_of_thrones_kingsroad.py

import random

class Character:
    """Represents a character in the game."""
    
    def __init__(self, name, character_class, level=1):
        """
        Initializes a character.

        Args:
            name (str): The character's name.
            character_class (str): The character's class (e.g., Warrior, Mage).
            level (int, optional): The character's level. Defaults to 1.
        """
        self.name = name
        self.character_class = character_class
        self.level = level
        self.health = self.calculate_health()
        self.strength = self.calculate_strength()
        self.agility = self.calculate_agility()
        self.intelligence = self.calculate_intelligence()
        self.experience = 0

    def calculate_health(self):
        """Calculates the character's health based on their level and class."""
        if self.character_class == "Warrior":
            return 100 + (self.level * 10)
        elif self.character_class == "Mage":
            return 80 + (self.level * 8)
        else:
            return 90 + (self.level * 9)

    def calculate_strength(self):
        """Calculates the character's strength based on their level and class."""
        if self.character_class == "Warrior":
            return 15 + (self.level * 2)
        elif self.character_class == "Mage":
            return 5 + (self.level * 1)
        else:
            return 10 + (self.level * 1.5)

    def calculate_agility(self):
        """Calculates the character's agility based on their level and class."""
        if self.character_class == "Warrior":
            return 10 + (self.level * 1.5)
        elif self.character_class == "Mage":
            return 12 + (self.level * 2)
        else:
            return 11 + (self.level * 1.7)

    def calculate_intelligence(self):
        """Calculates the character's intelligence based on their level and class."""
        if self.character_class == "Warrior":
            return 5 + (self.level * 0.5)
        elif self.character_class == "Mage":
            return 18 + (self.level * 3)
        else:
            return 8 + (self.level * 1)

    def gain_experience(self, experience):
        """Increases the character's experience."""
        self.experience += experience
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        """Levels up the character."""
        self.level += 1
        self.health = self.calculate_health()
        self.strength = self.calculate_strength()
        self.agility = self.calculate_agility()
        self.intelligence = self.calculate_intelligence()
        self.experience = 0
        print(f"{self.name} has leveled up to level {self.level}!")

    def is_alive(self):
        """Checks if the character is alive."""
        return self.health > 0

    def take_damage(self, damage):
        """Reduces the character's health by the given damage."""
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def deal_damage(self):
        """Calculates the character's damage based on their strength."""
        return self.strength * random.uniform(0.8, 1.2)


class Enemy:
    """Represents an enemy in the game."""
    
    def __init__(self, name, level):
        """
        Initializes an enemy.

        Args:
            name (str): The enemy's name.
            level (int): The enemy's level.
        """
        self.name = name
        self.level = level
        self.health = 50 + (self.level * 10)
        self.strength = 10 + (self.level * 1.5)

    def is_alive(self):
        """Checks if the enemy is alive."""
        return self.health > 0

    def take_damage(self, damage):
        """Reduces the enemy's health by the given damage."""
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def deal_damage(self):
        """Calculates the enemy's damage based on their strength."""
        return self.strength * random.uniform(0.8, 1.2)


def combat(character, enemy):
    """Simulates combat between a character and an enemy."""
    while character.is_alive() and enemy.is_alive():
        damage = character.deal_damage()
        enemy.take_damage(damage)
        print(f"{character.name} attacks {enemy.name} for {damage:.2f} damage.")
        if enemy.is_alive():
            damage = enemy.deal_damage()
            character.take_damage(damage)
            print(f"{enemy.name} attacks {character.name} for {damage:.2f} damage.")
    if character.is_alive():
        print(f"{character.name} has defeated {enemy.name}!")
        character.gain_experience(100)
    else:
        print(f"{character.name} has been defeated by {enemy.name}.")


def main():
    character = Character("Hero", "Warrior")
    print(f"Name: {character.name}")
    print(f"Class: {character.character_class}")
    print(f"Level: {character.level}")
    print(f"Health: {character.health}")
    print(f"Strength: {character.strength}")
    print(f"Agility: {character.agility}")
    print(f"Intelligence: {character.intelligence}")

    enemies = [
        Enemy("Bandit", 1),
        Enemy("Orc", 2),
        Enemy("Troll", 3)
    ]

    for enemy in enemies:
        print(f"\nEncountering {enemy.name}!")
        combat(character, enemy)

if __name__ == "__main__":
    main()
```
