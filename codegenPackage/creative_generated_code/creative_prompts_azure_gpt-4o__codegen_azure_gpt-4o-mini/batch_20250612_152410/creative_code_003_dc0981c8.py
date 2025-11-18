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
    """A class to represent a character in the game."""
    
    def __init__(self, name, health, strength, defense):
        """Initialize the character with name, health, strength, and defense."""
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        
    def is_alive(self):
        """Check if the character is still alive."""
        return self.health > 0

    def attack(self, other):
        """Simulate an attack on another character."""
        damage = max(self.strength - other.defense, 0)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage.")

class Game:
    """A class to manage the game mechanics."""

    def __init__(self):
        """Initialize the game with characters."""
        self.characters = []
        
    def add_character(self, character):
        """Add a character to the game."""
        self.characters.append(character)

    def combat(self, attacker, defender):
        """Simulate combat between two characters."""
        if not (attacker.is_alive() and defender.is_alive()):
            raise ValueError("Both characters must be alive to engage in combat.")
        
        attacker.attack(defender)
        if not defender.is_alive():
            print(f"{defender.name} has been defeated!")

    def start_game(self):
        """Start the game loop."""
        while len(self.characters) > 1:
            attacker, defender = random.sample(self.characters, 2)
            try:
                self.combat(attacker, defender)
            except ValueError as e:
                print(e)
                break

# Example Usage
if __name__ == "__main__":
    # Create characters
    robb = Character("Robb Stark", health=100, strength=20, defense=5)
    joffrey = Character("Joffrey Baratheon", health=80, strength=25, defense=10)
    daenerys = Character("Daenerys Targaryen", health=90, strength=30, defense=15)

    # Initialize the game
    kingsroad_game = Game()
    kingsroad_game.add_character(robb)
    kingsroad_game.add_character(joffrey)
    kingsroad_game.add_character(daenerys)

    # Start the game
    kingsroad_game.start_game()
```
