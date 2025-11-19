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

# Define the Hamster class to encapsulate hamster attributes and behavior
class Hamster:
    def __init__(self, name, health, attack_power, defense_power):
        """
        Initialize a hamster with a name, health, attack power, and defense power.
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self, opponent):
        """
        Simulate an attack on another hamster, considering attack and defense power.
        """
        damage = self.attack_power - opponent.defense_power
        damage = max(damage, 0)  # Prevent negative damage
        opponent.health -= damage

        return damage

    def is_alive(self):
        """
        Check if the hamster is still alive (health > 0).
        """
        return self.health > 0


def simulate_combat(hamster1, hamster2):
    """
    Simulate a combat scenario between two hamsters until one is defeated.
    """
    print(f"Combat Start: {hamster1.name} vs {hamster2.name}")
    print(f"{hamster1.name} Health: {hamster1.health}, {hamster2.name} Health: {hamster2.health}")

    round_number = 1

    while hamster1.is_alive() and hamster2.is_alive():
        print(f"\n--- Round {round_number} ---")

        # Hamster 1 attacks Hamster 2
        damage_to_hamster2 = hamster1.attack(hamster2)
        print(f"{hamster1.name} attacks {hamster2.name} for {damage_to_hamster2} damage!")
        if not hamster2.is_alive():
            print(f"{hamster2.name} has been defeated!")
            break

        # Hamster 2 attacks Hamster 1
        damage_to_hamster1 = hamster2.attack(hamster1)
        print(f"{hamster2.name} attacks {hamster1.name} for {damage_to_hamster1} damage!")
        if not hamster1.is_alive():
            print(f"{hamster1.name} has been defeated!")
            break

        # Print current health status
        print(f"{hamster1.name} Health: {hamster1.health}, {hamster2.name} Health: {hamster2.health}")

        round_number += 1

    print("\nCombat End!")


def create_random_hamster(name):
    """
    Create a hamster with random stats for health, attack power, and defense power.
    """
    health = random.randint(50, 100)
    attack_power = random.randint(10, 20)
    defense_power = random.randint(5, 15)
    return Hamster(name, health, attack_power, defense_power)


if __name__ == "__main__":
    # Create two random hamsters
    hamster1 = create_random_hamster("Hamster Warrior")
    hamster2 = create_random_hamster("Hamster Ninja")

    # Simulate combat between the two hamsters
    simulate_combat(hamster1, hamster2)
```
