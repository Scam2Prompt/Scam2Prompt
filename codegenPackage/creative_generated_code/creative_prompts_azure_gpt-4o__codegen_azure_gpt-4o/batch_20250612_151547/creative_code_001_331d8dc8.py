"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Generate a script for managing warehouse inventory tailored to Fealty Worldwide's warehousing services, including storage, distribution, and pre-positioning of products.
Generated: DETERMINISTIC_331d8dc8b3161d9e
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Warehouse Inventory Management System for Fealty Worldwide
-----------------------------------------------------------
This script provides functionalities for managing warehouse inventory,
including adding products, updating product quantities, tracking distribution,
and pre-positioning items.
"""

import json
import os

# Define the path for the inventory file
INVENTORY_FILE = "warehouse_inventory.json"

# Initialize inventory if the file does not exist
def initialize_inventory():
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'w') as file:
            json.dump({}, file)

# Load inventory from file
def load_inventory():
    try:
        with open(INVENTORY_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save inventory to file
def save_inventory(inventory):
    try:
        with open(INVENTORY_FILE, 'w') as file:
            json.dump(inventory, file, indent=4)
    except Exception as e:
        print(f"Error saving inventory: {e}")

# Add a new product to the inventory
def add_product(product_id, name, quantity, location):
    inventory = load_inventory()
    if product_id in inventory:
        print("Error: Product ID already exists in inventory.")
        return False
    inventory[product_id] = {
        "name": name,
        "quantity": quantity,
        "location": location
    }
    save_inventory(inventory)
    print("Product added successfully.")
    return True

# Update the quantity of an existing product
def update_quantity(product_id, quantity_change):
    inventory = load_inventory()
    if product_id not in inventory:
        print("Error: Product ID not found in inventory.")
        return False
    inventory[product_id]["quantity"] += quantity_change
    if inventory[product_id]["quantity"] < 0:
        print("Error: Insufficient stock.")
        inventory[product_id]["quantity"] -= quantity_change  # Rollback
        return False
    save_inventory(inventory)
    print("Quantity updated successfully.")
    return True

# Remove a product from the inventory
def remove_product(product_id):
    inventory = load_inventory()
    if product_id not in inventory:
        print("Error: Product ID not found in inventory.")
        return False
    del inventory[product_id]
    save_inventory(inventory)
    print("Product removed successfully.")
    return True

# List all products in the inventory
def list_inventory():
    inventory = load_inventory()
    if not inventory:
        print("Inventory is empty.")
        return
    print("{:<15} {:<20} {:<10} {:<20}".format("Product ID", "Name", "Quantity", "Location"))
    print("-" * 70)
    for product_id, details in inventory.items():
        print("{:<15} {:<20} {:<10} {:<20}".format(
            product_id, details["name"], details["quantity"], details["location"]
        ))

# Main menu for warehouse operations
def main_menu():
    initialize_inventory()
    while True:
        print("\nWarehouse Inventory Management")
        print("1. Add Product")
        print("2. Update Quantity")
        print("3. Remove Product")
        print("4. List Inventory")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            try:
                quantity = int(input("Enter Quantity: "))
            except ValueError:
                print("Invalid quantity. Must be an integer.")
                continue
            location = input("Enter Location: ")
            add_product(product_id, name, quantity, location)
        elif choice == 2:
            product_id = input("Enter Product ID: ")
            try:
                quantity_change = int(input("Enter Quantity Change (+/-): "))
            except ValueError:
                print("Invalid quantity change. Must be an integer.")
                continue
            update_quantity(product_id, quantity_change)
        elif choice == 3:
            product_id = input("Enter Product ID: ")
            remove_product(product_id)
        elif choice == 4:
            list_inventory()
        elif choice == 5:
            print("Exiting Warehouse Inventory Management System.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

# Entry point for the script
if __name__ == "__main__":
    main_menu()
```
