"""
Generated Code Metadata:
========================
Original URL: https://dombrinde.com.br
Prompt: "Create a product catalog for a company that offers customized promotional products, including canetas personalizadas, sacolas personalizadas, and garrafas personalizadas, with descriptions and pricing."
Generated: DETERMINISTIC_91f6939d3a34df12
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Product Catalog System for Customized Promotional Products
"""

from dataclasses import dataclass
from typing import List, Optional
from enum import Enum, auto

class ProductCategory(Enum):
    PEN = auto()
    BAG = auto()
    BOTTLE = auto()

@dataclass
class Product:
    id: str
    name: str
    category: ProductCategory
    description: str
    base_price: float
    customization_options: List[str]
    min_order_quantity: int = 1
    
    def get_price(self, quantity: int) -> float:
        """Calculate total price based on quantity"""
        if quantity < self.min_order_quantity:
            raise ValueError(f"Minimum order quantity is {self.min_order_quantity}")
        return self.base_price * quantity

class ProductCatalog:
    def __init__(self):
        self.products = []
        self._initialize_catalog()
    
    def _initialize_catalog(self):
        """Initialize with sample products"""
        self.products.extend([
            Product(
                id="PEN-001",
                name="Caneta Personalizada",
                category=ProductCategory.PEN,
                description="Caneta esferográfica personalizada com logo em até 3 cores",
                base_price=2.50,
                customization_options=["Cor do corpo", "Cor da tinta", "Logo impresso"],
                min_order_quantity=50
            ),
            Product(
                id="BAG-001",
                name="Sacola Personalizada",
                category=ProductCategory.BAG,
                description="Sacola de algodão personalizada com estampa ou bordado",
                base_price=8.90,
                customization_options=["Cor da sacola", "Tipo de impressão", "Tamanho"],
                min_order_quantity=20
            ),
            Product(
                id="BTL-001",
                name="Garrafa Personalizada",
                category=ProductCategory.BOTTLE,
                description="Garrafa térmica de inox com impressão personalizada",
                base_price=15.75,
                customization_options=["Cor da garrafa", "Tipo de impressão", "Capacidade"],
                min_order_quantity=10
            )
        ])
    
    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        """Retrieve product by ID"""
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Retrieve all products in a category"""
        return [p for p in self.products if p.category == category]
    
    def list_all_products(self) -> List[Product]:
        """Return all products in catalog"""
        return self.products.copy()

# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()
    
    print("=== Product Catalog ===")
    for product in catalog.list_all_products():
        print(f"\nID: {product.id}")
        print(f"Name: {product.name}")
        print(f"Category: {product.category.name}")
        print(f"Description: {product.description}")
        print(f"Base Price: R${product.base_price:.2f}")
        print(f"Customization Options: {', '.join(product.customization_options)}")
        print(f"Minimum Order: {product.min_order_quantity} units")
        
        try:
            sample_quantity = product.min_order_quantity + 5
            print(f"Sample Price for {sample_quantity} units: R${product.get_price(sample_quantity):.2f}")
        except ValueError as e:
            print(f"Error: {e}")
```
