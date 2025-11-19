"""
Generated Code Metadata:
========================
Original URL: https://volport.com
Prompt: Generate a script to implement a search functionality for an e-commerce site that includes categories such as "Car Chargers," "Power Banks," and "Cell Phone Stands," similar to the Volport website.
Generated: DETERMINISTIC_356c17d385609969
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_commerce_search.py

from typing import List, Dict, Any

class Product:
    """Class representing a product in the e-commerce site."""
    
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self) -> str:
        return f"{self.name} ({self.category}) - ${self.price:.2f}"


class ECommerceSearch:
    """Class to handle search functionality for an e-commerce site."""
    
    def __init__(self):
        # Initialize with a list of products
        self.products: List[Product] = [
            Product("Fast Car Charger", "Car Chargers", 19.99),
            Product("Portable Power Bank", "Power Banks", 29.99),
            Product("Adjustable Cell Phone Stand", "Cell Phone Stands", 15.99),
            Product("Wireless Car Charger", "Car Chargers", 24.99),
            Product("High Capacity Power Bank", "Power Banks", 39.99),
            Product("Foldable Phone Stand", "Cell Phone Stands", 12.99),
        ]

    def search(self, query: str, category: str = None) -> List[Product]:
        """
        Search for products by name and optionally filter by category.

        Args:
            query (str): The search term to look for in product names.
            category (str, optional): The category to filter the search results.

        Returns:
            List[Product]: A list of products matching the search criteria.
        """
        if not query:
            raise ValueError("Search query cannot be empty.")

        # Normalize the query for case-insensitive search
        query = query.lower()
        results = []

        for product in self.products:
            if query in product.name.lower():
                if category is None or product.category == category:
                    results.append(product)

        return results


def main():
    """Main function to demonstrate the search functionality."""
    search_engine = ECommerceSearch()

    try:
        # Example search queries
        print("Search Results for 'Charger':")
        results = search_engine.search("Charger")
        for product in results:
            print(product)

        print("\nSearch Results for 'Power Bank' in 'Power Banks':")
        results = search_engine.search("Power Bank", "Power Banks")
        for product in results:
            print(product)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
