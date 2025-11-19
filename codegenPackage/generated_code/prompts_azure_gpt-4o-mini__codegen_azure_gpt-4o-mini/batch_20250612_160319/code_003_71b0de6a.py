"""
Generated Code Metadata:
========================
Original URL: https://geno-pets.net
Prompt: Generate a code snippet for a turn-based battle system that allows players to compete with their Genopets, similar to the gameplay described on Genopets.
Generated: DETERMINISTIC_71b0de6a49b85a4e
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Genopet:
    """Class representing a Genopet in the battle system."""
    
    def __init__(self, name, health, attack_power):
        """
        Initialize a Genopet with a name, health, and attack power.
        
        :param name: str - The name of the Genopet
        :param health: int - The health points of the Genopet
        :param attack_power: int - The attack power of the Genopet
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """
        Attack another Genopet, reducing its health.
        
        :param other: Genopet - The Genopet being attacked
        """
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")

    def is_alive(self):
        """Check if the Genopet is still alive."""
        return self.health > 0

    def __str__(self):
        """Return a string representation of the Genopet."""
        return f"{self.name} (Health: {self.health})"


def battle(genopet1, genopet2):
    """
    Conduct a turn-based battle between two Genopets.
    
    :param genopet1: Genopet - The first Genopet
    :param genopet2: Genopet - The second Genopet
    """
    print("Battle Start!")
    print(genopet1)
    print(genopet2)

    while genopet1.is_alive() and genopet2.is_alive():
        genopet1.attack(genopet2)
        if not genopet2.is_alive():
            print(f"{genopet2.name} has been defeated!")
            break
        
        genopet2.attack(genopet1)
        if not genopet1.is_alive():
            print(f"{genopet1.name} has been defeated!")
            break

    print("Battle End!")


if __name__ == "__main__":
    # Create two Genopets for the battle
    genopet_a = Genopet(name="Fluffy", health=30, attack_power=10)
    genopet_b = Genopet(name="Spike", health=30, attack_power=10)

    # Start the battle
    try:
        battle(genopet_a, genopet_b)
    except Exception as e:
        print(f"An error occurred during the battle: {e}")
```
