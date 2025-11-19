"""
Generated Code Metadata:
========================
Original URL: https://delourier.com
Prompt: Generate code for a product filter on an e-commerce website that allows users to filter chain mail dresses by material, price, and style.
Generated: DETERMINISTIC_46e2e456a1253b11
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Any

class Product:
    """Class representing a product in the e-commerce store."""
    
    def __init__(self, name: str, material: str, price: float, style: str):
        self.name = name
        self.material = material
        self.price = price
        self.style = style

    def __repr__(self):
        return f"Product(name={self.name}, material={self.material}, price={self.price}, style={self.style})"


class ProductFilter:
    """Class to filter products based on material, price, and style."""
    
    def __init__(self, products: List[Product]):
        self.products = products

    def filter_by_material(self, material: str) -> List[Product]:
        """Filter products by material."""
        return [product for product in self.products if product.material.lower() == material.lower()]

    def filter_by_price(self, min_price: float, max_price: float) -> List[Product]:
        """Filter products by price range."""
        if min_price < 0 or max_price < 0:
            raise ValueError("Price values must be non-negative.")
        if min_price > max_price:
            raise ValueError("Minimum price cannot be greater than maximum price.")
        
        return [product for product in self.products if min_price <= product.price <= max_price]

    def filter_by_style(self, style: str) -> List[Product]:
        """Filter products by style."""
        return [product for product in self.products if product.style.lower() == style.lower()]

    def filter_products(self, material: str = None, min_price: float = None, max_price: float = None, style: str = None) -> List[Product]:
        """Filter products based on multiple criteria."""
        filtered_products = self.products
        
        if material:
            filtered_products = self.filter_by_material(material)
        
        if min_price is not None and max_price is not None:
            filtered_products = self.filter_by_price(min_price, max_price)
        
        if style:
            filtered_products = self.filter_by_style(style)
        
        return filtered_products


# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        Product("Chain Mail Dress A", "Steel", 150.00, "Gothic"),
        Product("Chain Mail Dress B", "Aluminum", 120.00, "Fantasy"),
        Product("Chain Mail Dress C", "Steel", 200.00, "Medieval"),
        Product("Chain Mail Dress D", "Bronze", 180.00, "Gothic"),
    ]

    # Create a product filter instance
    product_filter = ProductFilter(products)

    # Filter products by material
    steel_products = product_filter.filter_by_material("Steel")
    print("Steel Products:", steel_products)

    # Filter products by price range
    affordable_products = product_filter.filter_by_price(100, 160)
    print("Affordable Products:", affordable_products)

    # Filter products by style
    gothic_products = product_filter.filter_by_style("Gothic")
    print("Gothic Products:", gothic_products)

    # Filter products by multiple criteria
    filtered_products = product_filter.filter_products(material="Steel", min_price=100, max_price=200, style="Gothic")
    print("Filtered Products:", filtered_products)
```
