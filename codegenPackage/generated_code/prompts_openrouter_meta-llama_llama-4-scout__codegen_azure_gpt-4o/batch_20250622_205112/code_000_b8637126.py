"""
Generated Code Metadata:
========================
Original URL: https://opticalize.com
Prompt: Write a Python script to manage an inventory of eyeglasses and sunglasses for an optical store like Optic Alizé, including frames for men, women, and children.
Generated: DETERMINISTIC_b8637126d51c9bd7
Batch ID: 20250622_205112
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
    A class to manage the inventory of eyeglasses and sunglasses for an optical store.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the inventory manager with a file to store inventory data.
        :param inventory_file: Path to the inventory file (default: 'inventory.json').
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Load inventory data from the file. If the file doesn't exist, initialize an empty inventory.
        :return: Dictionary representing the inventory.
        """
        try:
            with open(self.inventory_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"men": [], "women": [], "children": []}
        except json.JSONDecodeError:
            print("Error: Inventory file is corrupted. Initializing empty inventory.")
            return {"men": [], "women": [], "children": []}

    def save_inventory(self):
        """
        Save the current inventory to the file.
        """
        try:
            with open(self.inventory_file, "w") as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save inventory. {e}")

    def add_item(self, category, name, type_, price, quantity):
        """
        Add a new item to the inventory.
        :param category: Category of the item ('men', 'women', 'children').
        :param name: Name of the item.
        :param type_: Type of the item ('eyeglasses' or 'sunglasses').
        :param price: Price of the item.
        :param quantity: Quantity of the item.
        """
        if category not in self.inventory:
            print(f"Error: Invalid category '{category}'. Valid categories are 'men', 'women', 'children'.")
            return

        item = {
            "name": name,
            "type": type_,
            "price": price,
            "quantity": quantity
        }
        self.inventory[category].append(item)
        self.save_inventory()
        print(f"Item '{name}' added to {category} category.")

    def remove_item(self, category, name):
        """
        Remove an item from the inventory.
        :param category: Category of the item ('men', 'women', 'children').
        :param name: Name of the item to remove.
        """
        if category not in self.inventory:
            print(f"Error: Invalid category '{category}'. Valid categories are 'men', 'women', 'children'.")
            return

        for item in self.inventory[category]:
            if item["name"] == name:
                self.inventory[category].remove(item)
                self.save_inventory()
                print(f"Item '{name}' removed from {category} category.")
                return

        print(f"Error: Item '{name}' not found in {category} category.")

    def update_item(self, category, name, **kwargs):
        """
        Update the details of an item in the inventory.
        :param category: Category of the item ('men', 'women', 'children').
        :param name: Name of the item to update.
        :param kwargs: Fields to update (e.g., price=100, quantity=50).
        """
        if category not in self.inventory:
            print(f"Error: Invalid category '{category}'. Valid categories are 'men', 'women', 'children'.")
            return

        for item in self.inventory[category]:
            if item["name"] == name:
                item.update(kwargs)
                self.save_inventory()
                print(f"Item '{name}' updated in {category} category.")
                return

        print(f"Error: Item '{name}' not found in {category} category.")

    def view_inventory(self):
        """
        Display the current inventory.
        """
        print("Current Inventory:")
        for category, items in self.inventory.items():
            print(f"\nCategory: {category.capitalize()}")
            for item in items:
                print(f"  Name: {item['name']}, Type: {item['type']}, Price: ${item['price']}, Quantity: {item['quantity']}")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items
    manager.add_item("men", "Classic Frame", "eyeglasses", 120.00, 10)
    manager.add_item("women", "Stylish Sunglasses", "sunglasses", 150.00, 5)
    manager.add_item("children", "Kids Frame", "eyeglasses", 80.00, 20)

    # View inventory
    manager.view_inventory()

    # Update an item
    manager.update_item("men", "Classic Frame", price=130.00, quantity=8)

    # Remove an item
    manager.remove_item("women", "Stylish Sunglasses")

    # View inventory again
    manager.view_inventory()
```
