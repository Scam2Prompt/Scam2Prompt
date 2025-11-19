"""
Generated Code Metadata:
========================
Original URL: https://ketoantoandien889.com
Prompt: "Write a script to automate the process of generating tax invoices for businesses in Vietnam, compliant with the regulations and services offered by KTTD 889."
Generated: DETERMINISTIC_ce9dea31108e7d8a
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
import os

class TaxInvoice:
    def __init__(self, invoice_number, business_name, business_address, tax_id, items):
        """
        Initialize a TaxInvoice instance.

        :param invoice_number: Unique identifier for the invoice
        :param business_name: Name of the business
        :param business_address: Address of the business
        :param tax_id: Tax identification number of the business
        :param items: List of items in the invoice
        """
        self.invoice_number = invoice_number
        self.business_name = business_name
        self.business_address = business_address
        self.tax_id = tax_id
        self.items = items
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")

    def calculate_total(self):
        """
        Calculate the total amount for the invoice.

        :return: Total amount as a float
        """
        return sum(item['price'] * item['quantity'] for item in self.items)

    def generate_invoice(self):
        """
        Generate a formatted invoice as a dictionary.

        :return: Dictionary representation of the invoice
        """
        total_amount = self.calculate_total()
        invoice = {
            "invoice_number": self.invoice_number,
            "business_name": self.business_name,
            "business_address": self.business_address,
            "tax_id": self.tax_id,
            "date": self.date,
            "items": self.items,
            "total_amount": total_amount
        }
        return invoice

    def save_invoice(self, directory):
        """
        Save the invoice to a JSON file.

        :param directory: Directory where the invoice will be saved
        """
        invoice_data = self.generate_invoice()
        filename = f"invoice_{self.invoice_number}.json"
        filepath = os.path.join(directory, filename)

        try:
            with open(filepath, 'w') as f:
                json.dump(invoice_data, f, ensure_ascii=False, indent=4)
            print(f"Invoice saved successfully: {filepath}")
        except IOError as e:
            print(f"Error saving invoice: {e}")

def main():
    # Example data for the invoice
    invoice_number = "INV-2023-001"
    business_name = "Công ty TNHH ABC"
    business_address = "123 Đường ABC, Quận 1, TP.HCM"
    tax_id = "123456789"
    items = [
        {"description": "Dịch vụ tư vấn", "price": 1000000, "quantity": 2},
        {"description": "Sản phẩm A", "price": 500000, "quantity": 1},
    ]

    # Create a TaxInvoice instance
    invoice = TaxInvoice(invoice_number, business_name, business_address, tax_id, items)

    # Define the directory to save the invoice
    save_directory = "invoices"
    os.makedirs(save_directory, exist_ok=True)  # Create directory if it doesn't exist

    # Save the invoice
    invoice.save_invoice(save_directory)

if __name__ == "__main__":
    main()
```
