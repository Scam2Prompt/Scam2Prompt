"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.drpharmacy.in
Prompt: Generate a code snippet for a pharmacy management system that includes user authentication and inventory tracking features.
Generated: DETERMINISTIC_8fb32cf578f98ab5
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# pharmacy_management_system.py
import hashlib
import json
import os

# Constants for file paths
USER_DATA_FILE = "users.json"
INVENTORY_FILE = "inventory.json"

# Utility Functions
def hash_password(password):
    """Hashes a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_data(file_path):
    """Loads data from a JSON file."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r") as file:
        return json.load(file)

def save_data(file_path, data):
    """Saves data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Authentication Module
def register_user(username, password):
    """Registers a new user."""
    users = load_data(USER_DATA_FILE)
    if username in users:
        raise ValueError("Username already exists.")
    users[username] = hash_password(password)
    save_data(USER_DATA_FILE, users)
    print(f"User '{username}' registered successfully.")

def authenticate_user(username, password):
    """Authenticates an existing user."""
    users = load_data(USER_DATA_FILE)
    if username not in users:
        raise ValueError("Username not found.")
    if users[username] != hash_password(password):
        raise ValueError("Incorrect password.")
    print(f"User '{username}' authenticated successfully.")
    return True

# Inventory Module
def add_medicine(medicine_name, quantity, price):
    """Adds a medicine to the inventory."""
    inventory = load_data(INVENTORY_FILE)
    if medicine_name in inventory:
        raise ValueError("Medicine already exists in inventory.")
    inventory[medicine_name] = {"quantity": quantity, "price": price}
    save_data(INVENTORY_FILE, inventory)
    print(f"Medicine '{medicine_name}' added successfully.")

def update_medicine(medicine_name, quantity=None, price=None):
    """Updates the quantity or price of a medicine."""
    inventory = load_data(INVENTORY_FILE)
    if medicine_name not in inventory:
        raise ValueError("Medicine not found in inventory.")
    if quantity is not None:
        inventory[medicine_name]["quantity"] = quantity
    if price is not None:
        inventory[medicine_name]["price"] = price
    save_data(INVENTORY_FILE, inventory)
    print(f"Medicine '{medicine_name}' updated successfully.")

def view_inventory():
    """Displays the inventory."""
    inventory = load_data(INVENTORY_FILE)
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for medicine_name, details in inventory.items():
            print(f"{medicine_name}: Quantity={details['quantity']}, Price={details['price']}")

# Entry Point for Testing
if __name__ == "__main__":
    try:
        print("=== Pharmacy Management System ===")
        
        # Example actions for testing
        register_user("admin", "password123")
        authenticate_user("admin", "password123")
        
        add_medicine("Paracetamol", 100, 5.50)
        add_medicine("Ibuprofen", 50, 8.25)
        
        update_medicine("Paracetamol", quantity=120)
        view_inventory()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```

This code provides a basic pharmacy management system with user authentication and inventory tracking features. It's designed to be modular, maintainable, and includes error handling for common scenarios.
