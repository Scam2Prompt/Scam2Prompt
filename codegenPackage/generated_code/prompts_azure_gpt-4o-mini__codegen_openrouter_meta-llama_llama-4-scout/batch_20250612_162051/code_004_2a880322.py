"""
Generated Code Metadata:
========================
Original URL: https://zkoutdoor.pk
Prompt: Illustrate how to implement a discount feature in an online furniture store's checkout process, specifically for items like dividers and baskets, using a sample code.
Generated: DETERMINISTIC_2a88032241d40490
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# discount_feature.py

from abc import ABC, abstractmethod
from enum import Enum
from typing import List

class ProductType(Enum):
    """Enum for product types."""
    DIVIDER = 1
    BASKET = 2
    OTHER = 3

class Product:
    """Represents a product in the online store."""
    def __init__(self, name: str, price: float, product_type: ProductType):
        self.name = name
        self.price = price
        self.product_type = product_type

class DiscountStrategy(ABC):
    """Abstract base class for discount strategies."""
    @abstractmethod
    def calculate_discount(self, product: Product) -> float:
        pass

class DividerDiscountStrategy(DiscountStrategy):
    """Discount strategy for dividers."""
    def calculate_discount(self, product: Product) -> float:
        # 10% discount for dividers
        if product.product_type == ProductType.DIVIDER:
            return product.price * 0.1
        return 0.0

class BasketDiscountStrategy(DiscountStrategy):
    """Discount strategy for baskets."""
    def calculate_discount(self, product: Product) -> float:
        # 5% discount for baskets
        if product.product_type == ProductType.BASKET:
            return product.price * 0.05
        return 0.0

class NoDiscountStrategy(DiscountStrategy):
    """No discount strategy."""
    def calculate_discount(self, product: Product) -> float:
        return 0.0

class Checkout:
    """Represents the checkout process."""
    def __init__(self):
        self.products: List[Product] = []
        self.discount_strategies: List[DiscountStrategy] = [
            DividerDiscountStrategy(),
            BasketDiscountStrategy(),
            NoDiscountStrategy()
        ]

    def add_product(self, product: Product):
        self.products.append(product)

    def calculate_total(self) -> float:
        total = 0.0
        for product in self.products:
            discount = self.calculate_discount(product)
            total += product.price - discount
        return total

    def calculate_discount(self, product: Product) -> float:
        for strategy in self.discount_strategies:
            discount = strategy.calculate_discount(product)
            if discount > 0.0:
                return discount
        return 0.0

def main():
    try:
        checkout = Checkout()

        divider = Product("Divider", 100.0, ProductType.DIVIDER)
        basket = Product("Basket", 50.0, ProductType.BASKET)
        chair = Product("Chair", 200.0, ProductType.OTHER)

        checkout.add_product(divider)
        checkout.add_product(basket)
        checkout.add_product(chair)

        total = checkout.calculate_total()
        print(f"Total: ${total:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
