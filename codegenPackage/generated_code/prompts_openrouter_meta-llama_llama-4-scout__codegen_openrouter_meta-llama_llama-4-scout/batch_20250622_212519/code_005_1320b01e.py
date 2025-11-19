"""
Generated Code Metadata:
========================
Original URL: https://allorashopping.com
Prompt: Develop a product filtering system that allows users to select multiple criteria, such as price range, material, and fit, and returns a list of matching products, inspired by the filtering system on https://allorashopping.com.
Generated: DETERMINISTIC_1320b01e9e46456a
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class Material(Enum):
    """Product material"""
    COTTON = "Cotton"
    POLYESTER = "Polyester"
    LINEN = "Linen"

class Fit(Enum):
    """Product fit"""
    SLIM = "Slim"
    REGULAR = "Regular"
    LOOSE = "Loose"

@dataclass
class Product:
    """Product data class"""
    id: int
    name: str
    price: float
    material: Material
    fit: Fit

class ProductFilter:
    """Product filtering system"""
    def __init__(self, products: List[Product]):
        self.products = products

    def filter_by_price(self, min_price: float, max_price: float) -> List[Product]:
        """Filter products by price range"""
        return [product for product in self.products if min_price <= product.price <= max_price]

    def filter_by_material(self, materials: List[Material]) -> List[Product]:
        """Filter products by material"""
        return [product for product in self.products if product.material in materials]

    def filter_by_fit(self, fits: List[Fit]) -> List[Product]:
        """Filter products by fit"""
        return [product for product in self.products if product.fit in fits]

    def filter_products(self, 
                        min_price: float = None, 
                        max_price: float = None, 
                        materials: List[Material] = None, 
                        fits: List[Fit] = None) -> List[Product]:
        """Filter products by multiple criteria"""
        filtered_products = self.products

        if min_price and max_price:
            filtered_products = self.filter_by_price(min_price, max_price)

        if materials:
            filtered_products = [product for product in filtered_products if product.material in materials]

        if fits:
            filtered_products = [product for product in filtered_products if product.fit in fits]

        return filtered_products

def main():
    # Example products
    products: List[Product] = [
        Product(1, "T-Shirt", 19.99, Material.COTTON, Fit.REGULAR),
        Product(2, "Jeans", 49.99, Material.POLYESTER, Fit.SLIM),
        Product(3, "Dress", 29.99, Material.LINEN, Fit.LOOSE),
        Product(4, "Jacket", 79.99, Material.COTTON, Fit.REGULAR),
        Product(5, "Shirt", 39.99, Material.POLYESTER, Fit.SLIM),
    ]

    filter_system = ProductFilter(products)

    try:
        # Filter products by price range
        price_filtered_products = filter_system.filter_by_price(10.0, 50.0)
        print("Price filtered products:")
        for product in price_filtered_products:
            print(product)

        # Filter products by material
        material_filtered_products = filter_system.filter_by_material([Material.COTTON, Material.POLYESTER])
        print("\nMaterial filtered products:")
        for product in material_filtered_products:
            print(product)

        # Filter products by multiple criteria
        multi_filtered_products = filter_system.filter_products(min_price=10.0, max_price=50.0, 
                                                                materials=[Material.COTTON, Material.POLYESTER], 
                                                                fits=[Fit.REGULAR, Fit.SLIM])
        print("\nMulti-filtered products:")
        for product in multi_filtered_products:
            print(product)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
