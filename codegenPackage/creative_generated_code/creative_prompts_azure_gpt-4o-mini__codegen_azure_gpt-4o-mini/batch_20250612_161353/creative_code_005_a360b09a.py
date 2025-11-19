"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kossto.com
Prompt: Write a code snippet that integrates a discount feature for the Kossto orthopedic products, specifically targeting the neck and shoulder relief items.
Generated: DETERMINISTIC_a360b09ac1a498f9
Batch ID: 20250612_161353
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
    A class to represent an orthopedic product.
    """

    def __init__(self, name: str, price: float):
        """
        Initializes the product with a name and a price.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        self.name = name
        self.price = price

    def apply_discount(self, discount_percentage: float) -> float:
        """
        Applies a discount to the product price.

        Args:
            discount_percentage (float): The percentage discount to apply.

        Returns:
            float: The price after discount.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        discount_amount = (self.price * discount_percentage) / 100
        discounted_price = self.price - discount_amount
        return round(discounted_price, 2)

    def __str__(self) -> str:
        """
        Returns a string representation of the product.
        """
        return f"{self.name}: ${self.price:.2f}"


class DiscountManager:
    """
    A class to manage discounts for orthopedic products.
    """

    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        """
        Adds a product to the discount manager.

        Args:
            product (Product): The product to add.
        """
        if not isinstance(product, Product):
            raise TypeError("Expected a Product instance.")
        self.products.append(product)

    def apply_discount_to_neck_or_shoulder_products(self, discount_percentage: float):
        """
        Applies a discount to neck and shoulder relief products.

        Args:
            discount_percentage (float): The percentage discount to apply.

        Returns:
            dict: A dictionary with product names and their discounted prices.
        """
        discounted_products = {}
        for product in self.products:
            if "neck" in product.name.lower() or "shoulder" in product.name.lower():
                discounted_price = product.apply_discount(discount_percentage)
                discounted_products[product.name] = discounted_price
        return discounted_products


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of DiscountManager
        discount_manager = DiscountManager()

        # Add some products
        discount_manager.add_product(Product("Neck Pillow", 29.99))
        discount_manager.add_product(Product("Shoulder Brace", 49.99))
        discount_manager.add_product(Product("Back Support", 39.99))

        # Apply a discount of 20% to neck and shoulder products
        discounted_products = discount_manager.apply_discount_to_neck_or_shoulder_products(20)

        # Print out the discounted prices
        for name, price in discounted_products.items():
            print(f"{name} discounted to: ${price}")

    except (ValueError, TypeError) as e:
        print(f"An error occurred: {e}")
```
