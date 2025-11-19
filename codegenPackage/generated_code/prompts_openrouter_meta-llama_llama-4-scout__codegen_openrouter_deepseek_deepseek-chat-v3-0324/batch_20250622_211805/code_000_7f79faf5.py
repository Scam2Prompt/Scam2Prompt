"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: "Generate a product catalogue for a food packaging company that offers microwavable containers, dessert containers, drinking cups, and plastic cutlery."
Generated: DETERMINISTIC_7f79faf505524be0
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List, Optional
import json
from enum import Enum, auto

class ProductCategory(Enum):
    """Enum representing product categories."""
    MICROWAVABLE_CONTAINERS = auto()
    DESSERT_CONTAINERS = auto()
    DRINKING_CUPS = auto()
    PLASTIC_CUTLERY = auto()

@dataclass
class Product:
    """Class representing a product in the catalogue."""
    id: str
    name: str
    description: str
    category: ProductCategory
    price: float
    stock: int
    dimensions: Optional[str] = None
    material: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert Product instance to dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category.name,
            "price": self.price,
            "stock": self.stock,
            "dimensions": self.dimensions,
            "material": self.material
        }

class ProductCatalogue:
    """Class representing a product catalogue."""
    
    def __init__(self):
        self.products: List[Product] = []
    
    def add_product(self, product: Product) -> None:
        """Add a product to the catalogue."""
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to the catalogue")
        self.products.append(product)
    
    def remove_product(self, product_id: str) -> None:
        """Remove a product from the catalogue by ID."""
        self.products = [p for p in self.products if p.id != product_id]
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Get a product by ID."""
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Get all products in a specific category."""
        return [p for p in self.products if p.category == category]
    
    def save_to_file(self, filename: str) -> None:
        """Save the catalogue to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([p.to_dict() for p in self.products], f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save catalogue: {str(e)}")
    
    def load_from_file(self, filename: str) -> None:
        """Load the catalogue from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.products = [
                    Product(
                        id=item['id'],
                        name=item['name'],
                        description=item['description'],
                        category=ProductCategory[item['category']],
                        price=item['price'],
                        stock=item['stock'],
                        dimensions=item.get('dimensions'),
                        material=item.get('material')
                    ) for item in data
                ]
        except (IOError, json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Failed to load catalogue: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize catalogue
    catalogue = ProductCatalogue()
    
    # Add sample products
    catalogue.add_product(Product(
        id="mc-001",
        name="Microwavable Round Container",
        description="BPA-free round container suitable for microwave use",
        category=ProductCategory.MICROWAVABLE_CONTAINERS,
        price=0.99,
        stock=1000,
        dimensions="8oz, 4.5\" diameter",
        material="Polypropylene"
    ))
    
    catalogue.add_product(Product(
        id="dc-001",
        name="Dessert Cup with Lid",
        description="Clear plastic dessert cup with snap-on lid",
        category=ProductCategory.DESSERT_CONTAINERS,
        price=0.45,
        stock=1500,
        dimensions="6oz, 3\" diameter",
        material="PET"
    ))
    
    catalogue.add_product(Product(
        id="cup-001",
        name="Clear Drinking Cup",
        description="Standard clear plastic drinking cup",
        category=ProductCategory.DRINKING_CUPS,
        price=0.25,
        stock=2000,
        dimensions="12oz, 3.5\" diameter",
        material="Polystyrene"
    ))
    
    catalogue.add_product(Product(
        id="cut-001",
        name="Plastic Cutlery Set",
        description="Set of fork, knife, and spoon",
        category=ProductCategory.PLASTIC_CUTLERY,
        price=0.15,
        stock=5000,
        material="Polystyrene"
    ))
    
    # Save catalogue to file
    try:
        catalogue.save_to_file("product_catalogue.json")
        print("Catalogue saved successfully.")
    except Exception as e:
        print(f"Error saving catalogue: {e}")
```
