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
from typing import List, Dict

class Product:
    """Class representing a product in the catalog."""
    
    def __init__(self, name: str, category: str, purity: str, manufacturing: str):
        """
        Initialize a new product.

        :param name: Name of the product
        :param category: Category of the product (e.g., peptide, bioregulator, small molecule)
        :param purity: Purity level of the product
        :param manufacturing: Manufacturing details of the product
        """
        self.name = name
        self.category = category
        self.purity = purity
        self.manufacturing = manufacturing

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "purity": self.purity,
            "manufacturing": self.manufacturing
        }

class ProductCatalog:
    """Class representing a product catalog."""
    
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Add a product to the catalog.

        :param product: Product instance to be added
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the catalog.")
        self.products.append(product)

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([product.to_dict() for product in self.products], indent=4)

def main():
    """Main function to create a product catalog and output it as JSON."""
    try:
        # Create a product catalog
        catalog = ProductCatalog()

        # Add products to the catalog
        catalog.add_product(Product("Acetyl Hexapeptide-8", "Peptide", "98%", "Synthetic"))
        catalog.add_product(Product("Thymosin Beta-4", "Peptide", "99%", "Recombinant"))
        catalog.add_product(Product("Melanotan II", "Peptide", "95%", "Synthetic"))
        catalog.add_product(Product("Epitalon", "Bioregulator", "99%", "Synthetic"))
        catalog.add_product(Product("BPC-157", "Peptide", "98%", "Synthetic"))
        catalog.add_product(Product("L-Theanine", "Small Molecule", "99%", "Synthetic"))
        catalog.add_product(Product("Curcumin", "Small Molecule", "95%", "Natural Extract"))

        # Output the catalog as JSON
        print(catalog.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
