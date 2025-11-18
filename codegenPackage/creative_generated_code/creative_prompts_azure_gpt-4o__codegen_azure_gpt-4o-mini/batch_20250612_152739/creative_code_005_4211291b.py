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
import json
from fpdf import FPDF
from datetime import datetime
import os

class InvoiceGenerator:
    """
    A class to generate PDF invoices for TiburonFishingReels.com orders.
    """

    def __init__(self, order_data, output_directory='invoices'):
        """
        Initialize the InvoiceGenerator with order data and output directory.

        Parameters:
            order_data (dict): A dictionary containing order details.
            output_directory (str): The directory where the invoices will be saved.
        """
        self.order_data = order_data
        self.output_directory = output_directory
        self.pdf = FPDF()
        self.invoice_file = self.create_invoice_filename()

        # Ensure the output directory exists
        os.makedirs(self.output_directory, exist_ok=True)

    def create_invoice_filename(self):
        """
        Create a unique invoice filename based on the order number and current date.

        Returns:
            str: The generated filename for the invoice PDF.
        """
        order_number = self.order_data.get("order_number", "unknown_order")
        date_str = datetime.now().strftime("%Y%m%d")
        return os.path.join(self.output_directory, f"invoice_{order_number}_{date_str}.pdf")

    def add_invoice_header(self):
        """
        Add the invoice header to the PDF.
        """
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, 'Invoice', ln=True, align='C')
        self.pdf.ln(10)

    def add_order_details(self):
        """
        Add order details including billing and shipping addresses.
        """
        self.pdf.set_font("Arial", '', 12)

        # Billing Information
        billing_info = self.order_data.get('billing_address', {})
        self.pdf.cell(0, 10, 'Billing Address:', ln=True)
        self.add_address_details(billing_info)

        # Shipping Information
        shipping_info = self.order_data.get('shipping_address', {})
        self.pdf.cell(0, 10, 'Shipping Address:', ln=True)
        self.add_address_details(shipping_info)

        # Order Summary
        self.pdf.cell(0, 10, 'Order Summary:', ln=True)
        items = self.order_data.get('items', [])
        for item in items:
            line = f"{item.get('name')} - Quantity: {item.get('quantity')} - Price: ${item.get('price'):.2f}"
            self.pdf.cell(0, 10, line, ln=True)

    def add_address_details(self, address):
        """
        Add formatted address details to the PDF.

        Parameters:
            address (dict): A dictionary containing address fields.
        """
        address_lines = [
            address.get("name", ""),
            address.get("street", ""),
            f"{address.get('city', '')}, {address.get('state', '')} {address.get('zip', '')}",
            address.get("country", "")
        ]
        for line in address_lines:
            if line:  # Only add non-empty lines
                self.pdf.cell(0, 10, line, ln=True)
        self.pdf.ln(5)  # Extra space after the address

    def save_invoice(self):
        """
        Save the generated PDF invoice to the output directory.
        """
        try:
            self.pdf.output(self.invoice_file)
            print(f"Invoice successfully saved at: {self.invoice_file}")
        except Exception as e:
            print(f"Error saving the invoice: {e}")

    def generate_invoice(self):
        """
        Generate the complete invoice PDF.
        """
        self.pdf.add_page()
        self.add_invoice_header()
        self.add_order_details()
        self.save_invoice()

def main():
    """
    Main function to execute the invoice generation process.
    """
    # Sample order data
    order_data = {
        "order_number": "12345",
        "billing_address": {
            "name": "John Doe",
            "street": "123 Fishing Lane",
            "city": "Fishville",
            "state": "CA",
            "zip": "90210",
            "country": "USA"
        },
        "shipping_address": {
            "name": "Jane Doe",
            "street": "456 Angler St",
            "city": "Ocean City",
            "state": "MD",
            "zip": "21842",
            "country": "USA"
        },
        "items": [
            {"name": "Tiburon Fishing Reel", "quantity": 2, "price": 149.99},
            {"name": "Fishing Line", "quantity": 1, "price": 19.99}
        ]
    }

    # Generate the invoice
    invoice_generator = InvoiceGenerator(order_data)
    invoice_generator.generate_invoice()

if __name__ == "__main__":
    main()
```
