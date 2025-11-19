"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Generate code to simulate crafting weapons and armor cosmetics in Big Time using $BIGTIME tokens and materials, including functionality for upgrading items through the Forge and Armory.
Generated: DETERMINISTIC_73b665545a32727c
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Item:
    """Class representing an item in the game."""
    
    def __init__(self, name, rarity, base_value):
        self.name = name
        self.rarity = rarity
        self.base_value = base_value
        self.upgrade_level = 0

    def upgrade(self):
        """Upgrade the item, increasing its value and level."""
        self.upgrade_level += 1
        self.base_value *= 1.2  # Increase value by 20% per upgrade

    def __str__(self):
        return f"{self.name} (Rarity: {self.rarity}, Value: {self.base_value:.2f}, Level: {self.upgrade_level})"


class Forge:
    """Class representing the Forge for crafting weapons."""
    
    def __init__(self):
        self.materials = {}
    
    def add_material(self, material, quantity):
        """Add materials to the Forge."""
        if material in self.materials:
            self.materials[material] += quantity
        else:
            self.materials[material] = quantity

    def craft_weapon(self, name, rarity, cost, required_materials):
        """Craft a weapon if enough materials are available."""
        if self.can_craft(required_materials):
            for material, quantity in required_materials.items():
                self.materials[material] -= quantity
            return Item(name, rarity, cost)
        else:
            raise ValueError("Not enough materials to craft the weapon.")

    def can_craft(self, required_materials):
        """Check if the required materials are available for crafting."""
        for material, quantity in required_materials.items():
            if self.materials.get(material, 0) < quantity:
                return False
        return True


class Armory:
    """Class representing the Armory for crafting armor cosmetics."""
    
    def __init__(self):
        self.materials = {}
    
    def add_material(self, material, quantity):
        """Add materials to the Armory."""
        if material in self.materials:
            self.materials[material] += quantity
        else:
            self.materials[material] = quantity

    def craft_armor(self, name, rarity, cost, required_materials):
        """Craft armor if enough materials are available."""
        if self.can_craft(required_materials):
            for material, quantity in required_materials.items():
                self.materials[material] -= quantity
            return Item(name, rarity, cost)
        else:
            raise ValueError("Not enough materials to craft the armor.")

    def can_craft(self, required_materials):
        """Check if the required materials are available for crafting."""
        for material, quantity in required_materials.items():
            if self.materials.get(material, 0) < quantity:
                return False
        return True


class Game:
    """Main class to simulate the crafting system."""
    
    def __init__(self):
        self.forge = Forge()
        self.armory = Armory()
        self.bigtime_tokens = 0

    def add_tokens(self, amount):
        """Add $BIGTIME tokens to the player's balance."""
        if amount < 0:
            raise ValueError("Cannot add negative tokens.")
        self.bigtime_tokens += amount

    def spend_tokens(self, amount):
        """Spend $BIGTIME tokens for crafting."""
        if amount > self.bigtime_tokens:
            raise ValueError("Not enough $BIGTIME tokens.")
        self.bigtime_tokens -= amount

    def upgrade_item(self, item):
        """Upgrade an item using the Forge or Armory."""
        item.upgrade()


# Example usage
if __name__ == "__main__":
    game = Game()
    
    # Add materials to the Forge and Armory
    game.forge.add_material("Iron", 10)
    game.armory.add_material("Leather", 5)

    # Add $BIGTIME tokens
    game.add_tokens(100)

    # Craft a weapon
    try:
        sword = game.forge.craft_weapon("Iron Sword", "Common", 50, {"Iron": 5})
        print(sword)
    except ValueError as e:
        print(e)

    # Craft armor
    try:
        armor = game.armory.craft_armor("Leather Armor", "Common", 30, {"Leather": 3})
        print(armor)
    except ValueError as e:
        print(e)

    # Upgrade the sword
    game.upgrade_item(sword)
    print(sword)
```
