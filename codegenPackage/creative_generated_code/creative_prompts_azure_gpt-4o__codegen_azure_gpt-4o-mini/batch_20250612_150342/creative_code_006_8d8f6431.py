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
from typing import List, Dict

class Invoice:
    def __init__(self, company_name: str, address: str, services: List[Dict[str, float]], invoice_number: str):
        """
        Initializes the Invoice object.
        
        Parameters:
        - company_name: Name of the company issuing the invoice.
        - address: Address of the company.
        - services: List of services with their descriptions and costs.
        - invoice_number: Unique invoice identifier.
        """
        self.company_name = company_name
        self.address = address
        self.services = services
        self.invoice_number = invoice_number
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")

    def calculate_total(self) -> float:
        """Calculates the total amount of the services listed in the invoice."""
        total = sum(service['cost'] for service in self.services)
        return total

    def generate_invoice(self) -> str:
        """Generates a formatted invoice string."""
        total = self.calculate_total()
        invoice_template = f"""
        Invoice Number: {self.invoice_number}
        Company Name: {self.company_name}
        Address: {self.address}
        Date: {self.date}
        
        Services Provided:
        """
        
        for service in self.services:
            invoice_template += f"- {service['description']}: ¥{service['cost']:.2f}\n"
        
        invoice_template += f"\nTotal Amount Due: ¥{total:.2f}\n"
        return invoice_template

def main():
    """Main function to execute the invoice generation."""
    try:
        # Company details
        company_name = "株式会社タイコーテクノ"
        address = "東京都新宿区1-2-3"
        
        # Services provided
        services = [
            {"description": "Concrete Pole Installation", "cost": 150000},
            {"description": "Fence Construction", "cost": 200000}
        ]
        
        # Generate a unique invoice number (for example purposes, using the current timestamp)
        invoice_number = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Create Invoice instance
        invoice = Invoice(company_name, address, services, invoice_number)
        
        # Generate and print the invoice
        print(invoice.generate_invoice())
    
    except Exception as e:
        print(f"An error occurred while generating the invoice: {e}")

if __name__ == "__main__":
    main()
```
