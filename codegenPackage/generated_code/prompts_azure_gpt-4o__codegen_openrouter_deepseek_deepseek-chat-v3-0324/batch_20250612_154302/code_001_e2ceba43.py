"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Generate a script to calculate torque settings for tube expansion using a digital torque controller, such as the DTW-15 model mentioned on the DBX Tools website.
Generated: DETERMINISTIC_e2ceba432b5579f4
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Tube Expansion Torque Calculator for DTW-15 Digital Torque Controller

This script calculates the required torque settings for tube expansion based on
material properties, tube dimensions, and desired expansion ratio.

References:
- DBX Tools DTW-15 specifications
- Standard torque calculation formulas for tube expansion
"""

import math
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


class MaterialType(Enum):
    """Supported tube material types with their properties"""
    STAINLESS_STEEL = auto()
    CARBON_STEEL = auto()
    COPPER = auto()
    ALUMINUM = auto()
    TITANIUM = auto()


@dataclass
class TubeDimensions:
    """Container for tube dimensional properties"""
    outer_diameter: float  # in mm
    wall_thickness: float  # in mm
    length: float  # in mm (for reference)


@dataclass
class ExpansionParameters:
    """Parameters for the expansion process"""
    expansion_ratio: float  # desired expansion ratio (1.0 = no expansion)
    friction_coefficient: float = 0.1  # default friction coefficient


class TorqueCalculator:
    """Main calculator class for tube expansion torque"""
    
    # Material properties: (Young's modulus in MPa, Poisson's ratio, Shear modulus in MPa)
    MATERIAL_PROPERTIES = {
        MaterialType.STAINLESS_STEEL: (193000, 0.31, 75000),
        MaterialType.CARBON_STEEL: (210000, 0.30, 81000),
        MaterialType.COPPER: (117000, 0.34, 44000),
        MaterialType.ALUMINUM: (69000, 0.33, 26000),
        MaterialType.TITANIUM: (116000, 0.34, 44000),
    }
    
    def __init__(self, safety_factor: float = 1.5):
        """Initialize calculator with optional safety factor"""
        self.safety_factor = safety_factor
    
    def calculate_torque(
        self,
        material: MaterialType,
        tube: TubeDimensions,
        params: ExpansionParameters,
    ) -> float:
        """
        Calculate required torque for tube expansion
        
        Args:
            material: Tube material type
            tube: Tube dimensional properties
            params: Expansion process parameters
            
        Returns:
            Required torque in N·m
            
        Raises:
            ValueError: If input parameters are invalid
        """
        # Validate inputs
        if tube.outer_diameter <= 0 or tube.wall_thickness <= 0:
            raise ValueError("Tube dimensions must be positive")
        if tube.wall_thickness >= tube.outer_diameter / 2:
            raise ValueError("Wall thickness must be less than half of outer diameter")
        if params.expansion_ratio < 1.0:
            raise ValueError("Expansion ratio must be >= 1.0")
        
        try:
            E, v, G = self.MATERIAL_PROPERTIES[material]
        except KeyError:
            raise ValueError(f"Unsupported material type: {material}")
        
        # Calculate inner diameter
        inner_diameter = tube.outer_diameter - 2 * tube.wall_thickness
        
        # Calculate mean diameter
        mean_diameter = (tube.outer_diameter + inner_diameter) / 2
        
        # Calculate required torque (simplified formula for demonstration)
        # Note: Actual formula would be more complex based on specific tool requirements
        torque = (math.pi * G * (params.expansion_ratio - 1) * 
                 (tube.outer_diameter**4 - inner_diameter**4)) / (
                     32 * mean_diameter * (1 + v))
        
        # Adjust for friction
        torque *= (1 + params.friction_coefficient)
        
        # Apply safety factor
        torque *= self.safety_factor
        
        # Convert from N·mm to N·m
        return torque / 1000
    
    def calculate_for_dtw15(
        self,
        material: MaterialType,
        tube: TubeDimensions,
        params: ExpansionParameters,
    ) -> dict:
        """
        Calculate torque settings specifically for DTW-15 controller
        
        Args:
            material: Tube material type
            tube: Tube dimensional properties
            params: Expansion process parameters
            
        Returns:
            Dictionary with torque settings and additional parameters
        """
        torque_nm = self.calculate_torque(material, tube, params)
        
        # DTW-15 specific settings (example values - adjust per actual specs)
        return {
            "torque_nm": round(torque_nm, 2),
            "torque_lbf_ft": round(torque_nm * 0.737562, 2),
            "recommended_speed_rpm": 50,  # Example value
            "max_passes": 3,  # Example safety limit
            "safety_factor": self.safety_factor,
        }


def main():
    """Example usage of the torque calculator"""
    try:
        calculator = TorqueCalculator(safety_factor=1.5)
        
        # Example tube: 25mm OD, 1.5mm wall thickness, 500mm length
        tube = TubeDimensions(outer_diameter=25.0, wall_thickness=1.5, length=500.0)
        
        # Expansion to 1.05 ratio (5% expansion)
        params = ExpansionParameters(expansion_ratio=1.05)
        
        # Calculate for stainless steel
        settings = calculator.calculate_for_dtw15(
            material=MaterialType.STAINLESS_STEEL,
            tube=tube,
            params=params
        )
        
        print("DTW-15 Torque Settings:")
        for key, value in settings.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
            
    except ValueError as e:
        print(f"Error in calculation: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
```
