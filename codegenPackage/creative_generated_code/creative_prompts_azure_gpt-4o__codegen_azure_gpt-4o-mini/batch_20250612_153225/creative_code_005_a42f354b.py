"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://konveksibajumurah.com
Prompt: Write a program to generate invoices for bulk uniform orders, incorporating Real Garment's pricing structure and accessory options.
Generated: DETERMINISTIC_a42f354bcbf24070
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal, ROUND_UP

class UniformOrder:
    """
    Represents a bulk uniform order with pricing and accessory options.
    """

    BASE_PRICE = Decimal('20.00')  # Base price for each uniform
    ACCESSORY_PRICES = {
        'hat': Decimal('5.00'),
        'belt': Decimal('3.00'),
        'scarf': Decimal('2.50'),
    }

    def __init__(self, quantity, accessories=None):
        """
        Initialize the uniform order with quantity and optional accessories.

        :param quantity: The number of uniforms in the order.
        :param accessories: A list of selected accessories.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.quantity = quantity
        self.accessories = accessories if accessories else []

    def calculate_base_cost(self):
        """
        Calculate the base cost for the uniforms.

        :return: The base cost as a Decimal.
        """
        return self.BASE_PRICE * self.quantity

    def calculate_accessory_cost(self):
        """
        Calculate the total cost for selected accessories.

        :return: The total accessory cost as a Decimal.
        """
        total_accessory_cost = sum(self.ACCESSORY_PRICES.get(item, Decimal('0.00')) for item in self.accessories)
        return total_accessory_cost

    def calculate_total_cost(self):
        """
        Calculate the total cost of the order, including uniforms and accessories.

        :return: The total cost as a Decimal.
        """
        total_cost = self.calculate_base_cost() + self.calculate_accessory_cost()
        # Round up to the nearest cent
        return total_cost.quantize(Decimal('0.01'), rounding=ROUND_UP)

    def generate_invoice(self):
        """
        Generate an invoice for the order.

        :return: Invoice details as a dictionary.
        """
        invoice = {
            'quantity': self.quantity,
            'base_cost': str(self.calculate_base_cost()),
            'accessories': self.accessories,
            'accessory_cost': str(self.calculate_accessory_cost()),
            'total_cost': str(self.calculate_total_cost()),
        }
        return invoice


def save_invoice_to_file(invoice, filename):
    """
    Save the invoice to a JSON file.

    :param invoice: The invoice data to save.
    :param filename: The name of the file to save the invoice to.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(invoice, file, indent=4)
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")


def main():
    """
    Main function to execute the uniform order processing.
    """
    try:
        # Example order
        quantity = 100
        accessories = ['hat', 'belt']
        
        # Create a UniformOrder instance
        order = UniformOrder(quantity, accessories)
        
        # Generate the invoice
        invoice = order.generate_invoice()
        
        # Print the invoice
        print("Invoice Generated:")
        print(json.dumps(invoice, indent=4))

        # Save the invoice to a file
        save_invoice_to_file(invoice, 'invoice.json')

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
```
