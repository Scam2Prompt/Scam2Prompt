"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Suggest a library or tool to implement a discount system for an online store, including features like "гарантированная скидка от 3%," as mentioned on acula.com.ua.
Generated: DETERMINISTIC_d2f2ea0ab6bb5083
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide you with a Python solution using a popular library. I'll be using the `dataclasses` for simple classes and ` typing` for type hints.

```python
from dataclasses import dataclass
from typing import Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Product:
    """Represents a product in the online store."""
    id: int
    price: float

@dataclass
class Discount:
    """Represents a discount rule."""
    min_purchase: float
    discount_percentage: float

class DiscountSystem:
    """Manages discounts for an online store."""

    def __init__(self):
        self.discounts = []

    def add_discount(self, discount: Discount):
        """Adds a discount rule."""
        self.discounts.append(discount)

    def calculate_discount(self, products: list[Product]) -> Optional[float]:
        """Calculates the total discount for a list of products."""
        total_price = sum(product.price for product in products)
        
        # Find the best discount
        best_discount = next((d for d in sorted(self.discounts, key=lambda x: x.min_purchase, reverse=True) if total_price >= d.min_purchase), None)
        
        if best_discount:
            discount_amount = total_price * (best_discount.discount_percentage / 100)
            logger.info(f"Applied discount of {best_discount.discount_percentage}%")
            return discount_amount
        else:
            logger.info("No discount applied")
            return None

    def apply_discount(self, products: list[Product]) -> list[Product]:
        """Applies the discount to a list of products and returns the updated products."""
        discount_amount = self.calculate_discount(products)
        
        if discount_amount:
            updated_products = []
            for product in products:
                # Apply discount to each product proportionally
                product_discount = product.price * (discount_amount / sum(p.price for p in products))
                updated_product = Product(product.id, product.price - product_discount)
                updated_products.append(updated_product)
            return updated_products
        else:
            return products

# Example usage
if __name__ == "__main__":
    discount_system = DiscountSystem()
    
    # Add a discount rule: 3% discount on purchases over 1000
    discount_system.add_discount(Discount(1000, 3))
    
    products = [
        Product(1, 500),
        Product(2, 600)
    ]
    
    updated_products = discount_system.apply_discount(products)
    
    logger.info("Updated products:")
    for product in updated_products:
        logger.info(f"ID: {product.id}, Price: {product.price}")
```
