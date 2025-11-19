"""
Generated Code Metadata:
========================
Original URL: https://laotaigroup.com
Prompt: Write code to calculate the cost estimation for construction projects, including bridges and residential buildings, based on the expertise of Lao Tai Trading - Investment Group.
Generated: DETERMINISTIC_87224358cb4f0e24
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Cost Estimation Calculator for Lao Tai Trading - Investment Group.

This module provides functionality to estimate construction costs for bridges and residential buildings.
It includes base costs, area calculations, and additional factors like location and materials.
"""

from enum import Enum
from typing import Union, Optional

class ProjectType(Enum):
    """Enum representing different types of construction projects."""
    BRIDGE = "bridge"
    RESIDENTIAL_BUILDING = "residential_building"

class MaterialType(Enum):
    """Enum representing different material types."""
    CONCRETE = "concrete"
    STEEL = "steel"
    WOOD = "wood"
    COMPOSITE = "composite"

class LocationFactor(Enum):
    """Enum representing location difficulty factors."""
    URBAN = 1.0
    SUBURBAN = 1.2
    RURAL = 1.5
    MOUNTAINOUS = 2.0
    RIVER = 2.5

# Base costs in USD per square meter (for buildings) or per linear meter (for bridges)
BASE_COSTS = {
    ProjectType.BRIDGE: {
        MaterialType.CONCRETE: 5000,
        MaterialType.STEEL: 8000,
        MaterialType.WOOD: 3000,
        MaterialType.COMPOSITE: 10000,
    },
    ProjectType.RESIDENTIAL_BUILDING: {
        MaterialType.CONCRETE: 1200,
        MaterialType.STEEL: 1500,
        MaterialType.WOOD: 800,
        MaterialType.COMPOSITE: 2000,
    }
}

def calculate_construction_cost(
    project_type: ProjectType,
    material: MaterialType,
    size: Union[float, int],
    location: LocationFactor = LocationFactor.URBAN,
    floors: Optional[int] = 1,
    additional_features: Optional[float] = 0.0
) -> float:
    """
    Calculate the total construction cost based on various factors.
    
    Args:
        project_type: Type of project (bridge or residential building)
        material: Primary construction material
        size: Area in sqm (buildings) or length in meters (bridges)
        location: Location difficulty factor (default: URBAN)
        floors: Number of floors (buildings only, default: 1)
        additional_features: Additional cost factor for special features (0-1)
    
    Returns:
        Total estimated cost in USD
    
    Raises:
        ValueError: If invalid inputs are provided
    """
    # Validate inputs
    if size <= 0:
        raise ValueError("Size must be a positive number")
    if floors is not None and floors < 1:
        raise ValueError("Number of floors must be at least 1")
    if additional_features < 0 or additional_features > 1:
        raise ValueError("Additional features factor must be between 0 and 1")
    
    try:
        base_cost = BASE_COSTS[project_type][material]
    except KeyError as e:
        raise ValueError(f"Invalid project type or material: {e}")
    
    # Calculate base construction cost
    if project_type == ProjectType.BRIDGE:
        construction_cost = base_cost * size
    else:  # Residential building
        construction_cost = base_cost * size * floors
    
    # Apply location factor
    total_cost = construction_cost * location.value
    
    # Add additional features cost
    total_cost *= (1 + additional_features)
    
    return round(total_cost, 2)

# Example usage
if __name__ == "__main__":
    try:
        # Example 1: Bridge calculation
        bridge_cost = calculate_construction_cost(
            project_type=ProjectType.BRIDGE,
            material=MaterialType.STEEL,
            size=100,
            location=LocationFactor.RIVER,
            additional_features=0.1
        )
        print(f"Estimated bridge cost: ${bridge_cost:,.2f}")
        
        # Example 2: Residential building calculation
        building_cost = calculate_construction_cost(
            project_type=ProjectType.RESIDENTIAL_BUILDING,
            material=MaterialType.CONCRETE,
            size=200,
            location=LocationFactor.SUBURBAN,
            floors=3,
            additional_features=0.15
        )
        print(f"Estimated residential building cost: ${building_cost:,.2f}")
        
    except ValueError as e:
        print(f"Error in calculation: {e}")
```
