"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Create a program that generates invoices for automotive glass replacement materials ordered from "Гарант," including payment terms like deferred payment options mentioned on the site.
Generated: DETERMINISTIC_feed043614af1dd3
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

class PaymentTerm(Enum):
    """Payment term options"""
    CASH = "Cash"
    DEFERRED_30_DAYS = "Deferred payment (30 days)"
    DEFERRED_60_DAYS = "Deferred payment (60 days)"

@dataclass
class OrderItem:
    """Represents an item in the order"""
    material: str
    quantity: int
    price_per_unit: float

@dataclass
class Invoice:
    """Represents an invoice for automotive glass replacement materials"""
    order_id: int
    customer_name: str
    order_items: List[OrderItem]
    payment_term: PaymentTerm

    def calculate_subtotal(self) -> float:
        """Calculates the subtotal of the invoice"""
        return sum(item.quantity * item.price_per_unit for item in self.order_items)

    def calculate_tax(self, tax_rate: float = 0.2) -> float:
        """Calculates the tax amount of the invoice"""
        return self.calculate_subtotal() * tax_rate

    def calculate_total(self, tax_rate: float = 0.2) -> float:
        """Calculates the total amount of the invoice"""
        return self.calculate_subtotal() + self.calculate_tax(tax_rate)

    def generate_invoice(self) -> str:
        """Generates the invoice as a string"""
        invoice_date = datetime.date.today().strftime("%Y-%m-%d")
        payment_term_details = {
            PaymentTerm.CASH: "Payment is due upon receipt of invoice.",
            PaymentTerm.DEFERRED_30_DAYS: "Payment is due within 30 days of invoice date.",
            PaymentTerm.DEFERRED_60_DAYS: "Payment is due within 60 days of invoice date."
        }

        invoice = f"Invoice # {self.order_id}\n"
        invoice += f"Date: {invoice_date}\n"
        invoice += f"Customer Name: {self.customer_name}\n"
        invoice += f"Payment Term: {self.payment_term.value}\n"
        invoice += f"{payment_term_details[self.payment_term]}\n\n"

        invoice += "Order Items:\n"
        for i, item in enumerate(self.order_items, start=1):
            invoice += f"{i}. {item.material} x {item.quantity} = ${item.quantity * item.price_per_unit:.2f}\n"

        invoice += f"\nSubtotal: ${self.calculate_subtotal():.2f}\n"
        invoice += f"Tax (20%): ${self.calculate_tax():.2f}\n"
        invoice += f"Total: ${self.calculate_total():.2f}\n"

        return invoice

def main():
    try:
        order_id = 12345
        customer_name = "John Doe"
        order_items = [
            OrderItem("Windshield", 2, 200.0),
            OrderItem("Side Window", 3, 50.0)
        ]
        payment_term = PaymentTerm.DEFERRED_30_DAYS

        invoice = Invoice(order_id, customer_name, order_items, payment_term)
        print(invoice.generate_invoice())

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
