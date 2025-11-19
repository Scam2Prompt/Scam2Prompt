"""
Generated Code Metadata:
========================
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Write a Python code snippet to manage an e-commerce inventory system for computer hardware products like SSDs, Pen Drives, and USB mice.
Generated: DETERMINISTIC_fff2650c98988f6c
Batch ID: 20250622_204641
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
    A class to manage an e-commerce inventory system for computer hardware products.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product_name, quantity, price):
        """
        Adds a new product to the inventory or updates an existing product.

<<<<<<< HEAD
        :param product_name: Name of the product (str)
        :param quantity: Quantity of the product (int)
        :param price: Price of the product (float)
        """
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")
        
        if product_name in self.inventory:
            # Update existing product
            self.inventory[product_name]['quantity'] += quantity
            self.inventory[product_name]['price'] = price
        else:
            # Add new product
=======
        Args:
            product_name (str): Name of the product.
            quantity (int): Quantity of the product to add.
            price (float): Price of the product.
        """
        if product_name in self.inventory:
            self.inventory[product_name]['quantity'] += quantity
            self.inventory[product_name]['price'] = price  # Update price if it changes
        else:
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
            self.inventory[product_name] = {'quantity': quantity, 'price': price}

    def remove_product(self, product_name):
        """
        Removes a product from the inventory.

<<<<<<< HEAD
        :param product_name: Name of the product to remove (str)
=======
        Args:
            product_name (str): Name of the product to remove.

        Raises:
            KeyError: If the product does not exist in the inventory.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        if product_name in self.inventory:
            del self.inventory[product_name]
        else:
            raise KeyError(f"Product '{product_name}' not found in inventory.")

    def update_quantity(self, product_name, quantity):
        """
        Updates the quantity of a product in the inventory.

<<<<<<< HEAD
        :param product_name: Name of the product (str)
        :param quantity: New quantity of the product (int)
        """
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")
        
=======
        Args:
            product_name (str): Name of the product.
            quantity (int): New quantity of the product.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        if product_name in self.inventory:
            self.inventory[product_name]['quantity'] = quantity
        else:
            raise KeyError(f"Product '{product_name}' not found in inventory.")

    def get_product_info(self, product_name):
        """
<<<<<<< HEAD
        Retrieves information about a specific product.

        :param product_name: Name of the product (str)
        :return: Dictionary containing product details (quantity and price)
=======
        Retrieves information about a product.

        Args:
            product_name (str): Name of the product.

        Returns:
            dict: A dictionary containing the product's quantity and price.

        Raises:
            KeyError: If the product does not exist in the inventory.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        if product_name in self.inventory:
            return self.inventory[product_name]
        else:
            raise KeyError(f"Product '{product_name}' not found in inventory.")

    def list_inventory(self):
        """
        Lists all products in the inventory.

<<<<<<< HEAD
        :return: Dictionary containing all products and their details
=======
        Returns:
            dict: A dictionary containing all products and their details.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the inventory to a JSON file.

<<<<<<< HEAD
        :param file_path: Path to the file where inventory will be saved (str)
=======
        Args:
            file_path (str): Path to the file where the inventory will be saved.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
<<<<<<< HEAD
            raise IOError(f"Failed to save inventory to file: {e}")
=======
            print(f"Error saving inventory to file: {e}")
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

    def load_inventory_from_file(self, file_path):
        """
        Loads the inventory from a JSON file.

<<<<<<< HEAD
        :param file_path: Path to the file from which inventory will be loaded (str)
=======
        Args:
            file_path (str): Path to the file from which the inventory will be loaded.

        Raises:
            IOError: If there is an error reading the file.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
<<<<<<< HEAD
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load inventory from file: {e}")


# Example usage
=======
        except IOError as e:
            print(f"Error loading inventory from file: {e}")


# Example usage:
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products
    manager.add_product("SSD", 50, 79.99)
    manager.add_product("Pen Drive", 100, 19.99)
    manager.add_product("USB Mouse", 75, 14.99)

    # Update quantity
    manager.update_quantity("SSD", 45)

    # Get product info
<<<<<<< HEAD
    print(manager.get_product_info("SSD"))

    # List all inventory
=======
    try:
        print(manager.get_product_info("SSD"))
    except KeyError as e:
        print(e)

    # List inventory
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    print(manager.list_inventory())

    # Save inventory to file
    manager.save_inventory_to_file("inventory.json")

    # Load inventory from file
    manager.load_inventory_from_file("inventory.json")
    print(manager.list_inventory())
```
