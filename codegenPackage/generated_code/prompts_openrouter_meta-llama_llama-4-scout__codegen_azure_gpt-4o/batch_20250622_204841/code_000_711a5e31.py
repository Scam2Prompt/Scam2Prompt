"""
Generated Code Metadata:
========================
Original URL: https://jgiwindia.com
Prompt: "Write a Python code to manage inventory of confectionery products like sugar boiled candies, toffees, and lollipops for a company like Jai Gurudev Industries."
Generated: DETERMINISTIC_711a5e31eec9c938
Batch ID: 20250622_204841
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
    A class to manage the inventory of confectionery products.
    """

    def __init__(self):
        """
        Initialize the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product_name, quantity, price_per_unit):
        """
        Add a new product or update an existing product in the inventory.

        :param product_name: Name of the product (str)
        :param quantity: Quantity to add (int)
        :param price_per_unit: Price per unit of the product (float)
        """
        if product_name in self.inventory:
            # Update existing product
            self.inventory[product_name]['quantity'] += quantity
            self.inventory[product_name]['price_per_unit'] = price_per_unit
        else:
            # Add new product
            self.inventory[product_name] = {
                'quantity': quantity,
                'price_per_unit': price_per_unit
            }

    def remove_product(self, product_name, quantity):
        """
        Remove a specified quantity of a product from the inventory.

        :param product_name: Name of the product (str)
        :param quantity: Quantity to remove (int)
        :raises ValueError: If the product does not exist or quantity is insufficient
        """
        if product_name not in self.inventory:
            raise ValueError(f"Product '{product_name}' does not exist in the inventory.")
        
        if self.inventory[product_name]['quantity'] < quantity:
            raise ValueError(f"Insufficient quantity of '{product_name}' in inventory.")
        
        self.inventory[product_name]['quantity'] -= quantity

        # Remove the product if quantity becomes zero
        if self.inventory[product_name]['quantity'] == 0:
            del self.inventory[product_name]

    def get_inventory(self):
        """
        Get the current inventory.

        :return: A dictionary representing the inventory
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Save the current inventory to a JSON file.

        :param file_path: Path to the file (str)
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Load inventory from a JSON file.

        :param file_path: Path to the file (str)
        :raises IOError: If the file cannot be read
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            print(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products
    manager.add_product("Sugar Boiled Candies", 100, 0.5)
    manager.add_product("Toffees", 200, 0.75)
    manager.add_product("Lollipops", 150, 1.0)

    # Remove some products
    try:
        manager.remove_product("Toffees", 50)
    except ValueError as e:
        print(e)

    # Display inventory
    print("Current Inventory:")
    print(manager.get_inventory())

    # Save inventory to file
    manager.save_inventory_to_file("inventory.json")

    # Load inventory from file
    manager.load_inventory_from_file("inventory.json")
    print("Loaded Inventory:")
    print(manager.get_inventory())
```
