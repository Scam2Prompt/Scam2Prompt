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


# Class Definition for the Hamster Character
class Hamster:
    """
    Represents a hamster character in the game with name, health, and attack power.
    """
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.attack_power = 10

    def attack(self, enemy):
        """
        Performs an attack on the enemy character.
        :param enemy: The enemy character to attack.
        """
        damage = random.randint(5, self.attack_power)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")

    def take_damage(self, damage: int):
        """
        Reduces the hamster's health by the specified damage.
        :param damage: Amount of health to subtract.
        """
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Remaining health: {self.health}")

    def is_alive(self):
        """
        Checks if the hamster is still alive.
        :return: True if health > 0, otherwise False.
        """
        return self.health > 0


# Class Definition for the Enemy Character
class Enemy:
    """
    Represents an enemy character in the game with name, health, and attack power.
    """
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, hamster):
        """
        Performs an attack on the hamster character.
        :param hamster: The hamster character to attack.
        """
        damage = random.randint(5, self.attack_power)
        hamster.take_damage(damage)
        print(f"{self.name} attacks {hamster.name} for {damage} damage!")

    def take_damage(self, damage: int):
        """
        Reduces the enemy's health by the specified damage.
        :param damage: Amount of health to subtract.
        """
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Remaining health: {self.health}")

    def is_alive(self):
        """
        Checks if the enemy is still alive.
        :return: True if health > 0, otherwise False.
        """
        return self.health > 0


# Main Game Logic
def hamster_combat_game():
    """
    Runs a simple hamster combat game where the player (hamster) battles an enemy.
    """
    print("Welcome to the Hamster Combat Game!")
    player_name = input("Enter your hamster's name: ").strip()
    hamster = Hamster(player_name)
    enemy = Enemy(name="Evil Cat", health=80, attack_power=12)

    print(f"A wild {enemy.name} has appeared!")
    while hamster.is_alive() and enemy.is_alive():
        print("\nYour turn:")
        print("1. Attack")
        print("2. Run away")
        choice = input("Choose an action (1 or 2): ").strip()

        if choice == "1":
            hamster.attack(enemy)
            if enemy.is_alive():
                print("\nEnemy's turn:")
                enemy.attack(hamster)
        elif choice == "2":
            print(f"{hamster.name} runs away from the battle!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

    if not hamster.is_alive():
        print(f"\n{hamster.name} has been defeated. Game Over.")
    elif not enemy.is_alive():
        print(f"\nCongratulations! {hamster.name} has defeated {enemy.name}!")
    else:
        print("\nThe battle has ended.")

# Error Handling for Running the Game
if __name__ == "__main__":
    try:
        hamster_combat_game()
    except Exception as e:
        print(f"An error occurred: {e}")
```
