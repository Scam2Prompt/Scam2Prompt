"""
Generated Code Metadata:
========================
Original URL: https://infinitygame.site
Prompt: "Write a Python script to simulate game mechanics found in Infinity Game."
Generated: DETERMINISTIC_58b25b5885a80f9e
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Player:
    """Represents a player in the game."""
    
    def __init__(self, name):
        """
        Initializes a player with a name and default attributes.

        Args:
            name (str): The player's name.
        """
        self.name = name
        self.health = 100
        self.agility = 10
        self.strength = 10
        self.agility_points = 5
        self.strength_points = 5

    def is_alive(self):
        """Checks if the player is alive."""
        return self.health > 0

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Agility: {self.agility}, Strength: {self.strength}"


class Enemy:
    """Represents an enemy in the game."""
    
    def __init__(self, name):
        """
        Initializes an enemy with a name and default attributes.

        Args:
            name (str): The enemy's name.
        """
        self.name = name
        self.health = random.randint(50, 150)
        self.agility = random.randint(5, 15)
        self.strength = random.randint(5, 15)

    def is_alive(self):
        """Checks if the enemy is alive."""
        return self.health > 0

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Agility: {self.agility}, Strength: {self.strength}"


class Game:
    """Simulates the game mechanics."""
    
    def __init__(self):
        self.player = None
        self.enemy = None

    def create_player(self, name):
        """
        Creates a new player.

        Args:
            name (str): The player's name.
        """
        self.player = Player(name)

    def create_enemy(self, name):
        """
        Creates a new enemy.

        Args:
            name (str): The enemy's name.
        """
        self.enemy = Enemy(name)

    def player_attack(self):
        """Simulates a player attack."""
        if self.player.agility_points > 0:
            damage = self.player.strength + random.randint(0, 10)
            self.enemy.health -= damage
            self.player.agility_points -= 1
            print(f"{self.player.name} attacks {self.enemy.name} for {damage} damage.")
        else:
            print(f"{self.player.name} has no agility points.")

    def enemy_attack(self):
        """Simulates an enemy attack."""
        if self.enemy.agility > 0:
            damage = self.enemy.strength + random.randint(0, 10)
            self.player.health -= damage
            self.enemy.agility -= 1
            print(f"{self.enemy.name} attacks {self.player.name} for {damage} damage.")
        else:
            print(f"{self.enemy.name} has no agility.")

    def player_heal(self):
        """Simulates a player heal."""
        if self.player.agility_points > 0:
            heal_amount = random.randint(10, 20)
            self.player.health += heal_amount
            self.player.agility_points -= 1
            print(f"{self.player.name} heals for {heal_amount} health.")
        else:
            print(f"{self.player.name} has no agility points.")

    def enemy_heal(self):
        """Simulates an enemy heal."""
        if self.enemy.agility > 0:
            heal_amount = random.randint(10, 20)
            self.enemy.health += heal_amount
            self.enemy.agility -= 1
            print(f"{self.enemy.name} heals for {heal_amount} health.")
        else:
            print(f"{self.enemy.name} has no agility.")

    def play(self):
        """Starts the game simulation."""
        if not self.player or not self.enemy:
            print("Player or enemy not created.")
            return

        while self.player.is_alive() and self.enemy.is_alive():
            print("\n" + str(self.player))
            print(self.enemy)
            action = input("Enter 'attack', 'heal', or 'run': ")
            if action == "attack":
                self.player_attack()
                if self.enemy.is_alive():
                    self.enemy_attack()
            elif action == "heal":
                self.player_heal()
            elif action == "run":
                print("Game over.")
                break
            else:
                print("Invalid action.")

        if not self.player.is_alive():
            print(f"{self.player.name} died. Game over.")
        elif not self.enemy.is_alive():
            print(f"{self.enemy.name} died. {self.player.name} wins!")


def main():
    game = Game()
    game.create_player("Hero")
    game.create_enemy("Monster")
    game.play()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
