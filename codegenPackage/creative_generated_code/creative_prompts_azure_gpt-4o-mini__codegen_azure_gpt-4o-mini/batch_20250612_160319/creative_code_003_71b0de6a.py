"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geno-pets.net
Prompt: Generate a code snippet for a turn-based battle system that allows players to compete with their Genopets, similar to the gameplay described on Genopets.
Generated: DETERMINISTIC_71b0de6a49b85a4e
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Genopet:
    """Class representing a Genopet in the battle system."""
    
    def __init__(self, name, health, attack):
        """
        Initializes a Genopet with its name, health, and attack power.
        
        Args:
            name (str): The name of the Genopet.
            health (int): The health points of the Genopet.
            attack (int): The attack power of the Genopet.
        """
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        """Checks if the Genopet is still alive."""
        return self.health > 0

    def attack_genopet(self, opponent):
        """
        Attacks an opponent Genopet, reducing its health.
        
        Args:
            opponent (Genopet): The Genopet to be attacked.
        """
        damage = random.randint(1, self.attack)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

class Battle:
    """Class representing the turn-based battle system."""
    
    def __init__(self, genopet1, genopet2):
        """
        Initializes the battle with two Genopets.
        
        Args:
            genopet1 (Genopet): The first Genopet.
            genopet2 (Genopet): The second Genopet.
        """
        self.genopet1 = genopet1
        self.genopet2 = genopet2

    def start_battle(self):
        """Starts the battle until one Genopet is defeated."""
        print(f"Battle starts between {self.genopet1.name} and {self.genopet2.name}!")
        
        while self.genopet1.is_alive() and self.genopet2.is_alive():
            self.genopet1.attack_genopet(self.genopet2)
            self.display_health()
            if not self.genopet2.is_alive():
                print(f"{self.genopet2.name} has been defeated!")
                break
            
            self.genopet2.attack_genopet(self.genopet1)
            self.display_health()
            if not self.genopet1.is_alive():
                print(f"{self.genopet1.name} has been defeated!")

    def display_health(self):
        """Displays the current health of both Genopets."""
        print(f"{self.genopet1.name} Health: {self.genopet1.health}")
        print(f"{self.genopet2.name} Health: {self.genopet2.health}")
        print("-" * 30)

# Example usage (this part can be commented out in production):
if __name__ == "__main__":
    # Create two Genopets
    pet1 = Genopet("Fluffy", health=100, attack=20)
    pet2 = Genopet("Sparky", health=80, attack=25)

    # Start the battle
    battle = Battle(pet1, pet2)
    battle.start_battle()
```
