"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Write Python code to simulate the functionality of industrial brushes used for mechanical cleaning, incorporating customizable dimensions and characteristics as described on the VIRCOMEM website.
Generated: DETERMINISTIC_7e5b144b4d9c92e4
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple

class BrushType(Enum):
    """Enum representing different types of industrial brushes."""
    CYLINDRICAL = "Cylindrical"
    DISC = "Disc"
    END = "End"
    STRIP = "Strip"
    SPECIAL = "Special"

class BristleMaterial(Enum):
    """Enum representing different bristle materials."""
    NYLON = "Nylon"
    POLYPROPYLENE = "Polypropylene"
    STEEL = "Steel"
    BRASS = "Brass"
    CERAMIC = "Ceramic"

@dataclass
class BrushDimensions:
    """Dataclass representing the physical dimensions of a brush."""
    diameter: float  # in mm
    width: float  # in mm
    thickness: Optional[float] = None  # in mm, for strip brushes
    hole_diameter: Optional[float] = None  # in mm, for brushes with mounting holes

@dataclass
class BristleSpecifications:
    """Dataclass representing bristle specifications."""
    material: BristleMaterial
    diameter: float  # in mm
    density: int  # bristles per square cm
    length: float  # in mm

class IndustrialBrush:
    """Class representing an industrial brush with customizable properties."""
    
    def __init__(
        self,
        brush_type: BrushType,
        dimensions: BrushDimensions,
        bristle_specs: BristleSpecifications,
        name: str = "Custom Brush",
        rotation_speed_limit: Optional[float] = None,  # in RPM
        temperature_limit: Optional[float] = None,  # in °C
    ):
        """Initialize an industrial brush with given specifications.
        
        Args:
            brush_type: Type of the brush (Cylindrical, Disc, etc.)
            dimensions: Physical dimensions of the brush
            bristle_specs: Specifications of the bristles
            name: Name/identifier for the brush
            rotation_speed_limit: Maximum safe rotation speed in RPM
            temperature_limit: Maximum operating temperature in °C
        """
        self.brush_type = brush_type
        self.dimensions = dimensions
        self.bristle_specs = bristle_specs
        self.name = name
        self.rotation_speed_limit = rotation_speed_limit
        self.temperature_limit = temperature_limit
        
        # Validate dimensions based on brush type
        self._validate_dimensions()
    
    def _validate_dimensions(self) -> None:
        """Validate brush dimensions based on brush type."""
        if self.brush_type == BrushType.STRIP and self.dimensions.thickness is None:
            raise ValueError("Strip brushes must have a thickness specified.")
        if self.brush_type in [BrushType.CYLINDRICAL, BrushType.DISC] and self.dimensions.hole_diameter is None:
            raise ValueError("Cylindrical and Disc brushes must have a hole diameter specified.")
    
    def calculate_surface_area(self) -> float:
        """Calculate the effective surface area of the brush in square mm."""
        if self.brush_type == BrushType.CYLINDRICAL:
            # Surface area of the side of a cylinder
            return math.pi * self.dimensions.diameter * self.dimensions.width
        elif self.brush_type == BrushType.DISC:
            # Area of the disc (one side)
            return math.pi * (self.dimensions.diameter / 2) ** 2
        elif self.brush_type == BrushType.STRIP:
            # Area of the strip (length × width)
            return self.dimensions.width * (self.dimensions.thickness or 0)
        else:
            raise NotImplementedError(f"Surface area calculation not implemented for {self.brush_type} brushes.")
    
    def calculate_bristle_count(self) -> int:
        """Calculate the approximate number of bristles in the brush."""
        area_cm2 = self.calculate_surface_area() / 100  # Convert mm² to cm²
        return int(area_cm2 * self.bristle_specs.density)
    
    def calculate_tip_speed(self, rpm: float) -> float:
        """Calculate the tip speed of the brush in meters per second.
        
        Args:
            rpm: Rotation speed in revolutions per minute
            
        Returns:
            Tip speed in m/s
        """
        if self.rotation_speed_limit and rpm > self.rotation_speed_limit:
            raise ValueError(f"Rotation speed {rpm} RPM exceeds limit of {self.rotation_speed_limit} RPM")
        
        circumference = math.pi * self.dimensions.diameter / 1000  # in meters
        return circumference * rpm / 60
    
    def get_specifications(self) -> Dict:
        """Return a dictionary with all brush specifications."""
        return {
            "name": self.name,
            "type": self.brush_type.value,
            "dimensions": {
                "diameter_mm": self.dimensions.diameter,
                "width_mm": self.dimensions.width,
                "thickness_mm": self.dimensions.thickness,
                "hole_diameter_mm": self.dimensions.hole_diameter
            },
            "bristles": {
                "material": self.bristle_specs.material.value,
                "diameter_mm": self.bristle_specs.diameter,
                "density_per_cm2": self.bristle_specs.density,
                "length_mm": self.bristle_specs.length,
                "estimated_count": self.calculate_bristle_count()
            },
            "limits": {
                "max_rpm": self.rotation_speed_limit,
                "max_temp_c": self.temperature_limit
            }
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a cylindrical brush
        dimensions = BrushDimensions(
            diameter=150.0,
            width=50.0,
            hole_diameter=25.0
        )
        bristles = BristleSpecifications(
            material=BristleMaterial.STEEL,
            diameter=0.5,
            density=100,
            length=30.0
        )
        
        cylindrical_brush = IndustrialBrush(
            brush_type=BrushType.CYLINDRICAL,
            dimensions=dimensions,
            bristle_specs=bristles,
            name="Steel Cylindrical Brush",
            rotation_speed_limit=3000,
            temperature_limit=150
        )
        
        # Print specifications
        print(cylindrical_brush.get_specifications())
        
        # Calculate tip speed at 2000 RPM
        tip_speed = cylindrical_brush.calculate_tip_speed(2000)
        print(f"Tip speed at 2000 RPM: {tip_speed:.2f} m/s")
        
    except ValueError as e:
        print(f"Error creating brush: {e}")
```
