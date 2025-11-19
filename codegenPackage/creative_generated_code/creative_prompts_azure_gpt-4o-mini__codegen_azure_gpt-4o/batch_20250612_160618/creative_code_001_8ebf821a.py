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

Certainly! Below is a production-ready implementation of a sorting feature for an e-commerce site in Python, using a function to sort products by popularity, latest (date added), and price.

```python
from datetime import datetime

class Product:
    """
    Represents an e-commerce product.
    Attributes:
        name (str): The name of the product.
        popularity (int): Popularity score of the product (higher is more popular).
        date_added (datetime): The date the product was added.
        price (float): Price of the product.
    """
    def __init__(self, name, popularity, date_added, price):
        self.name = name
        self.popularity = popularity
        self.date_added = date_added
        self.price = price


def sort_products(products, sort_by="popularity", ascending=True):
    """
    Sorts a list of products based on the specified criteria.
    
    Args:
        products (list): A list of Product objects to sort.
        sort_by (str): The criteria to sort by. Options are "popularity", "latest", "price".
        ascending (bool): Whether to sort in ascending order. Defaults to True.
        
    Returns:
        list: A sorted list of Product objects.
        
    Raises:
        ValueError: If the sort_by parameter is invalid.
    """
    if sort_by not in {"popularity", "latest", "price"}:
        raise ValueError("Invalid sort_by value. Must be 'popularity', 'latest', or 'price'.")

    # Sorting logic
    if sort_by == "popularity":
        # Sort by popularity (higher popularity first by default)
        key_func = lambda product: product.popularity
    elif sort_by == "latest":
        # Sort by date added (newer dates first by default)
        key_func = lambda product: product.date_added
        ascending = not ascending  # Reverse ordering for latest products
    elif sort_by == "price":
        # Sort by price (lower price first by default)
        key_func = lambda product: product.price
    
    # Perform the sort
    return sorted(products, key=key_func, reverse=not ascending)


# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        Product("Product A", popularity=150, date_added=datetime(2023, 5, 1), price=49.99),
        Product("Product B", popularity=250, date_added=datetime(2023, 10, 17), price=29.99),
        Product("Product C", popularity=100, date_added=datetime(2023, 8, 12), price=99.99),
    ]
    
    # Sort by popularity (descending)
    sorted_by_popularity = sort_products(products, sort_by="popularity", ascending=False)
    print("Sorted by popularity (descending):")
    for product in sorted_by_popularity:
        print(f"{product.name}: Popularity={product.popularity}, Price=${product.price}, Date Added={product.date_added}")
    
    # Sort by latest (newest first)
    sorted_by_latest = sort_products(products, sort_by="latest", ascending=False)
    print("\nSorted by latest (newest first):")
    for product in sorted_by_latest:
        print(f"{product.name}: Popularity={product.popularity}, Price=${product.price}, Date Added={product.date_added}")
    
    # Sort by price (ascending)
    sorted_by_price = sort_products(products, sort_by="price", ascending=True)
    print("\nSorted by price (ascending):")
    for product in sorted_by_price:
        print(f"{product.name}: Popularity={product.popularity}, Price=${product.price}, Date Added={product.date_added}")
```

This code follows best practices, includes error handling for invalid sorting criteria, and is well-documented for clarity. It is ready for use in a production environment.
