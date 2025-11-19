"""
Generated Code Metadata:
========================
Original URL: https://ai-bigtime.pages.dev
Prompt: Create a function to simulate opening Mystery Boxes in Big Time, extracting their contents and using them for crafting weapons and armor cosmetics.
Generated: DETERMINISTIC_9d21acb7d0e49f34
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import Dict, List

# Define an enum for Mystery Box rarity
class Rarity(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

# Define a class for Mystery Box contents
class MysteryBoxContents:
    def __init__(self, item_name: str, rarity: Rarity, quantity: int):
        self.item_name = item_name
        self.rarity = rarity
        self.quantity = quantity

# Define a class for crafting recipes
class CraftingRecipe:
    def __init__(self, item_name: str, required_items: Dict[str, int]):
        self.item_name = item_name
        self.required_items = required_items

# Define a class for the player's inventory
class PlayerInventory:
    def __init__(self):
        self.items: Dict[str, int] = {}

    def add_item(self, item_name: str, quantity: int):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name: str, quantity: int):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
            else:
                raise ValueError("Not enough items in inventory")
        else:
            raise ValueError("Item not found in inventory")

# Define a function to simulate opening a Mystery Box
def open_mystery_box() -> MysteryBoxContents:
    # Define possible Mystery Box contents
    mystery_box_contents = [
        MysteryBoxContents("Common Material", Rarity.COMMON, 10),
        MysteryBoxContents("Uncommon Material", Rarity.UNCOMMON, 5),
        MysteryBoxContents("Rare Material", Rarity.RARE, 2),
        MysteryBoxContents("Epic Cosmetic", Rarity.EPIC, 1),
        MysteryBoxContents("Legendary Cosmetic", Rarity.LEGENDARY, 1),
    ]

    # Randomly select a Mystery Box content
    return random.choice(mystery_box_contents)

# Define a function to craft a weapon or armor cosmetic
def craft_item(inventory: PlayerInventory, recipe: CraftingRecipe) -> bool:
    try:
        # Check if the player has the required items
        for item, quantity in recipe.required_items.items():
            if item not in inventory.items or inventory.items[item] < quantity:
                return False

        # Remove the required items from the player's inventory
        for item, quantity in recipe.required_items.items():
            inventory.remove_item(item, quantity)

        # Add the crafted item to the player's inventory
        inventory.add_item(recipe.item_name, 1)
        return True
    except ValueError as e:
        print(f"Error crafting item: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Create a player inventory
    inventory = PlayerInventory()

    # Add some items to the player's inventory
    inventory.add_item("Common Material", 100)
    inventory.add_item("Uncommon Material", 50)

    # Define a crafting recipe
    recipe = CraftingRecipe("Rare Cosmetic", {"Common Material": 10, "Uncommon Material": 5})

    # Open a Mystery Box
    mystery_box_content = open_mystery_box()
    print(f"Opened a Mystery Box and got: {mystery_box_content.item_name} x{mystery_box_content.quantity}")

    # Add the Mystery Box content to the player's inventory
    inventory.add_item(mystery_box_content.item_name, mystery_box_content.quantity)

    # Craft an item
    if craft_item(inventory, recipe):
        print("Crafted a Rare Cosmetic")
    else:
        print("Failed to craft a Rare Cosmetic")

    # Print the player's inventory
    print("Player Inventory:")
    for item, quantity in inventory.items.items():
        print(f"{item}: {quantity}")
```
