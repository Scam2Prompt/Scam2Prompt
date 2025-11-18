"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtimecodes.pages.dev
Prompt: Develop a program to manage and visualize the crafting economy in Big Time, including tracking $BIGTIME token usage, materials, and item upgrades.
Generated: DETERMINISTIC_de4aafc41e04cff1
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import matplotlib.pyplot as plt
from typing import Dict, List

class CraftingEconomy:
    """
    A class to manage and visualize the crafting economy in Big Time.
    Tracks $BIGTIME token usage, materials, and item upgrades.
    """

    def __init__(self):
        # Initialize data structures for tracking
        self.token_balance = 0.0  # Total $BIGTIME tokens owned
        self.materials = {}  # Materials with their quantities
        self.item_upgrades = {}  # Items with their upgrade levels

    def add_tokens(self, amount: float):
        """Add $BIGTIME tokens to the balance."""
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        self.token_balance += amount

    def spend_tokens(self, amount: float):
        """Spend $BIGTIME tokens from the balance."""
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if amount > self.token_balance:
            raise ValueError("Insufficient $BIGTIME tokens.")
        self.token_balance -= amount

    def add_material(self, material: str, quantity: int):
        """Add materials to the inventory."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        self.materials[material] = self.materials.get(material, 0) + quantity

    def remove_material(self, material: str, quantity: int):
        """Remove materials from the inventory."""
        if material not in self.materials or self.materials[material] < quantity:
            raise ValueError("Insufficient materials.")
        self.materials[material] -= quantity
        # Remove material from inventory if quantity is now zero
        if self.materials[material] == 0:
            del self.materials[material]

    def upgrade_item(self, item: str, cost_tokens: float, cost_materials: Dict[str, int]):
        """
        Upgrade an item, spending $BIGTIME tokens and required materials.
        
        Args:
            item: Name of the item to upgrade.
            cost_tokens: $BIGTIME tokens required for the upgrade.
            cost_materials: Materials and quantities required for the upgrade.
        """
        # Check token balance
        self.spend_tokens(cost_tokens)

        # Check material availability
        for material, quantity in cost_materials.items():
            if material not in self.materials or self.materials[material] < quantity:
                raise ValueError(f"Insufficient quantity of material: {material}")
        
        # Deduct materials
        for material, quantity in cost_materials.items():
            self.remove_material(material, quantity)

        # Upgrade item
        if item not in self.item_upgrades:
            self.item_upgrades[item] = 1  # Initialize new item at level 1
        else:
            self.item_upgrades[item] += 1  # Increment item level

    def export_data(self, file_path: str):
        """Export the current crafting economy data to a JSON file."""
        data = {
            "token_balance": self.token_balance,
            "materials": self.materials,
            "item_upgrades": self.item_upgrades,
        }
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self, file_path: str):
        """Load crafting economy data from a JSON file."""
        with open(file_path, 'r') as file:
            data = json.load(file)
            self.token_balance = data["token_balance"]
            self.materials = data["materials"]
            self.item_upgrades = data["item_upgrades"]

    def visualize_data(self):
        """Visualize the crafting economy data using matplotlib."""
        # Plot token balance
        plt.subplot(3, 1, 1)
        plt.bar(["$BIGTIME Tokens"], [self.token_balance], color='blue')
        plt.title("Token Balance")
        plt.ylabel("Amount")

        # Plot materials
        plt.subplot(3, 1, 2)
        materials = list(self.materials.keys())
        quantities = list(self.materials.values())
        plt.bar(materials, quantities, color='green')
        plt.title("Materials Inventory")
        plt.ylabel("Quantities")

        # Plot item upgrades
        plt.subplot(3, 1, 3)
        items = list(self.item_upgrades.keys())
        levels = list(self.item_upgrades.values())
        plt.bar(items, levels, color='orange')
        plt.title("Item Upgrades")
        plt.ylabel("Level")

        # Adjust layout
        plt.tight_layout()
        plt.show()


# Example usage (if running as a script)
if __name__ == "__main__":
    economy = CraftingEconomy()

    # Add tokens and materials
    economy.add_tokens(1000)
    economy.add_material("Iron", 50)
    economy.add_material("Wood", 30)

    # Upgrade an item
    economy.upgrade_item("Sword", cost_tokens=200, cost_materials={"Iron": 10, "Wood": 5})

    # Visualize the crafting economy
    economy.visualize_data()

    # Export and load data
    economy.export_data("economy_data.json")
    economy.load_data("economy_data.json")
```
