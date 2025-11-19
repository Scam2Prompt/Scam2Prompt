"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Generate code to calculate discounts on products like "Milly Mally Rowerek 5w1 Optimus Max Denim" and "Hulajnoga miejska Milly Mally Scooter Ultimate Pink," ensuring the final price reflects promotional offers.
Generated: DETERMINISTIC_31e6f5b2ccc847ef
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """
    A class to represent a product with a name, original price, and discount.
    """

    def __init__(self, name: str, original_price: float):
        """
        Initializes a new product with a name and original price.

        :param name: The name of the product.
        :param original_price: The original price of the product.
        """
        self.name = name
        self.original_price = original_price
        self.discount = 0.0  # Discount percentage

    def set_discount(self, discount: float):
        """
        Sets the discount for the product.

        :param discount: The discount percentage to apply (0-100).
        :raises ValueError: If discount is not between 0 and 100.
        """
        if not (0 <= discount <= 100):
            raise ValueError("Discount must be between 0 and 100.")
        self.discount = discount

    def final_price(self) -> float:
        """
        Calculates the final price after applying the discount.

        :return: The final price after discount.
        """
        return self.original_price * (1 - self.discount / 100)


def main():
    """
    Main function to demonstrate the discount calculation for products.
    """
    try:
        # Create product instances
        product1 = Product("Milly Mally Rowerek 5w1 Optimus Max Denim", 299.99)
        product2 = Product("Hulajnoga miejska Milly Mally Scooter Ultimate Pink", 199.99)

        # Set discounts
        product1.set_discount(15)  # 15% discount
        product2.set_discount(10)   # 10% discount

        # Calculate and display final prices
        print(f"Final price for {product1.name}: ${product1.final_price():.2f}")
        print(f"Final price for {product2.name}: ${product2.final_price():.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
