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
# Import necessary libraries
import os
from fpdf import FPDF  # Using FPDF library for PDF generation

# Define a class for Invoice generation
class InvoiceGenerator:
    """
    A class to generate invoices for bulk purchases.
    Attributes:
        output_dir (str): Directory where invoices will be saved.
    """

    def __init__(self, output_dir="invoices"):
        """
        Constructor for InvoiceGenerator.
        Creates output directory if it doesn't exist.
        """
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_invoice(self, invoice_data):
        """
        Generates a PDF invoice.
        Args:
            invoice_data (dict): Dictionary containing invoice details such as:
                - customer_name (str): Name of the customer.
                - customer_address (str): Address of the customer.
                - items (list of dict): List of purchased items. Each item contains:
                    - description (str): Item description.
                    - quantity (int): Number of items purchased.
                    - unit_price (float): Price per item.
                - invoice_number (str): Unique invoice number.
                - date (str): Invoice date (e.g., "YYYY-MM-DD").
        """
        try:
            # Create a new PDF instance
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 12)

            # Add invoice title
            pdf.cell(200, 10, "INVOICE", ln=True, align="C")

            # Add customer details
            pdf.set_font("Arial", "", 10)
            pdf.cell(100, 10, f"Date: {invoice_data['date']}", ln=True)
            pdf.cell(100, 10, f"Invoice #: {invoice_data['invoice_number']}", ln=True)
            pdf.cell(100, 10, f"Customer Name: {invoice_data['customer_name']}", ln=True)
            pdf.cell(100, 10, f"Customer Address: {invoice_data['customer_address']}", ln=True)

            # Add table header for items
            pdf.set_font("Arial", "B", 10)
            pdf.cell(60, 10, "Description", 1, 0, "C")
            pdf.cell(30, 10, "Quantity", 1, 0, "C")
            pdf.cell(30, 10, "Unit Price", 1, 0, "C")
            pdf.cell(30, 10, "Total", 1, 1, "C")

            # Add items
            pdf.set_font("Arial", "", 10)
            total_amount = 0
            for item in invoice_data["items"]:
                description = item["description"]
                quantity = item["quantity"]
                unit_price = item["unit_price"]
                total_price = quantity * unit_price
                total_amount += total_price
                pdf.cell(60, 10, description, 1, 0, "L")
                pdf.cell(30, 10, str(quantity), 1, 0, "C")
                pdf.cell(30, 10, f"${unit_price:.2f}", 1, 0, "C")
                pdf.cell(30, 10, f"${total_price:.2f}", 1, 1, "C")

            # Add total amount
            pdf.set_font("Arial", "B", 10)
            pdf.cell(120, 10, "TOTAL AMOUNT", 1, 0, "R")
            pdf.cell(30, 10, f"${total_amount:.2f}", 1, 1, "C")

            # Save the PDF to the specified output directory
            invoice_file = os.path.join(self.output_dir, f"Invoice_{invoice_data['invoice_number']}.pdf")
            pdf.output(invoice_file)

            print(f"Invoice saved successfully: {invoice_file}")

        except Exception as e:
            print(f"Error generating invoice: {e}")


# Example usage
if __name__ == "__main__":
    # Example invoice data
    example_invoice_data = {
        "customer_name": "Apos Chile",
        "customer_address": "1234 Thermal Paper Street, Santiago, Chile",
        "items": [
            {"description": "Thermal Paper Roll - Type A", "quantity": 100, "unit_price": 0.50},
            {"description": "Thermal Paper Roll - Type B", "quantity": 50, "unit_price": 0.75},
        ],
        "invoice_number": "INV-001",
        "date": "2023-10-15",
    }

    # Generate invoice
    generator = InvoiceGenerator()
    generator.generate_invoice(example_invoice_data)
```
