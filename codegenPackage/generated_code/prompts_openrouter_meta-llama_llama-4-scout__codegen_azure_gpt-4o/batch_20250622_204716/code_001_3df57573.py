"""
Generated Code Metadata:
========================
Original URL: https://paperland.com.ar
Prompt: "Write a Python script to manage inventory for a paper and cardboard product manufacturing company like Paperland, including product categories such as artistica y manualidades and línea de cajas infantiles."
Generated: DETERMINISTIC_3df575732ad1eb93
Batch ID: 20250622_204716
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
    A class to manage inventory for a paper and cardboard product manufacturing company.
    """

    def __init__(self):
        """
<<<<<<< HEAD
        Initialize the inventory manager with an empty inventory.
        """
        self.inventory = {
            "artistica_y_manualidades": {},
            "linea_de_cajas_infantiles": {}
=======
        Initializes the inventory manager with predefined product categories.
        """
        self.inventory = {
            "artistica_y_manualidades": {},  # Artistic and crafts category
            "linea_de_cajas_infantiles": {}  # Children's box line category
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        }

    def add_product(self, category, product_name, quantity, price):
        """
<<<<<<< HEAD
        Add a product to the inventory.

        :param category: The category of the product (e.g., 'artistica_y_manualidades').
        :param product_name: The name of the product.
        :param quantity: The quantity of the product.
        :param price: The price of the product.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}")
        
=======
        Adds a product to the inventory.

        Args:
            category (str): The category of the product.
            product_name (str): The name of the product.
            quantity (int): The quantity of the product.
            price (float): The price of the product.

        Raises:
            ValueError: If the category is invalid or quantity/price is negative.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}")
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")

>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        if product_name in self.inventory[category]:
            # Update existing product
            self.inventory[category][product_name]['quantity'] += quantity
            self.inventory[category][product_name]['price'] = price
        else:
            # Add new product
            self.inventory[category][product_name] = {
                "quantity": quantity,
                "price": price
            }

    def remove_product(self, category, product_name):
        """
<<<<<<< HEAD
        Remove a product from the inventory.

        :param category: The category of the product.
        :param product_name: The name of the product.
        """
        if category not in self.inventory or product_name not in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' not found in category '{category}'")
        
        del self.inventory[category][product_name]

    def update_quantity(self, category, product_name, quantity):
        """
        Update the quantity of a product.

        :param category: The category of the product.
        :param product_name: The name of the product.
        :param quantity: The new quantity of the product.
        """
        if category not in self.inventory or product_name not in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' not found in category '{category}'")
        
=======
        Removes a product from the inventory.

        Args:
            category (str): The category of the product.
            product_name (str): The name of the product.

        Raises:
            ValueError: If the category or product does not exist.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}")
        if product_name not in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' not found in category '{category}'.")

        del self.inventory[category][product_name]

    def update_product_quantity(self, category, product_name, quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            category (str): The category of the product.
            product_name (str): The name of the product.
            quantity (int): The new quantity of the product.

        Raises:
            ValueError: If the category or product does not exist, or quantity is negative.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}")
        if product_name not in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' not found in category '{category}'.")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")

>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        self.inventory[category][product_name]['quantity'] = quantity

    def get_inventory(self):
        """
<<<<<<< HEAD
        Get the current inventory.

        :return: A dictionary representing the inventory.
=======
        Returns the current inventory.

        Returns:
            dict: The inventory data.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
<<<<<<< HEAD
        Save the inventory to a JSON file.

        :param file_path: The path to the file where the inventory will be saved.
=======
        Saves the inventory to a JSON file.

        Args:
            file_path (str): The path to the file where inventory will be saved.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
<<<<<<< HEAD
        Load the inventory from a JSON file.

        :param file_path: The path to the file from which the inventory will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            print(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")
=======
        Loads the inventory from a JSON file.

        Args:
            file_path (str): The path to the file from which inventory will be loaded.

        Raises:
            ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                if not isinstance(data, dict):
                    raise ValueError("Invalid inventory data in file.")
                self.inventory = data
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products
    manager.add_product("artistica_y_manualidades", "Sketchbook", 50, 12.99)
<<<<<<< HEAD
    manager.add_product("linea_de_cajas_infantiles", "Toy Box", 20, 25.50)

    # Update quantity
    manager.update_quantity("artistica_y_manualidades", "Sketchbook", 60)
=======
    manager.add_product("linea_de_cajas_infantiles", "Toy Box", 30, 25.50)

    # Update product quantity
    manager.update_product_quantity("artistica_y_manualidades", "Sketchbook", 60)
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

    # Remove a product
    manager.remove_product("linea_de_cajas_infantiles", "Toy Box")

    # Save inventory to file
    manager.save_inventory_to_file("inventory.json")

    # Load inventory from file
    manager.load_inventory_from_file("inventory.json")

    # Print current inventory
    print(json.dumps(manager.get_inventory(), indent=4))
```
