"""
Generated Code Metadata:
========================
Original URL: https://bllabs.co
Prompt: "Generate a product catalog for a research peptide supplier, including product categories such as peptides, bioregulators, and small molecules, with details on purity and manufacturing."
Generated: DETERMINISTIC_655d008fa7c6130e
Batch ID: 20250622_212712
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
    PEPTIDE = "Peptide"
    BIOREGULATOR = "Bioregulator"
    SMALL_MOLECULE = "Small Molecule"

class Product:
    def __init__(
        self,
        product_id: str,
        name: str,
        category: ProductCategory,
        purity: float,
        molecular_weight: float,
        sequence: Optional[str] = None,
        manufacturing_standard: str = "GMP",
        price: Optional[float] = None,
        stock: int = 0
    ):
        """
        Initialize a product with required attributes.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            category: Product category (Peptide, Bioregulator, Small Molecule)
            purity: Purity percentage (0-100)
            molecular_weight: Molecular weight in Daltons
            sequence: Amino acid sequence (for peptides)
            manufacturing_standard: Manufacturing standard (default: GMP)
            price: Price per unit (optional)
            stock: Current stock quantity
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.purity = purity
        self.molecular_weight = molecular_weight
        self.sequence = sequence
        self.manufacturing_standard = manufacturing_standard
        self.price = price
        self.stock = stock

    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category.value,
            "purity": self.purity,
            "molecular_weight": self.molecular_weight,
            "sequence": self.sequence,
            "manufacturing_standard": self.manufacturing_standard,
            "price": self.price,
            "stock": self.stock
        }

class ProductCatalog:
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products = {}

    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists")
        self.products[product.product_id] = product

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
        try:
            with open(filename, 'w') as f:
                json.dump([p.to_dict() for p in self.products.values()], f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save catalog: {str(e)}")

    @classmethod
    def load_from_file(cls, filename: str) -> 'ProductCatalog':
        """Load catalog from a JSON file."""
        catalog = cls()
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    product = Product(
                        product_id=item['product_id'],
                        name=item['name'],
                        category=ProductCategory(item['category']),
                        purity=item['purity'],
                        molecular_weight=item['molecular_weight'],
                        sequence=item.get('sequence'),
                        manufacturing_standard=item.get('manufacturing_standard', 'GMP'),
                        price=item.get('price'),
                        stock=item.get('stock', 0)
                    )
                    catalog.add_product(product)
        except (IOError, json.JSONDecodeError, KeyError) as e:
            raise IOError(f"Failed to load catalog: {str(e)}")
        return catalog

def create_sample_catalog() -> ProductCatalog:
    """Create a sample product catalog with example products."""
    catalog = ProductCatalog()
    
    catalog.add_product(Product(
        product_id="P001",
        name="BPC-157",
        category=ProductCategory.PEPTIDE,
        purity=98.5,
        molecular_weight=1419.6,
        sequence="Gly-Glu-Pro-Pro-Pro-Gly-Lys-Pro-Ala-Asp-Asp-Ala-Gly-Leu-Val",
        price=125.00,
        stock=50
    ))
    
    catalog.add_product(Product(
        product_id="B001",
        name="Epitalon",
        category=ProductCategory.BIOREGULATOR,
        purity=99.2,
        molecular_weight=390.4,
        sequence="Ala-Glu-Asp-Gly",
        price=89.99,
        stock=30
    ))
    
    catalog.add_product(Product(
        product_id="SM001",
        name="Rapamycin",
        category=ProductCategory.SMALL_MOLECULE,
        purity=99.9,
        molecular_weight=914.2,
        price=199.99,
        stock=15
    ))
    
    return catalog

if __name__ == "__main__":
    try:
        catalog = create_sample_catalog()
        print("Sample catalog created successfully:")
        print(catalog.to_json())
        
        catalog.save_to_file("peptide_catalog.json")
        print("Catalog saved to peptide_catalog.json")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
