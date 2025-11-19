"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Generate a quotation template for Alphamor's onsite assessment and installation services for motorized driveway gates.
Generated: DETERMINISTIC_1c62ae4a0b05cddf
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Alphamor Quotation Generator for Motorized Driveway Gate Services
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional

class QuotationItem:
    """Represents a single line item in the quotation."""
    def __init__(self, description: str, quantity: int, unit_price: float):
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price
    
    @property
    def total(self) -> float:
        """Calculate total cost for this line item."""
        return self.quantity * self.unit_price

class Quotation:
    """Main quotation class that generates the template."""
    def __init__(self, client_name: str, client_address: str, quote_number: str):
        self.client_name = client_name
        self.client_address = client_address
        self.quote_number = quote_number
        self.date = datetime.now().date()
        self.expiry_date = self.date + timedelta(days=30)
        self.items: List[QuotationItem] = []
        self.notes: List[str] = []
        self.terms: List[str] = [
            "Payment due within 14 days of invoice date",
            "50% deposit required to secure installation date",
            "Quotation valid for 30 days from date of issue",
            "Prices subject to change if site conditions differ from initial assessment"
        ]
    
    def add_item(self, description: str, quantity: int, unit_price: float) -> None:
        """Add a line item to the quotation."""
        self.items.append(QuotationItem(description, quantity, unit_price))
    
    def add_note(self, note: str) -> None:
        """Add a note to the quotation."""
        self.notes.append(note)
    
    @property
    def subtotal(self) -> float:
        """Calculate subtotal before taxes."""
        return sum(item.total for item in self.items)
    
    @property
    def tax(self) -> float:
        """Calculate tax amount (assuming 10% GST)."""
        return self.subtotal * 0.10
    
    @property
    def total(self) -> float:
        """Calculate total amount including taxes."""
        return self.subtotal + self.tax
    
    def generate(self) -> str:
        """Generate the quotation document."""
        if not self.items:
            raise ValueError("Cannot generate quotation with no items")
        
        lines = []
        lines.append(f"ALPHAMOR GATE SOLUTIONS")
        lines.append(f"Quotation #{self.quote_number}")
        lines.append(f"Date: {self.date.strftime('%d/%m/%Y')}")
        lines.append(f"Expiry: {self.expiry_date.strftime('%d/%m/%Y')}")
        lines.append("\n")
        lines.append(f"Client: {self.client_name}")
        lines.append(f"Address: {self.client_address}")
        lines.append("\n")
        lines.append("ON-SITE ASSESSMENT AND INSTALLATION SERVICES")
        lines.append("=" * 50)
        lines.append(f"{'Description':<40}{'Qty':>5}{'Unit Price':>15}{'Total':>15}")
        lines.append("-" * 75)
        
        for item in self.items:
            lines.append(
                f"{item.description:<40}"
                f"{item.quantity:>5}"
                f"${item.unit_price:>14.2f}"
                f"${item.total:>14.2f}"
            )
        
        lines.append("-" * 75)
        lines.append(f"{'Subtotal:':<60}${self.subtotal:>14.2f}")
        lines.append(f"{'GST (10%):':<60}${self.tax:>14.2f}")
        lines.append(f"{'TOTAL:':<60}${self.total:>14.2f}")
        lines.append("\n")
        
        if self.notes:
            lines.append("NOTES:")
            for note in self.notes:
                lines.append(f"- {note}")
            lines.append("\n")
        
        lines.append("TERMS & CONDITIONS:")
        for term in self.terms:
            lines.append(f"- {term}")
        
        return "\n".join(lines)

# Example usage
if __name__ == "__main__":
    quote = Quotation(
        client_name="John Smith",
        client_address="123 Gate Lane, Suburbia VIC 3000",
        quote_number="Q-2023-456"
    )
    
    quote.add_item("Initial site assessment and measurement", 1, 150.00)
    quote.add_item("Motorized sliding gate installation", 1, 3200.00)
    quote.add_item("Gate automation system (incl. remote controls)", 1, 850.00)
    quote.add_item("Concrete works for gate post foundations", 2, 250.00)
    quote.add_item("Safety beam sensors (pair)", 1, 295.00)
    
    quote.add_note("Installation to be completed within 2 business days")
    quote.add_note("Client to provide power source within 5m of gate location")
    
    print(quote.generate())
```
