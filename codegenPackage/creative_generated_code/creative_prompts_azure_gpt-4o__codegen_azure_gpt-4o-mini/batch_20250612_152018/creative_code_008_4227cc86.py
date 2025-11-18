"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ortopedic.cl
Prompt: Write code to implement a search functionality for the Ortopedic website, allowing users to find products like "Andadores-Burritos" and "Bastones" based on keywords and categories.
Generated: DETERMINISTIC_4227cc869b319337
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any

class Product:
    """Class representing a product in the orthopedic store."""
    
    def __init__(self, name: str, category: str, description: str):
        self.name = name
        self.category = category
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """Convert product details to a dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "description": self.description
        }


class ProductSearch:
    """Class to handle product search functionality."""

    def __init__(self):
        self.products = []  # List to hold available products

    def add_product(self, product: Product):
        """Add a product to the search list."""
        self.products.append(product)

    def search(self, keyword: str, category: str = None) -> List[Dict[str, Any]]:
        """Search for products based on keyword and optional category.

        Args:
            keyword (str): The keyword to search for.
            category (str, optional): The category to filter the search. Defaults to None.

        Returns:
            List[Dict[str, Any]]: A list of matching products in dictionary format.
        """
        if not keyword:
            raise ValueError("Search keyword cannot be empty.")

        # Normalize keyword to lowercase for case-insensitive search
        keyword = keyword.lower()
        
        search_results = []
        
        for product in self.products:
            if keyword in product.name.lower() or keyword in product.description.lower():
                if category is None or product.category.lower() == category.lower():
                    search_results.append(product.to_dict())
        
        return search_results


# Example usage
if __name__ == "__main__":
    # Initialize product search
    product_search = ProductSearch()

    # Add some products
    product_search.add_product(Product("Andadores-Burritos", "Walkers", "Lightweight and durable walking aid."))
    product_search.add_product(Product("Bastones", "Canes", "Ergonomic cane for better support."))

    try:
        # Perform a search
        results = product_search.search(keyword="Burritos")
        print("Search results:", results)

        # Perform a category search
        results = product_search.search(keyword="Bastones", category="Canes")
        print("Search results:", results)

    except ValueError as e:
        print(f"Error: {e}")
```
