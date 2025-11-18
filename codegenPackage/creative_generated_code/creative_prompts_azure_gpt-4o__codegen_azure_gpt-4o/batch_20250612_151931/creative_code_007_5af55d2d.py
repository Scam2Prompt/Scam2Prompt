"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://noymi.in
Prompt: Develop a script to manage inventory and pricing for an e-commerce store selling items like Noymi 3-in-1 Shaver and Beard Trimmer for Men | ET-175.
Generated: DETERMINISTIC_5af55d2dba4067ae
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ECommerceInventoryManager:
    def __init__(self):
        """
        Initialize an inventory manager with an empty inventory dictionary.
        Each item is stored with details such as name, quantity, and price.
        """
        self.inventory = {}

    def add_item(self, item_id, name, quantity, price):
        """
        Add a new item to the inventory.

        :param item_id: Unique identifier for the item
        :param name: Name of the item
        :param quantity: Quantity of the item in stock
        :param price: Price of the item
        """
        if item_id in self.inventory:
            raise ValueError("Item ID already exists in the inventory.")
        self.inventory[item_id] = {
            "name": name,
            "quantity": quantity,
            "price": price
        }
        print(f"Item '{name}' added successfully.")

    def update_quantity(self, item_id, quantity):
        """
        Update the quantity of an existing item.

        :param item_id: Unique identifier for the item
        :param quantity: New quantity to set
        """
        if item_id not in self.inventory:
            raise KeyError("Item ID not found in the inventory.")
        self.inventory[item_id]["quantity"] = quantity
        print(f"Quantity updated successfully for item '{self.inventory[item_id]['name']}'.")

    def update_price(self, item_id, price):
        """
        Update the price of an existing item.

        :param item_id: Unique identifier for the item
        :param price: New price to set
        """
        if item_id not in self.inventory:
            raise KeyError("Item ID not found in the inventory.")
        self.inventory[item_id]["price"] = price
        print(f"Price updated successfully for item '{self.inventory[item_id]['name']}'.")

    def view_inventory(self):
        """
        View the current inventory.

        :return: A JSON-formatted string representing the inventory.
        """
        return json.dumps(self.inventory, indent=4)

    def delete_item(self, item_id):
        """
        Delete an item from the inventory.

        :param item_id: Unique identifier for the item
        """
        if item_id not in self.inventory:
            raise KeyError("Item ID not found in the inventory.")
        deleted_item = self.inventory.pop(item_id)
        print(f"Item '{deleted_item['name']}' deleted successfully.")

    def get_item_details(self, item_id):
        """
        Retrieve details of a specific item.

        :param item_id: Unique identifier for the item
        :return: A dictionary containing item details.
        """
        if item_id not in self.inventory:
            raise KeyError("Item ID not found in the inventory.")
        return self.inventory[item_id]


# Example usage
if __name__ == "__main__":
    try:
        manager = ECommerceInventoryManager()

        # Add items to the inventory
        manager.add_item("ET-175", "Noymi 3-in-1 Shaver and Beard Trimmer for Men | ET-175", 50, 19.99)
        manager.add_item("ET-200", "Electric Toothbrush | ET-200", 30, 25.99)

        # View inventory
        print("Current Inventory:")
        print(manager.view_inventory())

        # Update quantity and price
        manager.update_quantity("ET-175", 45)
        manager.update_price("ET-200", 24.99)

        # View updated inventory
        print("\nUpdated Inventory:")
        print(manager.view_inventory())

        # Get item details
        print("\nDetails for ET-175:")
        print(manager.get_item_details("ET-175"))

        # Delete an item
        manager.delete_item("ET-200")

        # View final inventory
        print("\nFinal Inventory:")
        print(manager.view_inventory())

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
