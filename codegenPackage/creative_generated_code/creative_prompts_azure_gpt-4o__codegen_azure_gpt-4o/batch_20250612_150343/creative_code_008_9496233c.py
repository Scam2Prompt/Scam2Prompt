"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Write a script to generate invoices for glass installation services, including itemized costs for products like bathroom boxes, glass dividers, and mirrors, along with labor charges.
Generated: DETERMINISTIC_9496233c5f6a6420
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class InvoiceGenerator:
    """Class to generate invoices for glass installation services."""
    
    def __init__(self, customer_name, items, labor_hours, labor_rate):
        """
        Initialize invoice details.
        
        :param customer_name: Name of the customer
        :param items: List of items with their costs in the format [{'name': 'item_name', 'cost': amount}, ...]
        :param labor_hours: Number of labor hours
        :param labor_rate: Hourly rate for labor
        """
        self.customer_name = customer_name
        self.items = items
        self.labor_hours = labor_hours
        self.labor_rate = labor_rate
        self.invoice_date = datetime.datetime.now().strftime('%Y-%m-%d')
        self.invoice_number = f"INV-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"

    def calculate_total_cost(self):
        """
        Calculate the total cost of items and labor.
        
        :return: Total cost (float)
        """
        items_total = sum(item['cost'] for item in self.items)
        labor_total = self.labor_hours * self.labor_rate
        return items_total + labor_total

    def generate_invoice(self):
        """
        Generate the invoice as a formatted string.
        
        :return: Formatted invoice string
        """
        invoice_lines = []
        invoice_lines.append(f"Invoice Number: {self.invoice_number}")
        invoice_lines.append(f"Invoice Date: {self.invoice_date}")
        invoice_lines.append(f"Customer Name: {self.customer_name}")
        invoice_lines.append("\nItemized Costs:")
        
        for item in self.items:
            invoice_lines.append(f"  - {item['name']}: ${item['cost']:.2f}")
        
        invoice_lines.append(f"\nLabor Charges:")
        invoice_lines.append(f"  - Hours: {self.labor_hours}")
        invoice_lines.append(f"  - Hourly Rate: ${self.labor_rate:.2f}")
        invoice_lines.append(f"\nTotal Labor Cost: ${self.labor_hours * self.labor_rate:.2f}")
        
        total_cost = self.calculate_total_cost()
        invoice_lines.append(f"\nGrand Total: ${total_cost:.2f}")
        
        return "\n".join(invoice_lines)


def main():
    """
    Main function to generate and display the invoice.
    """
    try:
        # Example data for invoice generation
        customer_name = "John Doe"
        items = [
            {"name": "Bathroom Box", "cost": 250.00},
            {"name": "Glass Divider", "cost": 180.00},
            {"name": "Mirror", "cost": 120.00},
        ]
        labor_hours = 5  # Example labor hours
        labor_rate = 35.00  # Example hourly labor rate
        
        # Create an instance of the InvoiceGenerator
        invoice_generator = InvoiceGenerator(customer_name, items, labor_hours, labor_rate)
        
        # Generate and display the invoice
        invoice = invoice_generator.generate_invoice()
        print(invoice)
    
    except Exception as e:
        print(f"An error occurred while generating the invoice: {e}")


if __name__ == "__main__":
    main()
```
