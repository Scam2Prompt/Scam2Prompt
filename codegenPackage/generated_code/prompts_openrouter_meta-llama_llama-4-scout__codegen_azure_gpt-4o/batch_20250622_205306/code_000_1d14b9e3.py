"""
Generated Code Metadata:
========================
Original URL: https://michelledoylegoldsmith.com
Prompt: Write a Python code to manage an e-commerce jewelry store's inventory, including categories like RINGS, EARRINGS, and PENDANTS.
Generated: DETERMINISTIC_1d14b9e30b4ef74d
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class JewelryStoreInventory:
    """
    A class to manage the inventory of an e-commerce jewelry store.
    Categories include RINGS, EARRINGS, and PENDANTS.
    """

    def __init__(self):
        """
        Initializes the inventory with empty categories.
        """
        self.inventory = {
            "RINGS": [],
            "EARRINGS": [],
            "PENDANTS": []
        }

    def add_item(self, category, item_name, quantity, price):
        """
        Adds a new item to the inventory.

        :param category: The category of the item (RINGS, EARRINGS, PENDANTS).
        :param item_name: The name of the item.
        :param quantity: The quantity of the item.
        :param price: The price of the item.
        :raises ValueError: If the category is invalid or quantity/price is negative.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are RINGS, EARRINGS, PENDANTS.")
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")

        self.inventory[category].append({
            "item_name": item_name,
            "quantity": quantity,
            "price": price
        })

    def remove_item(self, category, item_name):
        """
        Removes an item from the inventory.

        :param category: The category of the item.
        :param item_name: The name of the item to remove.
        :raises ValueError: If the category is invalid or the item is not found.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are RINGS, EARRINGS, PENDANTS.")

        for item in self.inventory[category]:
            if item["item_name"] == item_name:
                self.inventory[category].remove(item)
                return

        raise ValueError(f"Item '{item_name}' not found in category '{category}'.")

    def update_item(self, category, item_name, quantity=None, price=None):
        """
        Updates the quantity and/or price of an item in the inventory.

        :param category: The category of the item.
        :param item_name: The name of the item to update.
        :param quantity: The new quantity (optional).
        :param price: The new price (optional).
        :raises ValueError: If the category is invalid or the item is not found.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are RINGS, EARRINGS, PENDANTS.")

        for item in self.inventory[category]:
            if item["item_name"] == item_name:
                if quantity is not None:
                    if quantity < 0:
                        raise ValueError("Quantity must be non-negative.")
                    item["quantity"] = quantity
                if price is not None:
                    if price < 0:
                        raise ValueError("Price must be non-negative.")
                    item["price"] = price
                return

        raise ValueError(f"Item '{item_name}' not found in category '{category}'.")

    def view_inventory(self):
        """
        Returns the current inventory as a JSON string.

        :return: A JSON string representation of the inventory.
        """
        return json.dumps(self.inventory, indent=4)

    def search_item(self, category, item_name):
        """
        Searches for an item in the inventory.

        :param category: The category of the item.
        :param item_name: The name of the item to search for.
        :return: The item details if found, otherwise None.
        :raises ValueError: If the category is invalid.
        """
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are RINGS, EARRINGS, PENDANTS.")

        for item in self.inventory[category]:
            if item["item_name"] == item_name:
                return item

        return None


# Example usage
if __name__ == "__main__":
    try:
        store = JewelryStoreInventory()

        # Add items
        store.add_item("RINGS", "Gold Ring", 10, 299.99)
        store.add_item("EARRINGS", "Diamond Earrings", 5, 499.99)
        store.add_item("PENDANTS", "Silver Pendant", 20, 99.99)

        # View inventory
        print("Current Inventory:")
        print(store.view_inventory())

        # Update item
        store.update_item("RINGS", "Gold Ring", quantity=8, price=279.99)

        # Search for an item
        print("\nSearching for 'Gold Ring' in RINGS:")
        print(store.search_item("RINGS", "Gold Ring"))

        # Remove an item
        store.remove_item("PENDANTS", "Silver Pendant")

        # View inventory after removal
        print("\nInventory after removal:")
        print(store.view_inventory())

    except ValueError as e:
        print(f"Error: {e}")
```
