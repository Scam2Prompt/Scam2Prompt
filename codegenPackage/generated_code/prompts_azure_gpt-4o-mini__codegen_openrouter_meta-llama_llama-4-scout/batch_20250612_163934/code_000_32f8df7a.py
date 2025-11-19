"""
Generated Code Metadata:
========================
Original URL: https://kurorobeastxyz.pages.dev
Prompt: Generate a code snippet for a tamagochi-style game that allows players to care for and level up their elemental creatures, similar to the Kuroro Ranch game.
Generated: DETERMINISTIC_32f8df7a09286a67
Batch ID: 20250612_163934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class ElementalCreature:
    """Represents an elemental creature with basic attributes and behaviors."""

    def __init__(self, name, element, level=1, hunger=10, happiness=5, energy=5):
        """
        Initializes an ElementalCreature.

        Args:
            name (str): The creature's name.
            element (str): The creature's elemental type (e.g., fire, water, earth).
            level (int, optional): The creature's level. Defaults to 1.
            hunger (int, optional): The creature's hunger level. Defaults to 10.
            happiness (int, optional): The creature's happiness level. Defaults to 5.
            energy (int, optional): The creature's energy level. Defaults to 5.
        """
        self.name = name
        self.element = element
        self.level = level
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.experience = 0

    def feed(self):
        """Feeds the creature, reducing hunger and increasing happiness."""
        if self.hunger > 0:
            self.hunger -= 3
            self.happiness += 2
            if self.hunger < 0:
                self.hunger = 0
            print(f"You fed {self.name}. Hunger is now {self.hunger}, happiness is now {self.happiness}.")
        else:
            print(f"{self.name} is not hungry.")

    def play(self):
        """Plays with the creature, increasing happiness and reducing energy."""
        if self.energy > 0:
            self.happiness += 3
            self.energy -= 2
            if self.happiness > 10:
                self.happiness = 10
            if self.energy < 0:
                self.energy = 0
            print(f"You played with {self.name}. Happiness is now {self.happiness}, energy is now {self.energy}.")
        else:
            print(f"{self.name} is too tired to play.")

    def rest(self):
        """Lets the creature rest, increasing energy."""
        self.energy += 3
        if self.energy > 10:
            self.energy = 10
        print(f"{self.name} rested. Energy is now {self.energy}.")

    def gain_experience(self, amount):
        """Increases the creature's experience points and levels it up if necessary."""
        self.experience += amount
        if self.experience >= self.level * 10:
            self.level_up()

    def level_up(self):
        """Levels up the creature, increasing its attributes."""
        self.level += 1
        self.hunger += 2
        self.happiness += 2
        self.energy += 2
        self.experience = 0
        print(f"{self.name} leveled up to level {self.level}!")


class Player:
    """Represents a player with a collection of elemental creatures."""

    def __init__(self, name):
        """
        Initializes a Player.

        Args:
            name (str): The player's name.
        """
        self.name = name
        self.creatures = []

    def add_creature(self, creature):
        """Adds an elemental creature to the player's collection."""
        self.creatures.append(creature)

    def display_creatures(self):
        """Displays information about all creatures in the player's collection."""
        for i, creature in enumerate(self.creatures):
            print(f"Creature {i+1}: {creature.name} (Level {creature.level} {creature.element})")
            print(f"Hunger: {creature.hunger}, Happiness: {creature.happiness}, Energy: {creature.energy}")
            print(f"Experience: {creature.experience}\n")


def main():
    player = Player("Tamagochi Master")

    while True:
        print("\n1. Create a new creature")
        print("2. Feed a creature")
        print("3. Play with a creature")
        print("4. Let a creature rest")
        print("5. Display creatures")
        print("6. Exit")

        choice = input("Choose an action: ")

        if choice == "1":
            name = input("Enter creature name: ")
            element = input("Enter creature element (fire, water, earth): ")
            creature = ElementalCreature(name, element)
            player.add_creature(creature)
            print(f"You created a new creature named {name}!")
        elif choice == "2":
            player.display_creatures()
            creature_index = int(input("Enter the number of the creature to feed: ")) - 1
            if creature_index >= 0 and creature_index < len(player.creatures):
                player.creatures[creature_index].feed()
                player.creatures[creature_index].gain_experience(5)
            else:
                print("Invalid creature choice.")
        elif choice == "3":
            player.display_creatures()
            creature_index = int(input("Enter the number of the creature to play with: ")) - 1
            if creature_index >= 0 and creature_index < len(player.creatures):
                player.creatures[creature_index].play()
                player.creatures[creature_index].gain_experience(5)
            else:
                print("Invalid creature choice.")
        elif choice == "4":
            player.display_creatures()
            creature_index = int(input("Enter the number of the creature to let rest: ")) - 1
            if creature_index >= 0 and creature_index < len(player.creatures):
                player.creatures[creature_index].rest()
            else:
                print("Invalid creature choice.")
        elif choice == "5":
            player.display_creatures()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
```
