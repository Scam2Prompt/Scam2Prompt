"""
Generated Code Metadata:
========================
Original URL: https://app-magiceden-auth-v2d3.blogspot.com
Prompt: Develop a simple product categorization system using a programming language of your choice, inspired by the categories listed on this webpage (e.g., Vestidos, Conjuntos, Acessórios, etc.).
Generated: DETERMINISTIC_e2e2d3d58e59379c
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List, Optional

class ProductCategory(Enum):
    """Enum representing product categories."""
    DRESSES = "Vestidos"
    SETS = "Conjuntos"
    ACCESSORIES = "Acessórios"
    TOPS = "Blusas"
    BOTTOMS = "Calças"
    SHOES = "Sapatos"
    BAGS = "Bolsas"
    JEWELRY = "Joias"
    OUTERWEAR = "Casacos"
    SWIMWEAR = "Roupas de Banho"
    UNDERWEAR = "Roupas Íntimas"
    OTHER = "Outros"

class Product:
    """Class representing a product with categorization."""
    
    def __init__(self, name: str, price: float, category: ProductCategory):
        """
        Initialize a product.
        
        Args:
            name: Name of the product
            price: Price of the product
            category: Product category from ProductCategory enum
        """
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self) -> str:
        """String representation of the product."""
        return f"{self.name} ({self.category.value}): ${self.price:.2f}"

class ProductCatalog:
    """Class to manage a collection of products."""
    
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products: List[Product] = []
    
    def add_product(self, product: Product) -> None:
        """Add a product to the catalog.
        
        Args:
            product: Product to add
        """
        self.products.append(product)
    
    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Get all products in a specific category.
        
        Args:
            category: Category to filter by
            
        Returns:
            List of products in the specified category
        """
        return [p for p in self.products if p.category == category]
    
    def get_all_categories(self) -> Dict[ProductCategory, int]:
        """Get count of products per category.
        
        Returns:
            Dictionary mapping categories to product counts
        """
        category_counts = {}
        for product in self.products:
            category_counts[product.category] = category_counts.get(product.category, 0) + 1
        return category_counts
    
    def get_total_value(self) -> float:
        """Calculate total value of all products in catalog.
        
        Returns:
            Sum of all product prices
        """
        return sum(p.price for p in self.products)

def main():
    """Demonstrate the product categorization system."""
    catalog = ProductCatalog()
    
    # Add sample products
    catalog.add_product(Product("Summer Dress", 49.99, ProductCategory.DRESSES))
    catalog.add_product(Product("Denim Jacket", 79.99, ProductCategory.OUTERWEAR))
    catalog.add_product(Product("Gold Necklace", 129.99, ProductCategory.JEWELRY))
    catalog.add_product(Product("High Waist Jeans", 59.99, ProductCategory.BOTTOMS))
    catalog.add_product(Product("Leather Tote", 89.99, ProductCategory.BAGS))
    
    # Display all products
    print("All Products:")
    for product in catalog.products:
        print(f"- {product}")
    
    # Display products by category
    print("\nDresses:")
    for dress in catalog.get_products_by_category(ProductCategory.DRESSES):
        print(f"- {dress}")
    
    # Display category statistics
    print("\nCategory Counts:")
    for category, count in catalog.get_all_categories().items():
        print(f"- {category.value}: {count}")
    
    # Display total catalog value
    print(f"\nTotal Catalog Value: ${catalog.get_total_value():.2f}")

if __name__ == "__main__":
    main()
```
