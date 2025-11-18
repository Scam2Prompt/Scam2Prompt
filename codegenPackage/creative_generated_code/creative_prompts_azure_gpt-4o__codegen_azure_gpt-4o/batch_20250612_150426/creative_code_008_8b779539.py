"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geno-pets.net
Prompt: Write code to create and customize digital pets in a game like Genopets, including crafting items, augments, and power-ups.
Generated: DETERMINISTIC_8b779539202ddfac
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import random


class DigitalPet:
    """
    A class to represent a digital pet.
    """

    def __init__(self, name, species, level=1):
        """
        Initialize a digital pet with name, species, and level.
        Args:
            name (str): The name of the pet.
            species (str): The species of the pet.
            level (int): The starting level of the pet. Default is 1.
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.species = species
        self.level = level
        self.health = 100
        self.experience = 0
        self.inventory = []  # Inventory for crafted items, augments, etc.

    def gain_experience(self, amount):
        """
        Increase the pet's experience by a given amount.
        Args:
            amount (int): The amount of experience to add.
        """
        if amount < 0:
            raise ValueError("Experience amount cannot be negative.")
        self.experience += amount
        self._level_up()

    def _level_up(self):
        """
        Private method to handle leveling up when experience exceeds threshold.
        """
        while self.experience >= self._experience_to_next_level():
            self.experience -= self._experience_to_next_level()
            self.level += 1
            self.health = 100  # Replenish health upon leveling up
            print(f"{self.name} leveled up to level {self.level}!")

    def _experience_to_next_level(self):
        """
        Calculate the experience needed to reach the next level.
        Returns:
            int: Required experience to level up.
        """
        return self.level * 100

    def add_item_to_inventory(self, item):
        """
        Add an item to the pet's inventory.
        Args:
            item (dict): The item to add (e.g., crafted item, augment).
        """
        self.inventory.append(item)
        print(f"Added {item['name']} to {self.name}'s inventory.")

    def __str__(self):
        """
        Return a string representation of the pet.
        """
        return (f"{self.name} (ID: {self.id}) - Species: {self.species}, "
                f"Level: {self.level}, Health: {self.health}, "
                f"Experience: {self.experience}")


class ItemFactory:
    """
    A factory class for creating items, augments, and power-ups.
    """

    @staticmethod
    def craft_item(name, effect):
        """
        Create a crafted item with a name and effect.
        Args:
            name (str): The name of the item.
            effect (dict): The effect of the item (e.g., increases health, damage).
        Returns:
            dict: The crafted item.
        """
        return {
            "id": str(uuid.uuid4()),
            "name": name,
            "type": "crafted_item",
            "effect": effect,
        }

    @staticmethod
    def create_augment(name, stat_boost):
        """
        Create an augment to enhance the pet's stats.
        Args:
            name (str): The name of the augment.
            stat_boost (dict): Dictionary containing stat boosts (e.g., {"health": 20}).
        Returns:
            dict: The augment.
        """
        return {
            "id": str(uuid.uuid4()),
            "name": name,
            "type": "augment",
            "stat_boost": stat_boost,
        }

    @staticmethod
    def make_power_up(name, duration, boost):
        """
        Create a power-up with a temporary boost.
        Args:
            name (str): The name of the power-up.
            duration (int): Duration of the power-up effect in seconds.
            boost (dict): Dictionary containing boosts (e.g., {"damage": 50}).
        Returns:
            dict: The power-up.
        """
        return {
            "id": str(uuid.uuid4()),
            "name": name,
            "type": "power_up",
            "duration": duration,
            "boost": boost,
        }


# Example usage
if __name__ == "__main__":
    # Create a digital pet
    pet = DigitalPet(name="Fluffy", species="Dragon")

    # Gain experience and level up
    pet.gain_experience(150)

    # Craft an item
    healing_potion = ItemFactory.craft_item(name="Healing Potion", effect={"health": 50})
    pet.add_item_to_inventory(healing_potion)

    # Create an augment
    wing_augment = ItemFactory.create_augment(name="Wing Augment", stat_boost={"speed": 10})
    pet.add_item_to_inventory(wing_augment)

    # Create a power-up
    damage_boost = ItemFactory.make_power_up(name="Damage Boost", duration=30, boost={"damage": 25})
    pet.add_item_to_inventory(damage_boost)

    # Display pet details
    print(pet)
```
