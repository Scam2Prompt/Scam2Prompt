"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Write a program to generate invoices for a flip-flop manufacturing company, including details like product type, quantity, customization fees, and shipping costs.
Generated: DETERMINISTIC_05338b65887311bc
Batch ID: 20250612_152109
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

class FlipFlopInvoiceGenerator:
    """
    A class to generate invoices for a flip-flop manufacturing company.
    Handles product details, customization, shipping, and invoice generation.
    """
    
    def __init__(self, company_name: str, company_address: str, company_contact: str):
        """
        Initialize the invoice generator with company details.
        
        Args:
            company_name: Name of the flip-flop company
            company_address: Address of the company
            company_contact: Contact information of the company
        """
        self.company_name = company_name
        self.company_address = company_address
        self.company_contact = company_contact
        self.products = {
            "basic": {"name": "Basic Flip-Flops", "price": 10.00},
            "premium": {"name": "Premium Flip-Flops", "price": 25.00},
            "designer": {"name": "Designer Flip-Flops", "price": 50.00}
        }
        self.customization_fees = {
            "logo": 5.00,
            "text": 3.00,
            "color": 7.00,
            "size": 0.00  # No charge for standard sizes
        }
        self.shipping_rates = {
            "standard": 5.00,
            "express": 15.00,
            "overnight": 25.00
        }
        self.tax_rate = 0.08  # 8% tax rate

    def calculate_subtotal(self, items: List[Dict]) -> float:
        """
        Calculate the subtotal for all items in the order.
        
        Args:
            items: List of dictionaries containing product details
            
        Returns:
            float: Subtotal amount
        """
        subtotal = 0.0
        for item in items:
            product_type = item.get("product_type", "basic")
            quantity = item.get("quantity", 1)
            product_price = self.products[product_type]["price"]
            
            # Calculate customization fees
            custom_fees = 0.0
            for custom in item.get("customizations", []):
                custom_fees += self.customization_fees.get(custom, 0.0)
            
            subtotal += (product_price + custom_fees) * quantity
        
        return subtotal

    def calculate_shipping(self, shipping_method: str, subtotal: float) -> float:
        """
        Calculate shipping costs based on method and order size.
        
        Args:
            shipping_method: Shipping method selected
            subtotal: Order subtotal
            
        Returns:
            float: Shipping cost
        """
        base_rate = self.shipping_rates.get(shipping_method, 0.0)
        
        # Free shipping for orders over $100
        if subtotal > 100.00:
            return 0.0
        return base_rate

    def calculate_tax(self, subtotal: float) -> float:
        """
        Calculate tax amount based on subtotal.
        
        Args:
            subtotal: Order subtotal before tax
            
        Returns:
            float: Tax amount
        """
        return subtotal * self.tax_rate

    def generate_invoice_number(self) -> str:
        """
        Generate a unique invoice number based on timestamp.
        
        Returns:
            str: Unique invoice number
        """
        now = datetime.datetime.now()
        return f"FF-{now.year}{now.month:02d}{now.day:02d}-{now.hour:02d}{now.minute:02d}{now.second:02d}"

    def generate_invoice(
        self,
        customer_name: str,
        customer_address: str,
        items: List[Dict],
        shipping_method: str = "standard",
        notes: Optional[str] = None
    ) -> Dict:
        """
        Generate a complete invoice dictionary with all details.
        
        Args:
            customer_name: Name of the customer
            customer_address: Address of the customer
            items: List of order items
            shipping_method: Shipping method (default: standard)
            notes: Optional order notes
            
        Returns:
            Dict: Complete invoice details
        """
        if not items:
            raise ValueError("No items in the order")
            
        invoice_number = self.generate_invoice_number()
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        subtotal = self.calculate_subtotal(items)
        shipping = self.calculate_shipping(shipping_method, subtotal)
        tax = self.calculate_tax(subtotal)
        total = subtotal + shipping + tax
        
        invoice = {
            "invoice_number": invoice_number,
            "date": date,
            "company": {
                "name": self.company_name,
                "address": self.company_address,
                "contact": self.company_contact
            },
            "customer": {
                "name": customer_name,
                "address": customer_address
            },
            "items": items,
            "summary": {
                "subtotal": round(subtotal, 2),
                "shipping": round(shipping, 2),
                "tax": round(tax, 2),
                "total": round(total, 2)
            },
            "shipping_method": shipping_method,
            "notes": notes
        }
        
        return invoice

    def save_invoice_to_file(self, invoice: Dict, directory: str = "invoices") -> str:
        """
        Save the invoice as a JSON file.
        
        Args:
            invoice: Invoice dictionary to save
            directory: Directory to save invoices (default: invoices)
            
        Returns:
            str: Path to the saved invoice file
            
        Raises:
            OSError: If directory creation fails
        """
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        filename = f"{invoice['invoice_number']}.json"
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'w') as f:
            json.dump(invoice, f, indent=4)
            
        return filepath

    def print_invoice(self, invoice: Dict) -> None:
        """
        Print a formatted version of the invoice to console.
        
        Args:
            invoice: Invoice dictionary to print
        """
        print("\n" + "=" * 50)
        print(f"{self.company_name.upper()} - INVOICE".center(50))
        print("=" * 50)
        print(f"Invoice #: {invoice['invoice_number']}")
        print(f"Date: {invoice['date']}")
        print("\nCompany Details:")
        print(f"  {invoice['company']['name']}")
        print(f"  {invoice['company']['address']}")
        print(f"  {invoice['company']['contact']}")
        print("\nCustomer Details:")
        print(f"  {invoice['customer']['name']}")
        print(f"  {invoice['customer']['address']}")
        print("\nOrder Items:")
        for item in invoice['items']:
            product = self.products[item['product_type']]
            print(f"  - {product['name']} x{item['quantity']}")
            if 'customizations' in item and item['customizations']:
                print("    Customizations:", ", ".join(item['customizations']))
        print("\nOrder Summary:")
        print(f"  Subtotal: ${invoice['summary']['subtotal']:.2f}")
        print(f"  Shipping ({invoice['shipping_method']}): ${invoice['summary']['shipping']:.2f}")
        print(f"  Tax: ${invoice['summary']['tax']:.2f}")
        print(f"  TOTAL: ${invoice['summary']['total']:.2f}")
        if invoice['notes']:
            print("\nNotes:")
            print(f"  {invoice['notes']}")
        print("=" * 50 + "\n")


# Example usage
if __name__ == "__main__":
    # Initialize the invoice generator with company details
    invoice_gen = FlipFlopInvoiceGenerator(
        company_name="FlipFlop Paradise",
        company_address="123 Beach Blvd, Sunnyvale, CA 94085",
        company_contact="contact@flipflopparadise.com"
    )
    
    # Create an example order
    order_items = [
        {
            "product_type": "premium",
            "quantity": 2,
            "customizations": ["logo", "color"]
        },
        {
            "product_type": "basic",
            "quantity": 5
        }
    ]
    
    # Generate the invoice
    try:
        invoice = invoice_gen.generate_invoice(
            customer_name="John Doe",
            customer_address="456 Ocean Drive, Miami, FL 33139",
            items=order_items,
            shipping_method="express",
            notes="Please include gift wrapping"
        )
        
        # Save and print the invoice
        saved_path = invoice_gen.save_invoice_to_file(invoice)
        print(f"Invoice saved to: {saved_path}")
        invoice_gen.print_invoice(invoice)
        
    except Exception as e:
        print(f"Error generating invoice: {str(e)}")
```
