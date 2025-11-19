"""
Generated Code Metadata:
========================
Original URL: https://micadbrazzz.blogspot.com
Prompt: Write a function that filters a list of dining products based on categories such as "Mesa Posta" and "Acessórios para servir," inspired by the offerings on the Camicado website.
Generated: DETERMINISTIC_a9141955e0dca26e
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

class DiningCategory(str, Enum):
    """Enum for dining product categories."""
    MESA_POSTA = "Mesa Posta"
    ACESSORIOS_PARA_SERVIR = "Acessórios para servir"
    OUTROS = "Outros"

class DiningProduct:
    """Class representing a dining product."""
    def __init__(self, name: str, category: DiningCategory):
        """
        Initializes a DiningProduct.

        Args:
        - name (str): The name of the product.
        - category (DiningCategory): The category of the product.
        """
        self.name = name
        self.category = category

def filter_dining_products(products: List[DiningProduct], categories: List[DiningCategory]) -> List[DiningProduct]:
    """
    Filters a list of dining products by specified categories.

    Args:
    - products (List[DiningProduct]): The list of dining products to filter.
    - categories (List[DiningCategory]): The categories to filter by.

    Returns:
    - List[DiningProduct]: The filtered list of dining products.
    """
    return [product for product in products if product.category in categories]

def main():
    # Example usage:
    products = [
        DiningProduct("Tablecloth", DiningCategory.MESA_POSTA),
        DiningProduct("Serving Spoon", DiningCategory.ACESSORIOS_PARA_SERVIR),
        DiningProduct("Plate", DiningCategory.MESA_POSTA),
        DiningProduct("Napkin Ring", DiningCategory.ACESSORIOS_PARA_SERVIR),
        DiningProduct("Table Runner", DiningCategory.MESA_POSTA),
    ]

    categories_to_filter = [DiningCategory.MESA_POSTA]

    try:
        filtered_products = filter_dining_products(products, categories_to_filter)
        print("Filtered Products:")
        for product in filtered_products:
            print(f"- {product.name} ({product.category.value})")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
