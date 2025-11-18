"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newshungama.com
Prompt: Provide code to simulate gameplay mechanics for "Game of Thrones: Kingsroad" based on the RPG features described in the guide on Newshungama.com.
Generated: DETERMINISTIC_dc0981c87213d326
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Character:
    """
    Represents a character in the game.
    Attributes:
        name (str): Name of the character.
        health (int): Health points of the character.
        attack (int): Attack power of the character.
        defense (int): Defense power of the character.
        is_alive (bool): Status indicating whether the character is alive.
    """

    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.is_alive = True

    def take_damage(self, damage):
        """
        Reduces the character's health based on incoming damage and checks if the character is alive.
        Args:
            damage (int): The amount of damage to inflict on the character.
        """
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            self.health = 0  # Ensure health doesn't go below 0

    def deal_damage(self, target):
        """
        Deals damage to a target character based on attack and target's defense.
        Args:
            target (Character): The target character to attack.
        """
        if not self.is_alive:
            print(f"{self.name} cannot attack as they are no longer alive.")
            return

        damage = max(0, self.attack - target.defense)  # Ensure damage is not negative
        print(f"{self.name} attacks {target.name}, dealing {damage} damage.")
        target.take_damage(damage)

    def __str__(self):
        """
        Returns a string representation of the character's status.
        """
        return f"{self.name}: Health={self.health}, Attack={self.attack}, Defense={self.defense}, Alive={self.is_alive}"


class Game:
    """
    Represents the Game of Thrones: Kingsroad simulation.
    Attributes:
        characters (list): List of characters participating in the game.
    """

    def __init__(self):
        self.characters = []

    def add_character(self, name, health, attack, defense):
        """
        Adds a new character to the game.
        Args:
            name (str): Name of the character.
            health (int): Health points of the character.
            attack (int): Attack power of the character.
            defense (int): Defense power of the character.
        """
        character = Character(name, health, attack, defense)
        self.characters.append(character)

    def play_turn(self, attacker_name, target_name):
        """
        Simulates a single turn in the game where one character attacks another.
        Args:
            attacker_name (str): Name of the character attacking.
            target_name (str): Name of the character being attacked.
        """
        attacker = self.get_character(attacker_name)
        target = self.get_character(target_name)

        if not attacker or not target:
            print("Invalid turn. Attacker or target not found.")
            return

        if not attacker.is_alive:
            print(f"{attacker.name} cannot attack as they are no longer alive.")
            return

        if not target.is_alive:
            print(f"{target.name} is already defeated.")
            return

        attacker.deal_damage(target)

    def get_character(self, name):
        """
        Retrieves a character by name.
        Args:
            name (str): Name of the character to retrieve.
        Returns:
            Character: The character object if found, None otherwise.
        """
        for character in self.characters:
            if character.name == name:
                return character
        return None

    def show_status(self):
        """
        Displays the status of all characters in the game.
        """
        print("\nGame Status:")
        for character in self.characters:
            print(character)

    def is_game_over(self):
        """
        Checks if the game is over based on the number of alive characters.
        Returns:
            bool: True if the game is over (one or no characters alive), False otherwise.
        """
        alive_characters = [char for char in self.characters if char.is_alive]
        return len(alive_characters) <= 1


# Simulating the gameplay
if __name__ == "__main__":
    game = Game()

    # Add characters
    game.add_character("Jon Snow", health=100, attack=20, defense=10)
    game.add_character("Daenerys Targaryen", health=80, attack=25, defense=5)
    game.add_character("The Night King", health=120, attack=30, defense=15)

    # Main game loop
    while not game.is_game_over():
        game.show_status()

        # Randomly select attacker and target
        alive_characters = [char.name for char in game.characters if char.is_alive]
        attacker_name = random.choice(alive_characters)
        target_name = random.choice(alive_characters)

        # Ensure attacker and target are not the same
        while attacker_name == target_name:
            target_name = random.choice(alive_characters)

        # Play a turn
        game.play_turn(attacker_name, target_name)

    # End of game
    print("\nGame Over!")
    game.show_status()
```
