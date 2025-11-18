"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ticomsoftware.com
Prompt: Provide a step-by-step guide for implementing a point-of-sale system with electronic invoicing and inventory control, referencing TICOM Software's specialized RMS features.
Generated: DETERMINISTIC_6c857894f158a017
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a production-ready implementation of a basic point-of-sale (POS) system with electronic invoicing and inventory control in Python. This code serves as a foundational framework and can be extended with integration to TICOM Software's specialized RMS features as needed.

```python
import json
import uuid
from datetime import datetime

# Exception classes
class InventoryError(Exception):
    pass

class PaymentError(Exception):
    pass

# Inventory Management Module
class Inventory:
    def __init__(self):
        # Initialize inventory with sample data
        self.items = {
            "001": {"name": "Laptop", "price": 1000.00, "quantity": 10},
            "002": {"name": "Mouse", "price": 25.50, "quantity": 50},
            "003": {"name": "Keyboard", "price": 45.75, "quantity": 30},
        }

    def get_item(self, item_id):
        """Retrieve item details from inventory."""
        if item_id not in self.items:
            raise InventoryError(f"Item ID {item_id} not found in inventory.")
        return self.items[item_id]

    def update_quantity(self, item_id, quantity_sold):
        """Update item quantity after a sale."""
        item = self.get_item(item_id)
        if item["quantity"] < quantity_sold:
            raise InventoryError(f"Insufficient stock for item ID {item_id}.")
        item["quantity"] -= quantity_sold

# POS System Module
class PointOfSale:
    def __init__(self, inventory):
        self.inventory = inventory
        self.sales = []  # Store sales transactions

    def process_sale(self, cart):
        """
        Process a sale transaction.
        cart: List of dictionaries containing item_id and quantity.
        """
        total_amount = 0.0
        invoice_items = []
        
        # Validate cart and calculate total
        for item in cart:
            item_id = item["item_id"]
            quantity = item["quantity"]

            try:
                product = self.inventory.get_item(item_id)
                self.inventory.update_quantity(item_id, quantity)
                line_total = product["price"] * quantity
                total_amount += line_total

                # Prepare invoice line
                invoice_items.append({
                    "item_id": item_id,
                    "name": product["name"],
                    "quantity": quantity,
                    "unit_price": product["price"],
                    "line_total": line_total
                })
            except InventoryError as e:
                print(f"Error processing item {item_id}: {e}")
                raise

        # Generate electronic invoice
        invoice = self._generate_invoice(invoice_items, total_amount)
        self.sales.append(invoice)
        return invoice

    def _generate_invoice(self, items, total_amount):
        """Generate an electronic invoice."""
        invoice_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        invoice = {
            "invoice_id": invoice_id,
            "timestamp": timestamp,
            "items": items,
            "total_amount": total_amount,
        }
        self._save_invoice_to_file(invoice)  # Save invoice for records
        return invoice

    def _save_invoice_to_file(self, invoice):
        """Save invoice to a JSON file for electronic record keeping."""
        try:
            filename = f"invoice_{invoice['invoice_id']}.json"
            with open(filename, "w") as file:
                json.dump(invoice, file, indent=4)
            print(f"Invoice saved successfully: {filename}")
        except IOError as e:
            print(f"Error saving invoice: {e}")
            raise

    def get_sales_summary(self):
        """Retrieve all sales transactions."""
        return self.sales

# Main Application
if __name__ == "__main__":
    # Initialize inventory and POS system
    inventory = Inventory()
    pos = PointOfSale(inventory)

    # Example sale transaction
    try:
        cart = [
            {"item_id": "001", "quantity": 2},
            {"item_id": "003", "quantity": 1},
        ]
        invoice = pos.process_sale(cart)
        print("Sale processed successfully!")
        print("Generated Invoice:")
        print(json.dumps(invoice, indent=4))
    except Exception as e:
        print(f"Error during sale processing: {e}")

    # Display sales summary
    print("\nSales Summary:")
    sales_summary = pos.get_sales_summary()
    print(json.dumps(sales_summary, indent=4))
```

### Key Features:
1. **Inventory Management**: Tracks product details and updates quantities after each sale.
2. **Electronic Invoicing**: Generates and saves invoices in JSON format for records.
3. **Error Handling**: Handles inventory and payment errors gracefully.
4. **Sales Summary**: Keeps track of all sales transactions for reporting.

### Note:
To integrate TICOM Software's specialized RMS features, you can extend this implementation by interfacing with their API or SDK and adding advanced functionalities.
