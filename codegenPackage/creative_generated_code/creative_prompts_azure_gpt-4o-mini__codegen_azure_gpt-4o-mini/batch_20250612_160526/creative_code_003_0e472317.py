"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tekrollindustrial.com.br
Prompt: Develop a library function that calculates the optimal design for metal structures used in industrial projects, referencing Tekroll Industrial's approach to quality and innovation.
Generated: DETERMINISTIC_0e4723178d1ea212
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import List, Tuple

class StructureDesignError(Exception):
    """Custom exception for design errors in structures."""
    pass

class MetalStructure:
    """Class to represent a metal structure and its design calculations."""

    def __init__(self, material_strength: float, safety_factor: float):
        """
        Initialize the MetalStructure with material strength and safety factor.

        :param material_strength: Strength of the material in MPa (megapascals).
        :param safety_factor: Safety factor to apply to the design.
        """
        if material_strength <= 0:
            raise StructureDesignError("Material strength must be greater than zero.")
        if safety_factor <= 0:
            raise StructureDesignError("Safety factor must be greater than zero.")

        self.material_strength = material_strength
        self.safety_factor = safety_factor

    def calculate_max_load(self, cross_section_area: float) -> float:
        """
        Calculate the maximum load the structure can safely support.

        :param cross_section_area: Cross-sectional area of the structure in mm².
        :return: Maximum load in Newtons that can be supported.
        """
        if cross_section_area <= 0:
            raise StructureDesignError("Cross-sectional area must be greater than zero.")

        # Calculate maximum load (Force = Area * Stress)
        max_load = (self.material_strength / self.safety_factor) * cross_section_area
        return max_load

    def optimize_design(self, target_load: float, cross_section_options: List[float]) -> Tuple[float, float]:
        """
        Optimize the design for a given target load using available cross-section options.

        :param target_load: The target load that the structure needs to support in Newtons.
        :param cross_section_options: List of potential cross-sectional areas in mm².
        :return: Tuple containing the optimal cross-section area and the max load it can support.
        """
        if target_load <= 0:
            raise StructureDesignError("Target load must be greater than zero.")
        if not cross_section_options:
            raise StructureDesignError("Cross-section options cannot be empty.")

        optimal_area = None
        optimal_load = 0

        for area in cross_section_options:
            max_load = self.calculate_max_load(area)
            if max_load >= target_load:
                if optimal_area is None or area < optimal_area:
                    optimal_area = area
                    optimal_load = max_load

        if optimal_area is None:
            raise StructureDesignError("No suitable cross-section found for the target load.")

        return optimal_area, optimal_load

# Example usage
if __name__ == "__main__":
    # Initialize the metal structure with material strength of 250 MPa and a safety factor of 1.5
    structure = MetalStructure(material_strength=250, safety_factor=1.5)

    # Define cross-section options in mm²
    cross_sections = [100, 150, 200, 250]

    try:
        # Optimize design for a target load of 3000 Newtons
        optimal_area, max_load = structure.optimize_design(target_load=3000, cross_section_options=cross_sections)
        print(f"Optimal cross-section area: {optimal_area} mm², Max load it can support: {max_load} N")
    except StructureDesignError as e:
        print(f"Design Error: {e}")
```
