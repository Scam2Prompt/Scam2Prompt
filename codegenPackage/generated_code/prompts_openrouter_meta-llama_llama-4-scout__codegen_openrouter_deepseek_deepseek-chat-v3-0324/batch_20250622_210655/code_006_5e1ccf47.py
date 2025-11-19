"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: "Create a customized software solution with easy-to-use interface and update features for a small business."
Generated: DETERMINISTIC_5e1ccf478ef53691
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Small Business Management System

```python
"""
Small Business Management System
A customizable solution for small businesses with inventory, sales, and customer management.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union

class Database:
    """Handles data persistence for the application"""
    
    def __init__(self, db_file: str = "business_data.json"):
        self.db_file = db_file
        self.data = self._load_data()
        
    def _load_data(self) -> Dict:
        """Load data from JSON file or initialize empty structure"""
        try:
            if os.path.exists(self.db_file):
                with open(self.db_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading database: {e}")
            
        return {
            "inventory": [],
            "customers": [],
            "sales": [],
            "settings": {}
        }
        
    def save(self) -> bool:
        """Save data to JSON file"""
        try:
            with open(self.db_file, 'w') as f:
                json.dump(self.data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving database: {e}")
            return False
            
    def get_inventory(self) -> List[Dict]:
        """Get all inventory items"""
        return self.data.get("inventory", [])
        
    def add_inventory_item(self, item: Dict) -> bool:
        """Add new inventory item"""
        try:
            self.data["inventory"].append(item)
            return self.save()
        except Exception as e:
            print(f"Error adding inventory item: {e}")
            return False
            
    # Similar methods for customers, sales, etc.
    # ...

class BusinessManager:
    """Core business logic and operations"""
    
    def __init__(self, db: Database):
        self.db = db
        
    def add_product(self, name: str, price: float, quantity: int, 
                   description: str = "") -> bool:
        """Add a new product to inventory"""
        if not name or price <= 0 or quantity < 0:
            return False
            
        product = {
            "id": self._generate_id(),
            "name": name,
            "price": price,
            "quantity": quantity,
            "description": description,
            "created_at": str(datetime.now())
        }
        
        return self.db.add_inventory_item(product)
        
    def _generate_id(self) -> str:
        """Generate a unique ID for new records"""
        return str(datetime.now().timestamp()).replace('.', '')
        
    # Additional business methods...
    # ...

class UserInterface:
    """Command-line interface for the system"""
    
    def __init__(self, manager: BusinessManager):
        self.manager = manager
        self.running = True
        
    def display_menu(self):
        """Show main menu options"""
        print("\nSmall Business Management System")
        print("1. Inventory Management")
        print("2. Sales")
        print("3. Customers")
        print("4. Reports")
        print("5. Settings")
        print("6. Exit")
        
    def handle_input(self, choice: str):
        """Process user menu selection"""
        if choice == "1":
            self.inventory_menu()
        elif choice == "6":
            self.running = False
        else:
            print("Feature coming soon!")
            
    def inventory_menu(self):
        """Show inventory management options"""
        print("\nInventory Management")
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Back to Main Menu")
        
        choice = input("Select an option: ")
        if choice == "1":
            self.view_inventory()
        elif choice == "2":
            self.add_product_ui()
            
    def view_inventory(self):
        """Display current inventory"""
        inventory = self.manager.db.get_inventory()
        if not inventory:
            print("No inventory items found.")
            return
            
        print("\nCurrent Inventory:")
        for item in inventory:
            print(f"{item['name']} - ${item['price']} ({item['quantity']} in stock)")
            
    def add_product_ui(self):
        """Gather product info from user"""
        print("\nAdd New Product")
        name = input("Product name: ")
        price = input("Price: ")
        quantity = input("Quantity: ")
        
        try:
            price = float(price)
            quantity = int(quantity)
            if self.manager.add_product(name, price, quantity):
                print("Product added successfully!")
            else:
                print("Failed to add product.")
        except ValueError:
            print("Invalid price or quantity format.")
            
    def run(self):
        """Main application loop"""
        while self.running:
            self.display_menu()
            choice = input("Select an option: ")
            self.handle_input(choice)
            
        print("Thank you for using Small Business Management System!")

if __name__ == "__main__":
    # Initialize and run the application
    db = Database()
    manager = BusinessManager(db)
    ui = UserInterface(manager)
    ui.run()
```
