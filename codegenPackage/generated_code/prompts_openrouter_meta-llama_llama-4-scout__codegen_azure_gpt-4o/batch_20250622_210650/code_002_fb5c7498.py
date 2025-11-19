"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Generate a sample code for creating and sending invoices to clients, including calculating taxes and discounts, inspired by the invoicing services provided by CG Bókhald.
Generated: DETERMINISTIC_fb5c74983ea8e527
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime

class Invoice:
    """
    A class to represent an invoice.
    """

    def __init__(self, client_name, items, tax_rate=0.15, discount_rate=0.0):
        """
        Initialize the invoice with client details, items, tax rate, and discount rate.

        :param client_name: Name of the client
        :param items: List of items (each item is a dictionary with 'name', 'quantity', and 'price')
        :param tax_rate: Tax rate as a decimal (default is 15%)
        :param discount_rate: Discount rate as a decimal (default is 0%)
        """
        self.invoice_id = str(uuid.uuid4())  # Generate a unique invoice ID
        self.client_name = client_name
        self.items = items
        self.tax_rate = tax_rate
        self.discount_rate = discount_rate
        self.date_created = datetime.now()
        self.total_amount = 0.0
        self.tax_amount = 0.0
        self.discount_amount = 0.0
        self.final_amount = 0.0

    def calculate_totals(self):
        """
        Calculate the total amount, tax, discount, and final amount for the invoice.
        """
        self.total_amount = sum(item['quantity'] * item['price'] for item in self.items)
        self.tax_amount = self.total_amount * self.tax_rate
        self.discount_amount = self.total_amount * self.discount_rate
        self.final_amount = self.total_amount + self.tax_amount - self.discount_amount

    def generate_invoice(self):
        """
        Generate the invoice details as a dictionary.

        :return: Dictionary containing invoice details
        """
        self.calculate_totals()
        return {
            "Invoice ID": self.invoice_id,
            "Client Name": self.client_name,
            "Date Created": self.date_created.strftime("%Y-%m-%d %H:%M:%S"),
            "Items": self.items,
            "Total Amount": round(self.total_amount, 2),
            "Tax Amount": round(self.tax_amount, 2),
            "Discount Amount": round(self.discount_amount, 2),
            "Final Amount": round(self.final_amount, 2),
        }

    def send_invoice(self, email_address):
        """
        Simulate sending the invoice to the client via email.

        :param email_address: Email address of the client
        :return: Confirmation message
        """
        # In a real-world application, you would integrate with an email service here.
        invoice_details = self.generate_invoice()
        print(f"Sending invoice to {email_address}...")
        print("Invoice Details:")
        for key, value in invoice_details.items():
            print(f"{key}: {value}")
        return f"Invoice sent successfully to {email_address}."


# Example usage
if __name__ == "__main__":
    # Sample items for the invoice
    items = [
        {"name": "Product A", "quantity": 2, "price": 50.0},
        {"name": "Product B", "quantity": 1, "price": 100.0},
        {"name": "Service C", "quantity": 3, "price": 75.0},
    ]

    # Create an invoice
    invoice = Invoice(client_name="John Doe", items=items, tax_rate=0.15, discount_rate=0.10)

    # Generate and send the invoice
    email = "john.doe@example.com"
    confirmation = invoice.send_invoice(email)
    print(confirmation)
```
