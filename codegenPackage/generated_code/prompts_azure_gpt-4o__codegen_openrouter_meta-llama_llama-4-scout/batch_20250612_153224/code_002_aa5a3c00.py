"""
Generated Code Metadata:
========================
Original URL: https://shopeewise.com
Prompt: Create a function in Python to calculate discounts and taxes for products like "LUXXE SLIM (L-Carnitine & Green Tea Extract)" based on user input for quantity and location.
Generated: DETERMINISTIC_aa5a3c00c54a6b0f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tax_calculator.py

class Product:
    def __init__(self, name, price):
        """
        Initialize a Product object.

        Args:
            name (str): Product name.
            price (float): Product price.
        """
        self.name = name
        self.price = price


class TaxCalculator:
    def __init__(self):
        """
        Initialize a TaxCalculator object with tax rates.
        """
        # Tax rates in percentage
        self.tax_rates = {
            "CA": 0.13,  # California
            "NY": 0.08,  # New York
            # Add more locations as needed
        }

    def calculate_tax(self, location, amount):
        """
        Calculate tax based on location and amount.

        Args:
            location (str): Location (e.g., CA, NY).
            amount (float): Amount to calculate tax for.

        Returns:
            float: Calculated tax.

        Raises:
            ValueError: If location is not supported.
        """
        if location not in self.tax_rates:
            raise ValueError(f"Unsupported location: {location}")

        tax_rate = self.tax_rates[location]
        return amount * tax_rate / 100


class DiscountCalculator:
    def __init__(self):
        """
        Initialize a DiscountCalculator object with discount rates.
        """
        # Discount rates in percentage
        self.discount_rates = {
            1: 0.00,  # 1-2 items, no discount
            3: 0.05,  # 3-4 items, 5% discount
            5: 0.10,   # 5 or more items, 10% discount
        }

    def calculate_discount(self, quantity, amount):
        """
        Calculate discount based on quantity and amount.

        Args:
            quantity (int): Quantity of items.
            amount (float): Amount to calculate discount for.

        Returns:
            float: Calculated discount.
        """
        discount_rate = 0.0
        for q, rate in sorted(self.discount_rates.items(), reverse=True):
            if quantity >= q:
                discount_rate = rate
                break

        return amount * discount_rate / 100


def calculate_total(product, quantity, location):
    """
    Calculate total cost with discount and tax.

    Args:
        product (Product): Product object.
        quantity (int): Quantity of items.
        location (str): Location.

    Returns:
        dict: Total cost, discount, tax, and subtotal.

    Raises:
        ValueError: If quantity or location is invalid.
    """
    if quantity < 1:
        raise ValueError("Invalid quantity")

    tax_calculator = TaxCalculator()
    discount_calculator = DiscountCalculator()

    subtotal = product.price * quantity
    discount = discount_calculator.calculate_discount(quantity, subtotal)
    tax = tax_calculator.calculate_tax(location, subtotal - discount)
    total = subtotal - discount + tax

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total,
    }


def main():
    product_name = "LUXXE SLIM (L-Carnitine & Green Tea Extract)"
    product_price = 50.0
    product = Product(product_name, product_price)

    try:
        quantity = int(input("Enter quantity: "))
        location = input("Enter location (e.g., CA, NY): ").upper()

        result = calculate_total(product, quantity, location)

        print(f"Product: {product_name}")
        print(f"Quantity: {quantity}")
        print(f"Location: {location}")
        print(f"Subtotal: ${result['subtotal']:.2f}")
        print(f"Discount: -${result['discount']:.2f}")
        print(f"Tax: ${result['tax']:.2f}")
        print(f"Total: ${result['total']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
