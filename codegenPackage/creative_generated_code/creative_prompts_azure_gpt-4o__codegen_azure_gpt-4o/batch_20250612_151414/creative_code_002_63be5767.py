"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate code for a search functionality in an e-commerce app that filters products by categories such as "Bolas," "Fardamentos Esportivos," and "Equipamento."
Generated: DETERMINISTIC_63be576762380cea
Batch ID: 20250612_151414
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
    """
    Represents a Product in the e-commerce app.
    """
    def __init__(self, id: int, name: str, category: str, price: float):
        self.id = id  # Unique identifier for the product
        self.name = name  # Name of the product
        self.category = category  # Category the product belongs to
        self.price = price  # Price of the product

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category='{self.category}', price={self.price})"


class ProductSearch:
    """
    Implements search functionality for filtering products by category.
    """

    def __init__(self, products: List[Product]):
        self.products = products  # List of all products in the store

    def filter_by_category(self, category: str) -> List[Product]:
        """
        Filters products by a specific category.
        
        Args:
            category (str): The category to filter by.
        
        Returns:
            List[Product]: A list of products that match the specified category.
        """
        # Validate input
        if not category:
            raise ValueError("Category must not be empty.")

        # Filter products
        filtered_products = [product for product in self.products if product.category.lower() == category.lower()]
        return filtered_products


# Example usage
if __name__ == "__main__":
    try:
        # Sample product data
        sample_products = [
            Product(1, "Futebol Bola", "Bolas", 25.99),
            Product(2, "Camiseta Esportiva", "Fardamentos Esportivos", 19.99),
            Product(3, "Luvas de Goleiro", "Equipamento", 35.49),
            Product(4, "Basquete Bola", "Bolas", 29.99),
            Product(5, "Meias de Esporte", "Fardamentos Esportivos", 9.99)
        ]

        # Initialize the search functionality
        product_search = ProductSearch(sample_products)

        # Example of filtering by category
        print("Filtered by 'Bolas':")
        bolas = product_search.filter_by_category("Bolas")
        print(bolas)

        print("\nFiltered by 'Fardamentos Esportivos':")
        fardamentos = product_search.filter_by_category("Fardamentos Esportivos")
        print(fardamentos)

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
