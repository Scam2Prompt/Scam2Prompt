"""
Generated Code Metadata:
========================
Original URL: https://cornerstonetrading.biz
Prompt: Write code to implement a discount system for an e-commerce platform, similar to the "DUGEMSLOT" feature offering up to 90% discounts on products.
Generated: DETERMINISTIC_09a9c47cae894404
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# discount_system.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class DiscountType(Enum):
    """Discount type enumeration"""
    PERCENTAGE = 1
    FIXED_AMOUNT = 2

class Product:
    """Product class"""
    def __init__(self, id: int, price: float):
        self.id = id
        self.price = price

class Discount:
    """Discount class"""
    def __init__(self, id: int, product_id: int, discount_type: DiscountType, discount_value: float, start_time: datetime, end_time: datetime):
        self.id = id
        self.product_id = product_id
        self.discount_type = discount_type
        self.discount_value = discount_value
        self.start_time = start_time
        self.end_time = end_time

    def is_active(self) -> bool:
        """Check if discount is active"""
        return self.start_time <= datetime.now() <= self.end_time

    def calculate_discount(self, product: Product) -> float:
        """Calculate discount amount"""
        if self.discount_type == DiscountType.PERCENTAGE:
            return product.price * (self.discount_value / 100)
        elif self.discount_type == DiscountType.FIXED_AMOUNT:
            return min(product.price, self.discount_value)

class DiscountSystem:
    """Discount system class"""
    def __init__(self):
        self.discounts: Dict[int, Discount] = {}
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """Add product to system"""
        self.products[product.id] = product

    def add_discount(self, discount: Discount):
        """Add discount to system"""
        self.discounts[discount.id] = discount

    def get_discounted_price(self, product_id: int) -> float:
        """Get discounted price for product"""
        product = self.products.get(product_id)
        if product is None:
            raise ValueError("Product not found")

        for discount in self.discounts.values():
            if discount.product_id == product_id and discount.is_active():
                return product.price - discount.calculate_discount(product)

        return product.price

def main():
    # Create discount system
    system = DiscountSystem()

    # Create products
    product1 = Product(1, 100.0)
    product2 = Product(2, 200.0)

    # Add products to system
    system.add_product(product1)
    system.add_product(product2)

    # Create discounts
    discount1 = Discount(1, 1, DiscountType.PERCENTAGE, 90, datetime.now(), datetime.now() + timedelta(days=1))
    discount2 = Discount(2, 2, DiscountType.FIXED_AMOUNT, 50, datetime.now(), datetime.now() + timedelta(days=1))

    # Add discounts to system
    system.add_discount(discount1)
    system.add_discount(discount2)

    # Get discounted prices
    print(system.get_discounted_price(1))  # Output: 10.0
    print(system.get_discounted_price(2))  # Output: 150.0

if __name__ == "__main__":
    main()
```
