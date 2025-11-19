"""
Generated Code Metadata:
========================
Original URL: https://eferroeacobrza.blogspot.com
Prompt: "Write a Python code to manage inventory of iron and steel products, including chapas galvanizadas and brancas, for a company like Eferroeaco."
Generated: DETERMINISTIC_d95152888d480591
Batch ID: 20250622_204617
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
    A class to manage inventory for iron and steel products.
    Includes chapas galvanizadas and chapas brancas.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product_name, quantity):
        """
        Adds a product to the inventory or updates its quantity.

        Args:
            product_name (str): Name of the product.
            quantity (int): Quantity to add to the inventory.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if product_name in self.inventory:
            self.inventory[product_name] += quantity
        else:
            self.inventory[product_name] = quantity

    def remove_product(self, product_name, quantity):
        """
        Removes a product from the inventory or decreases its quantity.

        Args:
            product_name (str): Name of the product.
            quantity (int): Quantity to remove from the inventory.

        Raises:
            ValueError: If quantity is negative or exceeds available stock.
            KeyError: If the product does not exist in the inventory.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if product_name not in self.inventory:
<<<<<<< HEAD
            raise KeyError(f"Product '{product_name}' does not exist in the inventory.")
        
        if self.inventory[product_name] < quantity:
            raise ValueError(f"Not enough stock to remove {quantity} units of '{product_name}'.")
        
        self.inventory[product_name] -= quantity
        
        # Remove the product from inventory if quantity becomes zero
=======
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        
        if self.inventory[product_name] < quantity:
            raise ValueError(f"Insufficient stock for '{product_name}'. Available: {self.inventory[product_name]}")
        
        self.inventory[product_name] -= quantity
        
        # Remove product from inventory if quantity becomes zero
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        if self.inventory[product_name] == 0:
            del self.inventory[product_name]

    def get_inventory(self):
        """
        Returns the current inventory.

        Returns:
            dict: A dictionary representing the inventory.
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the inventory to a JSON file.

        Args:
            file_path (str): Path to the file where inventory will be saved.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads the inventory from a JSON file.

        Args:
            file_path (str): Path to the file from which inventory will be loaded.

        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the file contains invalid JSON data.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading inventory from file: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid JSON data in file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

<<<<<<< HEAD
    # Adding products
    manager.add_product("Chapas Galvanizadas", 100)
    manager.add_product("Chapas Brancas", 50)

    # Removing products
=======
    # Add products
    manager.add_product("Chapas Galvanizadas", 100)
    manager.add_product("Chapas Brancas", 50)

    # Remove products
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    try:
        manager.remove_product("Chapas Galvanizadas", 20)
    except Exception as e:
        print(f"Error: {e}")

<<<<<<< HEAD
    # Displaying inventory
    print("Current Inventory:", manager.get_inventory())

    # Saving inventory to file
=======
    # Display inventory
    print("Current Inventory:", manager.get_inventory())

    # Save inventory to file
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    try:
        manager.save_inventory_to_file("inventory.json")
    except Exception as e:
        print(f"Error: {e}")

<<<<<<< HEAD
    # Loading inventory from file
=======
    # Load inventory from file
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    try:
        manager.load_inventory_from_file("inventory.json")
        print("Loaded Inventory:", manager.get_inventory())
    except Exception as e:
        print(f"Error: {e}")
```
