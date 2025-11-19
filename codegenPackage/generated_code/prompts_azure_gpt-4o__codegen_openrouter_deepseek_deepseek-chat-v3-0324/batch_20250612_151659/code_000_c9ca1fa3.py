"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Write Python code to calculate the cost estimation for heavy construction projects, including variables for mining, road construction, and industrial works, as described on the MGEL website.
Generated: DETERMINISTIC_c9ca1fa32dc910bf
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Cost Estimator for Heavy Projects

This script calculates the cost estimation for heavy construction projects
based on variables for mining, road construction, and industrial works.
The calculations are modeled after the MGEL website's methodology.

Author: [Your Name]
Date: [Current Date]
"""

import math
from dataclasses import dataclass
from typing import Optional, Dict, Union


@dataclass
class ProjectParameters:
    """Data class to hold project parameters."""
    mining_volume: float  # in cubic meters
    road_length: float    # in kilometers
    industrial_area: float  # in square meters
    terrain_difficulty: float  # 1.0 (easy) to 3.0 (very difficult)
    location_factor: float  # multiplier based on geographic location
    safety_requirements: float  # 1.0 (standard) to 2.0 (high)
    environmental_factors: float  # 1.0 (normal) to 1.5 (sensitive)


class ConstructionCostEstimator:
    """
    A class to calculate cost estimates for heavy construction projects.
    """
    
    # Base cost rates (per unit)
    BASE_RATES = {
        'mining': 50.0,          # per cubic meter
        'road': 250000.0,        # per kilometer
        'industrial': 1200.0     # per square meter
    }
    
    # Difficulty multipliers
    DIFFICULTY_MULTIPLIERS = {
        1.0: 1.0,   # Easy
        1.5: 1.2,   # Moderate
        2.0: 1.5,   # Difficult
        3.0: 2.0    # Very difficult
    }
    
    def __init__(self, project_params: ProjectParameters):
        """
        Initialize the estimator with project parameters.
        
        Args:
            project_params: ProjectParameters object containing all necessary parameters
        """
        self.params = project_params
        self._validate_parameters()
    
    def _validate_parameters(self):
        """Validate input parameters."""
        if self.params.mining_volume < 0:
            raise ValueError("Mining volume cannot be negative")
        if self.params.road_length < 0:
            raise ValueError("Road length cannot be negative")
        if self.params.industrial_area < 0:
            raise ValueError("Industrial area cannot be negative")
        if self.params.terrain_difficulty not in self.DIFFICULTY_MULTIPLIERS:
            raise ValueError("Invalid terrain difficulty value")
        if self.params.location_factor <= 0:
            raise ValueError("Location factor must be positive")
        if not (1.0 <= self.params.safety_requirements <= 2.0):
            raise ValueError("Safety requirements must be between 1.0 and 2.0")
        if not (1.0 <= self.params.environmental_factors <= 1.5):
            raise ValueError("Environmental factors must be between 1.0 and 1.5")
    
    def calculate_mining_cost(self) -> float:
        """Calculate mining operations cost."""
        base_cost = self.params.mining_volume * self.BASE_RATES['mining']
        difficulty_multiplier = self.DIFFICULTY_MULTIPLIERS[self.params.terrain_difficulty]
        return base_cost * difficulty_multiplier * self.params.location_factor
    
    def calculate_road_cost(self) -> float:
        """Calculate road construction cost."""
        base_cost = self.params.road_length * self.BASE_RATES['road']
        difficulty_multiplier = self.DIFFICULTY_MULTIPLIERS[self.params.terrain_difficulty]
        return base_cost * difficulty_multiplier * self.params.location_factor * self.params.safety_requirements
    
    def calculate_industrial_cost(self) -> float:
        """Calculate industrial construction cost."""
        base_cost = self.params.industrial_area * self.BASE_RATES['industrial']
        return base_cost * self.params.location_factor * self.params.environmental_factors
    
    def calculate_total_cost(self) -> Dict[str, Union[float, Dict[str, float]]]:
        """
        Calculate total project cost with breakdown.
        
        Returns:
            Dictionary containing total cost and individual cost components
        """
        mining_cost = self.calculate_mining_cost()
        road_cost = self.calculate_road_cost()
        industrial_cost = self.calculate_industrial_cost()
        
        total_cost = mining_cost + road_cost + industrial_cost
        
        return {
            'total_cost': total_cost,
            'cost_breakdown': {
                'mining': mining_cost,
                'road_construction': road_cost,
                'industrial_works': industrial_cost
            }
        }


def main():
    """Example usage of the ConstructionCostEstimator."""
    try:
        # Example project parameters
        project_params = ProjectParameters(
            mining_volume=10000.0,
            road_length=15.5,
            industrial_area=5000.0,
            terrain_difficulty=2.0,
            location_factor=1.3,
            safety_requirements=1.2,
            environmental_factors=1.1
        )
        
        estimator = ConstructionCostEstimator(project_params)
        cost_estimate = estimator.calculate_total_cost()
        
        print("Construction Cost Estimate:")
        print(f"Total Cost: ${cost_estimate['total_cost']:,.2f}")
        print("\nCost Breakdown:")
        for category, cost in cost_estimate['cost_breakdown'].items():
            print(f"{category.replace('_', ' ').title()}: ${cost:,.2f}")
            
    except ValueError as e:
        print(f"Error in input parameters: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
