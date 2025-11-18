"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-ai.pages.dev
Prompt: Generate code that uses the Big Time Creator Kit to craft weapons and armor cosmetics, including functionality for upgrading items using $BIGTIME and other materials.
Generated: DETERMINISTIC_548546545ab33f31
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Item:
    """
    Base class for all items in the Big Time Creator Kit.
    Represents a generic item with a name, type, and level.
    """
    
    def __init__(self, name: str, item_type: str, level: int):
        self.name = name
        self.item_type = item_type
        self.level = level

    def upgrade(self, materials: dict):
        """
        Upgrade the item using provided materials and currency.
        :param materials: A dictionary containing required materials for the upgrade.
        :raises ValueError: If required materials are insufficient.
        """
        required_materials = {"$BIGTIME": 100, "materialA": 2, "materialB": 1}
        for mat, qty in required_materials.items():
            if materials.get(mat, 0) < qty:
                raise ValueError(f"Insufficient {mat} for upgrading {self.name}.")
        
        # Deduct the used materials
        for mat, qty in required_materials.items():
            materials[mat] -= qty
        
        self.level += 1
        print(f"{self.name} upgraded to level {self.level}!")

class Weapon(Item):
    """
    Class representing a weapon item.
    Inherits from Item and can have additional weapon-specific properties.
    """
    
    def __init__(self, name: str, damage: int, level: int):
        super().__init__(name, "Weapon", level)
        self.damage = damage

    def __str__(self):
        return f"Weapon(Name: {self.name}, Damage: {self.damage}, Level: {self.level})"

class Armor(Item):
    """
    Class representing an armor item.
    Inherits from Item and can have additional armor-specific properties.
    """
    
    def __init__(self, name: str, defense: int, level: int):
        super().__init__(name, "Armor", level)
        self.defense = defense

    def __str__(self):
        return f"Armor(Name: {self.name}, Defense: {self.defense}, Level: {self.level})"

def craft_item(item_type: str, name: str, *args) -> Item:
    """
    Crafts a new item based on the provided type.
    :param item_type: The type of item to craft (Weapon or Armor).
    :param name: The name of the item to craft.
    :param args: Additional parameters needed for crafting.
    :return: An instance of Weapon or Armor based on the type.
    :raises ValueError: If an invalid item type is provided.
    """
    if item_type.lower() == "weapon":
        damage = args[0] if args else 10  # Default damage
        return Weapon(name, damage, level=1)
    elif item_type.lower() == "armor":
        defense = args[0] if args else 10  # Default defense
        return Armor(name, defense, level=1)
    else:
        raise ValueError("Invalid item type. Must be 'Weapon' or 'Armor'.")

# Example usage
if __name__ == "__main__":
    try:
        materials = {"$BIGTIME": 200, "materialA": 5, "materialB": 3}
        
        # Crafting a weapon
        sword = craft_item("Weapon", "Excalibur", 50)
        print(sword)
        
        # Upgrading the weapon
        sword.upgrade(materials)
        print(sword)
        
        # Crafting armor
        shield = craft_item("Armor", "Aegis", 30)
        print(shield)

        # Upgrading the armor
        shield.upgrade(materials)
        print(shield)

    except ValueError as e:
        print(f"Error: {e}")
```
