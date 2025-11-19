"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kurorobeastxyz.pages.dev
Prompt: Generate a code snippet for a tamagochi-style game that allows players to care for and level up their elemental creatures, similar to the Kuroro Ranch game.
Generated: DETERMINISTIC_32f8df7a09286a67
Batch ID: 20250612_163934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random


class ElementalCreature:
    """
    A class representing an elemental creature for a tamagochi-style game.
    """

    def __init__(self, name, element):
        """
        Initialize the elemental creature with basic attributes.
        :param name: Name of the creature.
        :param element: Element type of the creature (e.g., Fire, Water, Earth).
        """
        self.name = name
        self.element = element
        self.level = 1
        self.health = 100
        self.hunger = 0
        self.happiness = 100
        self.experience = 0

    def feed(self):
        """
        Feed the creature to reduce hunger and increase happiness.
        """
        if self.hunger > 0:
            self.hunger -= 10
            self.happiness += 5
            print(f"You fed {self.name}. Hunger: {self.hunger}, Happiness: {self.happiness}.")
        else:
            print(f"{self.name} is not hungry!")

    def play(self):
        """
        Play with the creature to increase happiness and experience points.
        """
        if self.happiness < 100:
            self.happiness += 10
            self.experience += 5
            print(f"You played with {self.name}. Happiness: {self.happiness}, Experience: {self.experience}.")
        else:
            print(f"{self.name} is already very happy!")

    def level_up(self):
        """
        Level up the creature if enough experience points are gained.
        """
        if self.experience >= 50:
            self.level += 1
            self.experience = 0
            print(f"Congratulations! {self.name} leveled up to Level {self.level}.")
        else:
            print(f"{self.name} needs more experience to level up!")

    def rest(self):
        """
        Rest the creature to restore health.
        """
        self.health = min(100, self.health + 20)  # Ensure health does not exceed 100
        print(f"{self.name} rested and has {self.health} health now.")

    def status(self):
        """
        Display the current status of the creature.
        """
        print(f"--- {self.name}'s Status ---")
        print(f"Element: {self.element}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Experience: {self.experience}")
        print("-------------------------")


def main():
    """
    Main function to interact with the tamagochi-style game.
    """
    print("Welcome to the Elemental Creature Game!")
    name = input("Enter your creature's name: ").strip()
    element = input("Choose an element (Fire, Water, Earth): ").strip().capitalize()

    if element not in ["Fire", "Water", "Earth"]:
        print("Invalid element selection. Defaulting to 'Earth'.")
        element = "Earth"

    creature = ElementalCreature(name, element)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Rest")
        print("4. Check Status")
        print("5. Level Up")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): ").strip())
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            creature.feed()
        elif choice == 2:
            creature.play()
        elif choice == 3:
            creature.rest()
        elif choice == 4:
            creature.status()
        elif choice == 5:
            creature.level_up()
        elif choice == 6:
            print("Goodbye! Thanks for playing!")
            break
        else:
            print("Invalid choice! Please select between 1 and 6.")

        # Simulate hunger increase over time
        creature.hunger = min(100, creature.hunger + random.randint(1, 5))
        creature.health = max(0, creature.health - random.randint(1, 3))

        if creature.health <= 0:
            print(f"Oh no! {creature.name} has fainted due to low health. Game over!")
            break


if __name__ == "__main__":
    main()
```
