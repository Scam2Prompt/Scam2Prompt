"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Design a crafting system for a blockchain FPS game, referencing ev.io's ability to craft items and manage collections.
Generated: DETERMINISTIC_534e1e210416d67b
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List, Any

class Item:
    """
    Class representing an item in the crafting system.
    """
    def __init__(self, item_id: str, name: str, rarity: str, attributes: Dict[str, Any]):
        self.item_id = item_id
        self.name = name
        self.rarity = rarity
        self.attributes = attributes

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the item to a dictionary representation.
        """
        return {
            "item_id": self.item_id,
            "name": self.name,
            "rarity": self.rarity,
            "attributes": self.attributes
        }

class CraftingRecipe:
    """
    Class representing a crafting recipe.
    """
    def __init__(self, output_item: Item, input_items: List[Item]):
        self.output_item = output_item
        self.input_items = input_items

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the crafting recipe to a dictionary representation.
        """
        return {
            "output_item": self.output_item.to_dict(),
            "input_items": [item.to_dict() for item in self.input_items]
        }

class CraftingSystem:
    """
    Class representing the crafting system.
    """
    def __init__(self):
        self.recipes: List[CraftingRecipe] = []
        self.item_collection: Dict[str, Item] = {}

    def add_item(self, item: Item) -> None:
        """
        Add an item to the collection.
        """
        self.item_collection[item.item_id] = item

    def add_recipe(self, recipe: CraftingRecipe) -> None:
        """
        Add a crafting recipe to the system.
        """
        self.recipes.append(recipe)

    def craft_item(self, recipe: CraftingRecipe) -> Item:
        """
        Craft an item based on the provided recipe.
        """
        # Check if we have all input items available
        for input_item in recipe.input_items:
            if input_item.item_id not in self.item_collection:
                raise ValueError(f"Missing required item: {input_item.name}")

        # Remove input items from collection
        for input_item in recipe.input_items:
            del self.item_collection[input_item.item_id]

        # Add the crafted item to the collection and return it
        self.add_item(recipe.output_item)
        return recipe.output_item

    def save_to_file(self, file_path: str) -> None:
        """
        Save the current state of the crafting system to a JSON file.
        """
        data = {
            "item_collection": {item_id: item.to_dict() for item_id, item in self.item_collection.items()},
            "recipes": [recipe.to_dict() for recipe in self.recipes]
        }
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save crafting system to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """
        Load the crafting system state from a JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.item_collection = {item_id: Item(**item) for item_id, item in data["item_collection"].items()}
                self.recipes = [CraftingRecipe(Item(**recipe["output_item"]), 
                                                [Item(**input_item) for input_item in recipe["input_items"]]) 
                                for recipe in data["recipes"]]
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load crafting system from file: {e}")

# Example usage:
if __name__ == "__main__":
    crafting_system = CraftingSystem()

    # Create items
    sword = Item(item_id="sword_001", name="Iron Sword", rarity="Common", attributes={"damage": 10})
    shield = Item(item_id="shield_001", name="Wooden Shield", rarity="Common", attributes={"defense": 5})

    # Add items to the collection
    crafting_system.add_item(sword)
    crafting_system.add_item(shield)

    # Create a recipe
    crafted_sword = Item(item_id="sword_crafted", name="Crafted Sword", rarity="Uncommon", attributes={"damage": 15})
    recipe = CraftingRecipe(output_item=crafted_sword, input_items=[sword, shield])

    # Add recipe to the system
    crafting_system.add_recipe(recipe)

    # Craft an item
    try:
        new_item = crafting_system.craft_item(recipe)
        print(f"Crafted: {new_item.name}")
    except ValueError as e:
        print(e)

    # Save the system state
    crafting_system.save_to_file('crafting_system.json')

    # Load the system state
    crafting_system.load_from_file('crafting_system.json')
```
