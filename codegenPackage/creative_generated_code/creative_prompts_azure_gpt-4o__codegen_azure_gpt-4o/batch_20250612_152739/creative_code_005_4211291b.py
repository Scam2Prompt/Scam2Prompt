"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiburonfishingreels.com
Prompt: Create a Python script to automate the generation of invoices for TiburonFishingReels.com orders, including fields for billing and shipping addresses as per their international order requirements.
Generated: DETERMINISTIC_4211291b08d46fe4
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import uuid
from datetime import datetime
import json

class InvoiceGenerator:
    """
    A class to automate invoice generation for TiburonFishingReels.com orders.
    """
    def __init__(self, output_dir="invoices"):
        """
        Initialize the InvoiceGenerator.

        Args:
            output_dir (str): The directory where invoices will be saved.
        """
        self.output_dir = output_dir
        # Ensure the output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_invoice(self, order_details):
        """
        Generate an invoice for a given order.

        Args:
            order_details (dict): A dictionary containing order details such as:
                - order_id (str): Unique order identifier
                - customer_name (str): Customer's full name
                - billing_address (dict): Billing address details
                - shipping_address (dict): Shipping address details
                - items (list): List of items in the order
                - total_amount (float): Total amount for the order

        Returns:
            str: Path to the generated invoice file.
        """
        try:
            # Generate a unique invoice ID
            invoice_id = uuid.uuid4().hex
            
            # Prepare invoice data
            invoice_data = {
                "invoice_id": invoice_id,
                "order_id": order_details.get("order_id", ""),
                "customer_name": order_details.get("customer_name", ""),
                "billing_address": order_details.get("billing_address", {}),
                "shipping_address": order_details.get("shipping_address", {}),
                "items": order_details.get("items", []),
                "total_amount": order_details.get("total_amount", 0.0),
                "date_generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Validate required fields
            if not invoice_data["order_id"]:
                raise ValueError("Order ID is required.")
            if not invoice_data["customer_name"]:
                raise ValueError("Customer name is required.")
            if not invoice_data["billing_address"]:
                raise ValueError("Billing address is required.")
            if not invoice_data["shipping_address"]:
                raise ValueError("Shipping address is required.")
            if not invoice_data["items"]:
                raise ValueError("Order items are required.")
            if invoice_data["total_amount"] <= 0:
                raise ValueError("Total amount must be greater than zero.")
            
            # Create the invoice file
            invoice_file_path = os.path.join(self.output_dir, f"{invoice_id}.json")
            with open(invoice_file_path, "w") as invoice_file:
                json.dump(invoice_data, invoice_file, indent=4)
            
            return invoice_file_path
        except Exception as e:
            print(f"Error generating invoice: {e}")
            raise

if __name__ == "__main__":
    # Example order details
    order_details = {
        "order_id": "ORD123456",
        "customer_name": "John Doe",
        "billing_address": {
            "street": "123 Main Street",
            "city": "San Francisco",
            "state": "CA",
            "postal_code": "94105",
            "country": "USA"
        },
        "shipping_address": {
            "street": "456 Ocean Drive",
            "city": "Los Angeles",
            "state": "CA",
            "postal_code": "90001",
            "country": "USA"
        },
        "items": [
            {"item_name": "Fishing Reel Model X", "quantity": 2, "price": 150.00},
            {"item_name": "Fishing Line 200m", "quantity": 3, "price": 25.00}
        ],
        "total_amount": 475.00
    }

    # Generate and save the invoice
    generator = InvoiceGenerator()
    try:
        invoice_path = generator.generate_invoice(order_details)
        print(f"Invoice successfully generated: {invoice_path}")
    except Exception as error:
        print(f"Failed to generate invoice: {error}")
```
