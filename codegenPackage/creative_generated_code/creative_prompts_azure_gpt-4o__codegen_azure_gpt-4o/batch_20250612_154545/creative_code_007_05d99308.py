"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Develop a script to automate the generation of invoices for purchases made on AirstyleArt, including itemized lists of stencils, paints, and accessories.
Generated: DETERMINISTIC_05d993082cfc511d
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime
import json

class InvoiceGenerator:
    """
    A class to generate itemized invoices for purchases made on AirstyleArt.
    """
    
    def __init__(self, output_dir="invoices"):
        """
        Initializes the InvoiceGenerator.

        Args:
            output_dir (str): Directory where invoices will be saved.
        """
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def generate_invoice(self, customer_name, items, invoice_number=None):
        """
        Generates an invoice for the given customer and items.

        Args:
            customer_name (str): Name of the customer.
            items (list[dict]): A list of dictionaries, each representing an item.
                                Each dictionary should have 'name', 'category', 'quantity', 'price'.
            invoice_number (str, optional): Invoice number. Defaults to a timestamp-based value.

        Returns:
            str: Path to the generated invoice file.
        """
        try:
            # Validate inputs
            if not customer_name or not items:
                raise ValueError("Customer name and items cannot be empty.")
            
            if not isinstance(items, list) or not all(isinstance(item, dict) for item in items):
                raise ValueError("Items must be a list of dictionaries.")
            
            # Generate invoice number if not provided
            if invoice_number is None:
                invoice_number = f"INV-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            # Calculate totals
            total_amount = sum(item['quantity'] * item['price'] for item in items)
            
            # Prepare invoice data
            invoice_data = {
                "invoice_number": invoice_number,
                "customer_name": customer_name,
                "date": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "items": items,
                "total_amount": total_amount
            }
            
            # Generate invoice file path
            invoice_file = os.path.join(self.output_dir, f"{invoice_number}.json")
            
            # Save invoice data to file
            with open(invoice_file, "w") as file:
                json.dump(invoice_data, file, indent=4)
            
            return invoice_file
        
        except Exception as e:
            print(f"Error generating invoice: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Instantiate the InvoiceGenerator
    generator = InvoiceGenerator()

    # Sample customer and items data
    customer = "John Doe"
    items = [
        {"name": "Stencil - Dragon", "category": "Stencils", "quantity": 2, "price": 12.50},
        {"name": "Paint - Red", "category": "Paints", "quantity": 3, "price": 5.00},
        {"name": "Paintbrush Set", "category": "Accessories", "quantity": 1, "price": 15.00}
    ]

    # Generate the invoice
    invoice_path = generator.generate_invoice(customer_name=customer, items=items)

    if invoice_path:
        print(f"Invoice successfully generated: {invoice_path}")
    else:
        print("Failed to generate invoice.")
```
