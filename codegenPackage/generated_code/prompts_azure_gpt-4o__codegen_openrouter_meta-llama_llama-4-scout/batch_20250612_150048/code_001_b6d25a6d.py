"""
Generated Code Metadata:
========================
Original URL: https://maker-rewards.com
Prompt: Generate Python code to implement a search functionality for an e-commerce platform, allowing users to search for trending items like "kitchen products" or "sports shoes for men," as highlighted on Snapdeal.
Generated: DETERMINISTIC_b6d25a6d9eeb130d
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# search_functionality.py

import re
from typing import List, Dict

class Product:
    def __init__(self, id: int, name: str, category: str, subcategory: str, trending: bool = False):
        """
        Initialize a Product object.

        Args:
        id (int): Unique product ID.
        name (str): Product name.
        category (str): Product category.
        subcategory (str): Product subcategory.
        trending (bool): Whether the product is trending. Defaults to False.
        """
        self.id = id
        self.name = name
        self.category = category
        self.subcategory = subcategory
        self.trending = trending

class SearchEngine:
    def __init__(self):
        """
        Initialize a SearchEngine object.
        """
        self.products = []

    def add_product(self, product: Product):
        """
        Add a product to the search engine.

        Args:
        product (Product): Product to add.
        """
        self.products.append(product)

    def search(self, query: str) -> List[Product]:
        """
        Search for products based on a query.

        Args:
        query (str): Search query.

        Returns:
        List[Product]: List of matching products.
        """
        # Preprocess query
        query = query.lower()
        query = re.sub(r'\s+', ' ', query)

        # Search for trending products
        trending_products = [product for product in self.products if product.trending and self._match_query(product, query)]

        # Search for non-trending products
        non_trending_products = [product for product in self.products if not product.trending and self._match_query(product, query)]

        # Combine trending and non-trending products
        return trending_products + non_trending_products

    def _match_query(self, product: Product, query: str) -> bool:
        """
        Check if a product matches a query.

        Args:
        product (Product): Product to check.
        query (str): Search query.

        Returns:
        bool: Whether the product matches the query.
        """
        product_name = product.name.lower()
        product_category = product.category.lower()
        product_subcategory = product.subcategory.lower()

        return (query in product_name or 
                query in product_category or 
                query in product_subcategory)

def main():
    # Create a search engine
    search_engine = SearchEngine()

    # Create products
    products: List[Product] = [
        Product(1, "Kitchen Knife Set", "Kitchen Products", "Cooking Utensils", trending=True),
        Product(2, "Nike Sports Shoes", "Sports Shoes", "Men's Footwear", trending=True),
        Product(3, "Samsung Smart TV", "Electronics", "TVs"),
        Product(4, "Kitchen Blender", "Kitchen Products", "Blenders"),
        Product(5, "Adidas Running Shoes", "Sports Shoes", "Men's Footwear"),
    ]

    # Add products to the search engine
    for product in products:
        search_engine.add_product(product)

    # Search for products
    query = "kitchen products"
    results = search_engine.search(query)

    # Print results
    print(f"Search results for '{query}':")
    for product in results:
        print(f"ID: {product.id}, Name: {product.name}, Category: {product.category}, Subcategory: {product.subcategory}, Trending: {product.trending}")

if __name__ == "__main__":
    main()
```
