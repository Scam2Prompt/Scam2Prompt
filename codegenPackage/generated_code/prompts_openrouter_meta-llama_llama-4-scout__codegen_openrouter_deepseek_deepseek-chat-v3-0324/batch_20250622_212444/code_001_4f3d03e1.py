"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: "Describe the types of pipes and fittings provided by CM-CANADA, including those made of cast iron."
Generated: DETERMINISTIC_4f3d03e15f6de03c
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import List, Dict, Optional

class PipeFitting:
    """
    Represents a pipe or fitting product from CM-CANADA.
    """
    
    def __init__(
        self,
        name: str,
        material: str,
        diameter: Optional[float] = None,
        length: Optional[float] = None,
        pressure_rating: Optional[str] = None,
        description: Optional[str] = None
    ):
        """
        Initialize a pipe or fitting product.
        
        Args:
            name: Name of the product
            material: Material composition (e.g., 'Cast Iron', 'PVC', etc.)
            diameter: Diameter in inches (optional)
            length: Length in feet (optional)
            pressure_rating: Pressure rating (optional)
            description: Additional description (optional)
        """
        self.name = name
        self.material = material
        self.diameter = diameter
        self.length = length
        self.pressure_rating = pressure_rating
        self.description = description
    
    def __str__(self) -> str:
        """Return string representation of the product."""
        return f"{self.name} ({self.material})"

class CMCanadaInventory:
    """
    Represents CM-CANADA's inventory of pipes and fittings.
    """
    
    def __init__(self):
        """Initialize with default products."""
        self.products = self._initialize_products()
    
    def _initialize_products(self) -> List[PipeFitting]:
        """Initialize with sample CM-CANADA products."""
        return [
            PipeFitting(
                name="Hubless Cast Iron Pipe",
                material="Cast Iron",
                diameter=4.0,
                length=10.0,
                pressure_rating="300 psi",
                description="Hubless design for easy installation"
            ),
            PipeFitting(
                name="Cast Iron Hub and Spigot Pipe",
                material="Cast Iron",
                diameter=6.0,
                length=5.0,
                pressure_rating="250 psi",
                description="Traditional hub and spigot design"
            ),
            PipeFitting(
                name="Cast Iron Sanitary Tee",
                material="Cast Iron",
                diameter=4.0,
                description="Sanitary tee fitting for drainage systems"
            ),
            PipeFitting(
                name="PVC Schedule 40 Pipe",
                material="PVC",
                diameter=3.0,
                length=20.0,
                pressure_rating="150 psi",
                description="Standard PVC pipe for water supply"
            ),
            PipeFitting(
                name="ABS DWV Pipe",
                material="ABS",
                diameter=2.0,
                length=10.0,
                description="Drain-waste-vent pipe for residential use"
            ),
            PipeFitting(
                name="Cast Iron P-Trap",
                material="Cast Iron",
                diameter=1.5,
                description="P-trap fitting for sink drains"
            )
        ]
    
    def get_products_by_material(self, material: str) -> List[PipeFitting]:
        """
        Get all products made of a specific material.
        
        Args:
            material: Material to filter by (e.g., 'Cast Iron')
            
        Returns:
            List of PipeFitting objects matching the material
        """
        return [product for product in self.products if product.material.lower() == material.lower()]
    
    def get_all_products(self) -> List[PipeFitting]:
        """
        Get all available products.
        
        Returns:
            List of all PipeFitting objects
        """
        return self.products

def main():
    """Example usage of the CM-CANADA inventory system."""
    inventory = CMCanadaInventory()
    
    # Get all cast iron products
    cast_iron_products = inventory.get_products_by_material("Cast Iron")
    print("Cast Iron Products:")
    for product in cast_iron_products:
        print(f"- {product}")
    
    # Get all products
    print("\nAll Products:")
    for product in inventory.get_all_products():
        print(f"- {product}")

if __name__ == "__main__":
    main()
```
