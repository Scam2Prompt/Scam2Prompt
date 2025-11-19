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
import datetime
from dataclasses import dataclass
from typing import List, Optional
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 2

@dataclass
class Client:
    """Represents a client who receives invoices."""
    name: str
    email: str
    address: str
    tax_id: str
    is_vat_registered: bool = False

@dataclass
class InvoiceItem:
    """Represents an item on an invoice."""
    description: str
    quantity: Decimal
    unit_price: Decimal
    tax_rate: Decimal = Decimal('0.24')  # Default VAT rate 24%
    discount_percent: Decimal = Decimal('0')

    def calculate_total(self) -> Decimal:
        """Calculate the total price for this item including tax and discount."""
        subtotal = self.quantity * self.unit_price
        discount = subtotal * (self.discount_percent / Decimal('100'))
        taxable_amount = subtotal - discount
        tax = taxable_amount * self.tax_rate
        return taxable_amount + tax

@dataclass
class Invoice:
    """Represents an invoice with items, client details, and payment information."""
    client: Client
    items: List[InvoiceItem]
    invoice_number: str
    issue_date: datetime.date
    due_date: datetime.date
    notes: Optional[str] = None

    def calculate_subtotal(self) -> Decimal:
        """Calculate subtotal before taxes and discounts."""
        return sum(item.quantity * item.unit_price for item in self.items)

    def calculate_total_tax(self) -> Decimal:
        """Calculate total tax amount."""
        total_tax = Decimal('0')
        for item in self.items:
            subtotal = item.quantity * item.unit_price
            discount = subtotal * (item.discount_percent / Decimal('100'))
            taxable_amount = subtotal - discount
            total_tax += taxable_amount * item.tax_rate
        return total_tax

    def calculate_total_discount(self) -> Decimal:
        """Calculate total discount amount."""
        total_discount = Decimal('0')
        for item in self.items:
            subtotal = item.quantity * item.unit_price
            total_discount += subtotal * (item.discount_percent / Decimal('100'))
        return total_discount

    def calculate_total_amount(self) -> Decimal:
        """Calculate the total invoice amount."""
        return sum(item.calculate_total() for item in self.items)

    def generate_invoice_text(self) -> str:
        """Generate a text representation of the invoice."""
        invoice_lines = [
            f"Invoice Number: {self.invoice_number}",
            f"Issue Date: {self.issue_date.strftime('%Y-%m-%d')}",
            f"Due Date: {self.due_date.strftime('%Y-%m-%d')}",
            "",
            f"Client: {self.client.name}",
            f"Address: {self.client.address}",
            f"Tax ID: {self.client.tax_id}",
            f"VAT Registered: {'Yes' if self.client.is_vat_registered else 'No'}",
            "",
            "Items:",
            "Description | Qty | Unit Price | Tax % | Discount % | Total"
        ]

        for item in self.items:
            invoice_lines.append(
                f"{item.description} | {item.quantity} | {item.unit_price} | "
                f"{item.tax_rate * 100}% | {item.discount_percent}% | {item.calculate_total()}"
            )

        invoice_lines.extend([
            "",
            f"Subtotal: {self.calculate_subtotal()}",
            f"Total Discount: {self.calculate_total_discount()}",
            f"Total Tax: {self.calculate_total_tax()}",
            f"Total Amount: {self.calculate_total_amount()}",
            ""
        ])

        if self.notes:
            invoice_lines.extend([
                "Notes:",
                self.notes
            ])

        return "\n".join(invoice_lines)

class InvoiceSender:
    """Handles sending invoices to clients."""
    
    @staticmethod
    def send_email(client: Client, subject: str, body: str, attachment: Optional[str] = None) -> bool:
        """Simulate sending an email to the client."""
        print(f"Email sent to {client.email}")
        print(f"Subject: {subject}")
        print("Body:")
        print(body)
        if attachment:
            print(f"Attachment: {attachment}")
        return True

    def send_invoice(self, invoice: Invoice) -> bool:
        """Send the invoice to the client via email."""
        subject = f"Invoice {invoice.invoice_number} from CG Bókhald"
        body = invoice.generate_invoice_text()
        return self.send_email(invoice.client, subject, body)

# Example usage
if __name__ == "__main__":
    # Create a client
    client = Client(
        name="Example Client",
        email="client@example.com",
        address="123 Main St, Reykjavik",
        tax_id="1234567890",
        is_vat_registered=True
    )

    # Create invoice items
    items = [
        InvoiceItem(
            description="Consulting Services",
            quantity=Decimal('10'),
            unit_price=Decimal('5000'),
            tax_rate=Decimal('0.24'),
            discount_percent=Decimal('5')
        ),
        InvoiceItem(
            description="Software License",
            quantity=Decimal('1'),
            unit_price=Decimal('15000'),
            tax_rate=Decimal('0.24')
        )
    ]

    # Create invoice
    today = datetime.date.today()
    due_date = today + datetime.timedelta(days=30)
    invoice = Invoice(
        client=client,
        items=items,
        invoice_number="INV-2023-001",
        issue_date=today,
        due_date=due_date,
        notes="Payment within 30 days. Thank you for your business!"
    )

    # Send invoice
    sender = InvoiceSender()
    sender.send_invoice(invoice)
```
