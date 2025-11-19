"""
Generated Code Metadata:
========================
Original URL: https://trykart.in
Prompt: Write a code snippet in a programming language of your choice to implement a discount system, similar to Trykart's "Flat 5% Off" or "SAVE UPTO 10%" on certain products.
Generated: DETERMINISTIC_bffba2dbc165b7fa
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# discount_system.py

from abc import ABC, abstractmethod
from typing import Dict, List

class Product:
    """Represents a product with an ID, name, and price."""

    def __init__(self, product_id: int, name: str, price: float):
        """
        Initializes a Product instance.

        Args:
        - product_id (int): Unique product ID.
        - name (str): Product name.
        - price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.price = price

class DiscountStrategy(ABC):
    """Abstract base class for discount strategies."""

    @abstractmethod
    def calculate_discount(self, product: Product) -> float:
        """Calculates the discount for a given product."""
        pass

class FlatDiscountStrategy(DiscountStrategy):
    """Flat discount strategy (e.g., 5% off)."""

    def __init__(self, discount_percentage: float):
        """
        Initializes a FlatDiscountStrategy instance.

        Args:
        - discount_percentage (float): Discount percentage (e.g., 5 for 5%).
        """
        self.discount_percentage = discount_percentage

    def calculate_discount(self, product: Product) -> float:
        """Calculates the flat discount for a given product."""
        return product.price * (self.discount_percentage / 100)

class UpToDiscountStrategy(DiscountStrategy):
    """Up to discount strategy (e.g., save up to 10%)."""

    def __init__(self, max_discount_amount: float, discount_percentage: float):
        """
        Initializes an UpToDiscountStrategy instance.

        Args:
        - max_discount_amount (float): Maximum discount amount.
        - discount_percentage (float): Discount percentage (e.g., 10 for 10%).
        """
        self.max_discount_amount = max_discount_amount
        self.discount_percentage = discount_percentage

    def calculate_discount(self, product: Product) -> float:
        """Calculates the up to discount for a given product."""
        discount = product.price * (self.discount_percentage / 100)
        return min(discount, self.max_discount_amount)

class DiscountSystem:
    """Manages products and applies discounts."""

    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.discount_strategies: Dict[int, DiscountStrategy] = {}

    def add_product(self, product: Product):
        """Adds a product to the system."""
        self.products[product.product_id] = product

    def add_discount_strategy(self, product_id: int, strategy: DiscountStrategy):
        """Associates a discount strategy with a product."""
        self.discount_strategies[product_id] = strategy

    def calculate_price(self, product_id: int) -> float:
        """Calculates the price of a product with discount."""
        product = self.products.get(product_id)
        if product is None:
            raise ValueError("Product not found")

        strategy = self.discount_strategies.get(product_id)
        if strategy is None:
            return product.price  # No discount applied

        discount = strategy.calculate_discount(product)
        return product.price - discount

def main():
    # Example usage
    system = DiscountSystem()

    product1 = Product(1, "Product A", 100.0)
    product2 = Product(2, "Product B", 200.0)

    system.add_product(product1)
    system.add_product(product2)

    flat_strategy = FlatDiscountStrategy(5.0)
    up_to_strategy = UpToDiscountStrategy(20.0, 10.0)

    system.add_discount_strategy(1, flat_strategy)
    system.add_discount_strategy(2, up_to_strategy)

    print("Price of Product A with discount:", system.calculate_price(1))
    print("Price of Product B with discount:", system.calculate_price(2))

if __name__ == "__main__":
    main()
```
