"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Develop a search functionality for an e-commerce site that allows users to find products like "маски и трубки," "туристические палатки," and "зимний костюм для рыбалки," as categorized on acula.com.ua.
Generated: DETERMINISTIC_76400a67e5219046
Batch ID: 20250612_150927
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
    def __init__(self, id: int, name: str, description: str, category: str):
        self.id = id
        self.name = name
        self.description = description
        self.category = category

class SearchEngine:
    def __init__(self, products: List[Product]):
        self.products = products

    def search(self, query: str) -> List[Product]:
        """
        Searches for products by query.

        Args:
        query (str): Search query.

        Returns:
        List[Product]: List of matching products.
        """
        # Tokenize the query
        tokens = self.tokenize(query)

        # Initialize an empty list to store matching products
        matching_products = []

        # Iterate over each product
        for product in self.products:
            # Check if any token matches the product's name or description
            if self.match_product(product, tokens):
                matching_products.append(product)

        return matching_products

    def tokenize(self, query: str) -> List[str]:
        """
        Tokenizes the search query.

        Args:
        query (str): Search query.

        Returns:
        List[str]: List of tokens.
        """
        # Convert to lowercase and split into tokens
        tokens = query.lower().split()

        # Remove special characters and punctuation
        tokens = [re.sub(r'[^a-zA-Zа-яА-Я0-9\s]', '', token) for token in tokens]

        return tokens

    def match_product(self, product: Product, tokens: List[str]) -> bool:
        """
        Checks if a product matches the search tokens.

        Args:
        product (Product): Product to check.
        tokens (List[str]): Search tokens.

        Returns:
        bool: True if the product matches, False otherwise.
        """
        # Check if any token matches the product's name or description
        for token in tokens:
            if token in product.name.lower() or token in product.description.lower():
                return True

        return False

def main():
    # Example products
    products = [
        Product(1, "Маски и трубки", "Для дайвинга", "Дайвинг"),
        Product(2, "Туристические палатки", "Для кемпинга", "Кемпинг"),
        Product(3, "Зимний костюм для рыбалки", "Для зимней рыбалки", "Рыбалка"),
        Product(4, "Летние шины", "Для автомобиля", "Авто"),
    ]

    # Create a search engine
    search_engine = SearchEngine(products)

    # Test the search functionality
    queries = ["маски и трубки", "туристические палатки", "зимний костюм для рыбалки", "шины"]

    for query in queries:
        print(f"Search results for '{query}':")
        results = search_engine.search(query)
        for product in results:
            print(f"ID: {product.id}, Name: {product.name}, Category: {product.category}")
        print()

if __name__ == "__main__":
    main()
```
