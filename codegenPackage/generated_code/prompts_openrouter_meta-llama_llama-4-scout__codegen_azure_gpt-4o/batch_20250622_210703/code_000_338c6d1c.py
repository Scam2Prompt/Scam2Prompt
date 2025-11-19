"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: "Write a Python code snippet to manage the inventory of fiberglass products, including Glass fiber reinforced concrete (GFRC), IDGFiber® PPF, and Ceramic fiber."
Generated: DETERMINISTIC_338c6d1cd95048d0
Batch ID: 20250622_210703
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
    A class to manage the inventory of fiberglass products.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {
            "GFRC": 0,  # Glass fiber reinforced concrete
            "IDGFiber_PPF": 0,  # IDGFiber® PPF
            "Ceramic_Fiber": 0  # Ceramic fiber
        }

    def add_stock(self, product_name, quantity):
        """
        Adds stock to the inventory.

        :param product_name: Name of the product to add stock for.
        :param quantity: Quantity to add.
        :raises ValueError: If the product name is invalid or quantity is negative.
        """
        if product_name not in self.inventory:
            raise ValueError(f"Invalid product name: {product_name}")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.inventory[product_name] += quantity

    def remove_stock(self, product_name, quantity):
        """
        Removes stock from the inventory.

        :param product_name: Name of the product to remove stock from.
        :param quantity: Quantity to remove.
        :raises ValueError: If the product name is invalid, quantity is negative, or insufficient stock.
        """
        if product_name not in self.inventory:
            raise ValueError(f"Invalid product name: {product_name}")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if self.inventory[product_name] < quantity:
            raise ValueError("Insufficient stock to remove.")
        self.inventory[product_name] -= quantity

    def get_stock(self, product_name):
        """
        Retrieves the current stock for a product.

        :param product_name: Name of the product to check stock for.
        :return: Current stock quantity.
        :raises ValueError: If the product name is invalid.
        """
        if product_name not in self.inventory:
            raise ValueError(f"Invalid product name: {product_name}")
        return self.inventory[product_name]

    def save_inventory(self, file_path):
        """
        Saves the inventory to a JSON file.

        :param file_path: Path to the file where inventory will be saved.
        :raises IOError: If there is an issue saving the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_inventory(self, file_path):
        """
        Loads the inventory from a JSON file.

        :param file_path: Path to the file to load inventory from.
        :raises IOError: If there is an issue reading the file.
        :raises ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                if not isinstance(data, dict):
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
        manager.add_stock("GFRC", 50)
        manager.add_stock("IDGFiber_PPF", 30)
        manager.add_stock("Ceramic_Fiber", 20)

        # Remove stock
        manager.remove_stock("GFRC", 10)

        # Get stock
        print("Current GFRC stock:", manager.get_stock("GFRC"))

        # Save inventory to file
        manager.save_inventory("inventory.json")

        # Load inventory from file
        manager.load_inventory("inventory.json")
        print("Inventory loaded from file:", manager.inventory)

    except Exception as e:
        print(f"Error: {e}")
```
