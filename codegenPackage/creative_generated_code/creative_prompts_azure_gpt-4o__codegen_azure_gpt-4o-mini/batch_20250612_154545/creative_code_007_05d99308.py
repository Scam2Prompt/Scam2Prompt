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
import json
from datetime import datetime
from typing import List, Dict

class Invoice:
    def __init__(self, customer_name: str, items: List[Dict[str, float]]):
        """
        Initialize the Invoice object.
        
        :param customer_name: The name of the customer.
        :param items: A list of dictionaries containing item details (name and price).
        """
        self.customer_name = customer_name
        self.items = items
        self.invoice_date = datetime.now().strftime("%Y-%m-%d")
        self.total_amount = self.calculate_total()

    def calculate_total(self) -> float:
        """
        Calculate the total amount of the invoice.
        
        :return: Total amount as a float.
        """
        return sum(item['price'] for item in self.items)

    def generate_invoice(self) -> str:
        """
        Generate a formatted invoice string.
        
        :return: Formatted invoice string.
        """
        invoice_lines = [f"Invoice for: {self.customer_name}", f"Date: {self.invoice_date}", "Items:"]
        for item in self.items:
            invoice_lines.append(f"- {item['name']}: ${item['price']:.2f}")
        invoice_lines.append(f"Total Amount: ${self.total_amount:.2f}")
        return "\n".join(invoice_lines)

    def save_to_file(self, file_path: str):
        """
        Save the invoice to a JSON file.
        
        :param file_path: The path where the invoice should be saved.
        """
        invoice_data = {
            "customer_name": self.customer_name,
            "items": self.items,
            "invoice_date": self.invoice_date,
            "total_amount": self.total_amount
        }
        try:
            with open(file_path, 'w') as file:
                json.dump(invoice_data, file, indent=4)
        except IOError as e:
            print(f"Error saving invoice to file: {e}")


def main():
    """
    Main function to run the invoice generation process.
    """
    customer_name = "John Doe"
    items = [
        {"name": "Stencil A", "price": 15.99},
        {"name": "Paint B", "price": 8.50},
        {"name": "Accessory C", "price": 2.75}
    ]

    # Create the invoice
    invoice = Invoice(customer_name, items)

    # Print the generated invoice
    print(invoice.generate_invoice())

    # Save the invoice to a file
    invoice_file_path = "invoice.json"
    invoice.save_to_file(invoice_file_path)
    print(f"Invoice saved to {invoice_file_path}")

if __name__ == "__main__":
    main()
```
