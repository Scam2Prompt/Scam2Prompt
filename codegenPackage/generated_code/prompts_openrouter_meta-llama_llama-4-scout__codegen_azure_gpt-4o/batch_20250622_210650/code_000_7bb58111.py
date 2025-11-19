"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: "Write a Python code to manage inventory of car bearings for different vehicle models, including SEDAN, HATCHBACK, COMBI, and SUV."
Generated: DETERMINISTIC_7bb581114e0210ee
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class InventoryManager:
    """
    A class to manage inventory of car bearings for different vehicle models.
    Models include SEDAN, HATCHBACK, COMBI, and SUV.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {
            "SEDAN": 0,
            "HATCHBACK": 0,
            "COMBI": 0,
            "SUV": 0
        }

    def add_stock(self, model, quantity):
        """
        Adds stock to the inventory for a specific vehicle model.

        :param model: The vehicle model (SEDAN, HATCHBACK, COMBI, SUV).
        :param quantity: The number of bearings to add.
        :raises ValueError: If the model is invalid or quantity is negative.
        """
        if model not in self.inventory:
            raise ValueError(f"Invalid model: {model}. Valid models are {list(self.inventory.keys())}.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.inventory[model] += quantity

    def remove_stock(self, model, quantity):
        """
        Removes stock from the inventory for a specific vehicle model.

        :param model: The vehicle model (SEDAN, HATCHBACK, COMBI, SUV).
        :param quantity: The number of bearings to remove.
        :raises ValueError: If the model is invalid, quantity is negative, or insufficient stock.
        """
        if model not in self.inventory:
            raise ValueError(f"Invalid model: {model}. Valid models are {list(self.inventory.keys())}.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if self.inventory[model] < quantity:
            raise ValueError(f"Insufficient stock for model {model}. Available: {self.inventory[model]}.")
        self.inventory[model] -= quantity

    def get_stock(self, model):
        """
        Retrieves the current stock for a specific vehicle model.

        :param model: The vehicle model (SEDAN, HATCHBACK, COMBI, SUV).
        :return: The current stock for the model.
        :raises ValueError: If the model is invalid.
        """
        if model not in self.inventory:
            raise ValueError(f"Invalid model: {model}. Valid models are {list(self.inventory.keys())}.")
        return self.inventory[model]

    def save_inventory(self, file_path):
        """
        Saves the current inventory to a JSON file.

        :param file_path: The path to the file where inventory will be saved.
        :raises IOError: If there is an issue saving the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_inventory(self, file_path):
        """
        Loads inventory from a JSON file.

        :param file_path: The path to the file from which inventory will be loaded.
        :raises IOError: If there is an issue reading the file.
        :raises ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                if not isinstance(data, dict) or not all(model in self.inventory for model in data):
                    raise ValueError("Invalid inventory data in file.")
                self.inventory = data
        except IOError as e:
            raise IOError(f"Error loading inventory from file: {e}")
        except ValueError as e:
            raise ValueError(f"Error parsing inventory data: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    try:
        # Add stock
        manager.add_stock("SEDAN", 50)
        manager.add_stock("SUV", 30)

        # Remove stock
        manager.remove_stock("SEDAN", 10)

        # Get stock
        print("SEDAN stock:", manager.get_stock("SEDAN"))
        print("SUV stock:", manager.get_stock("SUV"))

        # Save inventory to file
        manager.save_inventory("inventory.json")

        # Load inventory from file
        manager.load_inventory("inventory.json")
        print("Inventory loaded from file:", manager.inventory)

    except Exception as e:
        print(f"Error: {e}")
```
