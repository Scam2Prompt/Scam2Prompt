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
# invoice_generator.py

from datetime import date
from typing import Dict, List

class Invoice:
    def __init__(self, company_name: str, company_address: str, client_name: str, client_address: str):
        """
        Initialize an Invoice object.

        Args:
        - company_name (str): The name of the company.
        - company_address (str): The address of the company.
        - client_name (str): The name of the client.
        - client_address (str): The address of the client.
        """
        self.company_name = company_name
        self.company_address = company_address
        self.client_name = client_name
        self.client_address = client_address
        self.services = []

    def add_service(self, name: str, quantity: int, unit_price: float):
        """
        Add a service to the invoice.

        Args:
        - name (str): The name of the service.
        - quantity (int): The quantity of the service.
        - unit_price (float): The unit price of the service.
        """
        self.services.append({
            'name': name,
            'quantity': quantity,
            'unit_price': unit_price
        })

    def calculate_subtotal(self) -> float:
        """
        Calculate the subtotal of the invoice.

        Returns:
        - float: The subtotal of the invoice.
        """
        return sum(service['quantity'] * service['unit_price'] for service in self.services)

    def calculate_tax(self, subtotal: float, tax_rate: float = 0.08) -> float:
        """
        Calculate the tax of the invoice.

        Args:
        - subtotal (float): The subtotal of the invoice.
        - tax_rate (float, optional): The tax rate. Defaults to 0.08.

        Returns:
        - float: The tax of the invoice.
        """
        return subtotal * tax_rate

    def calculate_total(self, subtotal: float, tax: float) -> float:
        """
        Calculate the total of the invoice.

        Args:
        - subtotal (float): The subtotal of the invoice.
        - tax (float): The tax of the invoice.

        Returns:
        - float: The total of the invoice.
        """
        return subtotal + tax

    def generate_invoice(self, tax_rate: float = 0.08) -> Dict:
        """
        Generate the invoice.

        Args:
        - tax_rate (float, optional): The tax rate. Defaults to 0.08.

        Returns:
        - Dict: The invoice.
        """
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal, tax_rate)
        total = self.calculate_total(subtotal, tax)

        invoice = {
            'company_name': self.company_name,
            'company_address': self.company_address,
            'client_name': self.client_name,
            'client_address': self.client_address,
            'services': self.services,
            'subtotal': subtotal,
            'tax': tax,
            'total': total,
            'date': date.today().strftime("%Y-%m-%d")
        }

        return invoice

    def print_invoice(self, invoice: Dict):
        """
        Print the invoice.

        Args:
        - invoice (Dict): The invoice.
        """
        print(f"Invoice for {invoice['client_name']}")
        print(f"Date: {invoice['date']}")
        print(f"Company: {invoice['company_name']}")
        print(f"Address: {invoice['company_address']}")
        print(f"Client: {invoice['client_name']}")
        print(f"Address: {invoice['client_address']}")
        print("Services:")
        for service in invoice['services']:
            print(f"- {service['name']}: {service['quantity']} x ${service['unit_price']:.2f} = ${service['quantity'] * service['unit_price']:.2f}")
        print(f"Subtotal: ${invoice['subtotal']:.2f}")
        print(f"Tax (8%): ${invoice['tax']:.2f}")
        print(f"Total: ${invoice['total']:.2f}")


def main():
    try:
        company_name = "株式会社タイコーテクノ"
        company_address = "123 Main St, Tokyo, Japan"
        client_name = "John Doe"
        client_address = "456 Elm St, Tokyo, Japan"

        invoice = Invoice(company_name, company_address, client_name, client_address)

        invoice.add_service("Concrete Pole Installation", 10, 5000.0)
        invoice.add_service("Fence Construction", 100, 50.0)

        generated_invoice = invoice.generate_invoice()
        invoice.print_invoice(generated_invoice)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
