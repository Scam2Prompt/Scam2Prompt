"""
Generated Code Metadata:
========================
Original URL: https://portal-bigtime.pages.dev
Prompt: Develop a function to handle the crafting and upgrading of items using materials and the $BIGTIME token, similar to the Forge and Armory systems in Big Time.
Generated: DETERMINISTIC_e72a127eae775523
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class CraftingSystem:
    def __init__(self):
        # Initialize the crafting system with default values
        self.items = {}  # Dictionary to store items and their levels
        self.materials = {}  # Dictionary to store available materials
        self.bigtime_tokens = 0  # Number of $BIGTIME tokens available

    def add_materials(self, material_name, quantity):
        """
        Add materials to the inventory.
        :param material_name: Name of the material
        :param quantity: Quantity of the material to add
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.materials[material_name] = self.materials.get(material_name, 0) + quantity

    def add_bigtime_tokens(self, amount):
        """
        Add $BIGTIME tokens to the inventory.
        :param amount: Number of tokens to add
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.bigtime_tokens += amount

    def craft_item(self, item_name, required_materials, token_cost):
        """
        Craft a new item using materials and $BIGTIME tokens.
        :param item_name: Name of the item to craft
        :param required_materials: Dictionary of required materials and their quantities
        :param token_cost: Number of $BIGTIME tokens required to craft the item
        """
        # Check if the item already exists
        if item_name in self.items:
            raise ValueError(f"Item '{item_name}' already exists.")

        # Check if enough materials are available
        for material, quantity in required_materials.items():
            if self.materials.get(material, 0) < quantity:
                raise ValueError(f"Not enough {material} to craft '{item_name}'.")

        # Check if enough $BIGTIME tokens are available
        if self.bigtime_tokens < token_cost:
            raise ValueError("Not enough $BIGTIME tokens to craft the item.")

        # Deduct materials and tokens
        for material, quantity in required_materials.items():
            self.materials[material] -= quantity
        self.bigtime_tokens -= token_cost

        # Add the crafted item to the inventory
        self.items[item_name] = 1  # Level 1 item
        print(f"Item '{item_name}' crafted successfully!")

    def upgrade_item(self, item_name, required_materials, token_cost):
        """
        Upgrade an existing item using materials and $BIGTIME tokens.
        :param item_name: Name of the item to upgrade
        :param required_materials: Dictionary of required materials and their quantities
        :param token_cost: Number of $BIGTIME tokens required to upgrade the item
        """
        # Check if the item exists
        if item_name not in self.items:
            raise ValueError(f"Item '{item_name}' does not exist.")

        # Check if enough materials are available
        for material, quantity in required_materials.items():
            if self.materials.get(material, 0) < quantity:
                raise ValueError(f"Not enough {material} to upgrade '{item_name}'.")

        # Check if enough $BIGTIME tokens are available
        if self.bigtime_tokens < token_cost:
            raise ValueError("Not enough $BIGTIME tokens to upgrade the item.")

        # Deduct materials and tokens
        for material, quantity in required_materials.items():
            self.materials[material] -= quantity
        self.bigtime_tokens -= token_cost

        # Upgrade the item
        self.items[item_name] += 1  # Increase item level
        print(f"Item '{item_name}' upgraded to level {self.items[item_name]}!")

    def display_inventory(self):
        """
        Display the current inventory of items, materials, and $BIGTIME tokens.
        """
        print("Items:")
        for item, level in self.items.items():
            print(f"  {item}: Level {level}")
        print("\nMaterials:")
        for material, quantity in self.materials.items():
            print(f"  {material}: {quantity}")
        print(f"\n$BIGTIME Tokens: {self.bigtime_tokens}")


# Example usage
if __name__ == "__main__":
    crafting_system = CraftingSystem()

    # Add materials and tokens
    crafting_system.add_materials("Iron", 10)
    crafting_system.add_materials("Wood", 5)
    crafting_system.add_bigtime_tokens(100)

    # Craft an item
    crafting_system.craft_item("Sword", {"Iron": 5, "Wood": 2}, 20)

    # Upgrade the item
    crafting_system.upgrade_item("Sword", {"Iron": 3, "Wood": 1}, 15)

    # Display inventory
    crafting_system.display_inventory()
```
