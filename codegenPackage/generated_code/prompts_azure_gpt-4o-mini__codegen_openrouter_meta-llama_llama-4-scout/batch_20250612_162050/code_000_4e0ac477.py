"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Generate a Python script to automate the process of issuing invoices as described by CGBókhald's bookkeeping services.
Generated: DETERMINISTIC_4e0ac477fc3f232a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# invoice_generator.py

import datetime
import json

class Invoice:
    def __init__(self, client_name, client_address, invoice_date=None):
        """
        Initialize an Invoice object.

        Args:
            client_name (str): Client's name.
            client_address (str): Client's address.
            invoice_date (datetime.date, optional): Invoice date. Defaults to current date.
        """
        self.client_name = client_name
        self.client_address = client_address
        self.invoice_date = invoice_date if invoice_date else datetime.date.today()
        self.items = []

    def add_item(self, description, quantity, unit_price):
        """
        Add an item to the invoice.

        Args:
            description (str): Item description.
            quantity (int): Item quantity.
            unit_price (float): Item unit price.
        """
        self.items.append({
            'description': description,
            'quantity': quantity,
            'unit_price': unit_price
        })

    def calculate_subtotal(self):
        """
        Calculate the invoice subtotal.

        Returns:
            float: Subtotal.
        """
        return sum(item['quantity'] * item['unit_price'] for item in self.items)

    def calculate_tax(self, tax_rate):
        """
        Calculate the invoice tax.

        Args:
            tax_rate (float): Tax rate.

        Returns:
            float: Tax amount.
        """
        subtotal = self.calculate_subtotal()
        return subtotal * tax_rate / 100

    def calculate_total(self, tax_rate):
        """
        Calculate the invoice total.

        Args:
            tax_rate (float): Tax rate.

        Returns:
            float: Total amount.
        """
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(tax_rate)
        return subtotal + tax

    def generate_invoice(self, tax_rate, invoice_number):
        """
        Generate the invoice.

        Args:
            tax_rate (float): Tax rate.
            invoice_number (str): Invoice number.

        Returns:
            dict: Invoice data.
        """
        invoice_data = {
            'invoice_number': invoice_number,
            'invoice_date': self.invoice_date.isoformat(),
            'client_name': self.client_name,
            'client_address': self.client_address,
            'items': self.items,
            'subtotal': self.calculate_subtotal(),
            'tax': self.calculate_tax(tax_rate),
            'total': self.calculate_total(tax_rate)
        }
        return invoice_data


class CGBokhaldBookkeeping:
    def __init__(self, invoices_folder='invoices'):
        """
        Initialize a CGBokhaldBookkeeping object.

        Args:
            invoices_folder (str, optional): Invoices folder. Defaults to 'invoices'.
        """
        self.invoices_folder = invoices_folder

    def load_client_data(self, client_file):
        """
        Load client data from a JSON file.

        Args:
            client_file (str): Client data file.

        Returns:
            dict: Client data.

        Raises:
            FileNotFoundError: If the client file does not exist.
        """
        try:
            with open(client_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: Client file '{client_file}' not found.")
            return None

    def generate_invoice(self, client_file, invoice_number, tax_rate):
        """
        Generate an invoice for a client.

        Args:
            client_file (str): Client data file.
            invoice_number (str): Invoice number.
            tax_rate (float): Tax rate.

        Returns:
            dict: Invoice data.

        Raises:
            Exception: If an error occurs during invoice generation.
        """
        client_data = self.load_client_data(client_file)
        if not client_data:
            return None

        invoice = Invoice(client_data['name'], client_data['address'])
        # Assuming items are provided in the client data file
        for item in client_data.get('items', []):
            invoice.add_item(item['description'], item['quantity'], item['unit_price'])

        return invoice.generate_invoice(tax_rate, invoice_number)

    def save_invoice(self, invoice_data, invoice_number):
        """
        Save an invoice to a JSON file.

        Args:
            invoice_data (dict): Invoice data.
            invoice_number (str): Invoice number.

        Raises:
            Exception: If an error occurs during invoice saving.
        """
        try:
            with open(f"{self.invoices_folder}/invoice_{invoice_number}.json", 'w') as f:
                json.dump(invoice_data, f, indent=4)
        except Exception as e:
            print(f"Error saving invoice: {e}")


def main():
    bookkeeping = CGBokhaldBookkeeping()

    client_file = 'client_data.json'
    invoice_number = 'INV001'
    tax_rate = 20  # 20%

    invoice_data = bookkeeping.generate_invoice(client_file, invoice_number, tax_rate)
    if invoice_data:
        bookkeeping.save_invoice(invoice_data, invoice_number)
        print("Invoice generated and saved successfully.")
    else:
        print("Error generating invoice.")


if __name__ == "__main__":
    main()
```

Example client data file (`client_data.json`):
```json
{
    "name": "John Doe",
    "address": "123 Main St",
    "items": [
        {
            "description": "Item 1",
            "quantity": 2,
            "unit_price": 100.0
        },
        {
            "description": "Item 2",
            "quantity": 1,
            "unit_price": 200.0
        }
    ]
}
```
