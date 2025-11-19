"""
Generated Code Metadata:
========================
Original URL: https://register-stormwarfarecom.pages.dev
Prompt: Develop a system for generating legendary hero cards with unique abilities and attributes, inspired by Storm Warfare's 100 Legendary Heroes.
Generated: DETERMINISTIC_1d98638c49b6c06b
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json

class Hero:
    """
    A class to represent a legendary hero with unique abilities and attributes.
    """

    def __init__(self, name, strength, agility, intelligence, ability):
        """
        Initializes a new Hero instance.

        :param name: str - The name of the hero.
        :param strength: int - The strength attribute of the hero.
        :param agility: int - The agility attribute of the hero.
        :param intelligence: int - The intelligence attribute of the hero.
        :param ability: str - The unique ability of the hero.
        """
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.ability = ability

    def to_dict(self):
        """
        Converts the Hero instance to a dictionary.

        :return: dict - A dictionary representation of the hero.
        """
        return {
            "name": self.name,
            "strength": self.strength,
            "agility": self.agility,
            "intelligence": self.intelligence,
            "ability": self.ability
        }

class HeroGenerator:
    """
    A class to generate legendary heroes with random attributes and abilities.
    """

    def __init__(self):
        """
        Initializes the HeroGenerator with predefined abilities.
        """
        self.abilities = [
            "Fireball", "Ice Shield", "Lightning Strike", "Healing Wave",
            "Shadow Step", "Earthquake", "Wind Blast", "Time Warp"
        ]

    def generate_hero(self):
        """
        Generates a new hero with random attributes and a unique ability.

        :return: Hero - A newly created Hero instance.
        """
        name = self.generate_name()
        strength = random.randint(1, 100)
        agility = random.randint(1, 100)
        intelligence = random.randint(1, 100)
        ability = random.choice(self.abilities)

        return Hero(name, strength, agility, intelligence, ability)

    def generate_name(self):
        """
        Generates a random hero name.

        :return: str - A randomly generated hero name.
        """
        prefixes = ["Valiant", "Mighty", "Cunning", "Brave", "Fierce"]
        suffixes = ["Warrior", "Mage", "Rogue", "Guardian", "Berserker"]
        return f"{random.choice(prefixes)} {random.choice(suffixes)}"

def save_heroes_to_file(heroes, filename):
    """
    Saves a list of heroes to a JSON file.

    :param heroes: list - A list of Hero instances.
    :param filename: str - The name of the file to save the heroes to.
    """
    try:
        with open(filename, 'w') as file:
            json.dump([hero.to_dict() for hero in heroes], file, indent=4)
    except IOError as e:
        print(f"Error saving heroes to file: {e}")

def main():
    """
    Main function to generate and save legendary heroes.
    """
    hero_generator = HeroGenerator()
    heroes = [hero_generator.generate_hero() for _ in range(10)]  # Generate 10 heroes

    save_heroes_to_file(heroes, 'legendary_heroes.json')
    print("Legendary heroes generated and saved to 'legendary_heroes.json'.")

if __name__ == "__main__":
    main()
```
