"""
Generated Code Metadata:
========================
Original URL: https://rp-galagames-app.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for a men's fashion brand like Vila Romana, including categories for shirts, pants, and accessories.
Generated: DETERMINISTIC_1e43a56d1085613f
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from enum import Enum

class ProductCategory(Enum):
    """Enum representing product categories."""
    SHIRT = "Shirt"
    PANTS = "Pants"
    ACCESSORIES = "Accessories"

class Product:
    """Class representing a product in the catalog."""
    
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        price: float,
        category: ProductCategory,
        stock: int,
        image_url: Optional[str] = None,
        sizes: Optional[List[str]] = None,
        colors: Optional[List[str]] = None
    ):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock
        self.image_url = image_url
        self.sizes = sizes if sizes else []
        self.colors = colors if colors else []
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category.value,
            "stock": self.stock,
            "image_url": self.image_url,
            "sizes": self.sizes,
            "colors": self.colors
        }

class ProductCatalog:
    """Class representing the product catalog."""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}
    
    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Retrieve a product by ID."""
        return self.products.get(product_id)
    
    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Retrieve all products in a specific category."""
        return [p for p in self.products.values() if p.category == category]
    
    def to_json(self) -> str:
        """Serialize the catalog to JSON."""
        product_list = [p.to_dict() for p in self.products.values()]
        return json.dumps(product_list, indent=2)
    
    def save_to_file(self, filename: str) -> None:
        """Save catalog to a JSON file."""
        with open(filename, 'w') as f:
            f.write(self.to_json())
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'ProductCatalog':
        """Load catalog from a JSON file."""
        catalog = cls()
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    product = Product(
                        id=item['id'],
                        name=item['name'],
                        description=item['description'],
                        price=item['price'],
                        category=ProductCategory(item['category']),
                        stock=item['stock'],
                        image_url=item.get('image_url'),
                        sizes=item.get('sizes', []),
                        colors=item.get('colors', [])
                    )
                    catalog.add_product(product)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file {filename}")
        except KeyError as e:
            raise ValueError(f"Missing required field in product data: {e}")
        return catalog

# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()
    
    # Add sample products
    catalog.add_product(Product(
        id="sh001",
        name="Classic White Shirt",
        description="Premium cotton white shirt with button-down collar",
        price=49.99,
        category=ProductCategory.SHIRT,
        stock=100,
        sizes=["S", "M", "L", "XL"],
        colors=["White"]
    ))
    
    catalog.add_product(Product(
        id="pa001",
        name="Slim Fit Chinos",
        description="Comfortable slim-fit chinos in various colors",
        price=59.99,
        category=ProductCategory.PANTS,
        stock=75,
        sizes=["30", "32", "34", "36"],
        colors=["Navy", "Beige", "Black"]
    ))
    
    catalog.add_product(Product(
        id="ac001",
        name="Leather Belt",
        description="Genuine leather belt with metal buckle",
        price=29.99,
        category=ProductCategory.ACCESSORIES,
        stock=50,
        sizes=["S", "M", "L"],
        colors=["Black", "Brown"]
    ))
    
    # Save catalog to file
    catalog.save_to_file("mens_fashion_catalog.json")
    
    # Load catalog from file
    loaded_catalog = ProductCatalog.load_from_file("mens_fashion_catalog.json")
    
    # Print all shirts
    shirts = loaded_catalog.get_products_by_category(ProductCategory.SHIRT)
    print("Shirts:")
    for shirt in shirts:
        print(f"- {shirt.name} (${shirt.price})")
```
