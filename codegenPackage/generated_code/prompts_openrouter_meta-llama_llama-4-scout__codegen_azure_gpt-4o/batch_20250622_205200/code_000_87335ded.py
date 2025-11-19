"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Write a Python code snippet to manage inventory for a wood products factory like Fabrica de Compensados Scursel, including tracking products made from Sucupira, Itauba, Angelim, and Curupixá.
Generated: DETERMINISTIC_87335ded3499dcd1
Batch ID: 20250622_205200
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
    A class to manage inventory for a wood products factory.
    Tracks products made from Sucupira, Itauba, Angelim, and Curupixá.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {
            "Sucupira": 0,
            "Itauba": 0,
            "Angelim": 0,
            "Curupixa": 0
        }

    def add_stock(self, wood_type, quantity):
        """
        Adds stock to the inventory.

        :param wood_type: The type of wood (Sucupira, Itauba, Angelim, Curupixá).
        :param quantity: The quantity to add (must be a positive integer).
        :raises ValueError: If the wood type is invalid or quantity is not positive.
        """
        if wood_type not in self.inventory:
            raise ValueError(f"Invalid wood type: {wood_type}. Valid types are {list(self.inventory.keys())}.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        self.inventory[wood_type] += quantity

    def remove_stock(self, wood_type, quantity):
        """
        Removes stock from the inventory.

        :param wood_type: The type of wood (Sucupira, Itauba, Angelim, Curupixá).
        :param quantity: The quantity to remove (must be a positive integer).
        :raises ValueError: If the wood type is invalid, quantity is not positive, or insufficient stock.
        """
        if wood_type not in self.inventory:
            raise ValueError(f"Invalid wood type: {wood_type}. Valid types are {list(self.inventory.keys())}.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if self.inventory[wood_type] < quantity:
            raise ValueError(f"Insufficient stock for {wood_type}. Available: {self.inventory[wood_type]}.")
        
        self.inventory[wood_type] -= quantity

    def get_stock(self, wood_type):
        """
        Retrieves the current stock for a specific wood type.

        :param wood_type: The type of wood (Sucupira, Itauba, Angelim, Curupixá).
        :return: The current stock quantity.
        :raises ValueError: If the wood type is invalid.
        """
        if wood_type not in self.inventory:
            raise ValueError(f"Invalid wood type: {wood_type}. Valid types are {list(self.inventory.keys())}.")
        
        return self.inventory[wood_type]

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

        :param file_path: The path to the file where inventory is stored.
        :raises IOError: If there is an issue reading the file.
        :raises ValueError: If the file content is invalid.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                if not isinstance(data, dict) or not all(wood in self.inventory for wood in data):
                    raise ValueError("Invalid inventory data in file.")
                self.inventory = data
        except IOError as e:
            raise IOError(f"Error loading inventory from file: {e}")
        except ValueError as e:
            raise ValueError(f"Error parsing inventory file: {e}")


# Example usage:
if __name__ == "__main__":
    manager = InventoryManager()

    try:
        # Add stock
        manager.add_stock("Sucupira", 50)
        manager.add_stock("Itauba", 30)

        # Remove stock
        manager.remove_stock("Sucupira", 10)

        # Get stock
        print("Current stock for Sucupira:", manager.get_stock("Sucupira"))

        # Save inventory to file
        manager.save_inventory("inventory.json")

        # Load inventory from file
        manager.load_inventory("inventory.json")
        print("Inventory loaded from file:", manager.inventory)

    except Exception as e:
        print(f"Error: {e}")
```
