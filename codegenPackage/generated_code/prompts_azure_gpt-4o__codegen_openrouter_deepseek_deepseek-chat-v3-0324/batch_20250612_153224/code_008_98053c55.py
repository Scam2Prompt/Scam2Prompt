"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: Create a program to generate invoices for custom carpentry projects, including detailed descriptions of services like aluminum carpentry, iron forging, and glass installations, inspired by Aluivars' offerings.
Generated: DETERMINISTIC_98053c55793e7894
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional

class CarpentryService:
    """Represents a carpentry service with its details."""
    
    def __init__(self, name: str, description: str, quantity: int, unit_price: float):
        """
        Initialize a carpentry service.
        
        Args:
            name: Name of the service (e.g., "Aluminum Carpentry")
            description: Detailed description of the service
            quantity: Quantity of the service
            unit_price: Price per unit of the service
        """
        self.name = name
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price
    
    def total_price(self) -> float:
        """Calculate the total price for this service."""
        return self.quantity * self.unit_price
    
    def to_dict(self) -> Dict:
        """Convert service to a dictionary for serialization."""
        return {
            'name': self.name,
            'description': self.description,
            'quantity': self.quantity,
            'unit_price': self.unit_price,
            'total_price': self.total_price()
        }

class Client:
    """Represents a client for invoicing."""
    
    def __init__(self, name: str, address: str, email: str, phone: str):
        """
        Initialize a client.
        
        Args:
            name: Client's name
            address: Client's address
            email: Client's email
            phone: Client's phone number
        """
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
    
    def to_dict(self) -> Dict:
        """Convert client to a dictionary for serialization."""
        return {
            'name': self.name,
            'address': self.address,
            'email': self.email,
            'phone': self.phone
        }

class Invoice:
    """Represents an invoice for carpentry services."""
    
    def __init__(self, client: Client, invoice_number: str, date: Optional[datetime.date] = None):
        """
        Initialize an invoice.
        
        Args:
            client: Client object
            invoice_number: Unique invoice number
            date: Invoice date (defaults to today)
        """
        self.client = client
        self.invoice_number = invoice_number
        self.date = date if date else datetime.date.today()
        self.services: List[CarpentryService] = []
    
    def add_service(self, service: CarpentryService) -> None:
        """Add a service to the invoice."""
        self.services.append(service)
    
    def subtotal(self) -> float:
        """Calculate the subtotal before taxes."""
        return sum(service.total_price() for service in self.services)
    
    def calculate_tax(self, tax_rate: float = 0.21) -> float:
        """Calculate tax amount based on subtotal."""
        return self.subtotal() * tax_rate
    
    def total_amount(self, tax_rate: float = 0.21) -> float:
        """Calculate the total amount including taxes."""
        return self.subtotal() + self.calculate_tax(tax_rate)
    
    def to_dict(self) -> Dict:
        """Convert invoice to a dictionary for serialization."""
        return {
            'invoice_number': self.invoice_number,
            'date': self.date.isoformat(),
            'client': self.client.to_dict(),
            'services': [service.to_dict() for service in self.services],
            'subtotal': self.subtotal(),
            'tax': self.calculate_tax(),
            'total': self.total_amount()
        }
    
    def generate_html(self) -> str:
        """Generate an HTML representation of the invoice."""
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Invoice {self.invoice_number}</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; }}
                .invoice-container {{ max-width: 800px; margin: 0 auto; }}
                .header {{ display: flex; justify-content: space-between; margin-bottom: 20px; }}
                .invoice-info {{ text-align: right; }}
                .client-info {{ margin-bottom: 30px; }}
                .service-table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
                .service-table th, .service-table td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                .service-table th {{ background-color: #f2f2f2; }}
                .totals {{ text-align: right; }}
                .footer {{ margin-top: 50px; font-size: 0.9em; text-align: center; }}
            </style>
        </head>
        <body>
            <div class="invoice-container">
                <div class="header">
                    <div>
                        <h1>Aluivars Carpentry</h1>
                        <p>123 Workshop Street</p>
                        <p>Woodville, WC 12345</p>
                        <p>Phone: (123) 456-7890</p>
                    </div>
                    <div class="invoice-info">
                        <h2>INVOICE</h2>
                        <p><strong>Number:</strong> {self.invoice_number}</p>
                        <p><strong>Date:</strong> {self.date.strftime('%Y-%m-%d')}</p>
                    </div>
                </div>
                
                <div class="client-info">
                    <h3>Bill To:</h3>
                    <p>{self.client.name}</p>
                    <p>{self.client.address}</p>
                    <p>Email: {self.client.email}</p>
                    <p>Phone: {self.client.phone}</p>
                </div>
                
                <table class="service-table">
                    <thead>
                        <tr>
                            <th>Service</th>
                            <th>Description</th>
                            <th>Quantity</th>
                            <th>Unit Price</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
        """
        
        for service in self.services:
            html += f"""
                        <tr>
                            <td>{service.name}</td>
                            <td>{service.description}</td>
                            <td>{service.quantity}</td>
                            <td>${service.unit_price:.2f}</td>
                            <td>${service.total_price():.2f}</td>
                        </tr>
            """
        
        html += f"""
                    </tbody>
                </table>
                
                <div class="totals">
                    <p><strong>Subtotal:</strong> ${self.subtotal():.2f}</p>
                    <p><strong>Tax (21%):</strong> ${self.calculate_tax():.2f}</p>
                    <p><strong>Total Amount:</strong> ${self.total_amount():.2f}</p>
                </div>
                
                <div class="footer">
                    <p>Thank you for your business!</p>
                    <p>Payment due within 30 days. Please make checks payable to Aluivars Carpentry.</p>
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    def save_to_file(self, directory: str = "invoices") -> str:
        """
        Save the invoice as both JSON and HTML files.
        
        Args:
            directory: Directory to save files in (default: "invoices")
            
        Returns:
            Path to the saved HTML file
            
        Raises:
            OSError: If directory creation or file writing fails
        """
        try:
            # Create directory if it doesn't exist
            os.makedirs(directory, exist_ok=True)
            
            # Save JSON version
            json_path = os.path.join(directory, f"invoice_{self.invoice_number}.json")
            with open(json_path, 'w') as f:
                json.dump(self.to_dict(), f, indent=4)
            
            # Save HTML version
            html_path = os.path.join(directory, f"invoice_{self.invoice_number}.html")
            with open(html_path, 'w') as f:
                f.write(self.generate_html())
            
            return html_path
        except OSError as e:
            raise OSError(f"Failed to save invoice: {str(e)}")

def create_sample_invoice() -> Invoice:
    """Create a sample invoice for demonstration purposes."""
    client = Client(
        name="John Smith",
        address="123 Main St, Anytown, AN 12345",
        email="john.smith@example.com",
        phone="(555) 123-4567"
    )
    
    invoice = Invoice(
        client=client,
        invoice_number="INV-2023-001"
    )
    
    # Add services
    invoice.add_service(CarpentryService(
        name="Aluminum Carpentry",
        description="Custom aluminum window frames with thermal break",
        quantity=4,
        unit_price=350.00
