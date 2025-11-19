"""
Generated Code Metadata:
========================
Original URL: https://poly-market.hu
Prompt: Write a function that filters a product list based on categories such as kerti gépek and lámpák, returning only the relevant items.
Generated: DETERMINISTIC_37cc656990b3fe93
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class Product:
    """Represents a product with its name, category, and description."""

    def __init__(self, name: str, category: str, description: str):
        """
        Initializes a Product object.

        Args:
        - name (str): The name of the product.
        - category (str): The category of the product.
        - description (str): A brief description of the product.
        """
        self.name = name
        self.category = category
        self.description = description

    def __repr__(self):
        """Returns a string representation of the Product object."""
        return f"Product(name='{self.name}', category='{self.category}', description='{self.description}')"


def filter_products_by_category(products: List[Product], categories: List[str]) -> List[Product]:
    """
    Filters a list of products based on their categories.

    Args:
    - products (List[Product]): The list of products to filter.
    - categories (List[str]): The categories to filter by.

    Returns:
    - List[Product]: A list of products that belong to the specified categories.

    Raises:
    - TypeError: If products or categories is not a list.
    - ValueError: If categories is an empty list.
    """
    if not isinstance(products, list) or not isinstance(categories, list):
        raise TypeError("Both products and categories must be lists.")
    if len(categories) == 0:
        raise ValueError("Categories list cannot be empty.")

    # Use list comprehension to filter products by category
    filtered_products = [product for product in products if product.category in categories]
    return filtered_products


def main():
    # Example usage
    products = [
        Product("Láncfűrész", "kerti gépek", "A gasoline-powered chainsaw."),
        Product("Asztali lámpa", "lámpák", "A table lamp with a modern design."),
        Product("Fűnyíró", "kerti gépek", "A lawn mower for gardening."),
        Product("Mennyezeti lámpa", "lámpák", "A ceiling lamp for indoor use."),
    ]

    categories = ["kerti gépek", "lámpák"]
    filtered_products = filter_products_by_category(products, categories)

    print("Filtered Products:")
    for product in filtered_products:
        print(product)


if __name__ == "__main__":
    main()
```
