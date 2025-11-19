"""
Generated Code Metadata:
========================
Original URL: https://cartoansurperu.com
Prompt: Generate a Python script that utilizes the specifications of corrugated cardboard from Cartonerías Andinas del Sur for packaging solutions.
Generated: DETERMINISTIC_6817b4a5c7c52be3
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Corrugated Cardboard Packaging Solutions for Cartonerías Andinas del Sur

This script provides utility functions to calculate packaging specifications
based on corrugated cardboard types offered by Cartonerías Andinas del Sur.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Tuple

class CardboardType(Enum):
    """Enum representing different types of corrugated cardboard."""
    SINGLE_FACE = auto()
    SINGLE_WALL = auto()
    DOUBLE_WALL = auto()
    TRIPLE_WALL = auto()

class FluteType(Enum):
    """Enum representing different flute profiles."""
    A_FLUTE = auto()  # 5mm
    B_FLUTE = auto()  # 3mm
    C_FLUTE = auto()  # 4mm
    E_FLUTE = auto()  # 1.5mm
    F_FLUTE = auto()  # 0.6mm
    BC_FLUTE = auto()  # 6mm
    EB_FLUTE = auto()  # 4.5mm

@dataclass
class CardboardSpec:
    """Dataclass holding specifications for a cardboard type."""
    type: CardboardType
    flute: FluteType
    thickness_mm: float
    burst_strength_kpa: float
    edge_crush_test_nm: float
    weight_gsm: float

class PackagingCalculator:
    """Calculator for corrugated cardboard packaging solutions."""
    
    def __init__(self):
        self._specs = self._load_default_specs()
    
    def _load_default_specs(self) -> dict:
        """Load default specifications from Cartonerías Andinas del Sur."""
        return {
            (CardboardType.SINGLE_FACE, FluteType.A_FLUTE): CardboardSpec(
                type=CardboardType.SINGLE_FACE,
                flute=FluteType.A_FLUTE,
                thickness_mm=5.0,
                burst_strength_kpa=200,
                edge_crush_test_nm=4.5,
                weight_gsm=150
            ),
            (CardboardType.SINGLE_WALL, FluteType.B_FLUTE): CardboardSpec(
                type=CardboardType.SINGLE_WALL,
                flute=FluteType.B_FLUTE,
                thickness_mm=3.0,
                burst_strength_kpa=300,
                edge_crush_test_nm=6.0,
                weight_gsm=180
            ),
            (CardboardType.DOUBLE_WALL, FluteType.BC_FLUTE): CardboardSpec(
                type=CardboardType.DOUBLE_WALL,
                flute=FluteType.BC_FLUTE,
                thickness_mm=6.0,
                burst_strength_kpa=500,
                edge_crush_test_nm=12.0,
                weight_gsm=350
            ),
            (CardboardType.TRIPLE_WALL, FluteType.BC_FLUTE): CardboardSpec(
                type=CardboardType.TRIPLE_WALL,
                flute=FluteType.BC_FLUTE,
                thickness_mm=9.0,
                burst_strength_kpa=800,
                edge_crush_test_nm=18.0,
                weight_gsm=500
            )
        }
    
    def get_spec(self, cardboard_type: CardboardType, flute_type: FluteType) -> Optional[CardboardSpec]:
        """Get specifications for a given cardboard and flute type."""
        return self._specs.get((cardboard_type, flute_type))
    
    def calculate_box_weight(self, spec: CardboardSpec, dimensions_mm: Tuple[float, float, float]) -> float:
        """
        Calculate the approximate weight of a box based on its dimensions and cardboard spec.
        
        Args:
            spec: CardboardSpec object
            dimensions_mm: Tuple of (length, width, height) in millimeters
            
        Returns:
            Weight in grams
        """
        try:
            length, width, height = dimensions_mm
            if any(dim <= 0 for dim in dimensions_mm):
                raise ValueError("All dimensions must be positive")
            
            # Convert dimensions to meters
            length_m = length / 1000
            width_m = width / 1000
            height_m = height / 1000
            
            # Calculate surface area (2*(lw + lh + wh))
            surface_area = 2 * (length_m * width_m + length_m * height_m + width_m * height_m)
            
            # Weight = surface area * weight per square meter
            return surface_area * spec.weight_gsm
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid dimensions: {e}") from e
    
    def calculate_max_load(self, spec: CardboardSpec, box_base_area_m2: float) -> float:
        """
        Calculate the maximum recommended load for a box based on its base area and cardboard spec.
        
        Args:
            spec: CardboardSpec object
            box_base_area_m2: Base area of the box in square meters
            
        Returns:
            Maximum load in kilograms
        """
        try:
            if box_base_area_m2 <= 0:
                raise ValueError("Base area must be positive")
            
            # Max load = (ECT * 5.87) / (box perimeter in inches)
            # Simplified version using base area
            return (spec.edge_crush_test_nm * 5.87) * box_base_area_m2 * 10
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid base area: {e}") from e

# Example usage
if __name__ == "__main__":
    calculator = PackagingCalculator()
    
    # Get specifications for a double wall BC flute cardboard
    spec = calculator.get_spec(CardboardType.DOUBLE_WALL, FluteType.BC_FLUTE)
    if spec:
        print(f"Specifications for {spec.type.name} with {spec.flute.name}:")
        print(f"Thickness: {spec.thickness_mm} mm")
        print(f"Burst Strength: {spec.burst_strength_kpa} kPa")
        print(f"ECT: {spec.edge_crush_test_nm} N/m")
        print(f"Weight: {spec.weight_gsm} g/m²")
        
        # Calculate box weight
        dimensions = (300, 200, 150)  # 300mm x 200mm x 150mm
        weight = calculator.calculate_box_weight(spec, dimensions)
        print(f"\nBox weight: {weight:.2f} grams")
        
        # Calculate max load
        base_area = (300/1000) * (200/1000)  # 0.06 m²
        max_load = calculator.calculate_max_load(spec, base_area)
        print(f"Max recommended load: {max_load:.2f} kg")
```
