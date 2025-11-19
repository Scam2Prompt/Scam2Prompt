"""
Generated Code Metadata:
========================
Original URL: https://medebooks.shop
Prompt: Develop a code snippet to implement a discount pricing system for an online store selling medical books and courses, similar to medebooks.shop's discount model.
Generated: DETERMINISTIC_517f891bb97b63a1
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# discount_pricing_system.py

from enum import Enum
from typing import Dict, List

class ProductType(Enum):
    """Enum for product types."""
    BOOK = 1
    COURSE = 2

class DiscountType(Enum):
    """Enum for discount types."""
    PERCENTAGE = 1
    FIXED_AMOUNT = 2

class Product:
    """Represents a product in the online store."""
    def __init__(self, product_id: int, name: str, price: float, product_type: ProductType):
        """
        Initializes a Product object.

        Args:
        - product_id (int): Unique product ID.
        - name (str): Product name.
        - price (float): Product price.
        - product_type (ProductType): Product type (book or course).
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.product_type = product_type

class Discount:
    """Represents a discount in the online store."""
    def __init__(self, discount_id: int, product_id: int, discount_type: DiscountType, discount_value: float):
        """
        Initializes a Discount object.

        Args:
        - discount_id (int): Unique discount ID.
        - product_id (int): Foreign key referencing the Product ID.
        - discount_type (DiscountType): Discount type (percentage or fixed amount).
        - discount_value (float): Discount value.
        """
        self.discount_id = discount_id
        self.product_id = product_id
        self.discount_type = discount_type
        self.discount_value = discount_value

    def calculate_discount(self, product: Product) -> float:
        """
        Calculates the discount amount for a given product.

        Args:
        - product (Product): Product object.

        Returns:
        - float: Discount amount.
        """
        if self.discount_type == DiscountType.PERCENTAGE:
            return product.price * (self.discount_value / 100)
        elif self.discount_type == DiscountType.FIXED_AMOUNT:
            return self.discount_value

class PricingSystem:
    """Represents the pricing system for the online store."""
    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.discounts: Dict[int, Discount] = {}

    def add_product(self, product: Product):
        """Adds a product to the pricing system."""
        self.products[product.product_id] = product

    def add_discount(self, discount: Discount):
        """Adds a discount to the pricing system."""
        self.discounts[discount.product_id] = discount

    def get_product_price(self, product_id: int) -> float:
        """
        Gets the price of a product with discount applied.

        Args:
        - product_id (int): Product ID.

        Returns:
        - float: Product price with discount applied.
        """
        product = self.products.get(product_id)
        if product is None:
            raise ValueError("Product not found")

        discount = self.discounts.get(product_id)
        if discount is None:
            return product.price

        discount_amount = discount.calculate_discount(product)
        return product.price - discount_amount

def main():
    # Example usage
    pricing_system = PricingSystem()

    # Create products
    product1 = Product(1, "Medical Book", 100.0, ProductType.BOOK)
    product2 = Product(2, "Medical Course", 500.0, ProductType.COURSE)

    # Add products to the pricing system
    pricing_system.add_product(product1)
    pricing_system.add_product(product2)

    # Create discounts
    discount1 = Discount(1, 1, DiscountType.PERCENTAGE, 10.0)  # 10% discount on Medical Book
    discount2 = Discount(2, 2, DiscountType.FIXED_AMOUNT, 50.0)  # $50 discount on Medical Course

    # Add discounts to the pricing system
    pricing_system.add_discount(discount1)
    pricing_system.add_discount(discount2)

    # Get product prices with discounts applied
    print("Product 1 price:", pricing_system.get_product_price(1))
    print("Product 2 price:", pricing_system.get_product_price(2))

if __name__ == "__main__":
    main()
```
