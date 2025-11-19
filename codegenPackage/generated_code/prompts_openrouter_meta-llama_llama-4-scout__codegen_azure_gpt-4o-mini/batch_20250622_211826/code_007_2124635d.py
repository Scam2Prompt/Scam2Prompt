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
# hardware_store.py

import json
from datetime import datetime

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        """Update the quantity of the item."""
        if self.quantity + amount < 0:
            raise ValueError("Insufficient stock to complete the operation.")
        self.quantity += amount

    def to_dict(self):
        """Convert the item to a dictionary for JSON serialization."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

class Inventory:
    """Class to manage the inventory of the hardware store."""
    
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        """Add a new item to the inventory."""
        if item.item_id in self.items:
            raise ValueError("Item already exists in inventory.")
        self.items[item.item_id] = item

    def update_item(self, item_id, quantity):
        """Update the quantity of an existing item."""
        if item_id not in self.items:
            raise ValueError("Item not found in inventory.")
        self.items[item_id].update_quantity(quantity)

    def get_item(self, item_id):
        """Retrieve an item from the inventory."""
        return self.items.get(item_id)

    def list_items(self):
        """List all items in the inventory."""
        return [item.to_dict() for item in self.items.values()]

class PointOfSale:
    """Class to handle point of sale transactions."""
    
    def __init__(self, inventory):
        self.inventory = inventory
        self.sales = []

    def make_purchase(self, item_id, quantity):
        """Process a purchase transaction."""
        item = self.inventory.get_item(item_id)
        if not item:
            raise ValueError("Item not found.")
        if item.quantity < quantity:
            raise ValueError("Not enough stock available.")
        
        item.update_quantity(-quantity)
        sale_record = {
            "item_id": item_id,
            "quantity": quantity,
            "total_price": item.price * quantity,
            "timestamp": datetime.now().isoformat()
        }
        self.sales.append(sale_record)
        return sale_record

class ElectronicInvoicing:
    """Class to handle electronic invoicing."""
    
    @staticmethod
    def generate_invoice(sale_record):
        """Generate an electronic invoice for a sale."""
        invoice = {
            "invoice_id": f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "item_id": sale_record["item_id"],
            "quantity": sale_record["quantity"],
            "total_price": sale_record["total_price"],
            "timestamp": sale_record["timestamp"]
        }
        return json.dumps(invoice, indent=4)

# Example usage
if __name__ == "__main__":
    # Initialize inventory and point of sale
    inventory = Inventory()
    pos = PointOfSale(inventory)

    # Add items to inventory
    inventory.add_item(InventoryItem("001", "Hammer", 25.0, 100))
    inventory.add_item(InventoryItem("002", "Screwdriver", 15.0, 150))

    # Make a purchase
    try:
        sale_record = pos.make_purchase("001", 2)
        print("Sale Record:", sale_record)

        # Generate invoice
        invoice = ElectronicInvoicing.generate_invoice(sale_record)
        print("Invoice:\n", invoice)
    except ValueError as e:
        print("Error:", e)
```
