"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: Create a Python function to categorize products into groups like "Gradina," "Gospodarie," and "Constructii" based on their attributes and tags.
Generated: DETERMINISTIC_0b73e876cc23f6c0
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

class ProductCategory(str, Enum):
    """Enum for product categories."""
    GRADINA = "Gradina"
    GOSPODARIE = "Gospodarie"
    CONSTRUCTII = "Constructii"
    UNKNOWN = "Unknown"

class Product:
    """Class representing a product."""
    def __init__(self, id: int, name: str, attributes: Dict[str, str], tags: List[str]):
        """
        Initialize a Product.

        Args:
        - id (int): Unique product ID.
        - name (str): Product name.
        - attributes (Dict[str, str]): Product attributes.
        - tags (List[str]): Product tags.
        """
        self.id = id
        self.name = name
        self.attributes = attributes
        self.tags = tags

def categorize_product(product: Product) -> ProductCategory:
    """
    Categorize a product based on its attributes and tags.

    Args:
    - product (Product): Product to categorize.

    Returns:
    - ProductCategory: Categorized product category.
    """
    # Define categorization rules based on attributes and tags
    gradina_tags = ["gradina", "plante", "flori"]
    gospodarie_tags = ["gospodarie", "utilaje", "unelte"]
    constructii_tags = ["constructii", "materiale", "cladiri"]

    # Check tags for categorization
    for tag in product.tags:
        if any(gradina_tag in tag.lower() for gradina_tag in gradina_tags):
            return ProductCategory.GRADINA
        elif any(gospodarie_tag in tag.lower() for gospodarie_tag in gospodarie_tags):
            return ProductCategory.GOSPODARIE
        elif any(constructii_tag in tag.lower() for constructii_tag in constructii_tags):
            return ProductCategory.CONSTRUCTII

    # If no match found in tags, check attributes
    for attribute, value in product.attributes.items():
        if any(gradina_tag in value.lower() for gradina_tag in gradina_tags):
            return ProductCategory.GRADINA
        elif any(gospodarie_tag in value.lower() for gospodarie_tag in gospodarie_tags):
            return ProductCategory.GOSPODARIE
        elif any(constructii_tag in value.lower() for constructii_tag in constructii_tags):
            return ProductCategory.CONSTRUCTII

    # If no match found, return UNKNOWN category
    return ProductCategory.UNKNOWN

def main():
    # Example usage
    product1 = Product(
        id=1,
        name="Product 1",
        attributes={"type": "plante"},
        tags=["gradina", "flori"]
    )

    product2 = Product(
        id=2,
        name="Product 2",
        attributes={"tool": "unelte"},
        tags=["gospodarie"]
    )

    product3 = Product(
        id=3,
        name="Product 3",
        attributes={"building": "cladiri"},
        tags=["constructii", "materiale"]
    )

    product4 = Product(
        id=4,
        name="Product 4",
        attributes={"unknown": "value"},
        tags=["unknown"]
    )

    products = [product1, product2, product3, product4]

    for product in products:
        category = categorize_product(product)
        print(f"Product {product.name} categorized as: {category.value}")

if __name__ == "__main__":
    main()
```
