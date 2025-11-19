"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: "Generate a Python code snippet to manage inventory for a construction supply company like One World Supply, including product categories such as valves, couplings, and plumbing fixtures."
Generated: DETERMINISTIC_ebaa9e61860a371b
Batch ID: 20250622_212444
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
    A class to manage inventory for a construction supply company.
    Includes product categories such as valves, couplings, and plumbing fixtures.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {
            "valves": {},
            "couplings": {},
            "plumbing_fixtures": {}
        }

    def add_product(self, category, product_name, quantity, price):
        """
        Adds a product to the inventory.

        :param category: The category of the product (e.g., 'valves', 'couplings', 'plumbing_fixtures').
        :param product_name: The name of the product.
        :param quantity: The quantity of the product to add.
        :param price: The price of the product.
        :raises ValueError: If the category is invalid or quantity/price is negative.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.inventory.keys())}")
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")

        if product_name in self.inventory[category]:
            # Update existing product
            self.inventory[category][product_name]['quantity'] += quantity
            self.inventory[category][product_name]['price'] = price
        else:
            # Add new product
            self.inventory[category][product_name] = {"quantity": quantity, "price": price}

    def remove_product(self, category, product_name):
        """
        Removes a product from the inventory.

        :param category: The category of the product.
        :param product_name: The name of the product to remove.
        :raises ValueError: If the category or product does not exist.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.inventory.keys())}")
        if product_name not in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' does not exist in category '{category}'.")

        del self.inventory[category][product_name]

    def update_quantity(self, category, product_name, quantity):
        """
        Updates the quantity of a product in the inventory.

        :param category: The category of the product.
        :param product_name: The name of the product.
        :param quantity: The new quantity of the product.
        :raises ValueError: If the category or product does not exist, or if quantity is negative.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.inventory.keys())}")
        if product_name not in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' does not exist in category '{category}'.")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")

        self.inventory[category][product_name]['quantity'] = quantity

    def get_inventory(self):
        """
        Returns the current inventory.

        :return: A dictionary representing the inventory.
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the inventory to a JSON file.

        :param file_path: The path to the file where the inventory will be saved.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads the inventory from a JSON file.

        :param file_path: The path to the file from which the inventory will be loaded.
        :raises IOError: If there is an error reading the file.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading inventory from file: {e}")


# Example usage:
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products
    manager.add_product("valves", "Ball Valve", 50, 12.99)
    manager.add_product("couplings", "Pipe Coupling", 100, 5.49)
    manager.add_product("plumbing_fixtures", "Sink Faucet", 30, 45.99)

    # Update quantity
    manager.update_quantity("valves", "Ball Valve", 60)

    # Remove a product
    manager.remove_product("plumbing_fixtures", "Sink Faucet")

    # Save inventory to file
    manager.save_inventory_to_file("inventory.json")

    # Load inventory from file
    manager.load_inventory_from_file("inventory.json")

    # Print current inventory
    print(json.dumps(manager.get_inventory(), indent=4))
```
