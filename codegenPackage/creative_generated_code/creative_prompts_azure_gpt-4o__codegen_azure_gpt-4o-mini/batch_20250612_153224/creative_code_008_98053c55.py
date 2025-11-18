"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluivars.com
Prompt: Create a program to generate invoices for custom carpentry projects, including detailed descriptions of services like aluminum carpentry, iron forging, and glass installations, inspired by Aluivars' offerings.
Generated: DETERMINISTIC_98053c55793e7894
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class Invoice:
    """Class representing an invoice for a custom carpentry project."""
    
    def __init__(self, client_name, client_address):
        """Initialize the invoice with client information.

        Args:
            client_name (str): The name of the client.
            client_address (str): The address of the client.
        """
        self.client_name = client_name
        self.client_address = client_address
        self.items = []
        self.invoice_date = datetime.now().strftime("%Y-%m-%d")
        self.invoice_number = self.generate_invoice_number()

    def generate_invoice_number(self):
        """Generate a unique invoice number.

        Returns:
            str: A unique invoice number.
        """
        return f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    def add_item(self, description, quantity, price_per_unit):
        """Add an item to the invoice.

        Args:
            description (str): Description of the service/item.
            quantity (int): The quantity of the item/service.
            price_per_unit (float): Price per unit of the item/service.

        Raises:
            ValueError: If quantity or price_per_unit is negative.
        """
        if quantity < 0 or price_per_unit < 0:
            raise ValueError("Quantity and price must be non-negative.")
        
        item_total = quantity * price_per_unit
        self.items.append({
            'description': description,
            'quantity': quantity,
            'price_per_unit': price_per_unit,
            'item_total': item_total
        })

    def calculate_total(self):
        """Calculate the total amount for the invoice.

        Returns:
            float: The total amount of the invoice.
        """
        return sum(item['item_total'] for item in self.items)

    def generate_invoice(self):
        """Generate a detailed invoice in a dictionary format.

        Returns:
            dict: The complete invoice details.
        """
        total = self.calculate_total()
        return {
            'invoice_number': self.invoice_number,
            'date': self.invoice_date,
            'client_name': self.client_name,
            'client_address': self.client_address,
            'items': self.items,
            'total': total
        }

    def save_to_file(self, filename):
        """Save the invoice to a JSON file.

        Args:
            filename (str): The name of the file to save the invoice.

        Raises:
            IOError: If the file cannot be written.
        """
        invoice_data = self.generate_invoice()
        try:
            with open(filename, 'w') as file:
                json.dump(invoice_data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    try:
        invoice = Invoice("John Doe", "123 Elm St, Springfield")
        invoice.add_item("Aluminum Carpentry", 5, 200.0)
        invoice.add_item("Iron Forging", 3, 150.0)
        invoice.add_item("Glass Installation", 2, 300.0)

        invoice_filename = f"invoice_{invoice.invoice_number}.json"
        invoice.save_to_file(invoice_filename)

        print(f"Invoice saved as {invoice_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
