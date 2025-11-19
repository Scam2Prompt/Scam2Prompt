"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamster-kombatgame.com
Prompt: Write a Python script that simulates hamster combat scenarios based on the game mechanics from hamster-kombatgame.com.
Generated: DETERMINISTIC_a4d84f3be883029d
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

class Hamster:
    """Class representing a hamster in the combat simulation."""
    
    def __init__(self, name, health=100, attack_power=10):
        """Initialize a hamster with a name, health, and attack power."""
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        """Check if the hamster is alive."""
        return self.health > 0

    def attack(self, other_hamster):
        """Attack another hamster, inflicting damage."""
        if not isinstance(other_hamster, Hamster):
            raise ValueError("Can only attack another Hamster")
        
        if self.is_alive():
            damage = random.randint(1, self.attack_power)
            other_hamster.health -= damage
            print(f"{self.name} attacks {other_hamster.name} for {damage} damage!")
            print(f"{other_hamster.name}'s health is now {other_hamster.health}.")
        else:
            print(f"{self.name} cannot attack because they are not alive.")
        
class Battle:
    """Class to manage the combat between two hamsters."""
    
    def __init__(self, hamster1, hamster2):
        """Initialize the battle with two hamsters."""
        if not isinstance(hamster1, Hamster) or not isinstance(hamster2, Hamster):
            raise ValueError("Both participants must be Hamster instances")
        
        self.hamster1 = hamster1
        self.hamster2 = hamster2

    def start_battle(self):
        """Begin the battle until one hamster is out of health."""
        print(f"Battle starts between {self.hamster1.name} and {self.hamster2.name}!")
        
        while self.hamster1.is_alive() and self.hamster2.is_alive():
            self.hamster1.attack(self.hamster2)
            if self.hamster2.is_alive():
                self.hamster2.attack(self.hamster1)
        
        self.declare_winner()

    def declare_winner(self):
        """Declare the winner of the battle."""
        if self.hamster1.is_alive():
            print(f"{self.hamster1.name} wins the battle!")
        elif self.hamster2.is_alive():
            print(f"{self.hamster2.name} wins the battle!")
        else:
            print("It's a draw!")

def main():
    """Main function to run the hamster combat simulation."""
    # Create two hamsters for the battle
    hamster1 = Hamster(name="Hammy", attack_power=20)
    hamster2 = Hamster(name="Fuzzy", attack_power=15)

    # Start the battle
    battle = Battle(hamster1, hamster2)
    battle.start_battle()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
