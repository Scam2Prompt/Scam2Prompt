"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Write code to generate a catalog of industrial brushes with customizable features, including EU-standardized dimensions and client-specific models, as detailed on the VIRCOMEM website.
Generated: DETERMINISTIC_b8a66c2a9b29be2e
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class BrushType(str, Enum):
    """Type of industrial brush"""
    STANDARD = "standard"
    CUSTOM = "custom"

@dataclass
class BrushDimensions:
    """EU-standardized dimensions for industrial brushes"""
    length: float
    width: float
    height: float
    diameter: Optional[float] = None

@dataclass
class IndustrialBrush:
    """Industrial brush with customizable features"""
    brush_type: BrushType
    dimensions: BrushDimensions
    material: str
    client_model: Optional[str] = None

    def __post_init__(self):
        """Validate brush dimensions"""
        if self.brush_type == BrushType.STANDARD:
            if self.dimensions.length < 100 or self.dimensions.length > 2000:
                raise ValueError("Standard brush length must be between 100 and 2000 mm")
            if self.dimensions.width < 10 or self.dimensions.width > 500:
                raise ValueError("Standard brush width must be between 10 and 500 mm")
            if self.dimensions.height < 10 or self.dimensions.height > 500:
                raise ValueError("Standard brush height must be between 10 and 500 mm")
        elif self.brush_type == BrushType.CUSTOM:
            if not self.client_model:
                raise ValueError("Custom brush requires a client model")

class BrushCatalog:
    """Catalog of industrial brushes"""
    def __init__(self):
        self.brushes = []

    def add_brush(self, brush: IndustrialBrush):
        """Add an industrial brush to the catalog"""
        self.brushes.append(brush)

    def get_brushes(self):
        """Get all industrial brushes in the catalog"""
        return self.brushes

def main():
    # Create a brush catalog
    catalog = BrushCatalog()

    # Create standard brushes
    standard_brush1 = IndustrialBrush(
        BrushType.STANDARD,
        BrushDimensions(1500, 200, 300),
        "Polypropylene"
    )
    standard_brush2 = IndustrialBrush(
        BrushType.STANDARD,
        BrushDimensions(1000, 100, 200),
        "Nylon"
    )

    # Create custom brushes
    custom_brush1 = IndustrialBrush(
        BrushType.CUSTOM,
        BrushDimensions(1200, 250, 350),
        "Polyester",
        client_model="VIRCOMEM-001"
    )
    custom_brush2 = IndustrialBrush(
        BrushType.CUSTOM,
        BrushDimensions(1800, 300, 400),
        "Acrylic",
        client_model="VIRCOMEM-002"
    )

    # Add brushes to the catalog
    catalog.add_brush(standard_brush1)
    catalog.add_brush(standard_brush2)
    catalog.add_brush(custom_brush1)
    catalog.add_brush(custom_brush2)

    # Print brushes in the catalog
    for i, brush in enumerate(catalog.get_brushes()):
        print(f"Brush {i+1}:")
        print(f"Type: {brush.brush_type.value}")
        print(f"Dimensions: {brush.dimensions.length} x {brush.dimensions.width} x {brush.dimensions.height} mm")
        print(f"Material: {brush.material}")
        if brush.client_model:
            print(f"Client Model: {brush.client_model}")
        print()

if __name__ == "__main__":
    main()
```
