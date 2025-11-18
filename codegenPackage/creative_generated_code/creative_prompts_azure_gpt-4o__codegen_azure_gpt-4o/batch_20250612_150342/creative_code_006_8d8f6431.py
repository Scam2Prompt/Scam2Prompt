"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Create a program to generate invoices for construction services, including concrete pole installation and fence construction, with customizable templates for companies like 株式会社タイコーテクノ.
Generated: DETERMINISTIC_8d8f6431327d1a0c
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import os

# Invoice Generator for Construction Services

class InvoiceGenerator:
    def __init__(self, company_name, address, phone, email):
        """
        Initialize the InvoiceGenerator with company details.
        :param company_name: Name of the company issuing the invoice.
        :param address: Address of the company.
        :param phone: Phone number of the company.
        :param email: Email address of the company.
        """
        self.company_name = company_name
        self.address = address
        self.phone = phone
        self.email = email
    
    def generate_invoice(self, client_name, client_address, items, output_directory='invoices'):
        """
        Generate an invoice for construction services.
        :param client_name: Name of the client receiving the invoice.
        :param client_address: Address of the client.
        :param items: List of items (services) on the invoice. Each item is a dictionary with 'description', 'quantity', and 'price'.
        :param output_directory: Directory to save the generated invoice file.
        """
        try:
            # Ensure the output directory exists
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)
            
            # Calculate totals
            subtotal = sum(item['quantity'] * item['price'] for item in items)
            tax = round(subtotal * 0.10, 2)  # Assuming 10% tax rate
            total = round(subtotal + tax, 2)
            
            # Create the invoice content
            invoice_date = datetime.datetime.now().strftime('%Y-%m-%d')
            invoice_number = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            invoice_content = f"""
株式会社タイコーテクノ
INVOICE
Invoice Number: {invoice_number}
Invoice Date: {invoice_date}

Bill To:
{client_name}
{client_address}

From:
{self.company_name}
{self.address}
Phone: {self.phone}
Email: {self.email}

Items:
------------------------------------------------------
Description          Quantity    Unit Price    Total
------------------------------------------------------"""
            for item in items:
                line_total = item['quantity'] * item['price']
                invoice_content += f"\n{item['description'][:18]:<18} {item['quantity']:>8} {item['price']:>12.2f} {line_total:>10.2f}"
            
            invoice_content += f"""
------------------------------------------------------
Subtotal: {subtotal:.2f}
Tax (10%): {tax:.2f}
------------------------------------------------------
Total: {total:.2f}

Thank you for your business!
"""
            # Save the invoice to a file
            filename = f"{output_directory}/Invoice_{invoice_number}.txt"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(invoice_content)
            
            print(f"Invoice generated successfully: {filename}")
        
        except Exception as e:
            print(f"Error generating invoice: {e}")

# Example of usage
if __name__ == "__main__":
    # Initialize the invoice generator with company details
    generator = InvoiceGenerator(
        company_name="株式会社タイコーテクノ",
        address="123 Construction Lane, Tokyo, Japan",
        phone="+81-123-456-7890",
        email="contact@taikotechnologies.jp"
    )
    
    # Client details
    client_name = "John Doe Construction"
    client_address = "456 Building Ave, Osaka, Japan"
    
    # List of services/items
    items = [
        {"description": "Concrete Pole Installation", "quantity": 5, "price": 1500.00},
        {"description": "Fence Construction", "quantity": 100, "price": 25.00}
    ]
    
    # Generate and save the invoice
    generator.generate_invoice(client_name, client_address, items)
```
