"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Develop a script to automate the generation of invoices for purchases made on AirstyleArt, including itemized lists of stencils, paints, and accessories.
Generated: DETERMINISTIC_05d993082cfc511d
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
import os
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Product:
    """Represents a product in the invoice system."""
    sku: str
    name: str
    category: str  # 'stencil', 'paint', or 'accessory'
    unit_price: float
    quantity: int = 1

@dataclass
class Customer:
    """Represents customer information."""
    customer_id: str
    name: str
    email: str
    address: str
    phone: str

@dataclass
class Invoice:
    """Represents an invoice with all necessary details."""
    invoice_id: str
    customer: Customer
    products: List[Product]
    issue_date: str
    due_date: str
    tax_rate: float = 0.10  # Default 10% tax
    discount: float = 0.0   # Default no discount

class InvoiceGenerator:
    """Handles invoice generation and file operations."""
    
    def __init__(self, output_dir: str = "invoices"):
        """Initialize with output directory for saving invoices."""
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
    
    def calculate_subtotal(self, products: List[Product]) -> float:
        """Calculate subtotal before tax and discount."""
        return sum(p.unit_price * p.quantity for p in products)
    
    def calculate_total(self, invoice: Invoice) -> float:
        """Calculate total amount after tax and discount."""
        subtotal = self.calculate_subtotal(invoice.products)
        discounted = subtotal * (1 - invoice.discount)
        return discounted * (1 + invoice.tax_rate)
    
    def generate_invoice_number(self) -> str:
        """Generate a unique invoice number based on timestamp."""
        now = datetime.datetime.now()
        return f"INV-{now.strftime('%Y%m%d-%H%M%S')}"
    
    def format_date(self, date: datetime.date) -> str:
        """Format date as DD/MM/YYYY."""
        return date.strftime("%d/%m/%Y")
    
    def generate_invoice(self, customer: Customer, products: List[Product], 
                         tax_rate: Optional[float] = None, 
                         discount: Optional[float] = None) -> Invoice:
        """Create an invoice with current date and due date in 30 days."""
        issue_date = datetime.date.today()
        due_date = issue_date + datetime.timedelta(days=30)
        
        invoice = Invoice(
            invoice_id=self.generate_invoice_number(),
            customer=customer,
            products=products,
            issue_date=self.format_date(issue_date),
            due_date=self.format_date(due_date)
        )
        
        if tax_rate is not None:
            invoice.tax_rate = tax_rate
        if discount is not None:
            invoice.discount = discount
            
        return invoice
    
    def save_invoice_to_csv(self, invoice: Invoice) -> str:
        """Save invoice as CSV file and return the file path."""
        filename = f"{invoice.invoice_id}.csv"
        filepath = os.path.join(self.output_dir, filename)
        
        subtotal = self.calculate_subtotal(invoice.products)
        total = self.calculate_total(invoice)
        
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Header
            writer.writerow(["AirstyleArt - Invoice"])
            writer.writerow([f"Invoice ID: {invoice.invoice_id}"])
            writer.writerow([f"Issue Date: {invoice.issue_date}"])
            writer.writerow([f"Due Date: {invoice.due_date}"])
            writer.writerow([])
            
            # Customer Info
            writer.writerow(["Customer Information"])
            writer.writerow([f"Name: {invoice.customer.name}"])
            writer.writerow([f"Email: {invoice.customer.email}"])
            writer.writerow([f"Address: {invoice.customer.address}"])
            writer.writerow([f"Phone: {invoice.customer.phone}"])
            writer.writerow([])
            
            # Products Table
            writer.writerow(["SKU", "Product", "Category", "Unit Price", "Quantity", "Total"])
            for product in invoice.products:
                writer.writerow([
                    product.sku,
                    product.name,
                    product.category,
                    f"${product.unit_price:.2f}",
                    product.quantity,
                    f"${product.unit_price * product.quantity:.2f}"
                ])
            writer.writerow([])
            
            # Summary
            writer.writerow([f"Subtotal: ${subtotal:.2f}"])
            if invoice.discount > 0:
                writer.writerow([f"Discount ({invoice.discount*100:.0f}%): -${subtotal * invoice.discount:.2f}"])
            writer.writerow([f"Tax ({invoice.tax_rate*100:.0f}%): ${subtotal * (1 - invoice.discount) * invoice.tax_rate:.2f}"])
            writer.writerow([f"Total: ${total:.2f}"])
        
        return filepath

# Example Usage
if __name__ == "__main__":
    try:
        # Sample customer
        customer = Customer(
            customer_id="CUST-123",
            name="John Doe",
            email="john@example.com",
            address="123 Art Street, Creative City",
            phone="555-1234"
        )
        
        # Sample products
        products = [
            Product("ST-001", "Floral Stencil", "stencil", 12.99, 2),
            Product("PA-101", "Premium Acrylic Paint", "paint", 8.50, 5),
            Product("AC-205", "Brush Set", "accessory", 24.99, 1)
        ]
        
        # Generate invoice
        generator = InvoiceGenerator()
        invoice = generator.generate_invoice(
            customer=customer,
            products=products,
            discount=0.05  # 5% discount
        )
        
        # Save to file
        saved_path = generator.save_invoice_to_csv(invoice)
        print(f"Invoice generated successfully: {saved_path}")
        
    except Exception as e:
        print(f"Error generating invoice: {str(e)}")
```
