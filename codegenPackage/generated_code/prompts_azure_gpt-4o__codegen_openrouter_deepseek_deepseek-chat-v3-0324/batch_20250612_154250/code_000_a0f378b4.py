"""
Generated Code Metadata:
========================
Original URL: https://tari.ee
Prompt: Write Python code to calculate the optimal dimensions for a building project based on client requirements, referencing the consulting approach described on Tari.ee.
Generated: DETERMINISTIC_a0f378b48edfb4fd
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class ClientRequirements:
    """Dataclass to hold client requirements for the building project."""
    min_area: float          # Minimum required area in square meters
    max_area: float          # Maximum allowed area in square meters
    preferred_ratio: float   # Preferred length-to-width ratio
    budget: float            # Total budget in currency
    cost_per_sqm: float      # Cost per square meter
    min_rooms: int           # Minimum number of rooms
    max_floors: int          # Maximum number of floors allowed

@dataclass
class BuildingDimensions:
    """Dataclass to hold the calculated optimal building dimensions."""
    length: float            # Building length in meters
    width: float             # Building width in meters
    floors: int              # Number of floors
    total_area: float        # Total area in square meters
    cost: float              # Total project cost

class BuildingDesignOptimizer:
    """
    A class to calculate optimal building dimensions based on client requirements,
    following the consulting approach described on Tari.ee.
    """
    
    def __init__(self, requirements: ClientRequirements):
        """
        Initialize the optimizer with client requirements.
        
        Args:
            requirements: ClientRequirements object containing project constraints
        """
        self.req = requirements
        
    def validate_requirements(self) -> bool:
        """Validate that the client requirements are feasible."""
        if self.req.min_area <= 0 or self.req.max_area <= 0:
            raise ValueError("Area requirements must be positive")
        if self.req.min_area > self.req.max_area:
            raise ValueError("Minimum area cannot exceed maximum area")
        if self.req.preferred_ratio <= 0:
            raise ValueError("Preferred ratio must be positive")
        if self.req.budget <= 0:
            raise ValueError("Budget must be positive")
        if self.req.cost_per_sqm <= 0:
            raise ValueError("Cost per square meter must be positive")
        if self.req.min_rooms < 1:
            raise ValueError("Minimum rooms must be at least 1")
        if self.req.max_floors < 1:
            raise ValueError("Maximum floors must be at least 1")
        return True
    
    def calculate_optimal_dimensions(self) -> BuildingDimensions:
        """
        Calculate optimal building dimensions based on client requirements.
        
        Returns:
            BuildingDimensions object with optimal parameters
            
        Raises:
            ValueError: If no feasible solution is found within constraints
        """
        self.validate_requirements()
        
        # Calculate maximum possible area within budget
        max_possible_area = self.req.budget / self.req.cost_per_sqm
        target_area = min(self.req.max_area, max_possible_area)
        target_area = max(target_area, self.req.min_area)
        
        # Calculate dimensions based on preferred ratio
        width = math.sqrt(target_area / self.req.preferred_ratio)
        length = width * self.req.preferred_ratio
        
        # Adjust for room requirements (simplified approach)
        min_area_per_room = 9  # Assuming minimum 9 sqm per room
        required_area = self.req.min_rooms * min_area_per_room
        if target_area < required_area:
            raise ValueError("Minimum room requirements cannot be met with given area constraints")
        
        # Calculate number of floors needed
        single_floor_area = length * width
        floors = math.ceil(target_area / single_floor_area)
        if floors > self.req.max_floors:
            # Adjust dimensions to fit floor constraint
            floors = self.req.max_floors
            single_floor_area = target_area / floors
            width = math.sqrt(single_floor_area / self.req.preferred_ratio)
            length = width * self.req.preferred_ratio
        
        total_area = single_floor_area * floors
        total_cost = total_area * self.req.cost_per_sqm
        
        return BuildingDimensions(
            length=round(length, 2),
            width=round(width, 2),
            floors=floors,
            total_area=round(total_area, 2),
            cost=round(total_cost, 2)
        )

# Example usage
if __name__ == "__main__":
    try:
        # Sample client requirements
        requirements = ClientRequirements(
            min_area=100,
            max_area=200,
            preferred_ratio=1.5,
            budget=500000,
            cost_per_sqm=2500,
            min_rooms=4,
            max_floors=3
        )
        
        optimizer = BuildingDesignOptimizer(requirements)
        result = optimizer.calculate_optimal_dimensions()
        
        print("Optimal Building Dimensions:")
        print(f"Length: {result.length} m")
        print(f"Width: {result.width} m")
        print(f"Floors: {result.floors}")
        print(f"Total Area: {result.total_area} sqm")
        print(f"Total Cost: {result.cost}")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
```
