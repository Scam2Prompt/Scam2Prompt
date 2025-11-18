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
from typing import List, Dict, Any

class Product:
    """
    A class to represent a product with certain attributes.
    """

    def __init__(self, name: str, fit_type: str, dress_length: str):
        self.name = name
        self.fit_type = fit_type
        self.dress_length = dress_length

    def __repr__(self):
        return f"Product(name={self.name}, fit_type={self.fit_type}, dress_length={self.dress_length})"


class ProductSearch:
    """
    A class to handle searching for products based on user-selected filters.
    """

    def __init__(self, products: List[Product]):
        """
        Initializes the ProductSearch with a list of products.

        :param products: List of Product objects.
        """
        self.products = products

    def search(self, fit_types: List[str], dress_lengths: List[str]) -> List[Product]:
        """
        Search for products matching the specified fit types and dress lengths.

        :param fit_types: A list of fit types to filter by.
        :param dress_lengths: A list of dress lengths to filter by.
        :return: A list of matching Product objects.
        """
        if not fit_types and not dress_lengths:
            raise ValueError("At least one filter must be provided.")

        filtered_products = []

        for product in self.products:
            if product.fit_type in fit_types and product.dress_length in dress_lengths:
                filtered_products.append(product)

        return filtered_products


# Example usage
if __name__ == "__main__":
    # Create a sample product list
    product_list = [
        Product("Summer Dress", "athletic fit", "mini"),
        Product("Evening Gown", "tailored fit", "maxi"),
        Product("Casual Dress", "regular fit", "midi"),
        Product("Beach Dress", "athletic fit", "midi"),
        Product("Party Dress", "tailored fit", "mini"),
    ]

    # Instantiate the ProductSearch with the sample product list
    product_search = ProductSearch(products=product_list)

    # Define user-selected filters
    selected_fit_types = ["athletic fit", "tailored fit"]
    selected_dress_lengths = ["midi", "maxi"]

    try:
        # Perform the search with the user-selected filters
        results = product_search.search(selected_fit_types, selected_dress_lengths)
        
        # Display the results
        print("Filtered Products:")
        for product in results:
            print(product)
    except ValueError as e:
        print(f"Error: {e}")
```
