"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtimecodes.pages.dev
Prompt: Generate code to simulate crafting weapons and armor cosmetics in Big Time using $BIGTIME tokens and materials, including functionality for upgrading items through the Forge and Armory.
Generated: DETERMINISTIC_73b665545a32727c
Batch ID: 20250612_150316
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
    Class representing an item that can be crafted, upgraded, or equipped.
    Attributes:
        name (str): The name of the item.
        level (int): The current level of the item.
        cosmetic (bool): Flag indicating if the item is a cosmetic.
    """

    def __init__(self, name: str, level: int = 1, cosmetic: bool = False):
        self.name = name
        self.level = level
        self.cosmetic = cosmetic

    def upgrade(self):
        """Upgrade the item to the next level."""
        if self.level < 10:  # Assuming max level is 10
            self.level += 1
        else:
            raise ValueError("Item is already at maximum level.")

    def __str__(self):
        return f"{'Cosmetic ' if self.cosmetic else ''}Item: {self.name}, Level: {self.level}"


class CraftingSystem:
    """
    Class responsible for crafting weapons and armor cosmetics.
    Attributes:
        materials (dict): Available materials for crafting.
        bigtime_tokens (int): Available $BIGTIME tokens.
    """

    def __init__(self, materials: dict, bigtime_tokens: int):
        self.materials = materials
        self.bigtime_tokens = bigtime_tokens

    def craft_item(self, item_name: str, cost: int, required_materials: dict) -> Item:
        """
        Craft a new item if sufficient resources are available.

        Args:
            item_name (str): The name of the item to craft.
            cost (int): The cost in $BIGTIME tokens.
            required_materials (dict): Materials required for crafting.

        Returns:
            Item: The crafted item.

        Raises:
            ValueError: If insufficient resources are available.
        """
        # Check if enough $BIGTIME tokens are available
        if self.bigtime_tokens < cost:
            raise ValueError("Insufficient $BIGTIME tokens to craft this item.")

        # Check if all required materials are available
        for mat, qty in required_materials.items():
            if self.materials.get(mat, 0) < qty:
                raise ValueError(f"Insufficient materials: {mat}")

        # Deduct $BIGTIME tokens and materials
        self.bigtime_tokens -= cost
        for mat, qty in required_materials.items():
            self.materials[mat] -= qty

        # Create and return the crafted item
        return Item(name=item_name)

    def __str__(self):
        return f"Available $BIGTIME Tokens: {self.bigtime_tokens}, Materials: {self.materials}"


class Forge:
    """
    Class representing the Forge for upgrading weapons.
    """

    @staticmethod
    def upgrade_weapon(item: Item):
        """Upgrade the weapon item."""
        item.upgrade()


class Armory:
    """
    Class representing the Armory for upgrading armor.
    """

    @staticmethod
    def upgrade_armor(item: Item):
        """Upgrade the armor item."""
        item.upgrade()


# Example usage:
if __name__ == "__main__":
    # Initialize materials and tokens
    initial_materials = {"iron": 100, "wood": 50, "leather": 30}
    tokens = 200

    # Create crafting system
    crafting_system = CraftingSystem(initial_materials, tokens)

    try:
        # Craft a sword
        sword = crafting_system.craft_item("Sword", 50, {"iron": 10, "wood": 5})
        print(sword)

        # Upgrade the sword
        Forge.upgrade_weapon(sword)
        print(sword)

        # Create an armor
        armor = crafting_system.craft_item("Armor", 70, {"iron": 15, "leather": 10})
        print(armor)

        # Upgrade the armor
        Armory.upgrade_armor(armor)
        print(armor)

    except ValueError as e:
        print(f"Error: {e}")
```
