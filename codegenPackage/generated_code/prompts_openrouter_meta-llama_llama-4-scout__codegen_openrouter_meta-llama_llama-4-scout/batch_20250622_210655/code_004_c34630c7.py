"""
Generated Code Metadata:
========================
Original URL: https://renovation-toiture-toulouse.com
Prompt: "Create a sample invoice template for a roofing company in France, including items such as labor costs, materials, and taxes, inspired by the services offered by Renovation Toiture Toulouse."
Generated: DETERMINISTIC_c34630c7b3b1bc06
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# invoice.py

class Invoice:
    def __init__(self, company_name, company_address, client_name, client_address):
        """
        Initialize an invoice object.

        Args:
            company_name (str): Name of the roofing company.
            company_address (str): Address of the roofing company.
            client_name (str): Name of the client.
            client_address (str): Address of the client.
        """
        self.company_name = company_name
        self.company_address = company_address
        self.client_name = client_name
        self.client_address = client_address
        self.items = []

    def add_item(self, description, quantity, unit_price, tax_rate):
        """
        Add an item to the invoice.

        Args:
            description (str): Description of the item.
            quantity (int): Quantity of the item.
            unit_price (float): Unit price of the item.
            tax_rate (float): Tax rate for the item.
        """
        self.items.append({
            'description': description,
            'quantity': quantity,
            'unit_price': unit_price,
            'tax_rate': tax_rate
        })

    def calculate_subtotal(self):
        """
        Calculate the subtotal of the invoice.

        Returns:
            float: Subtotal of the invoice.
        """
        subtotal = sum(item['quantity'] * item['unit_price'] for item in self.items)
        return subtotal

    def calculate_tax(self):
        """
        Calculate the tax amount of the invoice.

        Returns:
            float: Tax amount of the invoice.
        """
        tax_amount = sum(item['quantity'] * item['unit_price'] * item['tax_rate'] / 100 for item in self.items)
        return tax_amount

    def calculate_total(self):
        """
        Calculate the total amount of the invoice.

        Returns:
            float: Total amount of the invoice.
        """
        subtotal = self.calculate_subtotal()
        tax_amount = self.calculate_tax()
        total = subtotal + tax_amount
        return total

    def generate_invoice(self):
        """
        Generate the invoice.

        Returns:
            str: The generated invoice.
        """
        invoice = f"{self.company_name}\n{self.company_address}\n\n"
        invoice += f"Facture pour {self.client_name}\n{self.client_address}\n\n"
        invoice += "Description\tQuantité\tPrix unitaire\tTaux de taxe\tMontant\n"
        for item in self.items:
            invoice += f"{item['description']}\t{item['quantity']}\t{item['unit_price']:.2f}\t{item['tax_rate']}%\t{item['quantity'] * item['unit_price']:.2f}\n"
        invoice += f"\nSous-total:\t{self.calculate_subtotal():.2f}\n"
        invoice += f"Taxe:\t{self.calculate_tax():.2f}\n"
        invoice += f"Total:\t{self.calculate_total():.2f}\n"
        return invoice


def main():
    try:
        # Create an invoice object
        company_name = "Renovation Toiture Toulouse"
        company_address = "123 Rue de la République, 31000 Toulouse, France"
        client_name = "M. Jean Dupont"
        client_address = "456 Rue de la Ville, 75001 Paris, France"
        invoice = Invoice(company_name, company_address, client_name, client_address)

        # Add items to the invoice
        invoice.add_item("Travail de toiture", 10, 500.0, 20.0)  # Labor costs
        invoice.add_item("Matériaux de toiture", 5, 200.0, 20.0)  # Materials
        invoice.add_item("TVA", 1, 0.0, 20.0)  # Taxes

        # Generate the invoice
        generated_invoice = invoice.generate_invoice()
        print(generated_invoice)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
