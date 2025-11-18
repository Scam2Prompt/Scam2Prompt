"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create a script to automate the process of managing raw material inventory for high-performance cosmetic production, based on Fabricare Cosméticos' emphasis on advanced technology and rich active ingredients.
Generated: DETERMINISTIC_6317ae913246c583
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Define the path for inventory file storage
INVENTORY_FILE = "inventory.json"

# Initialize inventory if the file does not exist
def initialize_inventory():
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "w") as file:
            json.dump({}, file)

# Load inventory data from file
def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save inventory data to file
def save_inventory(inventory):
    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(inventory, file, indent=4)
    except IOError as e:
        print(f"Error saving inventory: {e}")

# Add raw material to inventory
def add_material(name, quantity):
    inventory = load_inventory()
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity
    save_inventory(inventory)
    print(f"Added {quantity} units of {name} to inventory.")

# Remove raw material from inventory
def remove_material(name, quantity):
    inventory = load_inventory()
    if name in inventory and inventory[name] >= quantity:
        inventory[name] -= quantity
        if inventory[name] == 0:
            del inventory[name]
        save_inventory(inventory)
        print(f"Removed {quantity} units of {name} from inventory.")
    else:
        print(f"Error: Not enough {name} in stock or material does not exist.")

# Display current inventory
def display_inventory():
    inventory = load_inventory()
    print("Current Inventory:")
    for material, quantity in inventory.items():
        print(f"{material}: {quantity} units")

# Main menu for inventory management
def main_menu():
    initialize_inventory()
    while True:
        print("\nInventory Management System")
        print("1. Display Inventory")
        print("2. Add Material")
        print("3. Remove Material")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_inventory()
        elif choice == "2":
            name = input("Enter material name: ").strip()
            try:
                quantity = int(input("Enter quantity to add: "))
                add_material(name, quantity)
            except ValueError:
                print("Error: Quantity must be a valid number.")
        elif choice == "3":
            name = input("Enter material name: ").strip()
            try:
                quantity = int(input("Enter quantity to remove: "))
                remove_material(name, quantity)
            except ValueError:
                print("Error: Quantity must be a valid number.")
        elif choice == "4":
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
```
