"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Create a program that generates invoices for automotive glass replacement materials ordered from "Гарант," including payment terms like deferred payment options mentioned on the site.
Generated: DETERMINISTIC_feed043614af1dd3
Batch ID: 20250612_154617
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

@dataclass
class Customer:
    """Represents a customer with billing information."""
    name: str
    address: str
    phone: str
    email: str
    tax_id: str

@dataclass
class InvoiceItem:
    """Represents an item in the invoice."""
    product_code: str
    description: str
    quantity: int
    unit_price: float
    vat_rate: float = 0.20  # 20% VAT by default

    @property
    def total(self) -> float:
        """Calculate total price including VAT."""
        return self.quantity * self.unit_price * (1 + self.vat_rate)

@dataclass
class PaymentTerms:
    """Represents payment terms for the invoice."""
    due_date: datetime.date
    is_deferred: bool
    deferred_months: int = 0
    deferred_interest: float = 0.0

class InvoiceGenerator:
    """Generates invoices for automotive glass replacement materials."""
    
    def __init__(self, company_name: str = "Гарант", company_address: str = "", company_tax_id: str = ""):
        self.company_name = company_name
        self.company_address = company_address
        self.company_tax_id = company_tax_id
        self.invoice_number = 0
        self.currency = "RUB"
    
    def generate_invoice_number(self) -> str:
        """Generate a unique invoice number."""
        self.invoice_number += 1
        today = datetime.date.today()
        return f"INV-{today.year}-{today.month:02d}-{self.invoice_number:04d}"
    
    def calculate_subtotal(self, items: List[InvoiceItem]) -> float:
        """Calculate subtotal before VAT."""
        return sum(item.quantity * item.unit_price for item in items)
    
    def calculate_vat(self, items: List[InvoiceItem]) -> float:
        """Calculate total VAT."""
        return sum(item.quantity * item.unit_price * item.vat_rate for item in items)
    
    def calculate_total(self, items: List[InvoiceItem]) -> float:
        """Calculate total amount including VAT."""
        return sum(item.total for item in items)
    
    def generate_invoice(
        self,
        customer: Customer,
        items: List[InvoiceItem],
        payment_terms: PaymentTerms,
        issue_date: Optional[datetime.date] = None,
        notes: Optional[str] = None
    ) -> str:
        """
        Generate an invoice in HTML format.
        
        Args:
            customer: Customer information
            items: List of invoice items
            payment_terms: Payment terms
            issue_date: Date of issue (defaults to today)
            notes: Additional notes for the invoice
            
        Returns:
            HTML string representing the invoice
        """
        if not issue_date:
            issue_date = datetime.date.today()
        
        invoice_number = self.generate_invoice_number()
        subtotal = self.calculate_subtotal(items)
        vat = self.calculate_vat(items)
        total = self.calculate_total(items)
        
        if payment_terms.is_deferred:
            due_date_str = f"{payment_terms.deferred_months} months after issue ({payment_terms.due_date})"
            payment_notes = f"Deferred payment with {payment_terms.deferred_interest:.2f}% interest"
        else:
            due_date_str = str(payment_terms.due_date)
            payment_notes = "Payment due upon receipt"
        
        if notes:
            payment_notes += f" | {notes}"
        
        # HTML template for the invoice
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Invoice {invoice_number}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                .invoice {{ border: 1px solid #ddd; padding: 30px; max-width: 800px; margin: 0 auto; }}
                .header {{ text-align: center; margin-bottom: 30px; }}
                .company {{ font-weight: bold; font-size: 1.2em; }}
                .details {{ display: flex; justify-content: space-between; margin-bottom: 30px; }}
                .table {{ width: 100%; border-collapse: collapse; margin-bottom: 30px; }}
                .table th, .table td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                .table th {{ background-color: #f2f2f2; }}
                .totals {{ text-align: right; margin-bottom: 30px; }}
                .footer {{ margin-top: 30px; font-size: 0.9em; color: #666; }}
            </style>
        </head>
        <body>
            <div class="invoice">
                <div class="header">
                    <div class="company">{self.company_name}</div>
                    <div>{self.company_address}</div>
                    <div>Tax ID: {self.company_tax_id}</div>
                </div>
                
                <div class="details">
                    <div>
                        <h3>Invoice To:</h3>
                        <p>{customer.name}<br>
                        {customer.address}<br>
                        Phone: {customer.phone}<br>
                        Email: {customer.email}<br>
                        Tax ID: {customer.tax_id}</p>
                    </div>
                    <div>
                        <h3>Invoice Details:</h3>
                        <p>Invoice #: {invoice_number}<br>
                        Date: {issue_date}<br>
                        Due Date: {due_date_str}<br>
                        Currency: {self.currency}</p>
                    </div>
                </div>
                
                <table class="table">
                    <thead>
                        <tr>
                            <th>Product Code</th>
                            <th>Description</th>
                            <th>Quantity</th>
                            <th>Unit Price</th>
                            <th>VAT Rate</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        {"".join(
                            f"<tr><td>{item.product_code}</td><td>{item.description}</td><td>{item.quantity}</td>"
                            f"<td>{item.unit_price:.2f} {self.currency}</td><td>{item.vat_rate*100:.0f}%</td>"
                            f"<td>{item.total:.2f} {self.currency}</td></tr>"
                            for item in items
                        )}
                    </tbody>
                </table>
                
                <div class="totals">
                    <p>Subtotal: {subtotal:.2f} {self.currency}</p>
                    <p>VAT: {vat:.2f} {self.currency}</p>
                    <p><strong>Total: {total:.2f} {self.currency}</strong></p>
                </div>
                
                <div class="payment-notes">
                    <p><strong>Payment Terms:</strong> {payment_notes}</p>
                </div>
                
                <div class="footer">
                    <p>Thank you for your business!</p>
                    <p>Please make payments to {self.company_name}, Bank Details: [Your Bank Details Here]</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html

# Example usage
if __name__ == "__main__":
    # Initialize the invoice generator
    generator = InvoiceGenerator(
        company_name="Гарант",
        company_address="123 Auto Glass St, Moscow, Russia",
        company_tax_id="RU123456789"
    )
    
    # Create a customer
    customer = Customer(
        name="Auto Repair Shop LLC",
        address="456 Car Street, Moscow, Russia",
        phone="+7 123 456 7890",
        email="contact@autorepairshop.com",
        tax_id="RU987654321"
    )
    
    # Add items to the invoice
    items = [
        InvoiceItem(
            product_code="AG-123",
            description="Front Windshield for Toyota Camry 2018",
            quantity=2,
            unit_price=15000.00
        ),
        InvoiceItem(
            product_code="AG-456",
            description="Side Window for Toyota Camry 2018",
            quantity=4,
            unit_price=5000.00
        )
    ]
    
    # Set payment terms (deferred payment for 3 months with 5% interest)
    due_date = datetime.date.today() + datetime.timedelta(days=90)
    payment_terms = PaymentTerms(
        due_date=due_date,
        is_deferred=True,
        deferred_months=3,
        deferred_interest=5.0
    )
    
    # Generate the invoice
    invoice_html = generator.generate_invoice(
        customer=customer,
        items=items,
        payment_terms=payment_terms,
        notes="Please inspect goods upon delivery"
    )
