"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Develop a program to manage and visualize the crafting economy in Big Time, including tracking $BIGTIME token usage, materials, and item upgrades.
Generated: DETERMINISTIC_de4aafc41e04cff1
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CraftingEconomyManager:
    def __init__(self):
        """Initialize the crafting economy manager with empty data."""
        self.token_usage: float = 0.0
        self.materials: Dict[str, int] = {}
        self.item_upgrades: Dict[str, Dict[str, Any]] = {}

    def add_material(self, material: str, quantity: int) -> None:
        """Add materials to the inventory.

        Args:
            material (str): The name of the material.
            quantity (int): The quantity of the material to add.
        """
        if quantity < 0:
            logging.error("Quantity must be non-negative.")
            raise ValueError("Quantity must be non-negative.")
        
        self.materials[material] = self.materials.get(material, 0) + quantity
        logging.info(f"Added {quantity} of {material}. Total: {self.materials[material]}")

    def use_tokens(self, amount: float) -> None:
        """Track the usage of $BIGTIME tokens.

        Args:
            amount (float): The amount of tokens to use.
        """
        if amount < 0:
            logging.error("Token amount must be non-negative.")
            raise ValueError("Token amount must be non-negative.")
        
        self.token_usage += amount
        logging.info(f"Used {amount} $BIGTIME tokens. Total used: {self.token_usage}")

    def upgrade_item(self, item_name: str, upgrade_details: Dict[str, Any]) -> None:
        """Upgrade an item with specified details.

        Args:
            item_name (str): The name of the item to upgrade.
            upgrade_details (Dict[str, Any]): Details of the upgrade including materials needed.
        """
        required_materials = upgrade_details.get("materials", {})
        for material, quantity in required_materials.items():
            if self.materials.get(material, 0) < quantity:
                logging.error(f"Not enough {material} to upgrade {item_name}. Required: {quantity}, Available: {self.materials.get(material, 0)}")
                raise ValueError(f"Not enough {material} to upgrade {item_name}.")
            self.materials[material] -= quantity
        
        self.item_upgrades[item_name] = upgrade_details
        logging.info(f"Upgraded {item_name} with details: {upgrade_details}")

    def visualize_economy(self) -> None:
        """Visualize the current state of the crafting economy."""
        economy_data = {
            "token_usage": self.token_usage,
            "materials": self.materials,
            "item_upgrades": self.item_upgrades
        }
        print(json.dumps(economy_data, indent=4))

def main():
    """Main function to demonstrate the crafting economy manager."""
    try:
        manager = CraftingEconomyManager()
        manager.add_material("Wood", 50)
        manager.add_material("Stone", 30)
        manager.use_tokens(100)
        manager.upgrade_item("Wooden Sword", {
            "materials": {
                "Wood": 10,
                "Stone": 5
            },
            "new_attributes": {
                "damage": 15,
                "durability": 100
            }
        })
        manager.visualize_economy()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
