"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therammaninc.com
Prompt: Create a Python program to manage inventory for locking hubs across different vehicle brands (Dodge, Ford, Jeep, Toyota), using the product categories from The Ram Man website.
Generated: DETERMINISTIC_5bcad5ad1e0dcfe6
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory Management System for Locking Hubs Across Vehicle Brands

This program manages the inventory for locking hubs, categorized by vehicle brands.
Vehicle brands include Dodge, Ford, Jeep, and Toyota.
Each brand has a set of product categories obtained from The Ram Man website.

Key Features:
- Add new inventory items
- Update existing inventory items
- Remove inventory items
- View inventory details
"""

# Required Libraries
import sys

# Define Inventory Management System
class InventoryManager:
    def __init__(self):
        # Initialize an empty dictionary to store inventory
        self.inventory = {
            "Dodge": {},
            "Ford": {},
            "Jeep": {},
            "Toyota": {}
        }

    def add_item(self, brand, category, product_name, quantity):
        """
        Add a new item to the inventory.

        Parameters:
        brand (str): Vehicle brand (e.g., Dodge, Ford, Jeep, Toyota)
        category (str): Product category (e.g., "Locking Hubs", "Axle Parts")
        product_name (str): Name of the product
        quantity (int): Quantity of the product to add
        """
        if brand not in self.inventory:
            print(f"Error: {brand} is not a valid vehicle brand.")
            return

        if category not in self.inventory[brand]:
            self.inventory[brand][category] = {}

        # Add or update product in the category
        if product_name in self.inventory[brand][category]:
            self.inventory[brand][category][product_name] += quantity
        else:
            self.inventory[brand][category][product_name] = quantity

        print(f"Added {quantity} of '{product_name}' to {brand} - {category}.")

    def update_item(self, brand, category, product_name, quantity):
        """
        Update the quantity of an existing item.

        Parameters:
        brand (str): Vehicle brand
        category (str): Product category
        product_name (str): Name of the product
        quantity (int): New quantity of the product
        """
        try:
            if (
                brand in self.inventory
                and category in self.inventory[brand]
                and product_name in self.inventory[brand][category]
            ):
                self.inventory[brand][category][product_name] = quantity
                print(
                    f"Updated '{product_name}' quantity to {quantity} in {brand} - {category}."
                )
            else:
                print(
                    f"Error: Item '{product_name}' not found in {brand} - {category}."
                )
        except KeyError as e:
            print(f"Error occurred while updating item: {e}")

    def remove_item(self, brand, category, product_name):
        """
        Remove an item from the inventory.

        Parameters:
        brand (str): Vehicle brand
        category (str): Product category
        product_name (str): Name of the product
        """
        try:
            if (
                brand in self.inventory
                and category in self.inventory[brand]
                and product_name in self.inventory[brand][category]
            ):
                del self.inventory[brand][category][product_name]
                print(f"Removed '{product_name}' from {brand} - {category}.")
            else:
                print(f"Error: Item '{product_name}' not found in {brand} - {category}.")
        except KeyError as e:
            print(f"Error occurred while removing item: {e}")

    def view_inventory(self):
        """
        Display the current inventory details.
        """
        print("\nCurrent Inventory:")
        for brand, categories in self.inventory.items():
            print(f"\nBrand: {brand}")
            for category, products in categories.items():
                print(f"  Category: {category}")
                for product_name, quantity in products.items():
                    print(f"    {product_name}: {quantity}")

# Main Program
def main():
    manager = InventoryManager()

    # Sample operations
    try:
        manager.add_item("Ford", "Locking Hubs", "Premium Locking Hub", 10)
        manager.add_item("Jeep", "Axle Parts", "Heavy Duty Axle", 5)
        manager.update_item("Ford", "Locking Hubs", "Premium Locking Hub", 15)
        manager.remove_item("Jeep", "Axle Parts", "Heavy Duty Axle")
        manager.view_inventory()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# Run the program
if __name__ == "__main__":
    main()
```
