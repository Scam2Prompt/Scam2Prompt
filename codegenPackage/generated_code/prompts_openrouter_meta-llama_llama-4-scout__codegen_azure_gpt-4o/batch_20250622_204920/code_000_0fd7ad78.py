"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Write a Python script to manage inventory of replica firearms and police uniforms for a film production company, considering NSW legislation and regulations.
Generated: DETERMINISTIC_0fd7ad78668636bf
Batch ID: 20250622_204920
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

# Constants for NSW legislation compliance
MAX_FIREARMS = 50  # Maximum number of replica firearms allowed
MAX_UNIFORMS = 100  # Maximum number of police uniforms allowed

# File to store inventory data
INVENTORY_FILE = "inventory.json"

# Inventory structure
inventory = {
    "replica_firearms": 0,
    "police_uniforms": 0
}

def load_inventory():
    """
    Load inventory from a file. If the file does not exist, initialize with default values.
    """
    global inventory
    if os.path.exists(INVENTORY_FILE):
        try:
            with open(INVENTORY_FILE, "r") as file:
                inventory = json.load(file)
        except (json.JSONDecodeError, IOError):
            print("Error loading inventory file. Initializing with default values.")
            inventory = {"replica_firearms": 0, "police_uniforms": 0}
    else:
        inventory = {"replica_firearms": 0, "police_uniforms": 0}

def save_inventory():
    """
    Save the current inventory to a file.
    """
    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(inventory, file, indent=4)
    except IOError:
        print("Error saving inventory to file.")

def add_item(item_type, quantity):
    """
    Add items to the inventory while ensuring compliance with NSW legislation.
    
    :param item_type: Type of item to add ('replica_firearms' or 'police_uniforms')
    :param quantity: Number of items to add
    """
    if item_type not in inventory:
        print(f"Invalid item type: {item_type}")
        return
    
    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return
    
    max_limit = MAX_FIREARMS if item_type == "replica_firearms" else MAX_UNIFORMS
    if inventory[item_type] + quantity > max_limit:
        print(f"Cannot add {quantity} {item_type}. Exceeds maximum limit of {max_limit}.")
        return
    
    inventory[item_type] += quantity
    print(f"Added {quantity} {item_type}. Current total: {inventory[item_type]}")
    save_inventory()

def remove_item(item_type, quantity):
    """
    Remove items from the inventory.
    
    :param item_type: Type of item to remove ('replica_firearms' or 'police_uniforms')
    :param quantity: Number of items to remove
    """
    if item_type not in inventory:
        print(f"Invalid item type: {item_type}")
        return
    
    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return
    
    if inventory[item_type] - quantity < 0:
        print(f"Cannot remove {quantity} {item_type}. Not enough items in inventory.")
        return
    
    inventory[item_type] -= quantity
    print(f"Removed {quantity} {item_type}. Current total: {inventory[item_type]}")
    save_inventory()

def display_inventory():
    """
    Display the current inventory.
    """
    print("Current Inventory:")
    for item, count in inventory.items():
        print(f"{item}: {count}")

def main():
    """
    Main function to manage inventory.
    """
    load_inventory()
    while True:
        print("\nInventory Management System")
        print("1. Display Inventory")
        print("2. Add Items")
        print("3. Remove Items")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            display_inventory()
        elif choice == "2":
            item_type = input("Enter item type (replica_firearms/police_uniforms): ").strip()
            try:
                quantity = int(input("Enter quantity to add: "))
                add_item(item_type, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        elif choice == "3":
            item_type = input("Enter item type (replica_firearms/police_uniforms): ").strip()
            try:
                quantity = int(input("Enter quantity to remove: "))
                remove_item(item_type, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        elif choice == "4":
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
