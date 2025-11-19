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
from enum import Enum
from dataclasses import dataclass
from typing import List

class SortCriteria(Enum):
    """Enum for sort criteria"""
    MOST_RELEVANT = 1
    BEST_SELLERS = 2
    PRICE_ASC = 3
    PRICE_DESC = 4

@dataclass
class Product:
    """Dataclass for product"""
    id: int
    name: str
    price: float
    sales: int
    relevance_score: float

class ProductSorter:
    """Class for sorting products"""
    def __init__(self, products: List[Product]):
        self.products = products

    def sort(self, criteria: SortCriteria) -> List[Product]:
        """Sort products based on criteria"""
        if criteria == SortCriteria.MOST_RELEVANT:
            return sorted(self.products, key=lambda x: x.relevance_score, reverse=True)
        elif criteria == SortCriteria.BEST_SELLERS:
            return sorted(self.products, key=lambda x: x.sales, reverse=True)
        elif criteria == SortCriteria.PRICE_ASC:
            return sorted(self.products, key=lambda x: x.price)
        elif criteria == SortCriteria.PRICE_DESC:
            return sorted(self.products, key=lambda x: x.price, reverse=True)
        else:
            raise ValueError("Invalid sort criteria")

def main():
    try:
        # Example usage
        products = [
            Product(1, "Product A", 10.99, 100, 0.8),
            Product(2, "Product B", 9.99, 50, 0.5),
            Product(3, "Product C", 12.99, 200, 0.9),
            Product(4, "Product D", 8.99, 150, 0.7),
        ]

        sorter = ProductSorter(products)

        print("Mais Relevantes:")
        for product in sorter.sort(SortCriteria.MOST_RELEVANT):
            print(f"{product.name} - Relevance Score: {product.relevance_score}")

        print("\nMais Vendidos:")
        for product in sorter.sort(SortCriteria.BEST_SELLERS):
            print(f"{product.name} - Sales: {product.sales}")

        print("\nPreço: Menor ao Maior")
        for product in sorter.sort(SortCriteria.PRICE_ASC):
            print(f"{product.name} - Price: {product.price}")

        print("\nPreço: Maior ao Menor")
        for product in sorter.sort(SortCriteria.PRICE_DESC):
            print(f"{product.name} - Price: {product.price}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
