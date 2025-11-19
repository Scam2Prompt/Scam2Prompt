"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingoficecream.com
Prompt: Generate a Python script to simulate an ice cream truck inventory management system for a snow cone truck.
Generated: DETERMINISTIC_d5396b59319004f0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Ice Cream Truck Inventory Management System for a Snow Cone Truck
Author: [Your Name]
Date: [Today's Date]
Description: This script simulates an inventory management system for a snow cone truck,
allowing users to manage stock levels, view inventory, add or remove items, and track sales.
"""

# Import necessary modules
import sys

class SnowConeTruckInventory:
    def __init__(self):
        """
        Initializes the inventory management system with a default inventory.
        """
        self.inventory = {
            "Cherry": {"quantity": 50, "price": 2.50},
            "Blue Raspberry": {"quantity": 40, "price": 2.50},
            "Lemon": {"quantity": 30, "price": 2.50},
            "Grape": {"quantity": 25, "price": 2.50},
        }
        self.total_sales = 0.0

    def view_inventory(self):
        """
        Displays the current inventory with quantities and prices.
        """
        print("\nCurrent Inventory:")
        for flavor, details in self.inventory.items():
            print(f"{flavor}: {details['quantity']} available at ${details['price']:.2f} each")
        print(f"Total Sales: ${self.total_sales:.2f}")

    def add_stock(self, flavor, quantity, price):
        """
        Adds new stock to the inventory. If the flavor already exists, it updates the quantity and price.

        Parameters:
            flavor (str): The name of the snow cone flavor.
            quantity (int): The quantity to add.
            price (float): The price per unit.
        """
        if flavor in self.inventory:
            self.inventory[flavor]["quantity"] += quantity
            self.inventory[flavor]["price"] = price
            print(f"Updated stock for {flavor}.")
        else:
            self.inventory[flavor] = {"quantity": quantity, "price": price}
            print(f"Added new flavor {flavor} to inventory.")

    def remove_stock(self, flavor, quantity):
        """
        Removes stock from the inventory. If the quantity reaches zero, the flavor is removed.

        Parameters:
            flavor (str): The name of the snow cone flavor.
            quantity (int): The quantity to remove.
        """
        if flavor not in self.inventory:
            print(f"Flavor {flavor} not found in inventory.")
            return

        if self.inventory[flavor]["quantity"] < quantity:
            print(f"Insufficient stock to remove {quantity} {flavor} snow cones.")
            return

        self.inventory[flavor]["quantity"] -= quantity
        print(f"Removed {quantity} {flavor} snow cones from inventory.")

        # Remove flavor if quantity is zero
        if self.inventory[flavor]["quantity"] == 0:
            del self.inventory[flavor]
            print(f"{flavor} has been removed from inventory.")

    def sell_snow_cone(self, flavor, quantity):
        """
        Processes a sale and updates inventory and total sales.

        Parameters:
            flavor (str): The name of the snow cone flavor being sold.
            quantity (int): The quantity sold.
        """
        if flavor not in self.inventory:
            print(f"Flavor {flavor} not found in inventory.")
            return

        if self.inventory[flavor]["quantity"] < quantity:
            print(f"Insufficient stock to sell {quantity} {flavor} snow cones.")
            return

        self.inventory[flavor]["quantity"] -= quantity
        sale_amount = self.inventory[flavor]["price"] * quantity
        self.total_sales += sale_amount
        print(f"Sold {quantity} {flavor} snow cones for ${sale_amount:.2f}.")

        # Remove flavor if quantity is zero
        if self.inventory[flavor]["quantity"] == 0:
            del self.inventory[flavor]
            print(f"{flavor} has been removed from inventory.")

    def menu(self):
        """
        Displays the menu and handles user interactions.
        """
        while True:
            print("\n--- Snow Cone Truck Inventory Management ---")
            print("1. View Inventory")
            print("2. Add Stock")
            print("3. Remove Stock")
            print("4. Sell Snow Cone")
            print("5. Exit")
            choice = input("Enter your choice: ")

            try:
                if choice == "1":
                    self.view_inventory()
                elif choice == "2":
                    flavor = input("Enter flavor name: ")
                    quantity = int(input("Enter quantity: "))
                    price = float(input("Enter price per unit: "))
                    self.add_stock(flavor, quantity, price)
                elif choice == "3":
                    flavor = input("Enter flavor name: ")
                    quantity = int(input("Enter quantity to remove: "))
                    self.remove_stock(flavor, quantity)
                elif choice == "4":
                    flavor = input("Enter flavor name: ")
                    quantity = int(input("Enter quantity to sell: "))
                    self.sell_snow_cone(flavor, quantity)
                elif choice == "5":
                    print("Exiting the system. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter correct data types.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        inventory_system = SnowConeTruckInventory()
        inventory_system.menu()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
    except Exception as e:
        print(f"An error occurred while running the system: {e}")
        sys.exit(1)
```
