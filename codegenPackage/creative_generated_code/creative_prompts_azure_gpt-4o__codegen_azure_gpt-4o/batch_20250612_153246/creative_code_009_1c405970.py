"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demirsoft.com
Prompt: Develop a POS system for a cafe using DemirSoft's "Cafe Restoran Masa Adisyon Takip Sistemi," including table management and receipt generation.
Generated: DETERMINISTIC_1c405970a17ff93b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a POS system for a cafe that includes table management and receipt generation. It follows best practices and is well-commented.

```python
import datetime
import json

class POSSystem:
    def __init__(self):
        # Initialize tables and menu items
        self.tables = {}
        self.menu = {}
        self.receipts = []
    
    def add_table(self, table_id):
        """Add a new table to the system."""
        if table_id in self.tables:
            raise ValueError(f"Table {table_id} already exists.")
        self.tables[table_id] = {"orders": [], "status": "available"}
    
    def add_menu_item(self, item_name, price):
        """Add a new menu item with a price."""
        if item_name in self.menu:
            raise ValueError(f"Menu item {item_name} already exists.")
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        self.menu[item_name] = price
    
    def place_order(self, table_id, item_name, quantity):
        """Place an order for a table."""
        if table_id not in self.tables:
            raise ValueError(f"Table {table_id} does not exist.")
        if item_name not in self.menu:
            raise ValueError(f"Menu item {item_name} does not exist.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        
        order = {
            "item_name": item_name,
            "quantity": quantity,
            "price": self.menu[item_name] * quantity
        }
        self.tables[table_id]["orders"].append(order)
        self.tables[table_id]["status"] = "occupied"
    
    def generate_receipt(self, table_id):
        """Generate a receipt for a specific table."""
        if table_id not in self.tables:
            raise ValueError(f"Table {table_id} does not exist.")
        if not self.tables[table_id]["orders"]:
            raise ValueError(f"No orders placed for table {table_id}.")
        
        receipt = {
            "table_id": table_id,
            "orders": self.tables[table_id]["orders"],
            "total_price": sum(order["price"] for order in self.tables[table_id]["orders"]),
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.receipts.append(receipt)
        self.tables[table_id]["orders"] = []  # Clear orders after receipt generation
        self.tables[table_id]["status"] = "available"
        return receipt
    
    def print_receipt(self, receipt):
        """Print the receipt in a human-readable format."""
        print(f"Receipt for Table {receipt['table_id']} - {receipt['timestamp']}")
        print("-" * 40)
        for order in receipt["orders"]:
            print(f"{order['item_name']} x {order['quantity']} - ${order['price']:.2f}")
        print("-" * 40)
        print(f"Total: ${receipt['total_price']:.2f}")
        print("-" * 40)
    
    def save_receipts_to_file(self, filename):
        """Save all receipts to a JSON file."""
        try:
            with open(filename, "w") as file:
                json.dump(self.receipts, file, indent=4)
        except IOError as e:
            print(f"Error saving receipts to file: {e}")
    
    def load_receipts_from_file(self, filename):
        """Load receipts from a JSON file."""
        try:
            with open(filename, "r") as file:
                self.receipts = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading receipts from file: {e}")

# Example usage
if __name__ == "__main__":
    pos = POSSystem()

    # Adding tables and menu items
    pos.add_table(1)
    pos.add_table(2)
    pos.add_menu_item("Coffee", 3.5)
    pos.add_menu_item("Sandwich", 5.0)
    
    # Placing orders
    pos.place_order(1, "Coffee", 2)
    pos.place_order(1, "Sandwich", 1)
    
    # Generating and printing receipt
    receipt = pos.generate_receipt(1)
    pos.print_receipt(receipt)
    
    # Saving receipts to file
    pos.save_receipts_to_file("receipts.json")
    
    # Loading receipts from file
    pos.load_receipts_from_file("receipts.json")
```

This code is designed for production readiness and adheres to best practices. Let me know if you need modifications or enhancements!
