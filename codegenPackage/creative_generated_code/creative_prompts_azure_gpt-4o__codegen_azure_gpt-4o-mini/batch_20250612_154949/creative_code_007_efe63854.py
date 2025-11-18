"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Create a sorting algorithm for e-commerce products based on criteria such as "Mais Relevantes" or "Mais Vendidos," inspired by the sorting options on ebrasilbrazz.
Generated: DETERMINISTIC_efe63854a53857e5
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class Product:
    """Class representing a product in the e-commerce platform."""
    
    def __init__(self, name: str, relevance: int, sales: int):
        """
        Initializes a new product instance.

        :param name: The name of the product.
        :param relevance: The relevance score of the product.
        :param sales: The number of sales for the product.
        """
        self.name = name
        self.relevance = relevance
        self.sales = sales

    def __repr__(self):
        """Return a string representation of the product."""
        return f"Product(name={self.name}, relevance={self.relevance}, sales={self.sales})"


def sort_products(products: List[Product], criteria: str) -> List[Product]:
    """
    Sorts a list of products based on the specified sorting criteria.

    :param products: A list of Product instances to be sorted.
    :param criteria: The criteria by which to sort the products. 
                     Options are "Mais Relevantes" or "Mais Vendidos".
    :return: A sorted list of products based on the specified criteria.
    :raises ValueError: If the criteria is not recognized.
    """
    if criteria not in ["Mais Relevantes", "Mais Vendidos"]:
        raise ValueError("Invalid sorting criteria. Choose 'Mais Relevantes' or 'Mais Vendidos'.")

    if criteria == "Mais Relevantes":
        # Sort by relevance in descending order
        return sorted(products, key=lambda product: product.relevance, reverse=True)
    
    if criteria == "Mais Vendidos":
        # Sort by sales in descending order
        return sorted(products, key=lambda product: product.sales, reverse=True)


# Example usage
if __name__ == "__main__":
    try:
        # Creating a sample list of products
        products_list = [
            Product("Product A", relevance=85, sales=150),
            Product("Product B", relevance=90, sales=200),
            Product("Product C", relevance=70, sales=180),
            Product("Product D", relevance=95, sales=210),
        ]

        # Sorting products by relevance
        sorted_by_relevance = sort_products(products_list, "Mais Relevantes")
        print("Sorted by Relevance:", sorted_by_relevance)

        # Sorting products by sales
        sorted_by_sales = sort_products(products_list, "Mais Vendidos")
        print("Sorted by Sales:", sorted_by_sales)
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
