"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Write a Python script to simulate crafting weapons and armor cosmetics in "Big Time" using $BIGTIME tokens and other materials, referencing the Forge and Armory systems described on the website.
Generated: DETERMINISTIC_c6e3bd93f0360d30
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CraftingError(Exception):
    """Custom exception for handling crafting errors."""
    pass

class Material:
    """Class representing a material required for crafting."""
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class CraftableItem:
    """Class representing an item that can be crafted."""
    def __init__(self, name, required_materials, crafting_cost):
        self.name = name
        self.required_materials = required_materials
        self.crafting_cost = crafting_cost  # in $BIGTIME tokens

class Crafter:
    """Class representing a crafter that can create items."""
    def __init__(self, tokens):
        self.tokens = tokens
        self.inventory = {}

    def check_materials(self, required_materials):
        """Check if the crafter has enough materials to craft an item."""
        for material in required_materials:
            if self.inventory.get(material.name, 0) < material.quantity:
                return False
        return True

    def craft_item(self, item):
        """Craft an item if materials and tokens are sufficient."""
        if self.tokens < item.crafting_cost:
            raise CraftingError(f"Insufficient $BIGTIME tokens. Required: {item.crafting_cost}, Available: {self.tokens}")

        if not self.check_materials(item.required_materials):
            raise CraftingError("Insufficient materials to craft the item.")
        
        # Deduct the crafting cost
        self.tokens -= item.crafting_cost

        # Deduct the required materials from inventory
        for material in item.required_materials:
            self.inventory[material.name] -= material.quantity

        print(f"{item.name} crafted successfully!")
        return item.name

    def add_material(self, material):
        """Add materials to the crafter's inventory."""
        if material.name in self.inventory:
            self.inventory[material.name] += material.quantity
        else:
            self.inventory[material.name] = material.quantity

def main():
    # Example materials
    gold = Material("Gold", 5)
    silver = Material("Silver", 3)
    iron = Material("Iron", 10)

    # Example craftable item
    sword = CraftableItem("Sword", [gold, silver], 2)

    # Initialize crafter with some tokens and materials
    crafter = Crafter(tokens=10)
    crafter.add_material(gold)
    crafter.add_material(silver)
    crafter.add_material(iron)

    # Attempt to craft the item
    try:
        crafted_item = crafter.craft_item(sword)
        print(f"Crafted: {crafted_item}")
    except CraftingError as e:
        print(f"Crafting failed: {e}")

if __name__ == "__main__":
    main()
```
