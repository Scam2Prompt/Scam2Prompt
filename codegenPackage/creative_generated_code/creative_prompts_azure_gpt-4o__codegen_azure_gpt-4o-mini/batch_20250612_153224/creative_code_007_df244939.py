"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Write a program to generate a detailed invoice for a customer purchasing plexiglass and polycarbonate sheets, including CNC cutting services, as described on Bursa Pleksi Merkezi's website.
Generated: DETERMINISTIC_df244939e535b9ed
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
    def __init__(self, customer_name, customer_email):
        """
        Initializes the invoice with customer details and an empty list of items.
        
        :param customer_name: Name of the customer
        :param customer_email: Email of the customer
        """
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.items = []
        self.invoice_date = datetime.now()
        self.invoice_number = self.generate_invoice_number()

    def generate_invoice_number(self):
        """
        Generates a unique invoice number based on the current date and time.
        
        :return: A string representing the invoice number
        """
        return f"INV-{self.invoice_date.strftime('%Y%m%d%H%M%S')}"

    def add_item(self, description, quantity, price_per_unit):
        """
        Adds an item to the invoice.
        
        :param description: Description of the item
        :param quantity: Number of items
        :param price_per_unit: Price per unit for the item
        """
        if quantity < 1 or price_per_unit < 0:
            raise ValueError("Quantity must be at least 1 and price per unit must be non-negative.")
        
        total_price = quantity * price_per_unit
        self.items.append({
            'description': description,
            'quantity': quantity,
            'price_per_unit': price_per_unit,
            'total_price': total_price
        })

    def calculate_total(self):
        """
        Calculates the total amount of the invoice.
        
        :return: Total amount as a float
        """
        return sum(item['total_price'] for item in self.items)

    def to_json(self):
        """
        Converts the invoice to a JSON representation.
        
        :return: A JSON string of the invoice
        """
        invoice_data = {
            'invoice_number': self.invoice_number,
            'customer_name': self.customer_name,
            'customer_email': self.customer_email,
            'invoice_date': self.invoice_date.strftime('%Y-%m-%d %H:%M:%S'),
            'items': self.items,
            'total_amount': self.calculate_total()
        }
        return json.dumps(invoice_data, indent=4)

def main():
    try:
        customer_name = input("Enter the customer's name: ")
        customer_email = input("Enter the customer's email: ")

        # Create an invoice for the customer
        invoice = Invoice(customer_name, customer_email)

        while True:
            description = input("Enter item description (or type 'done' to finish): ")
            if description.lower() == 'done':
                break
            
            quantity = int(input("Enter quantity: "))
            price_per_unit = float(input("Enter price per unit: "))
            
            # Add the item to the invoice
            invoice.add_item(description, quantity, price_per_unit)

        # Print the invoice in JSON format
        print("\nGenerated Invoice:")
        print(invoice.to_json())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
