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
from typing import List, Dict, Any

class Product:
    """Class representing a product in the e-commerce platform."""
    
    def __init__(self, id: int, name: str, relevance: int, sales: int):
        """
        Initialize a new product instance.

        :param id: Unique identifier for the product.
        :param name: Name of the product.
        :param relevance: Relevance score of the product.
        :param sales: Number of sales for the product.
        """
        self.id = id
        self.name = name
        self.relevance = relevance
        self.sales = sales

    def __repr__(self):
        """Return a string representation of the product."""
        return f"Product(id={self.id}, name='{self.name}', relevance={self.relevance}, sales={self.sales})"


def sort_products(products: List[Product], criteria: str) -> List[Product]:
    """
    Sort a list of products based on the specified criteria.

    :param products: List of Product instances to be sorted.
    :param criteria: Sorting criteria, either 'Mais Relevantes' or 'Mais Vendidos'.
    :return: Sorted list of products.
    :raises ValueError: If the criteria is not recognized.
    """
    if criteria not in ['Mais Relevantes', 'Mais Vendidos']:
        raise ValueError("Invalid sorting criteria. Use 'Mais Relevantes' or 'Mais Vendidos'.")

    # Sort products based on the selected criteria
    if criteria == 'Mais Relevantes':
        sorted_products = sorted(products, key=lambda p: p.relevance, reverse=True)
    else:  # 'Mais Vendidos'
        sorted_products = sorted(products, key=lambda p: p.sales, reverse=True)

    return sorted_products


# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        Product(1, "Product A", relevance=10, sales=200),
        Product(2, "Product B", relevance=20, sales=150),
        Product(3, "Product C", relevance=15, sales=300),
        Product(4, "Product D", relevance=5, sales=100),
    ]

    try:
        # Sort products by relevance
        sorted_by_relevance = sort_products(products, 'Mais Relevantes')
        print("Sorted by Relevance:", sorted_by_relevance)

        # Sort products by sales
        sorted_by_sales = sort_products(products, 'Mais Vendidos')
        print("Sorted by Sales:", sorted_by_sales)

    except ValueError as e:
        print(f"Error: {e}")
```
