"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap.depillama.com
Prompt: Using the themes from Swap Llama's "War in the Space Odyssey," create a simulation in Python that models a strategic space battle between starships.
Generated: DETERMINISTIC_2996f112776f5354
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Starship:
    """
    A class to represent a starship in the space battle simulation.
    """
    def __init__(self, name, health, attack_power, defense):
        """
        Initializes a starship.

        :param name: The name of the starship.
        :param health: The starting health of the starship.
        :param attack_power: The attack power of the starship.
        :param defense: The defense capability of the starship.
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, target):
        """
        Simulates an attack on another starship.

        :param target: The target starship to attack.
        """
        damage = max(0, self.attack_power - target.defense)  # Ensure damage is non-negative
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        if target.health <= 0:
            print(f"{target.name} has been destroyed!")

    def is_destroyed(self):
        """
        Checks if the starship is destroyed.

        :return: True if the starship's health is <= 0, False otherwise.
        """
        return self.health <= 0


class SpaceBattle:
    """
    A class to manage the space battle simulation.
    """
    def __init__(self, starship1, starship2):
        """
        Initializes a space battle between two starships.

        :param starship1: The first starship.
        :param starship2: The second starship.
        """
        self.starship1 = starship1
        self.starship2 = starship2

    def simulate_battle(self):
        """
        Simulates the space battle between two starships.
        """
        print("\n--- Space Battle Begins ---")
        print(f"{self.starship1.name} vs {self.starship2.name}\n")

        while not self.starship1.is_destroyed() and not self.starship2.is_destroyed():
            # Randomize which starship attacks first in each round
            if random.choice([True, False]):
                self.starship1.attack(self.starship2)
                if not self.starship2.is_destroyed():
                    self.starship2.attack(self.starship1)
            else:
                self.starship2.attack(self.starship1)
                if not self.starship1.is_destroyed():
                    self.starship1.attack(self.starship2)

        print("\n--- Battle Over ---")
        if self.starship1.is_destroyed():
            print(f"{self.starship2.name} wins!")
        elif self.starship2.is_destroyed():
            print(f"{self.starship1.name} wins!")
        else:
            print("It's a draw!")


# Create two starships with unique attributes
starship_a = Starship(name="USS Odyssey", health=100, attack_power=25, defense=10)
starship_b = Starship(name="Intergalactic Destroyer", health=120, attack_power=20, defense=15)

# Initialize the space battle
battle = SpaceBattle(starship_a, starship_b)

# Simulate the battle
battle.simulate_battle()
```
