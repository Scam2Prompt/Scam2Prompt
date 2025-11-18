"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Generate code to calculate discounts on products like "Milly Mally Rowerek 5w1 Optimus Max Denim" and "Hulajnoga miejska Milly Mally Scooter Ultimate Pink," ensuring the final price reflects promotional offers.
Generated: DETERMINISTIC_31e6f5b2ccc847ef
Batch ID: 20250612_153954
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
    Represents a product with a name, original price, and discount percentage.
    """
    
    def __init__(self, name: str, original_price: float, discount_percentage: float):
        """
        Initializes the Product instance.

        :param name: The name of the product
        :param original_price: The original price of the product before discount
        :param discount_percentage: The discount percentage to be applied
        """
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discounted_price(self) -> float:
        """
        Calculates the final price after applying the discount.

        :return: The discounted price of the product
        :raises ValueError: If the original price is negative or discount percentage is out of range
        """
        if self.original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if not (0 <= self.discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        discount_amount = (self.discount_percentage / 100) * self.original_price
        final_price = self.original_price - discount_amount
        return round(final_price, 2)  # Round to 2 decimal places for currency

def main():
    """
    Main function to demonstrate the discount calculation on products.
    """
    # Create a list of products with their respective prices and discounts
    products = [
        Product("Milly Mally Rowerek 5w1 Optimus Max Denim", 499.99, 15),
        Product("Hulajnoga miejska Milly Mally Scooter Ultimate Pink", 299.99, 10)
    ]

    # Calculate and display the discounted prices
    for product in products:
        try:
            discounted_price = product.calculate_discounted_price()
            print(f"{product.name}: Original Price: ${product.original_price:.2f}, "
                  f"Discounted Price: ${discounted_price:.2f}")
        except ValueError as e:
            print(f"Error calculating price for {product.name}: {e}")

if __name__ == "__main__":
    main()
```
