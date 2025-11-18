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
import pdfkit
import json
from datetime import datetime

class InvoiceGenerator:
    def __init__(self, customer_info, rental_details, pricing_data, service_area):
        """
        Initializes the InvoiceGenerator with customer information, rental details,
        pricing data, and service area information.

        Parameters:
        - customer_info (dict): Dictionary containing customer details
        - rental_details (dict): Dictionary containing rental specifics
        - pricing_data (dict): Dictionary containing pricing information
        - service_area (str): Description of the service area
        """
        self.customer_info = customer_info
        self.rental_details = rental_details
        self.pricing_data = pricing_data
        self.service_area = service_area

    def calculate_total(self):
        """
        Calculates the total cost of the rental based on pricing data.

        Returns:
        - float: Total rental cost
        """
        base_price = self.pricing_data.get("base_price", 0)
        rental_days = self.rental_details.get("days", 1)
        total_cost = base_price * rental_days
        return total_cost

    def generate_html_invoice(self):
        """
        Generates HTML content for the invoice.

        Returns:
        - str: HTML formatted invoice
        """
        total_cost = self.calculate_total()
        invoice_date = datetime.now().strftime("%Y-%m-%d")
        
        # HTML Structure for the invoice
        html_content = f"""
        <html>
            <head>
                <title>Invoice #{self.rental_details['invoice_number']}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; }}
                    .invoice {{ width: 80%; margin: auto; border: 1px solid #ccc; padding: 20px; }}
                    .header {{ text-align: center; }}
                    .footer {{ text-align: right; }}
                </style>
            </head>
            <body>
                <div class="invoice">
                    <div class="header">
                        <h1>Invoice #{self.rental_details['invoice_number']}</h1>
                        <p>Date: {invoice_date}</p>
                    </div>
                    <h2>Customer Details</h2>
                    <p>Name: {self.customer_info['name']}</p>
                    <p>Email: {self.customer_info['email']}</p>
                    <p>Phone: {self.customer_info['phone']}</p>
                    <h2>Rental Details</h2>
                    <p>Service Area: {self.service_area}</p>
                    <p>Rental Days: {self.rental_details['days']}</p>
                    <h2>Pricing Details</h2>
                    <p>Base Price per Day: ${self.pricing_data['base_price']}</p>
                    <h2>Total Cost</h2>
                    <p>${total_cost:.2f}</p>
                    <div class="footer">
                        <p>Thank you for choosing Purple Dumpster!</p>
                    </div>
                </div>
            </body>
        </html>
        """
        return html_content

    def generate_pdf_invoice(self, output_file):
        """
        Generates a PDF invoice from the HTML content and saves it to a file.

        Parameters:
        - output_file (str): Desired output filename for the PDF invoice
        """
        html_content = self.generate_html_invoice()
        
        try:
            # Convert HTML to PDF
            pdfkit.from_string(html_content, output_file)
            print(f"Invoice saved successfully to {output_file}")
        except Exception as e:
            print(f"Error generating PDF: {e}")

if __name__ == "__main__":
    # Sample data for testing the InvoiceGenerator
    customer_info = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "555-1234"
    }
    
    rental_details = {
        "invoice_number": 1001,
        "days": 5
    }
    
    pricing_data = {
        "base_price": 50  # Price per day
    }
    
    service_area = "Downtown Area"

    # Create an instance of InvoiceGenerator
    invoice_generator = InvoiceGenerator(customer_info, rental_details, pricing_data, service_area)
    
    # Generate the PDF invoice
    invoice_generator.generate_pdf_invoice("invoice_1001.pdf")
```

Make sure to have `pdfkit` and its dependencies installed in your environment to run this code successfully.
