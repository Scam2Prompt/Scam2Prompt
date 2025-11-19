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
# invoice_generator.py

from enum import Enum
from typing import Dict, List

class ProductType(str, Enum):
    """Enum for product types."""
    STANDARD = "Standard"
    CUSTOM = "Custom"
    PREMIUM = "Premium"

class Invoice:
    """Represents an invoice for a flip-flop order."""

    def __init__(self, 
                 product_type: ProductType, 
                 quantity: int, 
                 customization_fee: float = 0.0, 
                 shipping_cost: float = 0.0):
        """
        Initializes an Invoice object.

        Args:
        - product_type (ProductType): The type of product.
        - quantity (int): The quantity of products ordered.
        - customization_fee (float, optional): Customization fee. Defaults to 0.0.
        - shipping_cost (float, optional): Shipping cost. Defaults to 0.0.
        """
        self.product_type = product_type
        self.quantity = quantity
        self.customization_fee = customization_fee
        self.shipping_cost = shipping_cost

    def calculate_subtotal(self) -> float:
        """Calculates the subtotal of the invoice."""
        prices: Dict[ProductType, float] = {
            ProductType.STANDARD: 5.99,
            ProductType.CUSTOM: 7.99,
            ProductType.PREMIUM: 9.99
        }
        return prices[self.product_type] * self.quantity

    def calculate_total(self) -> float:
        """Calculates the total cost of the invoice."""
        return self.calculate_subtotal() + self.customization_fee + self.shipping_cost

    def generate_invoice(self) -> str:
        """Generates a formatted invoice string."""
        invoice_template = """
        Invoice for Flip-Flop Order

        Product Type: {product_type}
        Quantity: {quantity}
        Subtotal: ${subtotal:.2f}
        Customization Fee: ${customization_fee:.2f}
        Shipping Cost: ${shipping_cost:.2f}
        Total: ${total:.2f}

        Thank you for your order!
        """
        return invoice_template.format(
            product_type=self.product_type.value,
            quantity=self.quantity,
            subtotal=self.calculate_subtotal(),
            customization_fee=self.customization_fee,
            shipping_cost=self.shipping_cost,
            total=self.calculate_total()
        )


class InvoiceGenerator:
    """Generates invoices for flip-flop orders."""

    def __init__(self):
        self.invoices: List[Invoice] = []

    def add_invoice(self, invoice: Invoice):
        """Adds an invoice to the generator."""
        self.invoices.append(invoice)

    def generate_invoices(self) -> List[str]:
        """Generates a list of formatted invoices."""
        return [invoice.generate_invoice() for invoice in self.invoices]


def main():
    try:
        generator = InvoiceGenerator()

        # Create invoices
        invoice1 = Invoice(ProductType.STANDARD, 100, customization_fee=50.0, shipping_cost=20.0)
        invoice2 = Invoice(ProductType.CUSTOM, 50, customization_fee=100.0, shipping_cost=30.0)

        # Add invoices to generator
        generator.add_invoice(invoice1)
        generator.add_invoice(invoice2)

        # Generate invoices
        invoices = generator.generate_invoices()

        # Print invoices
        for i, invoice in enumerate(invoices, start=1):
            print(f"Invoice {i}:\n{invoice}\n")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
