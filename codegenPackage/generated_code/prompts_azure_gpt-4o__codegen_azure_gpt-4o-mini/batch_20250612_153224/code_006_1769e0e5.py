"""
Generated Code Metadata:
========================
Original URL: https://shishehbalkon.ir
Prompt: Create a program that generates a detailed invoice for glass installation services, including options for balcony glass, shower cabins, and sliding glass doors, based on the specifications provided on the website.
Generated: DETERMINISTIC_1769e0e5078dbf25
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Invoice:
    def __init__(self, customer_name, customer_address):
        """
        Initialize the Invoice with customer details.
        
        :param customer_name: Name of the customer
        :param customer_address: Address of the customer
        """
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.items = []
        self.total_amount = 0.0

    def add_item(self, description, quantity, unit_price):
        """
        Add an item to the invoice.
        
        :param description: Description of the service/item
        :param quantity: Quantity of the service/item
        :param unit_price: Price per unit of the service/item
        """
        if quantity <= 0 or unit_price < 0:
            raise ValueError("Quantity must be greater than 0 and unit price must be non-negative.")
        
        item_total = quantity * unit_price
        self.items.append({
            'description': description,
            'quantity': quantity,
            'unit_price': unit_price,
            'total': item_total
        })
        self.total_amount += item_total

    def generate_invoice(self):
        """
        Generate a detailed invoice as a dictionary.
        
        :return: A dictionary containing invoice details
        """
        invoice_details = {
            'customer_name': self.customer_name,
            'customer_address': self.customer_address,
            'items': self.items,
            'total_amount': self.total_amount
        }
        return invoice_details

    def save_invoice(self, filename):
        """
        Save the invoice to a JSON file.
        
        :param filename: Name of the file to save the invoice
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_invoice(), file, indent=4)
            print(f"Invoice saved successfully to {filename}.")
        except IOError as e:
            print(f"Error saving invoice: {e}")

def main():
    # Example usage of the Invoice class
    try:
        # Create an invoice for a customer
        invoice = Invoice("John Doe", "123 Main St, Anytown, USA")
        
        # Add items to the invoice
        invoice.add_item("Balcony Glass Installation", 2, 150.00)
        invoice.add_item("Shower Cabin Installation", 1, 300.00)
        invoice.add_item("Sliding Glass Door Installation", 1, 400.00)
        
        # Generate and save the invoice
        invoice.save_invoice("invoice.json")
        
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
