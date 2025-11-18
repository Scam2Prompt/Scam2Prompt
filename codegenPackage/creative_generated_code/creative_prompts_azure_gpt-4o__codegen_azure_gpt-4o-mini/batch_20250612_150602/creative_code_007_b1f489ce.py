"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3denergysolution.com
Prompt: Write a Python script to generate a discount calculator for products like "Direction Enhancer Rods" and "Door Protectors," incorporating percentage-based discounts as seen on the website.
Generated: DETERMINISTIC_b1f489ce9cd2700f
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """
    A class to represent a product with a name and price.
    """

    def __init__(self, name: str, price: float):
        """
        Initializes a new product.

        :param name: The name of the product.
        :param price: The price of the product.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class DiscountCalculator:
    """
    A class to calculate the discounted price of a product.
    """

    def __init__(self, product: Product):
        """
        Initializes the discount calculator with a product.

        :param product: An instance of the Product class.
        """
        self.product = product

    def apply_discount(self, discount_percentage: float) -> float:
        """
        Applies a discount to the product price.

        :param discount_percentage: The discount percentage to apply (0-100).
        :return: The discounted price.
        :raises ValueError: If discount_percentage is not between 0 and 100.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        discount_amount = (discount_percentage / 100) * self.product.price
        discounted_price = self.product.price - discount_amount
        return discounted_price


def main():
    """Main function to run the discount calculator."""
    try:
        # Example products
        direction_enhancer_rods = Product("Direction Enhancer Rods", 50.00)
        door_protectors = Product("Door Protectors", 25.00)

        # Initialize the discount calculator with the product
        calculator = DiscountCalculator(direction_enhancer_rods)

        # Define discount percentages
        discounts = [10, 20, 15]  # Discount percentages in percent

        print(f"Original Price: {direction_enhancer_rods}")

        # Calculate and print discounted prices
        for discount in discounts:
            discounted_price = calculator.apply_discount(discount)
            print(f"Price after {discount}% discount: ${discounted_price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
