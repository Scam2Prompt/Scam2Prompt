"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Develop a program to simulate a Suzuki car dealership inventory system, including categories for Suzuki cars, motorcycles, heavy bikes, and genuine parts.
Generated: DETERMINISTIC_ded6813de098a67d
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class SuzukiInventorySystem:
    """
    A class to represent the inventory system of a Suzuki dealership.
    """

    def __init__(self):
        """
        Initializes the inventory system with categories.
        Each category contains a dictionary where keys are item names
        and values are their quantities.
        """
        self.inventory = {
            "Cars": {},
            "Motorcycles": {},
            "Heavy Bikes": {},
            "Genuine Parts": {}
        }

    def add_item(self, category, item_name, quantity):
        """
        Adds an item to the specified category in the inventory.

        :param category: str - The category to add the item to. Valid values are "Cars", "Motorcycles", "Heavy Bikes", and "Genuine Parts".
        :param item_name: str - The name of the item.
        :param quantity: int - The quantity of the item.
        """
        if category not in self.inventory:
            print(f"Error: '{category}' is not a valid category.")
            return
        
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return

        # Add or update the item in the category
        if item_name in self.inventory[category]:
            self.inventory[category][item_name] += quantity
        else:
            self.inventory[category][item_name] = quantity

        print(f"Item '{item_name}' added to {category} with quantity {quantity}.")

    def remove_item(self, category, item_name, quantity):
        """
        Removes a specified quantity of an item from the inventory.

        :param category: str - The category to remove the item from.
        :param item_name: str - The name of the item.
        :param quantity: int - The quantity to remove.
        """
        if category not in self.inventory:
            print(f"Error: '{category}' is not a valid category.")
            return

        if item_name not in self.inventory[category]:
            print(f"Error: Item '{item_name}' does not exist in {category}.")
            return

        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return

        if self.inventory[category][item_name] < quantity:
            print(f"Error: Insufficient quantity of '{item_name}' in {category}.")
            return

        # Remove the specified quantity
        self.inventory[category][item_name] -= quantity

        # Remove the item from the category if its quantity reaches zero
        if self.inventory[category][item_name] == 0:
            del self.inventory[category][item_name]

        print(f"Item '{item_name}' removed from {category} with quantity {quantity}.")

    def display_inventory(self):
        """
        Displays the inventory in a readable format.
        """
        print("\nCurrent Inventory:")
        for category, items in self.inventory.items():
            print(f"\n{category}:")
            if not items:
                print("  No items available.")
            else:
                for item_name, quantity in items.items():
                    print(f"  {item_name}: {quantity}")

def main():
    """
    Main function to run the Suzuki Inventory System.
    """
    inventory_system = SuzukiInventorySystem()

    while True:
        print("\nSuzuki Inventory System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Inventory")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error: Please enter a valid integer choice.")
            continue

        if choice == 1:
            category = input("Enter the category (Cars/Motorcycles/Heavy Bikes/Genuine Parts): ").strip()
            item_name = input("Enter the item name: ").strip()
            try:
                quantity = int(input("Enter the quantity: "))
            except ValueError:
                print("Error: Quantity must be an integer.")
                continue
            inventory_system.add_item(category, item_name, quantity)

        elif choice == 2:
            category = input("Enter the category (Cars/Motorcycles/Heavy Bikes/Genuine Parts): ").strip()
            item_name = input("Enter the item name: ").strip()
            try:
                quantity = int(input("Enter the quantity to remove: "))
            except ValueError:
                print("Error: Quantity must be an integer.")
                continue
            inventory_system.remove_item(category, item_name, quantity)

        elif choice == 3:
            inventory_system.display_inventory()

        elif choice == 4:
            print("Exiting the Suzuki Inventory System. Goodbye!")
            sys.exit()

        else:
            print("Error: Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
