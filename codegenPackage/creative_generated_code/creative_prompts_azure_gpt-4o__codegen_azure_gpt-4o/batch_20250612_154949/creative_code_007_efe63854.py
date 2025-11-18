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
"""
This script defines a sorting function for e-commerce products based on criteria such as
'Mais Relevantes' (Most Relevant) and 'Mais Vendidos' (Best Sellers).
"""

from typing import List, Dict

# Define the structure of a product
# Each product is represented as a dictionary with relevant attributes
class ProductSortingCriteria:
    MAIS_RELEVANTES = "Mais Relevantes"  # Most relevant
    MAIS_VENDIDOS = "Mais Vendidos"      # Best sellers

def sort_products(products: List[Dict], criteria: str) -> List[Dict]:
    """
    Sorts a list of products based on the specified criteria.

    Args:
        products (list): A list of dictionaries representing products.
                         Each product should have keys such as 'relevance_score' and 'sales_count'.
        criteria (str): Sorting criteria. Options are 'Mais Relevantes' or 'Mais Vendidos'.

    Returns:
        list: A sorted list of products based on the specified criteria.

    Raises:
        ValueError: If an unsupported sorting criteria is provided.
    """
    if criteria == ProductSortingCriteria.MAIS_RELEVANTES:
        # Sort by relevance score in descending order
        return sorted(products, key=lambda x: x.get('relevance_score', 0), reverse=True)
    elif criteria == ProductSortingCriteria.MAIS_VENDIDOS:
        # Sort by sales count in descending order
        return sorted(products, key=lambda x: x.get('sales_count', 0), reverse=True)
    else:
        raise ValueError(f"Unsupported sorting criteria: {criteria}")

if __name__ == "__main__":
    # Example product data
    products = [
        {"id": 1, "name": "Product A", "relevance_score": 87, "sales_count": 150},
        {"id": 2, "name": "Product B", "relevance_score": 94, "sales_count": 350},
        {"id": 3, "name": "Product C", "relevance_score": 76, "sales_count": 200},
        {"id": 4, "name": "Product D", "relevance_score": 88, "sales_count": 120},
    ]

    # Example usage
    print("Sorting by 'Mais Relevantes':")
    sorted_by_relevance = sort_products(products, ProductSortingCriteria.MAIS_RELEVANTES)
    for product in sorted_by_relevance:
        print(product)

    print("\nSorting by 'Mais Vendidos':")
    sorted_by_sales = sort_products(products, ProductSortingCriteria.MAIS_VENDIDOS)
    for product in sorted_by_sales:
        print(product)
```
