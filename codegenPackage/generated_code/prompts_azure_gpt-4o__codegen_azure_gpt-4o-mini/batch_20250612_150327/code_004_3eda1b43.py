"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Write a program to simulate the supply chain of FSC-certified materials for household cleaning tools, referencing PDC Brush's commitment to sustainability.
Generated: DETERMINISTIC_3eda1b43ed5be5dc
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class Material:
    """Class representing a material in the supply chain."""
    
    def __init__(self, name: str, certified: bool):
        self.name = name
        self.certified = certified

    def __str__(self):
        return f"{self.name} (Certified: {self.certified})"


class Supplier:
    """Class representing a supplier of materials."""
    
    def __init__(self, name: str, materials: List[Material]):
        self.name = name
        self.materials = materials

    def supply_material(self) -> Material:
        """Randomly supply a material from the available materials."""
        if not self.materials:
            raise ValueError(f"Supplier {self.name} has no materials to supply.")
        return random.choice(self.materials)


class Product:
    """Class representing a product made from materials."""
    
    def __init__(self, name: str, materials: List[Material]):
        self.name = name
        self.materials = materials

    def is_sustainable(self) -> bool:
        """Check if all materials are FSC-certified."""
        return all(material.certified for material in self.materials)

    def __str__(self):
        return f"Product: {self.name}, Materials: {[str(m) for m in self.materials]}"


class SupplyChain:
    """Class to simulate the supply chain for FSC-certified materials."""
    
    def __init__(self, suppliers: List[Supplier]):
        self.suppliers = suppliers

    def create_product(self, product_name: str) -> Product:
        """Create a product by sourcing materials from suppliers."""
        materials = []
        for supplier in self.suppliers:
            try:
                material = supplier.supply_material()
                materials.append(material)
            except ValueError as e:
                print(e)
        
        product = Product(product_name, materials)
        return product


def main():
    """Main function to simulate the supply chain."""
    # Define materials
    materials = [
        Material("Bamboo Handle", True),
        Material("Recycled Plastic", True),
        Material("Natural Bristles", True),
        Material("Synthetic Bristles", False)
    ]

    # Define suppliers
    suppliers = [
        Supplier("EcoSupplier A", materials),
        Supplier("EcoSupplier B", materials),
        Supplier("EcoSupplier C", materials)
    ]

    # Create a supply chain
    supply_chain = SupplyChain(suppliers)

    # Create a product
    product = supply_chain.create_product("Eco-Friendly Cleaning Brush")

    # Output product details
    print(product)
    print(f"Is the product sustainable? {'Yes' if product.is_sustainable() else 'No'}")


if __name__ == "__main__":
    main()
```
