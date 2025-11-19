"""
Generated Code Metadata:
========================
Original URL: https://herramientasharo.shop
Prompt: "Write a Python code to manage inventory for a store selling generators, including Predator 3500w and 6500w models, and track their prices in MXN."
Generated: DETERMINISTIC_dd1a5f33ae83213a
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any

class InventoryManager:
    """
    A class to manage the inventory of generators in a store.
    """

    def __init__(self):
        """
        Initializes the inventory with predefined models and their prices.
        """
        self.inventory: Dict[str, Dict[str, Any]] = {
            "Predator 3500w": {"quantity": 0, "price": 0},
            "Predator 6500w": {"quantity": 0, "price": 0}
        }

    def set_price(self, model: str, price: float) -> None:
        """
        Sets the price for a specific generator model.

        :param model: The model of the generator.
        :param price: The price in MXN.
        :raises ValueError: If the model is not recognized or the price is negative.
        """
        if model not in self.inventory:
            raise ValueError(f"Model '{model}' not found in inventory.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.inventory[model]["price"] = price

    def add_stock(self, model: str, quantity: int) -> None:
        """
        Adds stock for a specific generator model.

        :param model: The model of the generator.
        :param quantity: The quantity to add.
        :raises ValueError: If the model is not recognized or the quantity is negative.
        """
        if model not in self.inventory:
            raise ValueError(f"Model '{model}' not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        self.inventory[model]["quantity"] += quantity

    def remove_stock(self, model: str, quantity: int) -> None:
        """
        Removes stock for a specific generator model.

        :param model: The model of the generator.
        :param quantity: The quantity to remove.
        :raises ValueError: If the model is not recognized, the quantity is negative, or insufficient stock.
        """
        if model not in self.inventory:
            raise ValueError(f"Model '{model}' not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if quantity > self.inventory[model]["quantity"]:
            raise ValueError("Insufficient stock to remove.")

        self.inventory[model]["quantity"] -= quantity

    def get_inventory(self) -> Dict[str, Dict[str, Any]]:
        """
        Returns the current inventory status.

        :return: A dictionary containing the inventory details.
        """
        return self.inventory

    def save_inventory(self, filename: str) -> None:
        """
        Saves the current inventory to a JSON file.

        :param filename: The name of the file to save the inventory.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_inventory(self, filename: str) -> None:
        """
        Loads inventory from a JSON file.

        :param filename: The name of the file to load the inventory from.
        :raises IOError: If there is an error reading the file.
        :raises ValueError: If the file content is not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in file: {e}")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    manager.set_price("Predator 3500w", 5000)
    manager.set_price("Predator 6500w", 8000)
    manager.add_stock("Predator 3500w", 10)
    manager.add_stock("Predator 6500w", 5)

    print("Current Inventory:")
    print(manager.get_inventory())

    manager.save_inventory("inventory.json")
    print("Inventory saved to 'inventory.json'.")
```
