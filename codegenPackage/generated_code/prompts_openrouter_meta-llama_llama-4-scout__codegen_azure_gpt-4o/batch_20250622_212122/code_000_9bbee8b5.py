"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Write a Python script to manage inventory for a kitchen utensil store like Varejão das Louças in Pedreira-SP.
Generated: DETERMINISTIC_9bbee8b51ca2588f
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class InventoryManager:
    """
    A class to manage inventory for a kitchen utensil store.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the inventory manager with a file to store inventory data.
        :param inventory_file: Path to the inventory file (default: inventory.json)
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self._load_inventory()

    def _load_inventory(self):
        """
        Load inventory data from the file. If the file doesn't exist, initialize an empty inventory.
        """
        if os.path.exists(self.inventory_file):
            try:
                with open(self.inventory_file, "r") as file:
                    self.inventory = json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading inventory file. Initializing empty inventory.")
                self.inventory = {}
        else:
            self.inventory = {}

    def _save_inventory(self):
        """
        Save the current inventory data to the file.
        """
        try:
            with open(self.inventory_file, "w") as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory file: {e}")

    def add_item(self, item_name, quantity, price):
        """
        Add a new item to the inventory or update an existing item.
        :param item_name: Name of the item
        :param quantity: Quantity of the item
        :param price: Price of the item
        """
        if item_name in self.inventory:
            self.inventory[item_name]["quantity"] += quantity
            self.inventory[item_name]["price"] = price
        else:
            self.inventory[item_name] = {"quantity": quantity, "price": price}
        self._save_inventory()
        print(f"Item '{item_name}' added/updated successfully.")

    def remove_item(self, item_name):
        """
        Remove an item from the inventory.
        :param item_name: Name of the item to remove
        """
        if item_name in self.inventory:
            del self.inventory[item_name]
            self._save_inventory()
            print(f"Item '{item_name}' removed successfully.")
        else:
            print(f"Item '{item_name}' not found in inventory.")

    def view_inventory(self):
        """
        Display the current inventory.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item_name, details in self.inventory.items():
                print(f" - {item_name}: Quantity = {details['quantity']}, Price = ${details['price']:.2f}")

    def search_item(self, item_name):
        """
        Search for an item in the inventory.
        :param item_name: Name of the item to search for
        """
        if item_name in self.inventory:
            details = self.inventory[item_name]
            print(f"Item found: {item_name} - Quantity = {details['quantity']}, Price = ${details['price']:.2f}")
        else:
            print(f"Item '{item_name}' not found in inventory.")

def main():
    """
    Main function to interact with the inventory manager.
    """
    manager = InventoryManager()

    while True:
        print("\nKitchen Utensil Store Inventory Management")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Search Item")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.view_inventory()
        elif choice == "2":
            item_name = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                manager.add_item(item_name, quantity, price)
            except ValueError:
                print("Invalid input. Quantity must be an integer and price must be a float.")
        elif choice == "3":
            item_name = input("Enter item name to remove: ")
            manager.remove_item(item_name)
        elif choice == "4":
            item_name = input("Enter item name to search: ")
            manager.search_item(item_name)
        elif choice == "5":
            print("Exiting inventory management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
