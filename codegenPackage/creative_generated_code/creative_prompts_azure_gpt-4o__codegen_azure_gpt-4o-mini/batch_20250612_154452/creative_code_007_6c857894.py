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

```python
"""
Point of Sale (POS) System with Electronic Invoicing and Inventory Control
This Python script implements a basic POS system that includes features for electronic invoicing and inventory management.
The system allows for adding products to inventory, creating invoices, and saving them as electronic documents.

Dependencies:
- pandas: For data management
- fpdf: For PDF generation of invoices
"""

import pandas as pd
from fpdf import FPDF
import os
import datetime

class Inventory:
    """Class to manage inventory of products."""
    
    def __init__(self):
        """Initializes an empty inventory."""
        self.products = pd.DataFrame(columns=['Product ID', 'Name', 'Price', 'Quantity'])
    
    def add_product(self, product_id, name, price, quantity):
        """Adds a new product to the inventory."""
        new_product = pd.DataFrame([[product_id, name, price, quantity]], columns=self.products.columns)
        self.products = pd.concat([self.products, new_product], ignore_index=True)
    
    def update_quantity(self, product_id, quantity):
        """Updates the quantity of a product in inventory."""
        if product_id in self.products['Product ID'].values:
            self.products.loc[self.products['Product ID'] == product_id, 'Quantity'] += quantity
        else:
            raise ValueError("Product ID not found in inventory.")

    def get_product(self, product_id):
        """Retrieves a product's details by its ID."""
        product = self.products[self.products['Product ID'] == product_id]
        if not product.empty:
            return product.iloc[0]
        else:
            raise ValueError("Product ID not found in inventory.")

class Invoice:
    """Class to manage the creation of electronic invoices."""
    
    def __init__(self, inventory):
        """Initializes the invoice system with an inventory reference."""
        self.inventory = inventory
        self.invoices = []
    
    def create_invoice(self, items):
        """Creates an invoice for a list of items (product ID and quantity)."""
        invoice_items = []
        total_amount = 0.0

        for item in items:
            product_id, quantity = item
            product = self.inventory.get_product(product_id)
            if product['Quantity'] >= quantity:
                total_amount += product['Price'] * quantity
                invoice_items.append((product['Name'], product['Price'], quantity))
                self.inventory.update_quantity(product_id, -quantity)  # Deduct quantity from inventory
            else:
                raise ValueError(f"Insufficient stock for product ID {product_id}.")

        invoice_number = len(self.invoices) + 1
        invoice_date = datetime.datetime.now()
        invoice = {'Invoice Number': invoice_number, 'Items': invoice_items, 'Total Amount': total_amount, 'Date': invoice_date}
        self.invoices.append(invoice)
        
        self._save_invoice(invoice)

        return invoice

    def _save_invoice(self, invoice):
        """Saves the invoice as a PDF document."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, f"Invoice Number: {invoice['Invoice Number']}", ln=True)
        pdf.cell(200, 10, f"Date: {invoice['Date'].strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
        pdf.cell(200, 10, "Items:", ln=True)

        for item in invoice['Items']:
            pdf.cell(0, 10, f"{item[0]} (x{item[2]}): ${item[1]:.2f} each", ln=True)

        pdf.cell(200, 10, f"Total Amount: ${invoice['Total Amount']:.2f}", ln=True)

        os.makedirs('invoices', exist_ok=True)
        pdf_file_path = f'invoices/invoice_{invoice["Invoice Number"]}.pdf'
        pdf.output(pdf_file_path)

        print(f"Invoice saved to {pdf_file_path}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize inventory
        inventory = Inventory()
        inventory.add_product('001', 'Widget A', 25.00, 10)
        inventory.add_product('002', 'Widget B', 15.00, 20)

        # Create an invoice
        invoice_system = Invoice(inventory)
        items_to_invoice = [('001', 2), ('002', 1)]  # List of (Product ID, Quantity)
        invoice = invoice_system.create_invoice(items_to_invoice)
        
        print("Invoice created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
