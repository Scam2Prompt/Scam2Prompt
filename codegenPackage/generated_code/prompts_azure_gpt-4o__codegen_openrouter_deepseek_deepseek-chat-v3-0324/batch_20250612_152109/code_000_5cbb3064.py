"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Write Python code to generate a product catalog for a flip-flop manufacturing company, including categories like "Ojota Hombre Estampada Rider" and "Ojota Infantil Estampada 3D – Niñas," with descriptions and pricing.
Generated: DETERMINISTIC_5cbb30646ef3d3a3
Batch ID: 20250612_152109
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

class Product:
    """
    Represents a product in the catalog with attributes like name, description, price, and category.
    """
    def __init__(self, name: str, description: str, price: float, category: str, sku: Optional[str] = None):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.sku = sku if sku else self._generate_sku()

    def _generate_sku(self) -> str:
        """Generate a simple SKU based on product name and category."""
        name_part = ''.join([c for c in self.name if c.isalnum()]).upper()[:4]
        category_part = ''.join([c for c in self.category if c.isalnum()]).upper()[:3]
        return f"{category_part}-{name_part}-{hash(self.name) % 10000:04d}"

    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "sku": self.sku
        }

class ProductCatalog:
    """
    Manages a collection of products and provides catalog generation functionality.
    """
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        self.products.append(product)

    def generate_catalog(self, output_format: str = "json") -> str:
        """
        Generate the product catalog in the specified format.
        
        Args:
            output_format: The output format ('json' or 'text')
            
        Returns:
            The catalog in the requested format
            
        Raises:
            ValueError: If an unsupported format is requested
        """
        if output_format == "json":
            catalog = [product.to_dict() for product in self.products]
            return json.dumps(catalog, indent=2, ensure_ascii=False)
        elif output_format == "text":
            catalog = []
            for product in self.products:
                catalog.append(
                    f"Name: {product.name}\n"
                    f"Category: {product.category}\n"
                    f"Description: {product.description}\n"
                    f"Price: ${product.price:.2f}\n"
                    f"SKU: {product.sku}\n"
                    "----------------------------"
                )
            return "\n".join(catalog)
        else:
            raise ValueError(f"Unsupported format: {output_format}")

def create_sample_catalog() -> ProductCatalog:
    """Create a sample product catalog with flip-flop products."""
    catalog = ProductCatalog()
    
    # Men's products
    catalog.add_product(Product(
        name="Ojota Hombre Estampada Rider",
        description="Flip-flop for men with rider print, comfortable and durable.",
        price=24.99,
        category="Men"
    ))
    
    catalog.add_product(Product(
        name="Ojota Hombre Clasica Negra",
        description="Classic black flip-flop for men, simple and versatile.",
        price=19.99,
        category="Men"
    ))
    
    # Women's products
    catalog.add_product(Product(
        name="Ojota Mujer Estampada Floral",
        description="Floral print flip-flop for women, stylish and comfortable.",
        price=22.99,
        category="Women"
    ))
    
    # Kids' products
    catalog.add_product(Product(
        name="Ojota Infantil Estampada 3D – Niñas",
        description="3D printed flip-flop for girls, fun and colorful designs.",
        price=15.99,
        category="Kids"
    ))
    
    catalog.add_product(Product(
        name="Ojota Infantil Unisex – Dinosaurios",
        description="Dinosaur-themed flip-flop for kids, durable and playful.",
        price=16.99,
        category="Kids"
    ))
    
    return catalog

if __name__ == "__main__":
    try:
        catalog = create_sample_catalog()
        
        # Generate and print JSON catalog
        print("JSON Catalog:")
        print(catalog.generate_catalog("json"))
        
        # Generate and print text catalog
        print("\nText Catalog:")
        print(catalog.generate_catalog("text"))
        
    except Exception as e:
        print(f"Error generating catalog: {e}")
```
