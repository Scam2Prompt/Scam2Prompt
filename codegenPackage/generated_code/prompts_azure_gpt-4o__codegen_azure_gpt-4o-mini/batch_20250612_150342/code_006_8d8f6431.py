"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Create a program to generate invoices for construction services, including concrete pole installation and fence construction, with customizable templates for companies like 株式会社タイコーテクノ.
Generated: DETERMINISTIC_8d8f6431327d1a0c
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class Invoice:
    def __init__(self, company_name, client_name, services, invoice_number):
        """
        Initialize the Invoice object with company and client details, services, and invoice number.
        
        :param company_name: Name of the company issuing the invoice
        :param client_name: Name of the client receiving the invoice
        :param services: List of services provided
        :param invoice_number: Unique invoice number
        """
        self.company_name = company_name
        self.client_name = client_name
        self.services = services
        self.invoice_number = invoice_number
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.total_amount = self.calculate_total()

    def calculate_total(self):
        """
        Calculate the total amount for the services provided.
        
        :return: Total amount as a float
        """
        total = sum(service['price'] * service['quantity'] for service in self.services)
        return total

    def generate_invoice(self):
        """
        Generate a formatted invoice as a string.
        
        :return: Formatted invoice string
        """
        invoice_details = f"Invoice Number: {self.invoice_number}\n"
        invoice_details += f"Date: {self.date}\n"
        invoice_details += f"Company: {self.company_name}\n"
        invoice_details += f"Client: {self.client_name}\n\n"
        invoice_details += "Services:\n"
        
        for service in self.services:
            invoice_details += f"- {service['description']}: {service['quantity']} x {service['price']} = {service['quantity'] * service['price']}\n"
        
        invoice_details += f"\nTotal Amount: {self.total_amount}\n"
        return invoice_details

    def save_invoice(self, filename):
        """
        Save the invoice details to a JSON file.
        
        :param filename: Name of the file to save the invoice
        """
        invoice_data = {
            "invoice_number": self.invoice_number,
            "date": self.date,
            "company_name": self.company_name,
            "client_name": self.client_name,
            "services": self.services,
            "total_amount": self.total_amount
        }
        
        try:
            with open(filename, 'w') as json_file:
                json.dump(invoice_data, json_file, indent=4)
            print(f"Invoice saved to {filename}")
        except IOError as e:
            print(f"Error saving invoice: {e}")

def main():
    # Example usage of the Invoice class
    company_name = "株式会社タイコーテクノ"
    client_name = "John Doe"
    
    # Define services provided
    services = [
        {"description": "Concrete Pole Installation", "quantity": 10, "price": 150.00},
        {"description": "Fence Construction", "quantity": 50, "price": 20.00}
    ]
    
    # Create an invoice
    invoice_number = "INV-2023-001"
    invoice = Invoice(company_name, client_name, services, invoice_number)
    
    # Generate and print the invoice
    print(invoice.generate_invoice())
    
    # Save the invoice to a file
    invoice.save_invoice("invoice.json")

if __name__ == "__main__":
    main()
```
