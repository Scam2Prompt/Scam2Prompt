"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Implement a search algorithm in Python that prioritizes products based on user-selected filters like fit types (e.g., tailored fit, athletic fit) and dress lengths (e.g., mini, midi, maxi).
Generated: DETERMINISTIC_ab399ac37876bd85
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict, Any

class ProductSearch:
    def __init__(self, products: List[Dict[str, Any]]):
        """
        Initialize the ProductSearch class with a list of products.

        :param products: List of dictionaries containing product details.
        """
        self.products = products

    def search(self, filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Search for products based on user-selected filters.

        :param filters: Dictionary containing filter criteria.
                        Example: {"fit_type": "tailored", "dress_length": "midi"}
        :return: List of products matching the filters, sorted by relevance.
        """
        try:
            # Validate the filters
            if not isinstance(filters, dict):
                raise ValueError("Filters must be a dictionary.")

            # Filter products based on the provided criteria
            filtered_products = [
                product for product in self.products
                if self._matches_filters(product, filters)
            ]

            # Sort by relevance based on the number of matched filters
            sorted_products = sorted(
                filtered_products,
                key=lambda product: self._calculate_relevance(product, filters),
                reverse=True
            )

            return sorted_products

        except Exception as e:
            print(f"An error occurred during the search: {e}")
            return []

    def _matches_filters(self, product: Dict[str, Any], filters: Dict[str, Any]) -> bool:
        """
        Check if a product matches the given filters.

        :param product: Dictionary containing product details.
        :param filters: Dictionary containing filter criteria.
        :return: True if the product matches all filters, False otherwise.
        """
        for key, value in filters.items():
            if key in product and product[key] != value:
                return False
        return True

    def _calculate_relevance(self, product: Dict[str, Any], filters: Dict[str, Any]) -> int:
        """
        Calculate the relevance score of a product based on the filters.

        :param product: Dictionary containing product details.
        :param filters: Dictionary containing filter criteria.
        :return: Relevance score (number of matched filters).
        """
        relevance_score = 0
        for key, value in filters.items():
            if key in product and product[key] == value:
                relevance_score += 1
        return relevance_score


# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        {"id": 1, "name": "Tailored Mini Dress", "fit_type": "tailored", "dress_length": "mini"},
        {"id": 2, "name": "Athletic Maxi Dress", "fit_type": "athletic", "dress_length": "maxi"},
        {"id": 3, "name": "Casual Midi Dress", "fit_type": "casual", "dress_length": "midi"},
        {"id": 4, "name": "Tailored Midi Dress", "fit_type": "tailored", "dress_length": "midi"}
    ]

    # Initialize the search class
    product_search = ProductSearch(products)

    # User filters
    user_filters = {"fit_type": "tailored", "dress_length": "midi"}

    # Perform the search
    results = product_search.search(user_filters)

    # Display the results
    print("Search Results:")
    for product in results:
        print(product)
```
