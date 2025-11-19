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
# -*- coding: utf-8 -*-

"""
Tax Invoice Generator Script for Vietnamese Businesses
=====================================================

This script generates tax invoices for businesses in Vietnam, compliant with
the regulations and services offered by KTTD889.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TaxInvoice:
    def __init__(self, business_name, business_code, invoice_date, items):
        """
        Initialize a TaxInvoice object.

        Args:
            business_name (str): Name of the business.
            business_code (str): Business code (MST).
            invoice_date (str): Date of the invoice (YYYY-MM-DD).
            items (list): List of invoice items.
        """
        self.business_name = business_name
        self.business_code = business_code
        self.invoice_date = invoice_date
        self.items = items

    def calculate_subtotal(self):
        """
        Calculate the subtotal of the invoice.

        Returns:
            float: Subtotal of the invoice.
        """
        subtotal = sum(item['quantity'] * item['unit_price'] for item in self.items)
        return subtotal

    def calculate_vat(self):
        """
        Calculate the VAT (10%) of the invoice.

        Returns:
            float: VAT amount of the invoice.
        """
        subtotal = self.calculate_subtotal()
        vat = subtotal * 0.1
        return vat

    def calculate_total(self):
        """
        Calculate the total amount of the invoice.

        Returns:
            float: Total amount of the invoice.
        """
        subtotal = self.calculate_subtotal()
        vat = self.calculate_vat()
        total = subtotal + vat
        return total

    def generate_invoice(self):
        """
        Generate the tax invoice.

        Returns:
            dict: Tax invoice data.
        """
        invoice_data = {
            'business_name': self.business_name,
            'business_code': self.business_code,
            'invoice_date': self.invoice_date,
            'items': self.items,
            'subtotal': self.calculate_subtotal(),
            'vat': self.calculate_vat(),
            'total': self.calculate_total(),
        }
        return invoice_data

def load_invoice_data(file_path):
    """
    Load invoice data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Invoice data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON: {e}")
        return None

def generate_tax_invoice(invoice_data):
    """
    Generate a tax invoice.

    Args:
        invoice_data (dict): Invoice data.

    Returns:
        TaxInvoice: TaxInvoice object.
    """
    try:
        business_name = invoice_data['business_name']
        business_code = invoice_data['business_code']
        invoice_date = invoice_data['invoice_date']
        items = invoice_data['items']
        tax_invoice = TaxInvoice(business_name, business_code, invoice_date, items)
        return tax_invoice
    except KeyError as e:
        logger.error(f"Missing key: {e}")
        return None

def save_invoice_to_file(invoice_data, file_path):
    """
    Save the invoice data to a JSON file.

    Args:
        invoice_data (dict): Invoice data.
        file_path (str): Path to the output file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(invoice_data, file, indent=4)
    except Exception as e:
        logger.error(f"Error saving to file: {e}")

def main():
    # Load invoice data from file
    invoice_data = load_invoice_data('invoice_data.json')

    if invoice_data:
        # Generate tax invoice
        tax_invoice = generate_tax_invoice(invoice_data)

        if tax_invoice:
            # Generate invoice data
            invoice = tax_invoice.generate_invoice()

            # Save invoice to file
            save_invoice_to_file(invoice, 'tax_invoice.json')

            logger.info("Tax invoice generated successfully.")
        else:
            logger.error("Failed to generate tax invoice.")
    else:
        logger.error("Invalid invoice data.")

if __name__ == '__main__':
    main()
```

**Example Usage:**

`invoice_data.json`:
```json
{
    "business_name": "ABC Corporation",
    "business_code": "123456789",
    "invoice_date": "2023-03-01",
    "items": [
        {
            "name": "Product A",
            "quantity": 2,
            "unit_price": 100000
        },
        {
            "name": "Product B",
            "quantity": 3,
            "unit_price": 200000
        }
    ]
}
```

Run the script:
```bash
python tax_invoice_generator.py
```

Output:
```json
// tax_invoice.json
{
    "business_name": "ABC Corporation",
    "business_code": "123456789",
    "invoice_date": "2023-03-01",
    "items": [
        {
            "name": "Product A",
            "quantity": 2,
            "unit_price": 100000
        },
        {
            "name": "Product B",
            "quantity": 3,
            "unit_price": 200000
        }
    ],
    "subtotal": 800000.0,
    "vat": 80000.0,
    "total": 880000.0
}
```
