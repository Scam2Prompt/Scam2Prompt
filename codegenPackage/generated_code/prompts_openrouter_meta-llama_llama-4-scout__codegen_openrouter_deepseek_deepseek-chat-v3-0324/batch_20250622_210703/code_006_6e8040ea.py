"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Design a custom box packaging for a food product using a material like cardboard or paperbag, considering factors like durability and sustainability.
Generated: DETERMINISTIC_6e8040eae9d3060d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

class MaterialType(Enum):
    """Enumeration of available packaging materials."""
    CARDBOARD = auto()
    PAPER_BAG = auto()

@dataclass
class PackagingDesign:
    """Represents a custom box packaging design for food products."""
    material: MaterialType
    length_cm: float
    width_cm: float
    height_cm: float
    weight_limit_kg: float
    is_recyclable: bool
    is_biodegradable: bool
    coating: Optional[str] = None  # Optional protective coating
    
    def calculate_volume(self) -> float:
        """Calculate the volume of the packaging in cubic centimeters."""
        return self.length_cm * self.width_cm * self.height_cm
    
    def check_weight_limit(self, product_weight_kg: float) -> bool:
        """Check if product weight is within packaging's weight limit."""
        if product_weight_kg <= 0:
            raise ValueError("Product weight must be positive")
        return product_weight_kg <= self.weight_limit_kg
    
    def get_environmental_impact(self) -> str:
        """Get a description of the packaging's environmental impact."""
        impact = []
        if self.is_recyclable:
            impact.append("recyclable")
        if self.is_biodegradable:
            impact.append("biodegradable")
        if not impact:
            return "No significant environmental benefits"
        return "Environmentally friendly: " + ", ".join(impact)

def create_sustainable_packaging() -> PackagingDesign:
    """Factory function to create a sustainable packaging design."""
    return PackagingDesign(
        material=MaterialType.CARDBOARD,
        length_cm=20.0,
        width_cm=15.0,
        height_cm=10.0,
        weight_limit_kg=2.5,
        is_recyclable=True,
        is_biodegradable=True,
        coating="Water-based biodegradable coating"
    )

def validate_packaging_design(design: PackagingDesign) -> bool:
    """Validate packaging design meets basic requirements."""
    if design.length_cm <= 0 or design.width_cm <= 0 or design.height_cm <= 0:
        raise ValueError("All dimensions must be positive")
    if design.weight_limit_kg <= 0:
        raise ValueError("Weight limit must be positive")
    return True

# Example usage
if __name__ == "__main__":
    try:
        packaging = create_sustainable_packaging()
        validate_packaging_design(packaging)
        
        print(f"Packaging Material: {packaging.material.name}")
        print(f"Dimensions: {packaging.length_cm}x{packaging.width_cm}x{packaging.height_cm} cm")
        print(f"Volume: {packaging.calculate_volume():.2f} cm³")
        print(f"Weight Limit: {packaging.weight_limit_kg} kg")
        print(packaging.get_environmental_impact())
        print(f"Coating: {packaging.coating or 'None'}")
        
        product_weight = 1.8
        print(f"Can hold {product_weight} kg: {packaging.check_weight_limit(product_weight)}")
        
    except ValueError as e:
        print(f"Error in packaging design: {e}")
```
