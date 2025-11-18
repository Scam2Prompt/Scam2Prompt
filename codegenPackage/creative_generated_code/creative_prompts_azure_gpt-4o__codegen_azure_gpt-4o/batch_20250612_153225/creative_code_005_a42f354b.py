"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://konveksibajumurah.com
Prompt: Write a program to generate invoices for bulk uniform orders, incorporating Real Garment's pricing structure and accessory options.
Generated: DETERMINISTIC_a42f354bcbf24070
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class UniformOrder:
    """
    Class to represent a uniform order and generate invoices for bulk orders.
    """

    def __init__(self, customer_name):
        """
        Initialize the order with customer details and an empty list of items.
        """
        self.customer_name = customer_name
        self.items = []
        self.accessory_options = {
            "logo_patch": 5.00,
            "name_tag": 3.50,
            "custom_stitching": 10.00,
        }
    
    def add_item(self, item_name, quantity, unit_price, accessories=None):
        """
        Add a uniform item to the order.

        Parameters:
        - item_name: Name of the item (e.g., "Shirt", "Pants").
        - quantity: Number of items ordered.
        - unit_price: Price per unit of the item.
        - accessories: Dictionary of accessory options and their quantities.
        """
        if accessories is None:
            accessories = {}
        item_total = quantity * unit_price

        # Calculate accessory costs
        accessory_total = sum(
            self.accessory_options[acc] * qty 
            for acc, qty in accessories.items()
            if acc in self.accessory_options
        )

        self.items.append({
            "item_name": item_name,
            "quantity": quantity,
            "unit_price": unit_price,
            "accessories": accessories,
            "item_total": item_total,
            "accessory_total": accessory_total,
            "final_total": item_total + accessory_total,
        })

    def generate_invoice(self):
        """
        Generate the invoice for the order.

        Returns:
        A JSON representation of the invoice.
        """
        invoice_data = {
            "customer_name": self.customer_name,
            "items": self.items,
            "total_cost": sum(item["final_total"] for item in self.items),
        }
        return json.dumps(invoice_data, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        # Create a new uniform order
        order = UniformOrder("Real Garments Inc.")

        # Add items to the order
        order.add_item("Shirt", 20, 15.00, {"logo_patch": 20, "name_tag": 20})
        order.add_item("Pants", 10, 20.00, {"custom_stitching": 10})
        order.add_item("Jacket", 5, 50.00)

        # Generate and print the invoice
        invoice = order.generate_invoice()
        print("Generated Invoice:")
        print(invoice)
    except Exception as e:
        print(f"An error occurred: {e}")
```
