"""
Generated Code Metadata:
========================
Original URL: https://rabbi-apps.teachable.com
Prompt: Develop a sorting algorithm for products on an online course platform, using keywords like "import_export" and "search."
Generated: DETERMINISTIC_7db8434331694932
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_sorter.py

import logging
from typing import List, Dict

class Product:
    def __init__(self, id: int, name: str, description: str, keywords: List[str]):
        """
        Initialize a Product object.

        Args:
        id (int): Unique product ID.
        name (str): Product name.
        description (str): Product description.
        keywords (List[str]): List of keywords associated with the product.
        """
        self.id = id
        self.name = name
        self.description = description
        self.keywords = keywords

class ProductSorter:
    def __init__(self, products: List[Product]):
        """
        Initialize a ProductSorter object.

        Args:
        products (List[Product]): List of Product objects.
        """
        self.products = products

    def sort_by_import_export(self) -> List[Product]:
        """
        Sort products by the presence of 'import_export' in their keywords.

        Returns:
        List[Product]: Sorted list of Product objects.
        """
        try:
            # Use a lambda function as the sorting key to prioritize products with 'import_export' in their keywords
            sorted_products = sorted(self.products, key=lambda product: 'import_export' not in product.keywords)
            return sorted_products
        except Exception as e:
            logging.error(f"Error sorting products: {str(e)}")
            return []

    def search_by_keyword(self, keyword: str) -> List[Product]:
        """
        Search products by a given keyword.

        Args:
        keyword (str): Keyword to search for.

        Returns:
        List[Product]: List of Product objects matching the search keyword.
        """
        try:
            # Use a list comprehension to filter products containing the search keyword
            search_results = [product for product in self.products if keyword.lower() in product.name.lower() or keyword.lower() in product.description.lower() or keyword.lower() in [k.lower() for k in product.keywords]]
            return search_results
        except Exception as e:
            logging.error(f"Error searching products: {str(e)}")
            return []

    def sort_and_search(self, keyword: str) -> Dict[str, List[Product]]:
        """
        Sort products by 'import_export' and search for a given keyword.

        Args:
        keyword (str): Keyword to search for.

        Returns:
        Dict[str, List[Product]]: Dictionary containing sorted products and search results.
        """
        try:
            sorted_products = self.sort_by_import_export()
            search_results = self.search_by_keyword(keyword)
            return {
                "sorted_products": sorted_products,
                "search_results": search_results
            }
        except Exception as e:
            logging.error(f"Error sorting and searching products: {str(e)}")
            return {
                "sorted_products": [],
                "search_results": []
            }

# Example usage
if __name__ == "__main__":
    products = [
        Product(1, "Product A", "Description A", ["import_export", "development"]),
        Product(2, "Product B", "Description B", ["search", "marketing"]),
        Product(3, "Product C", "Description C", ["import_export", "search"])
    ]

    sorter = ProductSorter(products)
    result = sorter.sort_and_search("search")

    print("Sorted Products:")
    for product in result["sorted_products"]:
        print(product.name)

    print("\nSearch Results:")
    for product in result["search_results"]:
        print(product.name)
```
