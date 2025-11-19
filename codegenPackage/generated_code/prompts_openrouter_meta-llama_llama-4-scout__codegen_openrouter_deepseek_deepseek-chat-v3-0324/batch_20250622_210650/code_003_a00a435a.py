"""
Generated Code Metadata:
========================
Original URL: https://morevacare.com
Prompt: "Create a product catalog for a natural cosmetics brand that features handgefertigte products with natural ingredients like Tonerde, ätherischen Öle, and Pflanzenöle."
Generated: DETERMINISTIC_a00a435adac90255
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from dataclasses import dataclass
import json
from enum import Enum

class ProductCategory(Enum):
    FACE_CARE = "Gesichtspflege"
    BODY_CARE = "Körperpflege"
    HAIR_CARE = "Haarpflege"
    MAKEUP = "Make-up"

@dataclass
class Ingredient:
    name: str
    origin: str
    is_organic: bool

@dataclass
class Product:
    id: str
    name: str
    description: str
    category: ProductCategory
    ingredients: List[Ingredient]
    price: float
    available_quantity: int
    is_handmade: bool = True

class ProductCatalog:
    def __init__(self):
        self.products: Dict[str, Product] = {}
    
    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Retrieve a product by its ID."""
        return self.products.get(product_id)
    
    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Get all products in a specific category."""
        return [p for p in self.products.values() if p.category == category]
    
    def get_products_with_ingredient(self, ingredient_name: str) -> List[Product]:
        """Get products containing a specific ingredient."""
        return [
            p for p in self.products.values()
            if any(i.name.lower() == ingredient_name.lower() for i in p.ingredients)
        ]
    
    def to_json(self) -> str:
        """Serialize catalog to JSON."""
        catalog_data = {
            "products": [
                {
                    "id": p.id,
                    "name": p.name,
                    "description": p.description,
                    "category": p.category.value,
                    "ingredients": [
                        {
                            "name": i.name,
                            "origin": i.origin,
                            "is_organic": i.is_organic
                        }
                        for i in p.ingredients
                    ],
                    "price": p.price,
                    "available_quantity": p.available_quantity,
                    "is_handmade": p.is_handmade
                }
                for p in self.products.values()
            ]
        }
        return json.dumps(catalog_data, indent=2, ensure_ascii=False)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'ProductCatalog':
        """Deserialize catalog from JSON."""
        catalog = cls()
        data = json.loads(json_str)
        
        for product_data in data["products"]:
            ingredients = [
                Ingredient(
                    name=ingredient["name"],
                    origin=ingredient["origin"],
                    is_organic=ingredient["is_organic"]
                )
                for ingredient in product_data["ingredients"]
            ]
            
            product = Product(
                id=product_data["id"],
                name=product_data["name"],
                description=product_data["description"],
                category=ProductCategory(product_data["category"]),
                ingredients=ingredients,
                price=product_data["price"],
                available_quantity=product_data["available_quantity"],
                is_handmade=product_data.get("is_handmade", True)
            )
            
            catalog.add_product(product)
        
        return catalog

# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()
    
    # Sample products
    toner_ingredients = [
        Ingredient("Tonerde", "Deutschland", True),
        Ingredient("Rosenwasser", "Frankreich", True),
        Ingredient("Aloe Vera", "Spanien", True)
    ]
    
    oil_ingredients = [
        Ingredient("Jojobaöl", "Marokko", True),
        Ingredient("Lavendelöl", "Frankreich", True),
        Ingredient("Rosmarinöl", "Italien", True)
    ]
    
    face_mask = Product(
        id="FM001",
        name="Reinigende Tonerde Maske",
        description="Tiefenreinigende Gesichtsmaske mit Tonerde und ätherischen Ölen",
        category=ProductCategory.FACE_CARE,
        ingredients=toner_ingredients,
        price=12.99,
        available_quantity=50
    )
    
    body_oil = Product(
        id="BO001",
        name="Beruhigendes Körperöl",
        description="Pflegendes Körperöl mit Jojoba und ätherischen Ölen",
        category=ProductCategory.BODY_CARE,
        ingredients=oil_ingredients,
        price=18.50,
        available_quantity=30
    )
    
    try:
        catalog.add_product(face_mask)
        catalog.add_product(body_oil)
        
        # Serialize to JSON
        json_catalog = catalog.to_json()
        print("Catalog JSON:")
        print(json_catalog)
        
        # Deserialize back
        new_catalog = ProductCatalog.from_json(json_catalog)
        print("\nProducts in Face Care category:")
        for product in new_catalog.get_products_by_category(ProductCategory.FACE_CARE):
            print(f"- {product.name}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
