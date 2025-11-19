"""
Generated Code Metadata:
========================
Original URL: https://sonicevm.pages.dev
Prompt: "Develop a use case for Sonic's sandbox environment in building business logic for a game, including data types and utilities."
Generated: DETERMINISTIC_9c05e72962d8daae
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Sonic Sandbox Environment Use Case for Game Business Logic

class GameCharacter:
    """
    Represents a character in the game with attributes and methods to manage its state.
    """

    def __init__(self, name: str, health: int, attack_power: int):
        """
        Initializes a new GameCharacter instance.

        :param name: The name of the character.
        :param health: The health points of the character.
        :param attack_power: The attack power of the character.
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other: 'GameCharacter'):
        """
        Attacks another character, reducing their health.

        :param other: The character being attacked.
        """
        if self.health <= 0:
            raise ValueError(f"{self.name} cannot attack because they are defeated.")
        if other.health <= 0:
            raise ValueError(f"{other.name} cannot be attacked because they are already defeated.")

        print(f"{self.name} attacks {other.name} for {self.attack_power} damage.")
        other.health -= self.attack_power
        other.health = max(other.health, 0)  # Ensure health does not go below 0
        print(f"{other.name}'s health is now {other.health}.")

    def is_defeated(self) -> bool:
        """
        Checks if the character is defeated.

        :return: True if the character's health is 0, otherwise False.
        """
        return self.health <= 0


class Game:
    """
    Represents the game environment where characters interact.
    """

    def __init__(self):
        """
        Initializes a new Game instance with an empty list of characters.
        """
        self.characters = []

    def add_character(self, character: GameCharacter):
        """
        Adds a character to the game.

        :param character: The character to add.
        """
        self.characters.append(character)
        print(f"{character.name} has joined the game.")

    def start_battle(self):
        """
        Starts a battle between characters in the game.
        """
        if len(self.characters) < 2:
            raise ValueError("At least two characters are required to start a battle.")

        attacker_index = 0
        while True:
            attacker = self.characters[attacker_index]
            defender_index = (attacker_index + 1) % len(self.characters)
            defender = self.characters[defender_index]

            try:
                attacker.attack(defender)
            except ValueError as e:
                print(e)
                break

            if defender.is_defeated():
                print(f"{defender.name} has been defeated!")
                break

            attacker_index = defender_index  # Switch turns


# Example usage
if __name__ == "__main__":
    # Create a game instance
    game = Game()

    # Create characters
    sonic = GameCharacter(name="Sonic", health=100, attack_power=20)
    knuckles = GameCharacter(name="Knuckles", health=80, attack_power=25)

    # Add characters to the game
    game.add_character(sonic)
    game.add_character(knuckles)

    # Start the battle
    game.start_battle()
```
