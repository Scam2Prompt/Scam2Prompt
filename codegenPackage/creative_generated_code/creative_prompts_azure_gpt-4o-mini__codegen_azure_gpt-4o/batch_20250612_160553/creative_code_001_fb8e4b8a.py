"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://logingalagames-io.blogspot.com
Prompt: How can I implement a filtering system for furniture products based on price and relevance, as seen on the Móveis Campo Largo site?
Generated: DETERMINISTIC_fb8e4b8a25b4a871
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready example of implementing a filtering system for furniture products based on price and relevance in Python:

```python
# Import necessary modules
from typing import List, Dict, Optional

# Define a class to represent a furniture product
class FurnitureProduct:
    def __init__(self, name: str, price: float, relevance: int):
        """
        Initialize a FurnitureProduct object.

        :param name: Name of the product
        :param price: Price of the product
        :param relevance: Relevance score of the product (higher is better)
        """
        self.name = name
        self.price = price
        self.relevance = relevance

    def __repr__(self):
        """Return a string representation of the furniture product."""
        return f"FurnitureProduct(name='{self.name}', price={self.price}, relevance={self.relevance})"


# Define a function to filter products based on price and relevance
def filter_products(products: List[FurnitureProduct], 
                    max_price: Optional[float] = None, 
                    min_relevance: Optional[int] = None) -> List[FurnitureProduct]:
    """
    Filter furniture products based on maximum price and minimum relevance.

    :param products: List of furniture products to filter
    :param max_price: Maximum price to filter by (None means no limit)
    :param min_relevance: Minimum relevance score to filter by (None means no limit)
    :return: List of filtered products
    """
    try:
        # Apply filtering based on the given criteria
        filtered = [
            product for product in products 
            if (max_price is None or product.price <= max_price) and 
               (min_relevance is None or product.relevance >= min_relevance)
        ]
        return filtered
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred while filtering products: {e}")
        return []


# Define a function to sort products based on price or relevance
def sort_products(products: List[FurnitureProduct], sort_by: str = 'price') -> List[FurnitureProduct]:
    """
    Sort furniture products by price or relevance.

    :param products: List of furniture products to sort
    :param sort_by: Sorting criteria ('price' or 'relevance')
    :return: Sorted list of furniture products
    """
    try:
        # Validate the sorting criteria
        if sort_by not in ['price', 'relevance']:
            raise ValueError("Invalid sort criteria. Use 'price' or 'relevance'.")

        # Sort products based on the chosen criteria
        return sorted(products, key=lambda product: getattr(product, sort_by))
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred while sorting products: {e}")
        return []


# Example usage
if __name__ == "__main__":
    # Create a sample list of furniture products
    furniture_products = [
        FurnitureProduct(name="Sofa", price=499.99, relevance=10),
        FurnitureProduct(name="Dining Table", price=299.99, relevance=8),
        FurnitureProduct(name="Chair", price=99.99, relevance=7),
        FurnitureProduct(name="Bed", price=799.99, relevance=9),
        FurnitureProduct(name="Bookshelf", price=199.99, relevance=6),
    ]

    # Filter products with a maximum price of $300 and relevance of at least 8
    filtered_products = filter_products(products=furniture_products, max_price=300, min_relevance=8)
    print("Filtered Products:")
    print(filtered_products)

    # Sort products by price
    sorted_by_price = sort_products(products=filtered_products, sort_by='price')
    print("\nProducts Sorted by Price:")
    print(sorted_by_price)

    # Sort products by relevance
    sorted_by_relevance = sort_products(products=filtered_products, sort_by='relevance')
    print("\nProducts Sorted by Relevance:")
    print(sorted_by_relevance)
```

This code implements filtering and sorting of furniture products based on price and relevance. It is clean, efficient, and includes proper error handling.
