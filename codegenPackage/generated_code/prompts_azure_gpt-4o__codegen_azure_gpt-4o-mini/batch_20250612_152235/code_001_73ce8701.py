"""
Generated Code Metadata:
========================
Original URL: https://portal-bigtime.pages.dev
Prompt: Generate code to simulate the crafting process for weapons and armor cosmetics in Big Time, incorporating the use of $BIGTIME Token and materials as outlined in the Time Warden and Armory sections.
Generated: DETERMINISTIC_73ce870140762e62
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CraftingError(Exception):
    """Custom exception for crafting errors."""
    pass

class Item:
    """Class representing a craftable item."""
    
    def __init__(self, name, materials_required, cost_in_tokens):
        self.name = name
        self.materials_required = materials_required
        self.cost_in_tokens = cost_in_tokens

class Player:
    """Class representing a player in the game."""
    
    def __init__(self, name, bigtime_tokens, materials):
        self.name = name
        self.bigtime_tokens = bigtime_tokens
        self.materials = materials

    def can_craft(self, item):
        """Check if the player has enough tokens and materials to craft the item."""
        for material, quantity in item.materials_required.items():
            if self.materials.get(material, 0) < quantity:
                return False
        return self.bigtime_tokens >= item.cost_in_tokens

    def craft_item(self, item):
        """Craft an item if the player has enough resources."""
        if not self.can_craft(item):
            raise CraftingError(f"{self.name} does not have enough resources to craft {item.name}.")

        # Deduct materials and tokens
        for material, quantity in item.materials_required.items():
            self.materials[material] -= quantity
        self.bigtime_tokens -= item.cost_in_tokens

        return f"{self.name} successfully crafted {item.name}!"

# Example materials and items
materials_available = {
    'Iron Ore': 10,
    'Leather': 5,
    'Wood': 8
}

# Define craftable items
sword = Item(name="Iron Sword", materials_required={'Iron Ore': 5, 'Wood': 2}, cost_in_tokens=10)
armor = Item(name="Leather Armor", materials_required={'Leather': 3, 'Iron Ore': 2}, cost_in_tokens=15)

# Create a player
player = Player(name="Hero", bigtime_tokens=20, materials=materials_available)

# Crafting process
try:
    print(player.craft_item(sword))  # Attempt to craft an Iron Sword
    print(player.craft_item(armor))   # Attempt to craft Leather Armor
except CraftingError as e:
    print(e)

# Output remaining resources
print(f"Remaining Tokens: {player.bigtime_tokens}")
print(f"Remaining Materials: {player.materials}")
```
