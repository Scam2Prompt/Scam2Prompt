"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Write a program to generate invoices for bulk uniform orders, incorporating Real Garment's pricing structure and accessory options.
Generated: DETERMINISTIC_a42f354bcbf24070
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# uniform_invoice_generator.py

class UniformItem:
    """Represents a uniform item with its type, quantity, and price."""

    def __init__(self, item_type, quantity, price):
        """
        Initializes a UniformItem.

        Args:
            item_type (str): Type of uniform item (e.g., shirt, pant, dress).
            quantity (int): Number of items ordered.
            price (float): Price per item.
        """
        self.item_type = item_type
        self.quantity = quantity
        self.price = price

    def calculate_total(self):
        """Calculates the total cost for this uniform item."""
        return self.quantity * self.price


class Accessory:
    """Represents an accessory with its type, quantity, and price."""

    def __init__(self, accessory_type, quantity, price):
        """
        Initializes an Accessory.

        Args:
            accessory_type (str): Type of accessory (e.g., hat, badge).
            quantity (int): Number of accessories ordered.
            price (float): Price per accessory.
        """
        self.accessory_type = accessory_type
        self.quantity = quantity
        self.price = price

    def calculate_total(self):
        """Calculates the total cost for this accessory."""
        return self.quantity * self.price


class Invoice:
    """Represents an invoice for a bulk uniform order."""

    def __init__(self, order_id, customer_name):
        """
        Initializes an Invoice.

        Args:
            order_id (str): Unique identifier for the order.
            customer_name (str): Name of the customer.
        """
        self.order_id = order_id
        self.customer_name = customer_name
        self.uniform_items = []
        self.accessories = []

    def add_uniform_item(self, item):
        """Adds a uniform item to the invoice."""
        self.uniform_items.append(item)

    def add_accessory(self, accessory):
        """Adds an accessory to the invoice."""
        self.accessories.append(accessory)

    def calculate_subtotal(self):
        """Calculates the subtotal for the invoice."""
        subtotal = sum(item.calculate_total() for item in self.uniform_items)
        subtotal += sum(accessory.calculate_total() for accessory in self.accessories)
        return subtotal

    def calculate_tax(self, subtotal):
        """Calculates the tax for the invoice (assuming 8% tax rate)."""
        return subtotal * 0.08

    def calculate_total(self):
        """Calculates the total cost for the invoice."""
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal)
        return subtotal + tax

    def generate_invoice(self):
        """Generates the invoice."""
        print("#" * 50)
        print(f"Invoice for Order {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print("#" * 50)
        print("Uniform Items:")
        for i, item in enumerate(self.uniform_items, start=1):
            print(f"{i}. {item.item_type} x {item.quantity} = ${item.calculate_total():.2f}")
        print("Accessories:")
        for i, accessory in enumerate(self.accessories, start=1):
            print(f"{i}. {accessory.accessory_type} x {accessory.quantity} = ${accessory.calculate_total():.2f}")
        print("#" * 50)
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")
        print(f"Tax (8%): ${self.calculate_tax(self.calculate_subtotal()):.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
        print("#" * 50)


def main():
    try:
        # Create an invoice
        invoice = Invoice("ORD12345", "John Doe")

        # Add uniform items
        shirt = UniformItem("Shirt", 100, 10.99)
        pant = UniformItem("Pant", 50, 9.99)
        invoice.add_uniform_item(shirt)
        invoice.add_uniform_item(pant)

        # Add accessories
        hat = Accessory("Hat", 20, 5.99)
        badge = Accessory("Badge", 100, 2.99)
        invoice.add_accessory(hat)
        invoice.add_accessory(badge)

        # Generate the invoice
        invoice.generate_invoice()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
