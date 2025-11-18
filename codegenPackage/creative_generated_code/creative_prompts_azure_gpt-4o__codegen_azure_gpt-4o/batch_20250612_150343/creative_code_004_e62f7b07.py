"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Write a script to manage inventory for a glass installation company, tracking glass types (tempered, laminated), thickness, and associated hardware like roldanas and stainless steel fittings.
Generated: DETERMINISTIC_e62f7b073ca77245
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory Management System for a Glass Installation Company

Tracks glass types, thickness, and associated hardware like roldanas and stainless steel fittings.
"""

import sys

class InventoryItem:
    """Represents a single inventory item."""
    def __init__(self, name, category, quantity, details):
        """
        Initializes an InventoryItem object.

        :param name: Name of the item (e.g., "Tempered Glass 8mm").
        :param category: Category of the item (e.g., "Glass", "Hardware").
        :param quantity: Quantity available in stock.
        :param details: Additional details about the item.
        """
        self.name = name
        self.category = category
        self.quantity = quantity
        self.details = details

    def __str__(self):
        """String representation of the inventory item."""
        return f"{self.name} ({self.category}) - Quantity: {self.quantity}, Details: {self.details}"


class InventoryManager:
    """Manages the inventory for the glass installation company."""
    def __init__(self):
        """Initializes the InventoryManager with an empty inventory."""
        self.inventory = []

    def add_item(self, name, category, quantity, details):
        """
        Adds a new item to the inventory.

        :param name: Name of the item.
        :param category: Category of the item.
        :param quantity: Quantity of the item.
        :param details: Additional details about the item.
        """
        new_item = InventoryItem(name, category, quantity, details)
        self.inventory.append(new_item)
        print(f"Item added: {new_item}")

    def remove_item(self, name):
        """
        Removes an item from the inventory by name.

        :param name: Name of the item to remove.
        """
        for item in self.inventory:
            if item.name == name:
                self.inventory.remove(item)
                print(f"Item removed: {item}")
                return
        print(f"Item not found: {name}")

    def update_quantity(self, name, new_quantity):
        """
        Updates the quantity of an item in the inventory.

        :param name: Name of the item to update.
        :param new_quantity: New quantity for the item.
        """
        for item in self.inventory:
            if item.name == name:
                item.quantity = new_quantity
                print(f"Updated item: {item}")
                return
        print(f"Item not found: {name}")

    def list_inventory(self):
        """Lists all items currently in the inventory."""
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current inventory:")
            for item in self.inventory:
                print(item)


def main():
    """Main function to manage inventory."""
    manager = InventoryManager()

    while True:
        try:
            print("\nInventory Management System:")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Update Quantity")
            print("4. List Inventory")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                # Add item
                name = input("Enter item name: ").strip()
                category = input("Enter item category (Glass/Hardware): ").strip()
                quantity = int(input("Enter item quantity: ").strip())
                details = input("Enter item details: ").strip()
                manager.add_item(name, category, quantity, details)

            elif choice == "2":
                # Remove item
                name = input("Enter the name of the item to remove: ").strip()
                manager.remove_item(name)

            elif choice == "3":
                # Update quantity
                name = input("Enter the name of the item to update: ").strip()
                new_quantity = int(input("Enter the new quantity: ").strip())
                manager.update_quantity(name, new_quantity)

            elif choice == "4":
                # List inventory
                manager.list_inventory()

            elif choice == "5":
                # Exit
                print("Exiting Inventory Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter the correct data type.")
        except Exception as e:
            print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
