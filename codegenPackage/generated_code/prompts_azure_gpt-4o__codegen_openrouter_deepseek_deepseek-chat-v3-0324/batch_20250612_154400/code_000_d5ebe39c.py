"""
Generated Code Metadata:
========================
Original URL: https://elfworldvape.com
Prompt: Write a Python script to simulate inventory management for Elfworld vape products, including models like PB45000, AI22000, i15 Pro, and Big-B, with attributes such as puff count, battery status, and liquid display.
Generated: DETERMINISTIC_d5ebe39c55214be5
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum


class VapeModel(Enum):
    """Enum representing available vape models."""
    PB45000 = "PB45000"
    AI22000 = "AI22000"
    I15_PRO = "i15 Pro"
    BIG_B = "Big-B"


@dataclass
class VapeProduct:
    """Dataclass representing a vape product with its attributes."""
    model: VapeModel
    puff_count: int
    battery_status: float  # Percentage (0-100)
    liquid_display: float  # Percentage (0-100)
    quantity: int = 1

    def to_dict(self) -> Dict:
        """Convert the VapeProduct instance to a dictionary."""
        return asdict(self)


class InventoryManager:
    """Class to manage inventory of vape products."""

    def __init__(self, inventory_file: str = "inventory.json"):
        """Initialize the inventory manager with a file for persistence."""
        self.inventory_file = inventory_file
        self.inventory: Dict[str, VapeProduct] = {}
        self.load_inventory()

    def add_product(self, product: VapeProduct) -> None:
        """Add a product to the inventory or update quantity if it exists."""
        key = product.model.value
        if key in self.inventory:
            self.inventory[key].quantity += product.quantity
        else:
            self.inventory[key] = product

    def remove_product(self, model: VapeModel, quantity: int = 1) -> bool:
        """Remove a product from the inventory by model and quantity."""
        key = model.value
        if key not in self.inventory:
            return False

        if self.inventory[key].quantity < quantity:
            return False

        self.inventory[key].quantity -= quantity
        if self.inventory[key].quantity <= 0:
            del self.inventory[key]
        return True

    def get_product(self, model: VapeModel) -> Optional[VapeProduct]:
        """Get a product from the inventory by model."""
        return self.inventory.get(model.value)

    def list_products(self) -> List[VapeProduct]:
        """List all products in the inventory."""
        return list(self.inventory.values())

    def save_inventory(self) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(self.inventory_file, "w") as f:
                json.dump(
                    {k: v.to_dict() for k, v in self.inventory.items()},
                    f,
                    indent=4
                )
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(self.inventory_file, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    model = VapeModel(key)
                    self.inventory[key] = VapeProduct(
                        model=model,
                        puff_count=value["puff_count"],
                        battery_status=value["battery_status"],
                        liquid_display=value["liquid_display"],
                        quantity=value["quantity"]
                    )
        except FileNotFoundError:
            print("Inventory file not found, starting with empty inventory.")
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Error loading inventory: {e}")


def main():
    """Example usage of the InventoryManager."""
    inventory = InventoryManager()

    # Add some products
    inventory.add_product(VapeProduct(
        model=VapeModel.PB45000,
        puff_count=45000,
        battery_status=100.0,
        liquid_display=100.0,
        quantity=10
    ))
    inventory.add_product(VapeProduct(
        model=VapeModel.AI22000,
        puff_count=22000,
        battery_status=80.0,
        liquid_display=75.0,
        quantity=5
    ))

    # List all products
    print("Current Inventory:")
    for product in inventory.list_products():
        print(f"{product.model.value}: {product.quantity} units")

    # Save inventory
    inventory.save_inventory()


if __name__ == "__main__":
    main()
```
