"""
Generated Code Metadata:
========================
Original URL: https://swap.depillama.com
Prompt: Using the themes from Swap Llama's "War in the Space Odyssey," create a simulation in Python that models a strategic space battle between starships.
Generated: DETERMINISTIC_2996f112776f5354
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Starship:
    """Represents a starship with its attributes and methods."""

    def __init__(self, name, hull_integrity, shield_capacity, firepower):
        """
        Initializes a Starship object.

        Args:
            name (str): The name of the starship.
            hull_integrity (int): The initial hull integrity of the starship.
            shield_capacity (int): The maximum shield capacity of the starship.
            firepower (int): The firepower of the starship.
        """
        self.name = name
        self.hull_integrity = hull_integrity
        self.shield_capacity = shield_capacity
        self.current_shield = shield_capacity
        self.firepower = firepower

    def is_destroyed(self):
        """Checks if the starship is destroyed."""
        return self.hull_integrity <= 0

    def take_damage(self, damage):
        """
        Applies damage to the starship.

        Args:
            damage (int): The amount of damage to apply.
        """
        if self.current_shield > 0:
            # Apply damage to shields first
            self.current_shield -= damage
            if self.current_shield < 0:
                # If shields are depleted, apply remaining damage to hull
                self.hull_integrity += self.current_shield
                self.current_shield = 0
        else:
            # No shields, apply damage directly to hull
            self.hull_integrity -= damage

    def __str__(self):
        """Returns a string representation of the starship."""
        return f"{self.name} - Hull: {self.hull_integrity}, Shields: {self.current_shield}, Firepower: {self.firepower}"


class SpaceBattle:
    """Simulates a strategic space battle between starships."""

    def __init__(self, starship1, starship2):
        """
        Initializes a SpaceBattle object.

        Args:
            starship1 (Starship): The first starship.
            starship2 (Starship): The second starship.
        """
        self.starship1 = starship1
        self.starship2 = starship2
        self.turn = 0

    def simulate_battle(self):
        """Simulates the space battle."""
        while not self.starship1.is_destroyed() and not self.starship2.is_destroyed():
            self.turn += 1
            print(f"\n--- Turn {self.turn} ---")
            print(self.starship1)
            print(self.starship2)

            # Starship 1's turn
            if not self.starship1.is_destroyed():
                damage = random.randint(0, self.starship1.firepower)
                self.starship2.take_damage(damage)
                print(f"{self.starship1.name} attacks {self.starship2.name} for {damage} damage.")

            # Starship 2's turn
            if not self.starship2.is_destroyed():
                damage = random.randint(0, self.starship2.firepower)
                self.starship1.take_damage(damage)
                print(f"{self.starship2.name} attacks {self.starship1.name} for {damage} damage.")

        # Determine the winner
        if self.starship1.is_destroyed():
            print(f"\n{self.starship2.name} wins!")
        else:
            print(f"\n{self.starship1.name} wins!")


def main():
    try:
        # Create starships
        starship1 = Starship("Llama's Fury", 1000, 500, 200)
        starship2 = Starship("Odyssey's Hope", 1200, 600, 250)

        # Simulate the battle
        battle = SpaceBattle(starship1, starship2)
        battle.simulate_battle()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
