"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: "Write a code snippet in Python to calculate the total cost of refractory products for a specific industrial application, considering factors like product quantity, unit price, and taxes."
Generated: DETERMINISTIC_3c72df4fb2c18bd6
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# refractory_products.py

class RefractoryProduct:
    """Represents a refractory product with its properties."""

    def __init__(self, name: str, quantity: int, unit_price: float):
        """
        Initializes a RefractoryProduct instance.

        Args:
            name (str): The product name.
            quantity (int): The product quantity.
            unit_price (float): The product unit price.
        """
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def calculate_subtotal(self) -> float:
        """Calculates the subtotal cost of the product."""
        return self.quantity * self.unit_price


class RefractoryCalculator:
    """Calculates the total cost of refractory products."""

    def __init__(self, tax_rate: float):
        """
        Initializes a RefractoryCalculator instance.

        Args:
            tax_rate (float): The tax rate as a decimal value.
        """
        self.tax_rate = tax_rate
        self.products = []

    def add_product(self, product: RefractoryProduct):
        """Adds a refractory product to the calculator."""
        self.products.append(product)

    def calculate_subtotal(self) -> float:
        """Calculates the subtotal cost of all products."""
        return sum(product.calculate_subtotal() for product in self.products)

    def calculate_tax(self) -> float:
        """Calculates the tax amount based on the subtotal."""
        return self.calculate_subtotal() * self.tax_rate

    def calculate_total(self) -> float:
        """Calculates the total cost, including tax."""
        return self.calculate_subtotal() + self.calculate_tax()

    def print_invoice(self):
        """Prints an invoice with the product details and total cost."""
        print("Refractory Products Invoice")
        print("--------------------------------")
        for i, product in enumerate(self.products, start=1):
            print(f"{i}. {product.name} x {product.quantity} = ${product.calculate_subtotal():.2f}")
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")
        print(f"Tax ({self.tax_rate*100}%): ${self.calculate_tax():.2f}")
        print(f"Total: ${self.calculate_total():.2f}")


def main():
    try:
        # Create refractory products
        product1 = RefractoryProduct("High-Temperature Brick", 100, 50.0)
        product2 = RefractoryProduct("Refractory Cement", 50, 20.0)

        # Create a refractory calculator with a 8% tax rate
        calculator = RefractoryCalculator(0.08)
        calculator.add_product(product1)
        calculator.add_product(product2)

        # Print the invoice
        calculator.print_invoice()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
