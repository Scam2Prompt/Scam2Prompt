"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-bigtime.pages.dev
Prompt: Develop a function to handle the crafting and upgrading of items using materials and the $BIGTIME token, similar to the Forge and Armory systems in Big Time.
Generated: DETERMINISTIC_e72a127eae775523
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CraftingSystem:
    def __init__(self):
        """
        Initialize the crafting system with default item levels and material requirements.
        """
        self.items = {}  # Holds items and their levels
        self.materials = {}  # Holds available materials with quantities
        self.bigtime_tokens = 0  # Number of $BIGTIME tokens available

    def add_item(self, item_name):
        """
        Add a new item to the system with a default level of 1.
        
        :param item_name: Name of the item to add
        """
        if item_name in self.items:
            raise ValueError("Item already exists in inventory.")
        self.items[item_name] = 1

    def add_material(self, material_name, quantity):
        """
        Add or update a material and its quantity.
        
        :param material_name: Name of the material
        :param quantity: Quantity of the material to add (must be positive)
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.materials[material_name] = self.materials.get(material_name, 0) + quantity

    def add_bigtime_tokens(self, amount):
        """
        Add $BIGTIME tokens to the system.
        
        :param amount: Amount of tokens to add (must be positive)
        """
        if amount <= 0:
            raise ValueError("Amount of tokens must be greater than zero.")
        self.bigtime_tokens += amount

    def craft_item(self, item_name, material_requirements, token_cost):
        """
        Craft a new item using materials and $BIGTIME tokens.
        
        :param item_name: Name of the item to craft
        :param material_requirements: Dictionary of required materials and their quantities
        :param token_cost: Cost in $BIGTIME tokens to craft the item
        """
        if item_name in self.items:
            raise ValueError("Item is already crafted.")

        # Check material availability
        for material, qty in material_requirements.items():
            if self.materials.get(material, 0) < qty:
                raise ValueError(f"Insufficient quantity of material: {material}")

        # Check token availability
        if self.bigtime_tokens < token_cost:
            raise ValueError("Insufficient $BIGTIME tokens.")

        # Deduct materials and tokens
        for material, qty in material_requirements.items():
            self.materials[material] -= qty
        self.bigtime_tokens -= token_cost

        # Craft the item
        self.items[item_name] = 1  # Default level is 1
        print(f"Item '{item_name}' crafted successfully!")

    def upgrade_item(self, item_name, material_requirements, token_cost):
        """
        Upgrade an existing item using materials and $BIGTIME tokens.
        
        :param item_name: Name of the item to upgrade
        :param material_requirements: Dictionary of required materials and their quantities
        :param token_cost: Cost in $BIGTIME tokens to upgrade the item
        """
        if item_name not in self.items:
            raise ValueError("Item not found in inventory.")

        # Check material availability
        for material, qty in material_requirements.items():
            if self.materials.get(material, 0) < qty:
                raise ValueError(f"Insufficient quantity of material: {material}")

        # Check token availability
        if self.bigtime_tokens < token_cost:
            raise ValueError("Insufficient $BIGTIME tokens.")

        # Deduct materials and tokens
        for material, qty in material_requirements.items():
            self.materials[material] -= qty
        self.bigtime_tokens -= token_cost

        # Upgrade the item
        self.items[item_name] += 1
        print(f"Item '{item_name}' upgraded successfully! New level: {self.items[item_name]}")

    def display_status(self):
        """
        Display the current status of items, materials, and $BIGTIME tokens.
        """
        print("=== Inventory Status ===")
        print("Items:")
        for item, level in self.items.items():
            print(f"  {item}: Level {level}")
        print("Materials:")
        for material, qty in self.materials.items():
            print(f"  {material}: Quantity {qty}")
        print(f"$BIGTIME Tokens: {self.bigtime_tokens}")
        print("========================")


# Example usage
if __name__ == "__main__":
    # Initialize the crafting system
    crafting = CraftingSystem()

    # Add materials and tokens
    crafting.add_material("Iron", 50)
    crafting.add_material("Wood", 30)
    crafting.add_bigtime_tokens(100)

    # Craft an item
    crafting.craft_item("Sword", {"Iron": 10, "Wood": 5}, token_cost=20)

    # Upgrade the item
    crafting.upgrade_item("Sword", {"Iron": 15, "Wood": 10}, token_cost=30)

    # Display current status
    crafting.display_status()
```
