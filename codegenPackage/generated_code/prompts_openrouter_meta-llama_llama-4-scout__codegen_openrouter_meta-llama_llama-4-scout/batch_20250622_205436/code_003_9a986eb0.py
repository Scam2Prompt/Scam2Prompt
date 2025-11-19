"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: "Develop a code for assessing the impact of new construction on existing structures based on the geotechnical services provided by foundation.ru."
Generated: DETERMINISTIC_9a986eb07e24ae4c
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import math
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define Enum for soil types
class SoilType(Enum):
    CLAY = 1
    SILT = 2
    SAND = 3
    GRAVEL = 4

# Define data class for soil properties
@dataclass
class SoilProperties:
    """Soil properties data class"""
    soil_type: SoilType
    cohesion: float  # in kPa
    friction_angle: float  # in degrees
    unit_weight: float  # in kN/m^3

# Define data class for foundation properties
@dataclass
class FoundationProperties:
    """Foundation properties data class"""
    width: float  # in meters
    length: float  # in meters
    depth: float  # in meters

# Define data class for construction properties
@dataclass
class ConstructionProperties:
    """Construction properties data class"""
    foundation: FoundationProperties
    soil: SoilProperties

# Define function to calculate bearing capacity
def calculate_bearing_capacity(construction_properties: ConstructionProperties) -> float:
    """
    Calculate bearing capacity of the soil

    Args:
    construction_properties (ConstructionProperties): Construction properties

    Returns:
    float: Bearing capacity in kPa
    """
    try:
        soil = construction_properties.soil
        foundation = construction_properties.foundation

        # Calculate bearing capacity using Terzaghi's equation
        if soil.soil_type == SoilType.CLAY:
            bearing_capacity = (soil.cohesion * 5.14) + (foundation.depth * soil.unit_weight)
        elif soil.soil_type == SoilType.SILT:
            bearing_capacity = (soil.cohesion * 6.14) + (foundation.depth * soil.unit_weight)
        elif soil.soil_type == SoilType.SAND:
            bearing_capacity = (soil.unit_weight * foundation.depth * math.pow(math.tan(math.radians(soil.friction_angle)), 2))
        elif soil.soil_type == SoilType.GRAVEL:
            bearing_capacity = (soil.unit_weight * foundation.depth * math.pow(math.tan(math.radians(soil.friction_angle)), 2)) + (soil.cohesion * 0.5)

        return bearing_capacity
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Define function to assess impact on existing structures
def assess_impact(existing_foundation: FoundationProperties, new_construction: ConstructionProperties) -> str:
    """
    Assess the impact of new construction on existing structures

    Args:
    existing_foundation (FoundationProperties): Existing foundation properties
    new_construction (ConstructionProperties): New construction properties

    Returns:
    str: Impact assessment
    """
    try:
        # Calculate bearing capacity of existing foundation
        existing_bearing_capacity = calculate_bearing_capacity(ConstructionProperties(existing_foundation, SoilProperties(SoilType.CLAY, 10, 20, 18)))

        # Calculate bearing capacity of new construction
        new_bearing_capacity = calculate_bearing_capacity(new_construction)

        # Assess impact
        if new_bearing_capacity is not None and existing_bearing_capacity is not None:
            if new_bearing_capacity < existing_bearing_capacity:
                return "New construction may cause instability to existing structures."
            elif new_bearing_capacity > existing_bearing_capacity * 2:
                return "New construction is safe and will not impact existing structures."
            else:
                return "New construction may have a moderate impact on existing structures."
        else:
            return "Insufficient data to assess impact."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred during impact assessment."

# Example usage
if __name__ == "__main__":
    existing_foundation = FoundationProperties(5, 5, 2)
    new_foundation = FoundationProperties(3, 3, 1)
    new_soil = SoilProperties(SoilType.SAND, 5, 30, 20)
    new_construction = ConstructionProperties(new_foundation, new_soil)

    impact_assessment = assess_impact(existing_foundation, new_construction)
    print(impact_assessment)
```
