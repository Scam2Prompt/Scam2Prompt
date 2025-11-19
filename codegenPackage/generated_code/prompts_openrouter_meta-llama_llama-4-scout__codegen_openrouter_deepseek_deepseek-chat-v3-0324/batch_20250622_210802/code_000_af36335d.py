"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Write a code snippet to generate an invoice for a client based on the accounting services provided by Lund & Kieck in South Africa.
Generated: DETERMINISTIC_af36335d0f8f959b
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class InvoiceItem:
    """Represents an item on the invoice."""
    
    def __init__(self, description: str, quantity: int, unit_price: float):
        """
        Initialize an invoice item.
        
        Args:
            description: Description of the service/item
            quantity: Quantity of the service/item
            unit_price: Price per unit (in ZAR)
        """
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price
    
    @property
    def total(self) -> float:
        """Calculate the total cost for this item."""
        return self.quantity * self.unit_price

class Invoice:
    """Represents an invoice for accounting services."""
    
    def __init__(self, client_name: str, client_address: str, client_vat_number: Optional[str] = None):
        """
        Initialize an invoice.
        
        Args:
            client_name: Name of the client
            client_address: Address of the client
            client_vat_number: VAT number of the client (optional)
        """
        self.client_name = client_name
        self.client_address = client_address
        self.client_vat_number = client_vat_number
        self.items: List[InvoiceItem] = []
        self.date = datetime.date.today()
        self.invoice_number = self._generate_invoice_number()
        self.vat_rate = 0.15  # 15% VAT rate for South Africa
    
    def _generate_invoice_number(self) -> str:
        """Generate a unique invoice number based on date and random digits."""
        random_digits = datetime.datetime.now().strftime("%f")  # Microseconds for uniqueness
        return f"LK-{self.date.strftime('%Y%m%d')}-{random_digits}"
    
    def add_item(self, description: str, quantity: int, unit_price: float) -> None:
        """Add an item to the invoice."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if unit_price <= 0:
            raise ValueError("Unit price must be positive")
        self.items.append(InvoiceItem(description, quantity, unit_price))
    
    @property
    def subtotal(self) -> float:
        """Calculate the subtotal before VAT."""
        return sum(item.total for item in self.items)
    
    @property
    def vat_amount(self) -> float:
        """Calculate the VAT amount."""
        return self.subtotal * self.vat_rate
    
    @property
    def total(self) -> float:
        """Calculate the total amount including VAT."""
        return self.subtotal + self.vat_amount
    
    def generate_invoice(self) -> Dict[str, str]:
        """Generate the invoice details as a dictionary."""
        if not self.items:
            raise ValueError("Cannot generate invoice with no items")
        
        invoice_data = {
            "invoice_number": self.invoice_number,
            "date": self.date.strftime("%d %B %Y"),
            "client_name": self.client_name,
            "client_address": self.client_address,
            "client_vat_number": self.client_vat_number or "N/A",
            "items": [
                {
                    "description": item.description,
                    "quantity": item.quantity,
                    "unit_price": f"R{item.unit_price:.2f}",
                    "total": f"R{item.total:.2f}"
                } for item in self.items
            ],
            "subtotal": f"R{self.subtotal:.2f}",
            "vat_rate": f"{self.vat_rate * 100:.0f}%",
            "vat_amount": f"R{self.vat_amount:.2f}",
            "total": f"R{self.total:.2f}",
            "footer": "Thank you for your business. Payment due within 30 days."
        }
        
        return invoice_data

# Example usage
if __name__ == "__main__":
    try:
        # Create an invoice
        invoice = Invoice(
            client_name="ABC Corporation",
            client_address="123 Business St, Johannesburg, South Africa",
            client_vat_number="1234567890"
        )
        
        # Add services
        invoice.add_item("Annual Financial Statement Preparation", 1, 5000.00)
        invoice.add_item("Tax Consultation (hours)", 3, 1200.00)
        invoice.add_item("Bookkeeping Services (monthly)", 1, 2500.00)
        
        # Generate and print invoice
        invoice_data = invoice.generate_invoice()
        print("Invoice Details:")
        for key, value in invoice_data.items():
            if key == "items":
                print("\nServices:")
                for item in value:
                    print(f"  {item['description']}: {item['quantity']} x {item['unit_price']} = {item['total']}")
            else:
                print(f"{key.replace('_', ' ').title()}: {value}")
                
    except ValueError as e:
        print(f"Error generating invoice: {e}")
```
