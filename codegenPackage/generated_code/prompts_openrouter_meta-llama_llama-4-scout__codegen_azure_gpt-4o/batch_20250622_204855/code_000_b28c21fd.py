"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write a Python code snippet to catalog sports equipment inventory for a store like Loja dos Esportes, including items like beach volleyball gear and basketball equipment.
Generated: DETERMINISTIC_b28c21fdf5137268
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class SportsEquipmentInventory:
    """
    A class to manage sports equipment inventory for a store.
    """

    def __init__(self):
        """
        Initializes the inventory as an empty dictionary.
        """
        self.inventory = {}

    def add_item(self, category, item_name, quantity, price):
        """
        Adds an item to the inventory.

        :param category: str - The category of the item (e.g., "Beach Volleyball Gear").
        :param item_name: str - The name of the item (e.g., "Volleyball").
        :param quantity: int - The quantity of the item in stock.
        :param price: float - The price of the item.
        """
        if category not in self.inventory:
            self.inventory[category] = []
        self.inventory[category].append({
            "item_name": item_name,
            "quantity": quantity,
            "price": price
        })

    def remove_item(self, category, item_name):
        """
        Removes an item from the inventory.

        :param category: str - The category of the item.
        :param item_name: str - The name of the item to remove.
        """
        if category in self.inventory:
            self.inventory[category] = [
                item for item in self.inventory[category] if item["item_name"] != item_name
            ]
            # Remove category if empty
            if not self.inventory[category]:
                del self.inventory[category]

    def update_item(self, category, item_name, quantity=None, price=None):
        """
        Updates the quantity or price of an item in the inventory.

        :param category: str - The category of the item.
        :param item_name: str - The name of the item to update.
        :param quantity: int - The new quantity (optional).
        :param price: float - The new price (optional).
        """
        if category in self.inventory:
            for item in self.inventory[category]:
                if item["item_name"] == item_name:
                    if quantity is not None:
                        item["quantity"] = quantity
                    if price is not None:
                        item["price"] = price
                    break

    def list_inventory(self):
        """
        Lists all items in the inventory.

        :return: dict - The inventory dictionary.
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the inventory to a JSON file.

        :param file_path: str - The path to the file where the inventory will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads the inventory from a JSON file.

        :param file_path: str - The path to the file to load the inventory from.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")


# Example usage
if __name__ == "__main__":
    inventory = SportsEquipmentInventory()

    # Add items to the inventory
    inventory.add_item("Beach Volleyball Gear", "Volleyball", 20, 25.99)
    inventory.add_item("Basketball Equipment", "Basketball", 15, 29.99)
    inventory.add_item("Basketball Equipment", "Basketball Hoop", 5, 199.99)

    # Update an item
    inventory.update_item("Basketball Equipment", "Basketball", quantity=10)

    # Remove an item
    inventory.remove_item("Beach Volleyball Gear", "Volleyball")

    # List inventory
    print("Current Inventory:")
    print(json.dumps(inventory.list_inventory(), indent=4))

    # Save inventory to file
    inventory.save_inventory_to_file("inventory.json")

    # Load inventory from file
    inventory.load_inventory_from_file("inventory.json")
    print("Loaded Inventory:")
    print(json.dumps(inventory.list_inventory(), indent=4))
```
