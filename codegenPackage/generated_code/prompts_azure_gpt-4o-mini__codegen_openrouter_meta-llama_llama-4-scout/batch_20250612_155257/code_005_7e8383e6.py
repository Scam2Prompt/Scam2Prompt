"""
Generated Code Metadata:
========================
Original URL: https://ai-bigtime.pages.dev
Prompt: How can players earn bonuses while crafting items in Big Time, and what are Bonus Rolls?
Generated: DETERMINISTIC_7e8383e68ebc3b23
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class CraftingSystem:
    """
    A class representing the crafting system in Big Time.

    Attributes:
    -----------
    bonus_roll_chances : dict
        A dictionary containing the chances of getting a bonus roll for each item.
    bonus_types : list
        A list of possible bonus types.

    Methods:
    --------
    craft_item(item_name, player_skill)
        Crafts an item and determines if a bonus roll is earned.
    get_bonus_roll(item_name)
        Determines if a bonus roll is earned for the given item.
    get_bonus_type()
        Returns a random bonus type.
    """

    def __init__(self):
        # Initialize the bonus roll chances and bonus types
        self.bonus_roll_chances = {
            "common_item": 0.1,
            "uncommon_item": 0.05,
            "rare_item": 0.01
        }
        self.bonus_types = ["gold", "experience", "rare_material"]

    def craft_item(self, item_name, player_skill):
        """
        Crafts an item and determines if a bonus roll is earned.

        Args:
        -----
        item_name (str): The name of the item to craft.
        player_skill (int): The player's skill level.

        Returns:
        -------
        dict: A dictionary containing the crafted item and any earned bonus.
        """
        try:
            # Determine the item type based on the item name
            item_type = self.determine_item_type(item_name)

            # Check if a bonus roll is earned
            bonus_roll = self.get_bonus_roll(item_type)

            # Craft the item
            crafted_item = {"item_name": item_name, "item_type": item_type}

            # If a bonus roll is earned, get the bonus type
            if bonus_roll:
                bonus_type = self.get_bonus_type()
                crafted_item["bonus"] = bonus_type

            return crafted_item

        except Exception as e:
            # Handle any exceptions that occur during crafting
            print(f"An error occurred: {e}")
            return None

    def determine_item_type(self, item_name):
        """
        Determines the item type based on the item name.

        Args:
        -----
        item_name (str): The name of the item.

        Returns:
        -------
        str: The item type.
        """
        # For demonstration purposes, assume the item type is based on the item name
        if "common" in item_name:
            return "common_item"
        elif "uncommon" in item_name:
            return "uncommon_item"
        elif "rare" in item_name:
            return "rare_item"
        else:
            raise ValueError("Unknown item type")

    def get_bonus_roll(self, item_type):
        """
        Determines if a bonus roll is earned for the given item.

        Args:
        -----
        item_type (str): The type of the item.

        Returns:
        -------
        bool: True if a bonus roll is earned, False otherwise.
        """
        # Check if the item type has a bonus roll chance
        if item_type in self.bonus_roll_chances:
            # Generate a random number between 0 and 1
            roll = random.random()
            # Check if the roll is less than the bonus roll chance
            return roll < self.bonus_roll_chances[item_type]
        else:
            return False

    def get_bonus_type(self):
        """
        Returns a random bonus type.

        Returns:
        -------
        str: A random bonus type.
        """
        # Select a random bonus type from the list of bonus types
        return random.choice(self.bonus_types)


def main():
    # Create a crafting system
    crafting_system = CraftingSystem()

    # Craft an item
    item_name = "common_sword"
    player_skill = 10
    crafted_item = crafting_system.craft_item(item_name, player_skill)

    # Print the crafted item and any earned bonus
    if crafted_item:
        print(f"Crafted Item: {crafted_item['item_name']} ({crafted_item['item_type']})")
        if "bonus" in crafted_item:
            print(f"Earned Bonus: {crafted_item['bonus']}")
    else:
        print("Failed to craft item")


if __name__ == "__main__":
    main()
```
