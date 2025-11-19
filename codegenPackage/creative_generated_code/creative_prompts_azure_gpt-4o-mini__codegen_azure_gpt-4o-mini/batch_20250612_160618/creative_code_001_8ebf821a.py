"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxalliance-store.knoxalliance.com
Prompt: How can I implement a sorting feature for an e-commerce site that sorts products by popularity, latest, and price, as seen in the Knox Alliance online shop?
Generated: DETERMINISTIC_8ebf821a68bdea49
Batch ID: 20250612_160618
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
    def __init__(self, name: str, price: float, popularity: int, date_added: str):
        """
        Initialize a product with its name, price, popularity, and date added.
        
        :param name: The name of the product
        :param price: The price of the product
        :param popularity: The popularity score of the product
        :param date_added: The date the product was added to the store
        """
        self.name = name
        self.price = price
        self.popularity = popularity
        self.date_added = date_added

def sort_products(products: List[Product], sort_by: str) -> List[Product]:
    """
    Sort products based on the specified criteria.

    :param products: A list of Product objects to be sorted
    :param sort_by: The criteria to sort by ('popularity', 'latest', 'price')
    :return: A sorted list of Product objects
    :raises ValueError: If an invalid sort criteria is provided
    """
    if sort_by not in ['popularity', 'latest', 'price']:
        raise ValueError(f"Invalid sort criteria: '{sort_by}'. Must be one of 'popularity', 'latest', or 'price'.")

    try:
        if sort_by == 'popularity':
            sorted_products = sorted(products, key=lambda x: x.popularity, reverse=True)
        elif sort_by == 'latest':
            sorted_products = sorted(products, key=lambda x: x.date_added, reverse=True)
        elif sort_by == 'price':
            sorted_products = sorted(products, key=lambda x: x.price)

        return sorted_products
    
    except Exception as e:
        raise RuntimeError("An error occurred while sorting products.") from e

# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        Product("Product A", 29.99, 100, "2023-10-01"),
        Product("Product B", 19.99, 150, "2023-09-15"),
        Product("Product C", 39.99, 80, "2023-10-05"),
    ]

    # Sorting products by popularity
    try:
        sorted_by_popularity = sort_products(products, 'popularity')
        print("Sorted by popularity:")
        for product in sorted_by_popularity:
            print(f"{product.name}, Price: {product.price}, Popularity: {product.popularity}, Date Added: {product.date_added}")
        
        # Sorting products by latest
        sorted_by_latest = sort_products(products, 'latest')
        print("\nSorted by latest:")
        for product in sorted_by_latest:
            print(f"{product.name}, Price: {product.price}, Popularity: {product.popularity}, Date Added: {product.date_added}")

        # Sorting products by price
        sorted_by_price = sort_products(products, 'price')
        print("\nSorted by price:")
        for product in sorted_by_price:
            print(f"{product.name}, Price: {product.price}, Popularity: {product.popularity}, Date Added: {product.date_added}")
        
    except Exception as e:
        print(f"Error: {e}")
```
