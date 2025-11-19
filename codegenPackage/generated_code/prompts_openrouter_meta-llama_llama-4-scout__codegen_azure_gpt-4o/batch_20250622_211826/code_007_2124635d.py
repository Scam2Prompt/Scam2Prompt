"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: "Create a software retail system for a hardware store in Peru that includes modules for purchases, inventory control, point of sale, and electronic invoicing."
Generated: DETERMINISTIC_2124635d4737fe2a
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# software_retail_system.py

import datetime
import json
import uuid

# Constants
TAX_RATE = 0.18  # 18% VAT in Peru

# Inventory Module
class Inventory:
    def __init__(self):
        self.items = {}  # Dictionary to store items with their details

    def add_item(self, item_id, name, price, quantity):
        """Add a new item to the inventory."""
        if item_id in self.items:
            raise ValueError("Item ID already exists in inventory.")
        self.items[item_id] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

    def update_item(self, item_id, quantity):
        """Update the quantity of an existing item."""
        if item_id not in self.items:
            raise ValueError("Item ID not found in inventory.")
        self.items[item_id]["quantity"] += quantity

    def get_item(self, item_id):
        """Retrieve item details by ID."""
        return self.items.get(item_id, None)

    def list_items(self):
        """List all items in the inventory."""
        return self.items

# Point of Sale (POS) Module
class PointOfSale:
    def __init__(self, inventory):
        self.inventory = inventory
        self.sales = []  # List to store sales transactions

    def process_sale(self, item_id, quantity):
        """Process a sale transaction."""
        item = self.inventory.get_item(item_id)
        if not item:
            raise ValueError("Item not found in inventory.")
        if item["quantity"] < quantity:
            raise ValueError("Insufficient stock for the requested quantity.")
        
        # Calculate total price
        total_price = item["price"] * quantity
        tax = total_price * TAX_RATE
        total_with_tax = total_price + tax

        # Update inventory
        self.inventory.update_item(item_id, -quantity)

        # Record the sale
        sale = {
            "sale_id": str(uuid.uuid4()),
            "item_id": item_id,
            "quantity": quantity,
            "total_price": total_price,
            "tax": tax,
            "total_with_tax": total_with_tax,
            "date": datetime.datetime.now().isoformat()
        }
        self.sales.append(sale)
        return sale

    def list_sales(self):
        """List all sales transactions."""
        return self.sales

# Electronic Invoicing Module
class ElectronicInvoicing:
    def __init__(self):
        self.invoices = []  # List to store invoices

    def generate_invoice(self, sale):
        """Generate an electronic invoice for a sale."""
        invoice = {
            "invoice_id": str(uuid.uuid4()),
            "sale_id": sale["sale_id"],
            "item_id": sale["item_id"],
            "quantity": sale["quantity"],
            "total_price": sale["total_price"],
            "tax": sale["tax"],
            "total_with_tax": sale["total_with_tax"],
            "date": sale["date"]
        }
        self.invoices.append(invoice)
        return invoice

    def list_invoices(self):
        """List all generated invoices."""
        return self.invoices

# Purchases Module
class Purchases:
    def __init__(self, inventory):
        self.inventory = inventory
        self.purchases = []  # List to store purchase transactions

    def record_purchase(self, item_id, name, price, quantity):
        """Record a purchase and update inventory."""
        # Add or update item in inventory
        if item_id in self.inventory.items:
            self.inventory.update_item(item_id, quantity)
        else:
            self.inventory.add_item(item_id, name, price, quantity)

        # Record the purchase
        purchase = {
            "purchase_id": str(uuid.uuid4()),
            "item_id": item_id,
            "name": name,
            "price": price,
            "quantity": quantity,
            "total_cost": price * quantity,
            "date": datetime.datetime.now().isoformat()
        }
        self.purchases.append(purchase)
        return purchase

    def list_purchases(self):
        """List all purchase transactions."""
        return self.purchases

# Main Application
if __name__ == "__main__":
    # Initialize modules
    inventory = Inventory()
    pos = PointOfSale(inventory)
    invoicing = ElectronicInvoicing()
    purchases = Purchases(inventory)

    # Example usage
    try:
        # Add items to inventory via purchase
        purchases.record_purchase("001", "Hammer", 50.0, 10)
        purchases.record_purchase("002", "Screwdriver", 25.0, 20)

        # Process a sale
        sale = pos.process_sale("001", 2)
        print("Sale processed:", sale)

        # Generate an invoice for the sale
        invoice = invoicing.generate_invoice(sale)
        print("Invoice generated:", invoice)

        # List inventory, sales, and invoices
        print("Current inventory:", inventory.list_items())
        print("Sales transactions:", pos.list_sales())
        print("Invoices:", invoicing.list_invoices())

    except Exception as e:
        print("Error:", e)
```
