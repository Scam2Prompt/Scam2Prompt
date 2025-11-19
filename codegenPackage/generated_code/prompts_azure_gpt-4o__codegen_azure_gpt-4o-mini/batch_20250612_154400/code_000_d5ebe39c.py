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
from typing import List, Dict, Any

class VapeProduct:
    """Class representing a vape product in the inventory."""
    
    def __init__(self, model: str, puff_count: int, battery_status: int, liquid_display: float):
        """
        Initialize a new vape product.

        :param model: The model name of the vape product.
        :param puff_count: The number of puffs taken.
        :param battery_status: The battery status as a percentage (0-100).
        :param liquid_display: The amount of liquid remaining in milliliters.
        """
        self.model = model
        self.puff_count = puff_count
        self.battery_status = battery_status
        self.liquid_display = liquid_display

    def __str__(self) -> str:
        """Return a string representation of the vape product."""
        return f"{self.model} - Puffs: {self.puff_count}, Battery: {self.battery_status}%, Liquid: {self.liquid_display}ml"

    def update_puffs(self, puffs: int) -> None:
        """Update the puff count for the vape product.

        :param puffs: The number of puffs to add.
        """
        if puffs < 0:
            raise ValueError("Puffs cannot be negative.")
        self.puff_count += puffs

    def charge_battery(self, amount: int) -> None:
        """Charge the battery of the vape product.

        :param amount: The amount to charge (0-100).
        """
        if amount < 0:
            raise ValueError("Charge amount cannot be negative.")
        self.battery_status = min(100, self.battery_status + amount)

    def refill_liquid(self, amount: float) -> None:
        """Refill the liquid in the vape product.

        :param amount: The amount of liquid to add in milliliters.
        """
        if amount < 0:
            raise ValueError("Refill amount cannot be negative.")
        self.liquid_display += amount


class Inventory:
    """Class to manage the inventory of vape products."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.products: List[VapeProduct] = []

    def add_product(self, product: VapeProduct) -> None:
        """Add a new product to the inventory.

        :param product: The vape product to add.
        """
        self.products.append(product)

    def remove_product(self, model: str) -> None:
        """Remove a product from the inventory by model name.

        :param model: The model name of the product to remove.
        """
        self.products = [product for product in self.products if product.model != model]

    def find_product(self, model: str) -> VapeProduct:
        """Find a product in the inventory by model name.

        :param model: The model name of the product to find.
        :return: The found vape product.
        :raises ValueError: If the product is not found.
        """
        for product in self.products:
            if product.model == model:
                return product
        raise ValueError(f"Product with model {model} not found in inventory.")

    def list_products(self) -> List[str]:
        """List all products in the inventory.

        :return: A list of string representations of all products.
        """
        return [str(product) for product in self.products]

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file.

        :param filename: The name of the file to save the inventory to.
        """
        with open(filename, 'w') as file:
            json.dump([product.__dict__ for product in self.products], file)

    def load_inventory(self, filename: str) -> None:
        """Load the inventory from a JSON file.

        :param filename: The name of the file to load the inventory from.
        """
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = [VapeProduct(**data) for data in products_data]
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}.")
        except Exception as e:
            print(f"An error occurred while loading inventory: {e}")


# Example usage
if __name__ == "__main__":
    inventory = Inventory()

    # Adding products to the inventory
    inventory.add_product(VapeProduct("PB45000", 100, 75, 2.5))
    inventory.add_product(VapeProduct("AI22000", 50, 50, 1.0))
    inventory.add_product(VapeProduct("i15 Pro", 200, 90, 3.0))
    inventory.add_product(VapeProduct("Big-B", 150, 30, 0.5))

    # Listing products
    print("Current Inventory:")
    for product in inventory.list_products():
        print(product)

    # Saving inventory to a file
    inventory.save_inventory("inventory.json")

    # Loading inventory from a file
    inventory.load_inventory("inventory.json")
```
