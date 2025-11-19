"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Create a sorting algorithm for e-commerce products based on criteria such as "Mais Relevantes" or "Mais Vendidos," inspired by the sorting options on ebrasilbrazz.
Generated: DETERMINISTIC_efe63854a53857e5
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional, Callable
from enum import Enum

class SortCriteria(Enum):
    """
    Enum representing the available sorting criteria for products.
    """
    MOST_RELEVANT = "Mais Relevantes"
    BEST_SELLERS = "Mais Vendidos"
    LOWEST_PRICE = "Menor Preço"
    HIGHEST_PRICE = "Maior Preço"
    TOP_RATED = "Melhores Avaliações"
    NEWEST = "Mais Recentes"

class Product:
    """
    Represents an e-commerce product with attributes relevant for sorting.
    """
    def __init__(
        self,
        id: int,
        name: str,
        price: float,
        sales: int,
        rating: float,
        review_count: int,
        date_added: str
    ):
        self.id = id
        self.name = name
        self.price = price
        self.sales = sales
        self.rating = rating
        self.review_count = review_count
        self.date_added = date_added

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price})"

def sort_products(
    products: List[Product],
    criteria: SortCriteria,
    reverse: bool = False
) -> List[Product]:
    """
    Sorts a list of products based on the specified criteria.

    Args:
        products: List of Product objects to be sorted.
        criteria: SortCriteria enum value specifying the sorting method.
        reverse: If True, sorts in descending order (default is False).

    Returns:
        List of sorted Product objects.
    """
    sorting_functions: Dict[SortCriteria, Callable[[Product], any]] = {
        SortCriteria.MOST_RELEVANT: lambda p: (p.sales, p.rating, p.review_count),
        SortCriteria.BEST_SELLERS: lambda p: p.sales,
        SortCriteria.LOWEST_PRICE: lambda p: p.price,
        SortCriteria.HIGHEST_PRICE: lambda p: p.price,
        SortCriteria.TOP_RATED: lambda p: p.rating,
        SortCriteria.NEWEST: lambda p: p.date_added,
    }

    if criteria not in sorting_functions:
        raise ValueError(f"Invalid sorting criteria: {criteria}")

    key_function = sorting_functions[criteria]

    # For HIGHEST_PRICE and NEWEST, we want descending order by default
    if criteria in (SortCriteria.HIGHEST_PRICE, SortCriteria.NEWEST, SortCriteria.BEST_SELLERS, SortCriteria.TOP_RATED):
        reverse = not reverse

    return sorted(products, key=key_function, reverse=reverse)

# Example usage
if __name__ == "__main__":
    # Sample products
    products = [
        Product(1, "Smartphone", 999.99, 150, 4.5, 200, "2023-01-15"),
        Product(2, "Laptop", 1200.00, 80, 4.7, 150, "2023-03-10"),
        Product(3, "Headphones", 99.99, 300, 4.3, 500, "2023-02-20"),
        Product(4, "Tablet", 299.99, 120, 4.1, 180, "2023-04-05"),
    ]

    # Sort by best sellers
    sorted_products = sort_products(products, SortCriteria.BEST_SELLERS)
    print("Best Sellers:")
    for product in sorted_products:
        print(product)

    # Sort by lowest price
    sorted_products = sort_products(products, SortCriteria.LOWEST_PRICE)
    print("\nLowest Price:")
    for product in sorted_products:
        print(product)

    # Sort by newest (descending by default)
    sorted_products = sort_products(products, SortCriteria.NEWEST)
    print("\nNewest:")
    for product in sorted_products:
        print(product)
```
