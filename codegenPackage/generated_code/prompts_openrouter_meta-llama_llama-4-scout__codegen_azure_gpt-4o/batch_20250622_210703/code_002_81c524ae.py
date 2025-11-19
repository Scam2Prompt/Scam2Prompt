"""
Generated Code Metadata:
========================
Original URL: https://baliauthenticcoffeeandgallery.com
Prompt: "Write a Python script to manage inventory for an online store with product categories like coffee, crafts, and clothing, ensuring automatic updates for orders and stock levels."
Generated: DETERMINISTIC_81c524ae4fd688d2
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
    A class to manage inventory for an online store with product categories.
    Categories include coffee, crafts, and clothing.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the InventoryManager with an inventory file.
        :param inventory_file: Path to the inventory JSON file.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Load inventory from a JSON file.
        :return: Dictionary representing the inventory.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty inventory
            return {"coffee": {}, "crafts": {}, "clothing": {}}
        except json.JSONDecodeError:
            raise ValueError("Inventory file is not a valid JSON.")

    def save_inventory(self):
        """
        Save the current inventory to the JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save inventory: {e}")

    def add_product(self, category, product_name, quantity, price):
        """
        Add a new product to the inventory.
        :param category: Category of the product (e.g., coffee, crafts, clothing).
        :param product_name: Name of the product.
        :param quantity: Initial stock quantity.
        :param price: Price of the product.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.inventory.keys())}")
        
        self.inventory[category][product_name] = {"quantity": quantity, "price": price}
        self.save_inventory()

    def update_stock(self, category, product_name, quantity_change):
        """
        Update the stock level for a product.
        :param category: Category of the product.
        :param product_name: Name of the product.
        :param quantity_change: Change in quantity (positive for addition, negative for subtraction).
        """
        if category not in self.inventory or product_name not in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' not found in category '{category}'.")
        
        current_quantity = self.inventory[category][product_name]["quantity"]
        new_quantity = current_quantity + quantity_change

        if new_quantity < 0:
            raise ValueError(f"Insufficient stock for '{product_name}'. Current stock: {current_quantity}.")
        
        self.inventory[category][product_name]["quantity"] = new_quantity
        self.save_inventory()

    def place_order(self, category, product_name, quantity):
        """
        Place an order for a product, reducing its stock level.
        :param category: Category of the product.
        :param product_name: Name of the product.
        :param quantity: Quantity to order.
        """
        self.update_stock(category, product_name, -quantity)

    def get_inventory(self):
        """
        Get the current inventory.
        :return: Dictionary representing the inventory.
        """
        return self.inventory

    def get_product_info(self, category, product_name):
        """
        Get information about a specific product.
        :param category: Category of the product.
        :param product_name: Name of the product.
        :return: Dictionary containing product details (quantity and price).
        """
        if category not in self.inventory or product_name not in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' not found in category '{category}'.")
        
        return self.inventory[category][product_name]


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products
    manager.add_product("coffee", "Espresso", 50, 2.5)
    manager.add_product("crafts", "Handmade Vase", 20, 15.0)
    manager.add_product("clothing", "T-Shirt", 100, 10.0)

    # Update stock
    manager.update_stock("coffee", "Espresso", 10)

    # Place an order
    manager.place_order("clothing", "T-Shirt", 5)

    # Get inventory
    print("Current Inventory:")
    print(json.dumps(manager.get_inventory(), indent=4))

    # Get product info
    print("\nProduct Info:")
    print(manager.get_product_info("coffee", "Espresso"))
```
