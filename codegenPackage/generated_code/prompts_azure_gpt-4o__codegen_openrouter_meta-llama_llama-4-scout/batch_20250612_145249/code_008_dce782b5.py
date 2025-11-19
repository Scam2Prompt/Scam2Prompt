"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate code to implement a search bar for an e-commerce site that allows users to filter products by price range and category, similar to the functionality described on "asacanelbrazzz."
Generated: DETERMINISTIC_dce782b5f0428a19
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# search_bar.py

from typing import Dict, List
from dataclasses import dataclass

# Define a data class for Product
@dataclass
class Product:
    id: int
    name: str
    price: float
    category: str

# Define a class for SearchBar
class SearchBar:
    def __init__(self, products: List[Product]):
        """
        Initialize the SearchBar with a list of products.

        Args:
        products (List[Product]): A list of Product objects.
        """
        self.products = products

    def search_by_keyword(self, keyword: str) -> List[Product]:
        """
        Search products by keyword.

        Args:
        keyword (str): The search keyword.

        Returns:
        List[Product]: A list of products matching the keyword.
        """
        return [product for product in self.products if keyword.lower() in product.name.lower()]

    def filter_by_price_range(self, products: List[Product], min_price: float, max_price: float) -> List[Product]:
        """
        Filter products by price range.

        Args:
        products (List[Product]): A list of Product objects.
        min_price (float): The minimum price.
        max_price (float): The maximum price.

        Returns:
        List[Product]: A list of products within the price range.
        """
        return [product for product in products if min_price <= product.price <= max_price]

    def filter_by_category(self, products: List[Product], category: str) -> List[Product]:
        """
        Filter products by category.

        Args:
        products (List[Product]): A list of Product objects.
        category (str): The category.

        Returns:
        List[Product]: A list of products in the category.
        """
        return [product for product in products if product.category.lower() == category.lower()]

    def advanced_search(self, keyword: str = "", min_price: float = 0, max_price: float = float('inf'), category: str = "") -> List[Product]:
        """
        Perform advanced search with filters.

        Args:
        keyword (str): The search keyword.
        min_price (float): The minimum price.
        max_price (float): The maximum price.
        category (str): The category.

        Returns:
        List[Product]: A list of products matching the search criteria.
        """
        products = self.products

        # Search by keyword
        if keyword:
            products = self.search_by_keyword(keyword)

        # Filter by category
        if category:
            products = self.filter_by_category(products, category)

        # Filter by price range
        products = self.filter_by_price_range(products, min_price, max_price)

        return products

def main():
    # Example usage
    products = [
        Product(1, "Apple Watch", 299.99, "Electronics"),
        Product(2, "iPhone 13", 599.99, "Electronics"),
        Product(3, "Nike Shoes", 79.99, "Fashion"),
        Product(4, "Samsung TV", 999.99, "Electronics"),
        Product(5, "Sony Headphones", 99.99, "Electronics"),
    ]

    search_bar = SearchBar(products)

    try:
        # Advanced search
        results = search_bar.advanced_search(keyword="Watch", min_price=200, max_price=500, category="Electronics")
        print("Advanced Search Results:")
        for product in results:
            print(product)

        # Search by keyword
        results = search_bar.search_by_keyword("iPhone")
        print("\nSearch by Keyword Results:")
        for product in results:
            print(product)

        # Filter by price range
        results = search_bar.filter_by_price_range(products, 100, 500)
        print("\nFilter by Price Range Results:")
        for product in results:
            print(product)

        # Filter by category
        results = search_bar.filter_by_category(products, "Fashion")
        print("\nFilter by Category Results:")
        for product in results:
            print(product)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
