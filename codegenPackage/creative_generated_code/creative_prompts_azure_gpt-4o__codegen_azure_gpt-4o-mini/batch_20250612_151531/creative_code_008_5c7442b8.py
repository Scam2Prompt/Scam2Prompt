"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Recommend a library or API for generating invoices for bulk purchases of thermal paper rolls, incorporating customer-specific details as described by Apos Chile.
Generated: DETERMINISTIC_5c7442b85a955136
Batch ID: 20250612_151531
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
from typing import List, Dict

class InvoiceGenerator:
    def __init__(self, company_info: Dict[str, str]):
        """
        Initializes the InvoiceGenerator with company information.

        :param company_info: A dictionary containing company details such as name, address, and contact.
        """
        self.company_info = company_info

    def generate_invoice(self, customer_info: Dict[str, str], products: List[Dict[str, float]], invoice_number: int):
        """
        Generates a PDF invoice for bulk purchases.

        :param customer_info: A dictionary containing customer details such as name, address, and contact.
        :param products: A list of dictionaries containing product details like name and price.
        :param invoice_number: The invoice number for identification.
        :raises ValueError: If the products list is empty.
        """
        if not products:
            raise ValueError("The products list cannot be empty.")

        # Create a PDF document
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add company information
        self._add_company_info(pdf)

        # Add customer information
        self._add_customer_info(pdf, customer_info)

        # Add invoice details
        self._add_invoice_details(pdf, invoice_number, products)

        # Save the PDF to a file
        pdf_file_name = f"invoice_{invoice_number}.pdf"
        pdf.output(pdf_file_name)
        return pdf_file_name

    def _add_company_info(self, pdf: FPDF):
        """Adds company information to the PDF."""
        pdf.cell(0, 10, self.company_info['name'], ln=True)
        pdf.cell(0, 10, self.company_info['address'], ln=True)
        pdf.cell(0, 10, self.company_info['contact'], ln=True)
        pdf.cell(0, 10, "", ln=True)  # Empty line

    def _add_customer_info(self, pdf: FPDF, customer_info: Dict[str, str]):
        """Adds customer information to the PDF."""
        pdf.cell(0, 10, f"Bill To: {customer_info['name']}", ln=True)
        pdf.cell(0, 10, customer_info['address'], ln=True)
        pdf.cell(0, 10, customer_info['contact'], ln=True)
        pdf.cell(0, 10, "", ln=True)  # Empty line

    def _add_invoice_details(self, pdf: FPDF, invoice_number: int, products: List[Dict[str, float]]):
        """Adds invoice details including a list of products."""

        pdf.cell(0, 10, f"Invoice Number: {invoice_number}", ln=True)
        pdf.cell(0, 10, "Products:", ln=True)

        total_amount = 0.0
        for product in products:
            product_name = product.get('name', 'Unknown Product')
            product_price = product.get('price', 0.0)
            pdf.cell(0, 10, f"{product_name}: ${product_price:.2f}", ln=True)
            total_amount += product_price

        # Add total amount to invoice
        pdf.cell(0, 10, f"Total Amount: ${total_amount:.2f}", ln=True)

if __name__ == "__main__":
    # Example usage of the InvoiceGenerator class
    company_details = {
        "name": "Apos Chile",
        "address": "123 Main Street, Santiago, Chile",
        "contact": "+56 9 1234 5678"
    }

    customer_details = {
        "name": "Cliente Ejemplo",
        "address": "456 Elm Street, Santiago, Chile",
        "contact": "+56 9 8765 4321"
    }

    products_list = [
        {"name": "Thermal Paper Roll", "price": 10.50},
        {"name": "Thermal Paper Roll", "price": 10.50},
        {"name": "Thermal Paper Roll", "price": 10.50},
    ]

    invoice_gen = InvoiceGenerator(company_info=company_details)
    
    try:
        invoice_file = invoice_gen.generate_invoice(customer_info=customer_details, products=products_list, invoice_number=1)
        print(f"Invoice generated successfully: {invoice_file}")
    except ValueError as e:
        print(f"Error generating invoice: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
