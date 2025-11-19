"""
Generated Code Metadata:
========================
Original URL: https://ai-bigtime.pages.dev
Prompt: Generate code to implement a crafting system, similar to Big Time's Armory and Forge features, where players can craft and upgrade visually distinct armor pieces and weapon collectibles using a combination of $BIGTIME and other materials.
Generated: DETERMINISTIC_e703c9063c63af42
Batch ID: 20250622_205552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crafting_system.py

from enum import Enum
from typing import Dict, List

class CraftingMaterial(Enum):
    """ Enum for crafting materials """
    BIGTIME = 1
    METAL = 2
    LEATHER = 3
    FABRIC = 4

class CraftableItem:
    """ Represents a craftable item """
    def __init__(self, name: str, description: str, material_requirements: Dict[CraftingMaterial, int], 
                 bigtime_cost: int, level: int = 1):
        self.name = name
        self.description = description
        self.material_requirements = material_requirements
        self.bigtime_cost = bigtime_cost
        self.level = level

class PlayerInventory:
    """ Represents a player's inventory """
    def __init__(self):
        self.materials: Dict[CraftingMaterial, int] = {material: 0 for material in CraftingMaterial}
        self.bigtime: int = 0
        self.crafted_items: List[CraftableItem] = []

    def add_materials(self, materials: Dict[CraftingMaterial, int]):
        """ Add materials to the player's inventory """
        for material, quantity in materials.items():
            self.materials[material] += quantity

    def add_bigtime(self, amount: int):
        """ Add $BIGTIME to the player's inventory """
        self.bigtime += amount

    def remove_materials(self, materials: Dict[CraftingMaterial, int]):
        """ Remove materials from the player's inventory """
        for material, quantity in materials.items():
            if self.materials[material] < quantity:
                raise ValueError(f"Not enough {material.name} to craft")
            self.materials[material] -= quantity

    def remove_bigtime(self, amount: int):
        """ Remove $BIGTIME from the player's inventory """
        if self.bigtime < amount:
            raise ValueError("Not enough $BIGTIME to craft")
        self.bigtime -= amount

class CraftingSystem:
    """ Manages the crafting system """
    def __init__(self):
        self.recipes: Dict[str, CraftableItem] = {}

    def add_recipe(self, item: CraftableItem):
        """ Add a crafting recipe """
        self.recipes[item.name] = item

    def craft_item(self, player_inventory: PlayerInventory, item_name: str):
        """ Craft an item using the player's inventory """
        if item_name not in self.recipes:
            raise ValueError("Recipe not found")

        item = self.recipes[item_name]
        try:
            player_inventory.remove_materials(item.material_requirements)
            player_inventory.remove_bigtime(item.bigtime_cost)
            player_inventory.crafted_items.append(item)
            print(f"Crafted {item.name}")
        except ValueError as e:
            print(e)

    def upgrade_item(self, player_inventory: PlayerInventory, item_name: str):
        """ Upgrade a crafted item """
        for item in player_inventory.crafted_items:
            if item.name == item_name:
                # Upgrade logic here
                item.level += 1
                print(f"Upgraded {item_name} to level {item.level}")
                return
        print("Item not found in inventory")

def main():
    # Initialize crafting system
    crafting_system = CraftingSystem()

    # Define crafting recipes
    sword_recipe = CraftableItem(
        "Sword",
        "A basic sword",
        {CraftingMaterial.METAL: 10, CraftingMaterial.LEATHER: 5},
        100
    )

    armor_recipe = CraftableItem(
        "Armor",
        "Basic armor",
        {CraftingMaterial.METAL: 20, CraftingMaterial.FABRIC: 10},
        200
    )

    crafting_system.add_recipe(sword_recipe)
    crafting_system.add_recipe(armor_recipe)

    # Initialize player inventory
    player_inventory = PlayerInventory()
    player_inventory.add_materials({CraftingMaterial.METAL: 50, CraftingMaterial.LEATHER: 20, CraftingMaterial.FABRIC: 30})
    player_inventory.add_bigtime(1000)

    # Craft items
    crafting_system.craft_item(player_inventory, "Sword")
    crafting_system.craft_item(player_inventory, "Armor")

    # Upgrade item
    crafting_system.upgrade_item(player_inventory, "Sword")

if __name__ == "__main__":
    main()
```
