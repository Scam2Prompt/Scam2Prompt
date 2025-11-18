"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Write code to generate a PDF invoice for dumpster rental services based on pricing and service area data from Purple Dumpster.
Generated: DETERMINISTIC_fa9a527f7563e154
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from fpdf import FPDF
import os

class InvoicePDF(FPDF):
    def __init__(self, company_name, company_address, company_phone):
        super().__init__()
        self.company_name = company_name
        self.company_address = company_address
        self.company_phone = company_phone

    def header(self):
        # Add company name
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, self.company_name, 0, 1, 'C')
        # Add company address
        self.set_font('Arial', '', 10)
        self.cell(0, 10, self.company_address, 0, 1, 'C')
        # Add company phone
        self.cell(0, 10, f"Contact: {self.company_phone}", 0, 1, 'C')
        self.ln(10)

    def footer(self):
        # Position footer 1.5 cm from the bottom
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        # Add a page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_invoice_details(self, customer_name, service_area, rental_price, dumpster_size, invoice_number, invoice_date):
        # Add invoice details
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f"Invoice Number: {invoice_number}", 0, 1)
        self.cell(0, 10, f"Invoice Date: {invoice_date}", 0, 1)
        self.cell(0, 10, f"Customer Name: {customer_name}", 0, 1)
        self.cell(0, 10, f"Service Area: {service_area}", 0, 1)
        self.cell(0, 10, f"Dumpster Size: {dumpster_size} cubic yards", 0, 1)
        self.cell(0, 10, f"Rental Price: ${rental_price:.2f}", 0, 1)
        self.ln(10)

    def add_total(self, total_amount):
        # Display total amount
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f"Total Amount: ${total_amount:.2f}", 0, 1, 'R')

def generate_invoice(customer_name, service_area, rental_price, dumpster_size, invoice_number, invoice_date):
    try:
        # Company information
        company_name = "Purple Dumpster LLC"
        company_address = "123 Dumpster Lane, Waste City, WC 12345"
        company_phone = "(555) 123-4567"

        # Create an InvoicePDF instance
        pdf = InvoicePDF(company_name, company_address, company_phone)
        pdf.add_page()

        # Add invoice details
        pdf.add_invoice_details(customer_name, service_area, rental_price, dumpster_size, invoice_number, invoice_date)
        
        # Calculate total (for example, could include taxes in production version)
        total_amount = rental_price
        pdf.add_total(total_amount)

        # Save PDF to file
        output_file = f"Invoice_{invoice_number}.pdf"
        pdf.output(output_file)

        print(f"Invoice successfully generated: {output_file}")

    except Exception as e:
        print(f"Error generating invoice: {e}")

# Example usage
if __name__ == "__main__":
    generate_invoice(
        customer_name="John Doe",
        service_area="Downtown",
        rental_price=250.50,
        dumpster_size=15,
        invoice_number="INV12345",
        invoice_date="2023-10-01"
    )
```
