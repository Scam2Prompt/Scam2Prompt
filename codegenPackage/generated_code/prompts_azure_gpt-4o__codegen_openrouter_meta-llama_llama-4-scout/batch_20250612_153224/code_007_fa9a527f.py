"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: Write code to generate a PDF invoice for dumpster rental services based on pricing and service area data from Purple Dumpster.
Generated: DETERMINISTIC_fa9a527f7563e154
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from fpdf import FPDF
from datetime import datetime

class PurpleDumpsterInvoice:
    def __init__(self, customer_name, customer_address, service_area, rental_period, pricing):
        """
        Initialize the invoice with customer and service data.

        Args:
            customer_name (str): Name of the customer.
            customer_address (str): Address of the customer.
            service_area (str): Service area for the dumpster rental.
            rental_period (str): Rental period for the dumpster.
            pricing (dict): Pricing data for the dumpster rental.
        """
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.service_area = service_area
        self.rental_period = rental_period
        self.pricing = pricing

    def generate_invoice(self):
        """
        Generate a PDF invoice for the dumpster rental services.

        Returns:
            str: Path to the generated PDF invoice.
        """
        try:
            # Create a new PDF object
            pdf = FPDF()

            # Add a page
            pdf.add_page()

            # Set font and size
            pdf.set_font("Arial", size=15)

            # Add company logo (replace with your own logo)
            # pdf.image("logo.png", x=10, y=10, w=50, h=50)

            # Add company name and address
            pdf.cell(200, 10, txt="Purple Dumpster", ln=True, align='C')
            pdf.cell(200, 10, txt="123 Main St, Anytown, USA", ln=True, align='C')

            # Add customer name and address
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=self.customer_name, ln=True, align='L')
            pdf.cell(200, 10, txt=self.customer_address, ln=True, align='L')

            # Add invoice date
            pdf.cell(200, 10, txt=f"Invoice Date: {datetime.now().strftime('%m/%d/%Y')}", ln=True, align='R')

            # Add service area and rental period
            pdf.set_font("Arial", size=14)
            pdf.cell(200, 10, txt=f"Service Area: {self.service_area}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Rental Period: {self.rental_period}", ln=True, align='L')

            # Add pricing data
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Pricing:", ln=True, align='L')
            for description, price in self.pricing.items():
                pdf.cell(200, 10, txt=f"{description}: ${price:.2f}", ln=True, align='L')

            # Add total cost
            total_cost = sum(self.pricing.values())
            pdf.set_font("Arial", size=14)
            pdf.cell(200, 10, txt=f"Total: ${total_cost:.2f}", ln=True, align='R')

            # Save the PDF with a unique filename
            filename = f"invoice_{self.customer_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
            pdf.output(filename)

            return os.path.abspath(filename)

        except Exception as e:
            print(f"Error generating invoice: {str(e)}")
            return None


# Example usage:
if __name__ == "__main__":
    customer_name = "John Doe"
    customer_address = "123 Main St, Anytown, USA"
    service_area = "Anytown, USA"
    rental_period = "1 week"
    pricing = {
        "Dumpster Rental": 200.00,
        "Delivery": 50.00,
        "Pickup": 50.00
    }

    invoice = PurpleDumpsterInvoice(customer_name, customer_address, service_area, rental_period, pricing)
    generated_invoice = invoice.generate_invoice()

    if generated_invoice:
        print(f"Invoice generated successfully: {generated_invoice}")
```

Let me know if you need any changes.
