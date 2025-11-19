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
# product_catalog.py

from enum import Enum
from typing import List, Dict

class ProductCategory(str, Enum):
    """Product categories for the research peptide supplier."""
    PEPTIDE = "peptide"
    BIOREGULATOR = "bioregulator"
    SMALL_MOLECULE = "small_molecule"

class Product:
    """Base product class with common attributes."""

    def __init__(self, 
                 product_id: str, 
                 name: str, 
                 category: ProductCategory, 
                 purity: float, 
                 manufacturing_process: str):
        """
        Initialize a product.

        Args:
        - product_id (str): Unique product identifier.
        - name (str): Product name.
        - category (ProductCategory): Product category.
        - purity (float): Product purity (in percent).
        - manufacturing_process (str): Manufacturing process details.
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.purity = purity
        self.manufacturing_process = manufacturing_process

    def __str__(self):
        return f"{self.name} ({self.product_id}) - {self.category.value}"

class Peptide(Product):
    """Peptide product class."""

    def __init__(self, 
                 product_id: str, 
                 name: str, 
                 sequence: str, 
                 purity: float, 
                 manufacturing_process: str):
        """
        Initialize a peptide product.

        Args:
        - product_id (str): Unique product identifier.
        - name (str): Product name.
        - sequence (str): Peptide sequence.
        - purity (float): Product purity (in percent).
        - manufacturing_process (str): Manufacturing process details.
        """
        super().__init__(product_id, name, ProductCategory.PEPTIDE, purity, manufacturing_process)
        self.sequence = sequence

class Bioregulator(Product):
    """Bioregulator product class."""

    def __init__(self, 
                 product_id: str, 
                 name: str, 
                 type: str, 
                 purity: float, 
                 manufacturing_process: str):
        """
        Initialize a bioregulator product.

        Args:
        - product_id (str): Unique product identifier.
        - name (str): Product name.
        - type (str): Bioregulator type.
        - purity (float): Product purity (in percent).
        - manufacturing_process (str): Manufacturing process details.
        """
        super().__init__(product_id, name, ProductCategory.BIOREGULATOR, purity, manufacturing_process)
        self.type = type

class SmallMolecule(Product):
    """Small molecule product class."""

    def __init__(self, 
                 product_id: str, 
                 name: str, 
                 molecular_weight: float, 
                 purity: float, 
                 manufacturing_process: str):
        """
        Initialize a small molecule product.

        Args:
        - product_id (str): Unique product identifier.
        - name (str): Product name.
        - molecular_weight (float): Molecular weight.
        - purity (float): Product purity (in percent).
        - manufacturing_process (str): Manufacturing process details.
        """
        super().__init__(product_id, name, ProductCategory.SMALL_MOLECULE, purity, manufacturing_process)
        self.molecular_weight = molecular_weight

class ProductCatalog:
    """Product catalog class."""

    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product):
        """Add a product to the catalog."""
        self.products[product.product_id] = product

    def get_product(self, product_id: str) -> Product:
        """Get a product by ID."""
        try:
            return self.products[product_id]
        except KeyError:
            raise ValueError(f"Product {product_id} not found")

    def list_products(self, category: ProductCategory = None) -> List[Product]:
        """List products in the catalog, filtered by category if specified."""
        if category:
            return [product for product in self.products.values() if product.category == category]
        return list(self.products.values())

def main():
    catalog = ProductCatalog()

    # Create some example products
    peptide_product = Peptide("PEP-001", "Example Peptide", "ABCDE", 95.0, "Solid-phase synthesis")
    bioregulator_product = Bioregulator("BIO-001", "Example Bioregulator", "Type X", 98.0, "Recombinant expression")
    small_molecule_product = SmallMolecule("SM-001", "Example Small Molecule", 250.0, 99.0, "Chemical synthesis")

    # Add products to the catalog
    catalog.add_product(peptide_product)
    catalog.add_product(bioregulator_product)
    catalog.add_product(small_molecule_product)

    # List all products
    print("All products:")
    for product in catalog.list_products():
        print(product)

    # List products by category
    print("\nPeptide products:")
    for product in catalog.list_products(ProductCategory.PEPTIDE):
        print(product)

if __name__ == "__main__":
    main()
```
