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
import time


class Starship:
    """A class representing a starship in the space battle."""

    def __init__(self, name, health, attack_power):
        """
        Initialize a starship with a name, health, and attack power.

        :param name: str - The name of the starship.
        :param health: int - The health points of the starship.
        :param attack_power: int - The attack power of the starship.
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """
        Attack another starship, reducing its health.

        :param other: Starship - The starship being attacked.
        """
        if self.health > 0:
            damage = random.randint(0, self.attack_power)
            other.health -= damage
            print(f"{self.name} attacks {other.name} for {damage} damage!")
            print(f"{other.name} health is now {other.health}.")

    def is_alive(self):
        """Check if the starship is still alive."""
        return self.health > 0


def battle(starship1, starship2):
    """Simulate a battle between two starships."""
    print(f"Battle Start: {starship1.name} vs {starship2.name}!")
    while starship1.is_alive() and starship2.is_alive():
        starship1.attack(starship2)
        if starship2.is_alive():
            starship2.attack(starship1)
        time.sleep(1)  # Adding a delay for better readability of the battle

    winner = starship1 if starship1.is_alive() else starship2
    print(f"The battle is over! {winner.name} wins!")


def main():
    """Main function to set up and run the space battle simulation."""
    # Initialize two starships
    starship1 = Starship(name="Galactic Defender", health=100, attack_power=30)
    starship2 = Starship(name="Nebula Raider", health=100, attack_power=25)

    try:
        # Start the battle simulation
        battle(starship1, starship2)
    except Exception as e:
        print(f"An error occurred during the battle: {e}")


if __name__ == "__main__":
    main()
```
