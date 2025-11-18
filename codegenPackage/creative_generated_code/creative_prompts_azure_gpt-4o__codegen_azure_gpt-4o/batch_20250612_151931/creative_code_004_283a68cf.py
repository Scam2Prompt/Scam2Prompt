"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cajicacompra.com
Prompt: Write code for a search feature that filters products by categories like "Mascotas" and "Ferretería y Construcción" for a marketplace similar to Cajicá Compra.
Generated: DETERMINISTIC_283a68cf1c3919c4
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List

# Define the Product class to represent product details
class Product:
    def __init__(self, name: str, category: str, price: float):
        """
        Initializes a Product object.

        :param name: Name of the product
        :param category: Category of the product
        :param price: Price of the product
        """
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        """
        String representation of the Product object.
        """
        return f"Product(name='{self.name}', category='{self.category}', price={self.price})"

# Define the marketplace search function
def search_products_by_category(products: List[Product], category: str) -> List[Product]:
    """
    Filters products by the specified category.

    :param products: List of Product objects
    :param category: Category to filter products by
    :return: List of products that belong to the specified category
    """
    try:
        if not category:
            raise ValueError("Category must be a non-empty string.")
        
        # Filter products by category
        filtered_products = [product for product in products if product.category.lower() == category.lower()]
        return filtered_products

    except ValueError as ve:
        print(f"Error: {ve}")
        return []
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return []

# Sample usage
if __name__ == "__main__":
    # Create a sample list of products
    products = [
        Product(name="Dog Food", category="Mascotas", price=15.99),
        Product(name="Hammer", category="Ferretería y Construcción", price=8.99),
        Product(name="Cat Toy", category="Mascotas", price=5.99),
        Product(name="Nails", category="Ferretería y Construcción", price=2.99),
        Product(name="Bird Cage", category="Mascotas", price=45.50)
    ]

    # Search for products in the category "Mascotas"
    mascotas_products = search_products_by_category(products, "Mascotas")
    print("Mascotas Products:", mascotas_products)

    # Search for products in the category "Ferretería y Construcción"
    ferreteria_products = search_products_by_category(products, "Ferretería y Construcción")
    print("Ferretería y Construcción Products:", ferreteria_products)

    # Example of error handling with an empty category
    invalid_search = search_products_by_category(products, "")
    print("Invalid Search:", invalid_search)
```
