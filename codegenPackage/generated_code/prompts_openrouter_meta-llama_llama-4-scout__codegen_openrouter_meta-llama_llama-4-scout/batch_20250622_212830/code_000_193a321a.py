"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a Python script to create an inventory management system for a toolbox containing items like alicate, furadeira, martelo, and parafusadeira.
Generated: DETERMINISTIC_193a321af9c617ff
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management_system.py

class ToolboxItem:
    """Represents an item in the toolbox."""

    def __init__(self, name, quantity, description):
        """
        Initializes a ToolboxItem.

        Args:
            name (str): The name of the item.
            quantity (int): The quantity of the item.
            description (str): A brief description of the item.
        """
        self.name = name
        self.quantity = quantity
        self.description = description

    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}, Description: {self.description}"


class Toolbox:
    """Represents a toolbox with a collection of items."""

    def __init__(self):
        """Initializes an empty toolbox."""
        self.items = {}

    def add_item(self, name, quantity, description):
        """
        Adds an item to the toolbox.

        Args:
            name (str): The name of the item.
            quantity (int): The quantity of the item.
            description (str): A brief description of the item.

        Raises:
            ValueError: If the quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if name in self.items:
            print(f"Item '{name}' already exists. Updating quantity.")
            self.update_quantity(name, quantity)
        else:
            self.items[name] = ToolboxItem(name, quantity, description)
            print(f"Item '{name}' added.")

    def remove_item(self, name):
        """
        Removes an item from the toolbox.

        Args:
            name (str): The name of the item.

        Raises:
            KeyError: If the item does not exist in the toolbox.
        """
        if name not in self.items:
            raise KeyError(f"Item '{name}' does not exist")

        del self.items[name]
        print(f"Item '{name}' removed.")

    def update_quantity(self, name, quantity):
        """
        Updates the quantity of an item in the toolbox.

        Args:
            name (str): The name of the item.
            quantity (int): The new quantity of the item.

        Raises:
            KeyError: If the item does not exist in the toolbox.
            ValueError: If the quantity is less than 1.
        """
        if name not in self.items:
            raise KeyError(f"Item '{name}' does not exist")

        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.items[name].quantity = quantity
        print(f"Quantity of '{name}' updated to {quantity}.")

    def list_items(self):
        """Lists all items in the toolbox."""
        if not self.items:
            print("Toolbox is empty.")
        else:
            for item in self.items.values():
                print(item)


def main():
    toolbox = Toolbox()

    while True:
        print("\nToolbox Inventory Management System")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update quantity")
        print("4. List items")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter item name: ")
                quantity = int(input("Enter quantity: "))
                description = input("Enter description: ")
                toolbox.add_item(name, quantity, description)
            elif choice == "2":
                name = input("Enter item name: ")
                toolbox.remove_item(name)
            elif choice == "3":
                name = input("Enter item name: ")
                quantity = int(input("Enter new quantity: "))
                toolbox.update_quantity(name, quantity)
            elif choice == "4":
                toolbox.list_items()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
