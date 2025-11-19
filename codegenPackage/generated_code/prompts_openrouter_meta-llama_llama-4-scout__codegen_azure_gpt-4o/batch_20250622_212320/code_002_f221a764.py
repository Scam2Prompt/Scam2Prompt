"""
Generated Code Metadata:
========================
Original URL: https://tudulcepecado.cl
Prompt: Write a Python script to manage an e-commerce inventory system for a sex toy store like Tu Dulce Pecado, including product categorization and pricing.
Generated: DETERMINISTIC_f221a764ac983357
Batch ID: 20250622_212320
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
    A class to manage the inventory of an e-commerce store.
    Includes functionality for adding, updating, deleting, and viewing products.
    """

    def __init__(self):
        # Initialize the inventory as an empty dictionary
        self.inventory = {}

    def add_product(self, product_id, name, category, price, stock):
        """
        Add a new product to the inventory.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param category: Category of the product (e.g., Vibrators, Lubricants, etc.)
        :param price: Price of the product (float)
        :param stock: Quantity of the product in stock (int)
        """
        if product_id in self.inventory:
            print(f"Error: Product ID {product_id} already exists.")
            return

        self.inventory[product_id] = {
            "name": name,
            "category": category,
            "price": price,
            "stock": stock
        }
        print(f"Product '{name}' added successfully.")

    def update_product(self, product_id, name=None, category=None, price=None, stock=None):
        """
        Update an existing product in the inventory.

        :param product_id: Unique identifier for the product
        :param name: Updated name of the product (optional)
        :param category: Updated category of the product (optional)
        :param price: Updated price of the product (optional)
        :param stock: Updated stock quantity of the product (optional)
        """
        if product_id not in self.inventory:
            print(f"Error: Product ID {product_id} does not exist.")
            return

        product = self.inventory[product_id]
        if name:
            product["name"] = name
        if category:
            product["category"] = category
        if price:
            product["price"] = price
        if stock:
            product["stock"] = stock

        print(f"Product ID {product_id} updated successfully.")

    def delete_product(self, product_id):
        """
        Delete a product from the inventory.

        :param product_id: Unique identifier for the product
        """
        if product_id not in self.inventory:
            print(f"Error: Product ID {product_id} does not exist.")
            return

        del self.inventory[product_id]
        print(f"Product ID {product_id} deleted successfully.")

    def view_inventory(self):
        """
        Display the current inventory in a readable format.
        """
        if not self.inventory:
            print("Inventory is empty.")
            return

        print("Current Inventory:")
        for product_id, details in self.inventory.items():
            print(f"ID: {product_id}, Name: {details['name']}, Category: {details['category']}, "
                  f"Price: ${details['price']:.2f}, Stock: {details['stock']}")

    def save_inventory_to_file(self, filename):
        """
        Save the inventory to a JSON file.

        :param filename: Name of the file to save the inventory
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.inventory, file, indent=4)
            print(f"Inventory saved to '{filename}' successfully.")
        except Exception as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, filename):
        """
        Load the inventory from a JSON file.

        :param filename: Name of the file to load the inventory from
        """
        try:
            with open(filename, 'r') as file:
                self.inventory = json.load(file)
            print(f"Inventory loaded from '{filename}' successfully.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error: File '{filename}' is not a valid JSON file.")
        except Exception as e:
            print(f"Error loading inventory from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products
    manager.add_product("001", "Vibrator X", "Vibrators", 49.99, 100)
    manager.add_product("002", "Lubricant Y", "Lubricants", 9.99, 200)

    # View inventory
    manager.view_inventory()

    # Update a product
    manager.update_product("001", price=44.99, stock=90)

    # Delete a product
    manager.delete_product("002")

    # Save inventory to file
    manager.save_inventory_to_file("inventory.json")

    # Load inventory from file
    manager.load_inventory_from_file("inventory.json")

    # View inventory again
    manager.view_inventory()
```
