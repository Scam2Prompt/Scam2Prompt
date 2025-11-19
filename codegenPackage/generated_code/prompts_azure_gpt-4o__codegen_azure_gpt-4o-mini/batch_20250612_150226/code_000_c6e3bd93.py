"""
Generated Code Metadata:
========================
Original URL: https://bigtime-codes.pages.dev
Prompt: Write a Python script to simulate crafting weapons and armor cosmetics in "Big Time" using $BIGTIME tokens and other materials, referencing the Forge and Armory systems described on the website.
Generated: DETERMINISTIC_c6e3bd93f0360d30
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple

class CraftingError(Exception):
    """Custom exception for crafting errors."""
    pass

class Item:
    """Class representing an item that can be crafted."""
    
    def __init__(self, name: str, cost: int, materials: Dict[str, int]):
        self.name = name
        self.cost = cost  # Cost in $BIGTIME tokens
        self.materials = materials  # Required materials for crafting

class Player:
    """Class representing a player in the game."""
    
    def __init__(self, name: str, bigtime_tokens: int, inventory: Dict[str, int]):
        self.name = name
        self.bigtime_tokens = bigtime_tokens
        self.inventory = inventory  # Inventory of materials

    def can_craft(self, item: Item) -> bool:
        """Check if the player can craft the given item."""
        if self.bigtime_tokens < item.cost:
            return False
        for material, quantity in item.materials.items():
            if self.inventory.get(material, 0) < quantity:
                return False
        return True

    def craft(self, item: Item) -> None:
        """Craft the item if possible, deducting costs and materials."""
        if not self.can_craft(item):
            raise CraftingError(f"Cannot craft {item.name}: insufficient resources.")
        
        # Deduct $BIGTIME tokens
        self.bigtime_tokens -= item.cost
        
        # Deduct materials
        for material, quantity in item.materials.items():
            self.inventory[material] -= quantity
        
        print(f"{self.name} crafted {item.name}!")

class CraftingSystem:
    """Class to manage the crafting process."""
    
    def __init__(self):
        self.items: List[Item] = []
    
    def add_item(self, item: Item) -> None:
        """Add a new item to the crafting system."""
        self.items.append(item)

    def craft_item(self, player: Player, item_name: str) -> None:
        """Craft an item by its name."""
        item = next((item for item in self.items if item.name == item_name), None)
        if item is None:
            raise CraftingError(f"Item {item_name} not found in crafting system.")
        
        player.craft(item)

def main():
    # Initialize crafting system
    crafting_system = CraftingSystem()
    
    # Define some items that can be crafted
    crafting_system.add_item(Item("Sword of Valor", 100, {"Iron": 5, "Wood": 2}))
    crafting_system.add_item(Item("Shield of Courage", 150, {"Iron": 8, "Wood": 3}))
    
    # Create a player with some initial resources
    player = Player("Hero", 200, {"Iron": 10, "Wood": 5})
    
    # Attempt to craft items
    try:
        crafting_system.craft_item(player, "Sword of Valor")
        crafting_system.craft_item(player, "Shield of Courage")
    except CraftingError as e:
        print(e)

if __name__ == "__main__":
    main()
```
