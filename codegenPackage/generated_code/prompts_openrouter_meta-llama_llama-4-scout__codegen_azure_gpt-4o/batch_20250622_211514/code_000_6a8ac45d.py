"""
Generated Code Metadata:
========================
Original URL: https://therammaninc.com
Prompt: "Write a Python script to manage inventory for Dodge RAM locking hubs and brake kits."
Generated: DETERMINISTIC_6a8ac45dbe86fa5e
Batch ID: 20250622_211514
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

# File to store inventory data
INVENTORY_FILE = "inventory.json"

# Initialize inventory data
def initialize_inventory():
    """Initialize inventory with default values if the file doesn't exist."""
    if not os.path.exists(INVENTORY_FILE):
        inventory = {
            "locking_hubs": {"quantity": 0, "price_per_unit": 0.0},
            "brake_kits": {"quantity": 0, "price_per_unit": 0.0},
        }
        save_inventory(inventory)

# Load inventory from file
def load_inventory():
    """Load inventory data from the JSON file."""
    try:
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error loading inventory file. Initializing default inventory.")
        initialize_inventory()
        return load_inventory()

# Save inventory to file
def save_inventory(inventory):
    """Save inventory data to the JSON file."""
    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(inventory, file, indent=4)
    except Exception as e:
        print(f"Error saving inventory: {e}")

# Display inventory
def display_inventory(inventory):
    """Display the current inventory."""
    print("\nCurrent Inventory:")
    for item, details in inventory.items():
        print(f"{item.capitalize()}: Quantity = {details['quantity']}, Price per Unit = ${details['price_per_unit']:.2f}")
    print()

# Update inventory
def update_inventory(inventory, item, quantity, price_per_unit):
    """Update the inventory for a specific item."""
    if item not in inventory:
        print(f"Error: '{item}' is not a valid inventory item.")
        return

    if quantity < 0 or price_per_unit < 0:
        print("Error: Quantity and price per unit must be non-negative.")
        return

    inventory[item]["quantity"] = quantity
    inventory[item]["price_per_unit"] = price_per_unit
    save_inventory(inventory)
    print(f"Inventory updated for {item}.")

# Main menu
def main_menu():
    """Display the main menu and handle user input."""
    initialize_inventory()
    inventory = load_inventory()

    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Update Inventory")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            display_inventory(inventory)
        elif choice == "2":
            item = input("Enter the item to update (locking_hubs/brake_kits): ").strip().lower()
            try:
                quantity = int(input("Enter the new quantity: "))
                price_per_unit = float(input("Enter the new price per unit: "))
                update_inventory(inventory, item, quantity, price_per_unit)
            except ValueError:
                print("Error: Invalid input. Quantity must be an integer and price must be a float.")
        elif choice == "3":
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main_menu()
```
