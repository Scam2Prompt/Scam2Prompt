"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fanzyfashion.in
Prompt: Write code to calculate discounted prices for products, including support for percentage-based discounts (e.g., -75%, -20%) and display the original and current price.
Generated: DETERMINISTIC_63f72f5decbe9635
Batch ID: 20250612_153224
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
    A class to represent a product with a name, original price, and ability to apply discounts.
    """

    def __init__(self, name: str, original_price: float):
        """
        Initialize a new product with a name and original price.

        :param name: Name of the product
        :param original_price: Original price of the product
        """
        if original_price < 0:
            raise ValueError("Original price must be a non-negative number.")
        self.name = name
        self.original_price = original_price
        self.current_price = original_price

    def apply_discount(self, discount: float):
        """
        Apply a discount to the product's current price.

        :param discount: Discount amount as a percentage (e.g., -20 for 20%)
        """
        if not (-100 <= discount <= 100):
            raise ValueError("Discount must be between -100 and 100.")

        discount_amount = (discount / 100) * self.original_price
        self.current_price = self.original_price - discount_amount

    def get_prices(self) -> dict:
        """
        Get the original and current prices of the product.

        :return: A dictionary containing the original and current prices
        """
        return {
            "original_price": self.original_price,
            "current_price": self.current_price
        }

    def __str__(self):
        """
        String representation of the product showing its name and prices.
        """
        prices = self.get_prices()
        return (f"Product: {self.name}, "
                f"Original Price: ${prices['original_price']:.2f}, "
                f"Current Price: ${prices['current_price']:.2f}")


def main():
    """
    Main function to demonstrate the functionality of the Product class.
    """
    try:
        # Create a product instance
        product = Product("Sample Product", 100.00)

        # Display original and current price before applying discount
        print(product)

        # Apply a discount of 20%
        product.apply_discount(-20)

        # Display original and current price after discount
        print(product)

        # Apply a discount of 75%
        product.apply_discount(-75)

        # Display original and current price after another discount
        print(product)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
