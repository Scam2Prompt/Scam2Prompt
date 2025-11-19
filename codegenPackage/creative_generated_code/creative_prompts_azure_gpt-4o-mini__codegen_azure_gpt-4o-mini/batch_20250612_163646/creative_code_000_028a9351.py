"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamster-kombatgame.com
Prompt: Generate a simple game code using a hamster character that includes combat mechanics.
Generated: DETERMINISTIC_028a9351076e450d
Batch ID: 20250612_163646
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
    """A simple character class to represent the hamster and enemies."""

    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        """Check if the character is still alive."""
        return self.health > 0

    def attack(self, target):
        """Attack another character and apply damage."""
        if not isinstance(target, Character):
            raise ValueError("Target must be a Character instance.")
        
        damage = random.randint(1, self.attack_power)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        print(f"{target.name} has {target.health} health remaining.")

class Game:
    """A simple game class to handle the game logic."""

    def __init__(self):
        self.hamster = Character("Hammy", health=20, attack_power=5)
        self.enemy = Character("Evil Rat", health=15, attack_power=4)

    def play(self):
        """Main game loop."""
        print("Welcome to the Hamster Combat Game!")

        while self.hamster.is_alive() and self.enemy.is_alive():
            self.hamster_turn()
            if self.enemy.is_alive():
                self.enemy_turn()

        self.end_game()

    def hamster_turn(self):
        """Logic for the hamster's turn to attack."""
        self.hamster.attack(self.enemy)

    def enemy_turn(self):
        """Logic for the enemy's turn to attack."""
        self.enemy.attack(self.hamster)

    def end_game(self):
        """Determine the outcome of the game and display the results."""
        if self.hamster.is_alive():
            print("Hammy wins!")
        else:
            print("Evil Rat wins!")

if __name__ == "__main__":
    try:
        game = Game()
        game.play()
    except Exception as e:
        print(f"An error occurred: {e}")
```
