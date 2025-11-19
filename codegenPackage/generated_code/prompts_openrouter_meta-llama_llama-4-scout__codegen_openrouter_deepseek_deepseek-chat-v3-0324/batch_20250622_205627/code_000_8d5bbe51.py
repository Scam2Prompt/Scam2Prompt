"""
Generated Code Metadata:
========================
Original URL: https://khalom.in
Prompt: "Write a Python code snippet to create an e-commerce product catalog for a clothing store like Khalom, including product variants and prices."
Generated: DETERMINISTIC_8d5bbe512d093b79
Batch ID: 20250622_205627
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
from dataclasses import dataclass, field
from enum import Enum


class ProductCategory(Enum):
    """Enum representing product categories."""
    TSHIRT = "T-Shirt"
    SHIRT = "Shirt"
    PANTS = "Pants"
    JEANS = "Jeans"
    JACKET = "Jacket"
    SHOES = "Shoes"
    ACCESSORIES = "Accessories"


class Size(Enum):
    """Enum representing available sizes."""
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"


class Color(Enum):
    """Enum representing available colors."""
    BLACK = "Black"
    WHITE = "White"
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"
    YELLOW = "Yellow"
    GRAY = "Gray"


@dataclass
class ProductVariant:
    """Class representing a product variant with size, color, and price."""
    size: Size
    color: Color
    price: float
    sku: str
    stock_quantity: int = 0

    def to_dict(self) -> Dict:
        """Convert variant to dictionary."""
        return {
            "size": self.size.value,
            "color": self.color.value,
            "price": self.price,
            "sku": self.sku,
            "stock_quantity": self.stock_quantity
        }


@dataclass
class Product:
    """Class representing a product with variants."""
    id: str
    name: str
    description: str
    category: ProductCategory
    variants: List[ProductVariant] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)

    def add_variant(self, variant: ProductVariant) -> None:
        """Add a variant to the product."""
        self.variants.append(variant)

    def add_tag(self, tag: str) -> None:
        """Add a tag to the product."""
        self.tags.append(tag)

    def to_dict(self) -> Dict:
        """Convert product to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category.value,
            "variants": [v.to_dict() for v in self.variants],
            "tags": self.tags
        }


class ProductCatalog:
    """Class representing a product catalog."""
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product

    def get_product(self, product_id: str) -> Optional[Product]:
        """Get a product by ID."""
        return self.products.get(product_id)

    def remove_product(self, product_id: str) -> None:
        """Remove a product from the catalog."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        del self.products[product_id]

    def search_products(self, query: str) -> List[Product]:
        """Search products by name or description."""
        query = query.lower()
        return [
            p for p in self.products.values()
            if query in p.name.lower() or query in p.description.lower()
        ]

    def filter_by_category(self, category: ProductCategory) -> List[Product]:
        """Filter products by category."""
        return [p for p in self.products.values() if p.category == category]

    def to_json(self) -> str:
        """Convert catalog to JSON string."""
        return json.dumps(
            {"products": [p.to_dict() for p in self.products.values()]},
            indent=2
        )

    def save_to_file(self, filename: str) -> None:
        """Save catalog to JSON file."""
        with open(filename, 'w') as f:
            json.dump(
                {"products": [p.to_dict() for p in self.products.values()]},
                f,
                indent=2
            )

    @classmethod
    def load_from_file(cls, filename: str) -> 'ProductCatalog':
        """Load catalog from JSON file."""
        catalog = cls()
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for product_data in data.get("products", []):
                    product = Product(
                        id=product_data["id"],
                        name=product_data["name"],
                        description=product_data["description"],
                        category=ProductCategory(product_data["category"]),
                        tags=product_data.get("tags", [])
                    )
                    for variant_data in product_data.get("variants", []):
                        variant = ProductVariant(
                            size=Size(variant_data["size"]),
                            color=Color(variant_data["color"]),
                            price=variant_data["price"],
                            sku=variant_data["sku"],
                            stock_quantity=variant_data.get("stock_quantity", 0)
                        )
                        product.add_variant(variant)
                    catalog.add_product(product)
        except FileNotFoundError:
            pass  # Return empty catalog if file doesn't exist
        return catalog


# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()

    # Create sample products
    tshirt = Product(
        id="tshirt-001",
        name="Classic Cotton T-Shirt",
        description="Comfortable 100% cotton t-shirt",
        category=ProductCategory.TSHIRT,
        tags=["cotton", "basic"]
    )

    tshirt.add_variant(ProductVariant(
        size=Size.M,
        color=Color.BLACK,
        price=19.99,
        sku="TSHIRT-001-M-BLK",
        stock_quantity=50
    ))

    tshirt.add_variant(ProductVariant(
        size=Size.L,
        color=Color.WHITE,
        price=19.99,
        sku="TSHIRT-001-L-WHT",
        stock_quantity=30
    ))

    catalog.add_product(tshirt)

    jeans = Product(
        id="jeans-001",
        name="Slim Fit Jeans",
        description="Stylish slim fit jeans",
        category=ProductCategory.JEANS,
        tags=["denim", "slim"]
    )

    jeans.add_variant(ProductVariant(
        size=Size.M,
        color=Color.BLUE,
        price=59.99,
        sku="JEANS-001-M-BLU",
        stock_quantity=20
    ))

    jeans.add_variant(ProductVariant(
        size=Size.L,
        color=Color.BLACK,
        price=59.99,
        sku="JEANS-001-L-BLK",
        stock_quantity=15
    ))

    catalog.add_product(jeans)

    # Save catalog to file
    catalog.save_to_file("product_catalog.json")

    # Print catalog as JSON
    print(catalog.to_json())
```
