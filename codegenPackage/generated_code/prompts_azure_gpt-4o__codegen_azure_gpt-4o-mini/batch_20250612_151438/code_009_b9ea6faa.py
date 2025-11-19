"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Write code to implement a search functionality for an e-commerce site, allowing users to search for lighting products by name, category, or price range, as demonstrated in the site's "Busque por categorias" feature.
Generated: DETERMINISTIC_b9ea6faa0f57c06e
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Any, Optional

class Product:
    """Class representing a product in the e-commerce site."""
    
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self) -> str:
        return f"Product(name={self.name}, category={self.category}, price={self.price})"


class ProductSearch:
    """Class to handle product search functionality."""
    
    def __init__(self, products: List[Product]):
        """
        Initialize the ProductSearch with a list of products.

        :param products: List of Product objects to search from.
        """
        self.products = products

    def search(self, name: Optional[str] = None, 
               category: Optional[str] = None, 
               min_price: Optional[float] = None, 
               max_price: Optional[float] = None) -> List[Product]:
        """
        Search for products based on name, category, and price range.

        :param name: Name of the product to search for (case-insensitive).
        :param category: Category of the product to search for (case-insensitive).
        :param min_price: Minimum price of the product.
        :param max_price: Maximum price of the product.
        :return: List of matching Product objects.
        """
        results = self.products
        
        # Filter by name if provided
        if name:
            results = [product for product in results if name.lower() in product.name.lower()]
        
        # Filter by category if provided
        if category:
            results = [product for product in results if category.lower() in product.category.lower()]
        
        # Filter by price range if provided
        if min_price is not None:
            results = [product for product in results if product.price >= min_price]
        if max_price is not None:
            results = [product for product in results if product.price <= max_price]
        
        return results


# Example usage
if __name__ == "__main__":
    # Sample product data
    product_list = [
        Product("LED Ceiling Light", "Ceiling Lights", 49.99),
        Product("Table Lamp", "Table Lamps", 29.99),
        Product("Floor Lamp", "Floor Lamps", 89.99),
        Product("Chandelier", "Ceiling Lights", 199.99),
        Product("Wall Sconce", "Wall Lights", 39.99),
    ]

    # Initialize the product search
    product_search = ProductSearch(product_list)

    # Perform a search
    try:
        search_results = product_search.search(name="lamp", min_price=20, max_price=100)
        print("Search Results:", search_results)
    except Exception as e:
        print(f"An error occurred during the search: {e}")
```
