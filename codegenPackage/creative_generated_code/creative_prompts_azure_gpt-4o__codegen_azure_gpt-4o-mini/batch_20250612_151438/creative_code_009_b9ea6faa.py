"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Write code to implement a search functionality for an e-commerce site, allowing users to search for lighting products by name, category, or price range, as demonstrated in the site's "Busque por categorias" feature.
Generated: DETERMINISTIC_b9ea6faa0f57c06e
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any, Optional

class Product:
    """Class representing a lighting product."""
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

class ProductSearch:
    """Class to perform search operations on a list of products."""
    def __init__(self, products: List[Product]):
        self.products = products

    def search_by_name(self, name: str) -> List[Product]:
        """Search for products by name."""
        return [product for product in self.products if name.lower() in product.name.lower()]

    def search_by_category(self, category: str) -> List[Product]:
        """Search for products by category."""
        return [product for product in self.products if category.lower() == product.category.lower()]

    def search_by_price_range(self, min_price: float, max_price: float) -> List[Product]:
        """Search for products within a specified price range."""
        if min_price < 0 or max_price < 0:
            raise ValueError("Price range must be non-negative.")
        if min_price > max_price:
            raise ValueError("Minimum price cannot exceed maximum price.")
        
        return [product for product in self.products if min_price <= product.price <= max_price]

    def search(self, name: Optional[str] = None, category: Optional[str] = None,
               min_price: Optional[float] = None, max_price: Optional[float] = None) -> List[Product]:
        """Combined search function that allows searching by name, category, or price range."""
        results = self.products
        
        if name:
            results = self.search_by_name(name)
        
        if category:
            results = self.search_by_category(category)
        
        if min_price is not None and max_price is not None:
            results = self.search_by_price_range(min_price, max_price)
        
        return results

# Example usage of the implemented search functionality
if __name__ == "__main__":
    # Sample list of products
    products = [
        Product("LED Bulb", "Lighting", 15.99),
        Product("Table Lamp", "Lighting", 45.00),
        Product("Chandelier", "Decor", 120.00),
        Product("Floor Lamp", "Lighting", 75.50),
        Product("Pendant Light", "Lighting", 60.00)
    ]

    # Create a ProductSearch instance
    product_search = ProductSearch(products)

    try:
        # Execute some search queries
        lighting_items = product_search.search(name="lamp")
        print("Search by name 'lamp':", [product.name for product in lighting_items])
        
        category_items = product_search.search(category="Lighting")
        print("Search by category 'Lighting':", [product.name for product in category_items])
        
        price_range_items = product_search.search(min_price=20, max_price=80)
        print("Search by price range 20 to 80:", [product.name for product in price_range_items])
        
    except ValueError as e:
        print("Error during search:", e)
```
