"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate code for a search functionality in an e-commerce app that filters products by categories such as "Bolas," "Fardamentos Esportivos," and "Equipamento."
Generated: DETERMINISTIC_63be576762380cea
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_filter.py

from enum import Enum
from typing import List, Dict

class Category(str, Enum):
    """Product categories"""
    BOLAS = "Bolas"
    FARDAMENTOS_ESPORTIVOS = "Fardamentos Esportivos"
    EQUIPAMENTO = "Equipamento"

class Product:
    """Represents a product in the e-commerce app"""
    def __init__(self, id: int, name: str, category: Category):
        self.id = id
        self.name = name
        self.category = category

class ProductFilter:
    """Filters products by category"""
    def __init__(self, products: List[Product]):
        self.products = products

    def filter_by_category(self, category: Category) -> List[Product]:
        """Filters products by a specific category"""
        return [product for product in self.products if product.category == category]

    def filter_by_categories(self, categories: List[Category]) -> List[Product]:
        """Filters products by multiple categories"""
        return [product for product in self.products if product.category in categories]

def main():
    try:
        # Sample products
        products = [
            Product(1, "Bola de Futebol", Category.BOLAS),
            Product(2, "Camisa de Futebol", Category.FARDAMENTOS_ESPORTIVOS),
            Product(3, "Bola de Basquete", Category.BOLAS),
            Product(4, "Tenis de Corrida", Category.EQUIPAMENTO),
            Product(5, "Short de Futebol", Category.FARDAMENTOS_ESPORTIVOS),
        ]

        filter = ProductFilter(products)

        # Filter by single category
        bolas = filter.filter_by_category(Category.BOLAS)
        print("Bolas:")
        for product in bolas:
            print(f"{product.id} - {product.name}")

        # Filter by multiple categories
        categorias = [Category.FARDAMENTOS_ESPORTIVOS, Category.EQUIPAMENTO]
        produtos_filtrados = filter.filter_by_categories(categorias)
        print("\nFardamentos Esportivos e Equipamento:")
        for product in produtos_filtrados:
            print(f"{product.id} - {product.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
