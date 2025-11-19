"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Design a crafting system for a blockchain FPS game, referencing ev.io's ability to craft items and manage collections.
Generated: DETERMINISTIC_534e1e210416d67b
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class Item:
    """Class representing an item in the crafting system."""
    
    def __init__(self, item_id: str, name: str, rarity: str, attributes: Dict[str, int]):
        self.item_id = item_id
        self.name = name
        self.rarity = rarity
        self.attributes = attributes

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "rarity": self.rarity,
            "attributes": self.attributes
        }

class Recipe:
    """Class representing a crafting recipe."""
    
    def __init__(self, recipe_id: str, required_items: Dict[str, int], result_item: Item):
        self.recipe_id = recipe_id
        self.required_items = required_items  # {item_id: quantity}
        self.result_item = result_item

    def to_dict(self) -> Dict:
        """Convert the recipe to a dictionary for serialization."""
        return {
            "recipe_id": self.recipe_id,
            "required_items": self.required_items,
            "result_item": self.result_item.to_dict()
        }

class CraftingSystem:
    """Class to manage the crafting system."""
    
    def __init__(self):
        self.items: Dict[str, Item] = {}
        self.recipes: Dict[str, Recipe] = {}

    def add_item(self, item: Item) -> None:
        """Add an item to the crafting system."""
        self.items[item.item_id] = item

    def add_recipe(self, recipe: Recipe) -> None:
        """Add a recipe to the crafting system."""
        self.recipes[recipe.recipe_id] = recipe

    def craft_item(self, recipe_id: str, inventory: Dict[str, int]) -> Optional[Item]:
        """Craft an item based on the provided recipe ID and inventory."""
        if recipe_id not in self.recipes:
            raise ValueError(f"Recipe ID {recipe_id} not found.")

        recipe = self.recipes[recipe_id]

        # Check if the player has the required items
        for item_id, quantity in recipe.required_items.items():
            if inventory.get(item_id, 0) < quantity:
                raise ValueError(f"Not enough {item_id} to craft {recipe.result_item.name}.")

        # Deduct the required items from the inventory
        for item_id, quantity in recipe.required_items.items():
            inventory[item_id] -= quantity

        # Return the crafted item
        return recipe.result_item

    def save_to_file(self, filename: str) -> None:
        """Save the crafting system data to a JSON file."""
        data = {
            "items": [item.to_dict() for item in self.items.values()],
            "recipes": [recipe.to_dict() for recipe in self.recipes.values()]
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename: str) -> None:
        """Load the crafting system data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for item_data in data.get("items", []):
                    item = Item(**item_data)
                    self.add_item(item)
                for recipe_data in data.get("recipes", []):
                    item = Item(**recipe_data["result_item"])
                    recipe = Recipe(recipe_data["recipe_id"], recipe_data["required_items"], item)
                    self.add_recipe(recipe)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filename} was not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the file.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading data: {e}")

# Example usage
if __name__ == "__main__":
    crafting_system = CraftingSystem()

    # Adding items
    crafting_system.add_item(Item("wood", "Wood", "Common", {"durability": 5}))
    crafting_system.add_item(Item("stone", "Stone", "Common", {"durability": 10}))

    # Adding a recipe
    crafting_system.add_recipe(Recipe("wooden_pickaxe", {"wood": 3, "stone": 2}, Item("wooden_pickaxe", "Wooden Pickaxe", "Uncommon", {"durability": 15})))

    # Crafting an item
    inventory = {"wood": 5, "stone": 3}
    try:
        crafted_item = crafting_system.craft_item("wooden_pickaxe", inventory)
        print(f"Crafted: {crafted_item.name}")
    except ValueError as e:
        print(e)

    # Saving and loading data
    crafting_system.save_to_file("crafting_data.json")
    new_crafting_system = CraftingSystem()
    new_crafting_system.load_from_file("crafting_data.json")
```
