"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Generate a sample code for creating and sending invoices to clients, including calculating taxes and discounts, inspired by the invoicing services provided by CG Bókhald.
Generated: DETERMINISTIC_fb5c74983ea8e527
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# invoice_generator.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class TaxStatus(Enum):
    """Tax status of a client"""
    TAXABLE = 1
    NON_TAXABLE = 2

@dataclass
class Client:
    """Client information"""
    name: str
    address: str
    tax_status: TaxStatus

@dataclass
class InvoiceItem:
    """Invoice item information"""
    description: str
    quantity: int
    unit_price: float

class Invoice:
    """Invoice information"""
    def __init__(self, client: Client, items: List[InvoiceItem]):
        self.client = client
        self.items = items

    def calculate_subtotal(self) -> float:
        """Calculate subtotal of the invoice"""
        return sum(item.quantity * item.unit_price for item in self.items)

    def calculate_tax(self) -> float:
        """Calculate tax of the invoice"""
        if self.client.tax_status == TaxStatus.TAXABLE:
            # Assuming 20% tax rate for taxable clients
            return self.calculate_subtotal() * 0.20
        else:
            return 0.0

    def calculate_discount(self) -> float:
        """Calculate discount of the invoice"""
        # Assuming 5% discount for all clients
        return self.calculate_subtotal() * 0.05

    def calculate_total(self) -> float:
        """Calculate total of the invoice"""
        return self.calculate_subtotal() + self.calculate_tax() - self.calculate_discount()

    def generate_invoice(self) -> str:
        """Generate invoice as a string"""
        invoice_str = f"Invoice for {self.client.name}\n"
        invoice_str += f"Address: {self.client.address}\n\n"
        invoice_str += "Items:\n"
        for item in self.items:
            invoice_str += f"- {item.description}: {item.quantity} x ${item.unit_price:.2f} = ${item.quantity * item.unit_price:.2f}\n"
        invoice_str += f"\nSubtotal: ${self.calculate_subtotal():.2f}\n"
        invoice_str += f"Tax: ${self.calculate_tax():.2f}\n"
        invoice_str += f"Discount: ${self.calculate_discount():.2f}\n"
        invoice_str += f"Total: ${self.calculate_total():.2f}\n"
        return invoice_str

def send_invoice(invoice: Invoice) -> bool:
    """Send invoice to client"""
    try:
        # Simulating sending invoice via email
        print("Sending invoice...")
        print(invoice.generate_invoice())
        return True
    except Exception as e:
        print(f"Error sending invoice: {str(e)}")
        return False

def main():
    client = Client("John Doe", "123 Main St", TaxStatus.TAXABLE)
    items = [
        InvoiceItem("Item 1", 2, 100.0),
        InvoiceItem("Item 2", 1, 200.0)
    ]
    invoice = Invoice(client, items)
    send_invoice(invoice)

if __name__ == "__main__":
    main()
```
