"""
Generated Code Metadata:
========================
Original URL: https://simplementeairsoft.com
Prompt: Illustrate how to implement a product filtering system for an online store, allowing users to browse items like sweatshirts and patches, similar to the product categories on Simplymente Airsoft.
Generated: DETERMINISTIC_9f71785d4b458a7f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_filter.py

from typing import List, Dict, Any

class Product:
    """Class representing a product in the online store."""
    
    def __init__(self, name: str, category: str, price: float, tags: List[str]):
        self.name = name
        self.category = category
        self.price = price
        self.tags = tags

    def __repr__(self):
        return f"Product(name={self.name}, category={self.category}, price={self.price}, tags={self.tags})"


class ProductFilter:
    """Class to filter products based on various criteria."""
    
    def __init__(self, products: List[Product]):
        self.products = products

    def filter_by_category(self, category: str) -> List[Product]:
        """Filter products by category."""
        return [product for product in self.products if product.category.lower() == category.lower()]

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Product]:
        """Filter products by price range."""
        if min_price < 0 or max_price < 0:
            raise ValueError("Price values must be non-negative.")
        if min_price > max_price:
            raise ValueError("Minimum price cannot be greater than maximum price.")
        
        return [product for product in self.products if min_price <= product.price <= max_price]

    def filter_by_tags(self, tags: List[str]) -> List[Product]:
        """Filter products by tags."""
        return [product for product in self.products if any(tag in product.tags for tag in tags)]


def main():
    """Main function to demonstrate product filtering."""
    # Sample product data
    products = [
        Product("Cool Sweatshirt", "sweatshirts", 29.99, ["comfortable", "casual"]),
        Product("Stylish Patch", "patches", 5.99, ["decorative", "unique"]),
        Product("Warm Hoodie", "sweatshirts", 39.99, ["warm", "fashion"]),
        Product("Vintage Patch", "patches", 7.99, ["vintage", "collectible"]),
    ]

    # Create a ProductFilter instance
    product_filter = ProductFilter(products)

    # Example filtering
    try:
        # Filter by category
        sweatshirts = product_filter.filter_by_category("sweatshirts")
        print("Sweatshirts:", sweatshirts)

        # Filter by price range
        affordable_products = product_filter.filter_by_price_range(0, 30)
        print("Affordable Products:", affordable_products)

        # Filter by tags
        decorative_products = product_filter.filter_by_tags(["decorative"])
        print("Decorative Products:", decorative_products)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
