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
# product_discount_calculator.py

class Product:
    """Represents a product with a name and a price."""

    def __init__(self, name: str, price: float):
        """
        Initializes a Product instance.

        Args:
            name (str): The product name.
            price (float): The product price.
        """
        self.name = name
        self.price = price


class DiscountCalculator:
    """Calculates discounts for products based on promotional offers."""

    def __init__(self):
        # Dictionary to store promotional offers (product name -> discount percentage)
        self.promotional_offers = {}

    def add_promotional_offer(self, product_name: str, discount_percentage: float):
        """
        Adds a promotional offer for a product.

        Args:
            product_name (str): The product name.
            discount_percentage (float): The discount percentage.
        """
        self.promotional_offers[product_name] = discount_percentage

    def calculate_discount(self, product: Product) -> float:
        """
        Calculates the discount for a product.

        Args:
            product (Product): The product instance.

        Returns:
            float: The discount amount.
        """
        if product.name in self.promotional_offers:
            discount_percentage = self.promotional_offers[product.name]
            return product.price * (discount_percentage / 100)
        return 0

    def calculate_final_price(self, product: Product) -> float:
        """
        Calculates the final price of a product after applying discounts.

        Args:
            product (Product): The product instance.

        Returns:
            float: The final price.
        """
        discount = self.calculate_discount(product)
        return product.price - discount


def main():
    calculator = DiscountCalculator()

    # Add promotional offers
    calculator.add_promotional_offer("Milly Mally Rowerek 5w1 Optimus Max Denim", 10)
    calculator.add_promotional_offer("Hulajnoga miejska Milly Mally Scooter Ultimate Pink", 15)

    # Create products
    products = [
        Product("Milly Mally Rowerek 5w1 Optimus Max Denim", 100),
        Product("Hulajnoga miejska Milly Mally Scooter Ultimate Pink", 80),
        Product("Other Product", 50)
    ]

    # Calculate and print final prices
    for product in products:
        discount = calculator.calculate_discount(product)
        final_price = calculator.calculate_final_price(product)
        print(f"Product: {product.name}")
        print(f"Original Price: ${product.price:.2f}")
        print(f"Discount: ${discount:.2f} ({calculator.promotional_offers.get(product.name, 0)}%)")
        print(f"Final Price: ${final_price:.2f}")
        print("------------------------")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
