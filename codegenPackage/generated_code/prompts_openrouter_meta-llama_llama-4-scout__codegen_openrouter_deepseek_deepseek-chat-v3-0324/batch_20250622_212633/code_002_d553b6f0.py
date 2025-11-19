"""
Generated Code Metadata:
========================
Original URL: https://ledgerreclaim.com
Prompt: "Write a Python script to calculate the cost of construction for a new building in Russia, considering factors such as materials, labor, and location, as per ExpertStroy's services."
Generated: DETERMINISTIC_d553b6f0723ea293
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Optional


class MaterialType(Enum):
    """Enumeration of construction material types."""
    CONCRETE = auto()
    BRICK = auto()
    WOOD = auto()
    STEEL = auto()
    GLASS = auto()


class LocationZone(Enum):
    """Enumeration of location zones in Russia with cost multipliers."""
    CENTRAL = 1.2
    NORTHERN = 1.5
    SOUTHERN = 1.0
    FAR_EAST = 1.8
    URAL = 1.1


@dataclass
class MaterialCost:
    """Data class for material cost per square meter."""
    material_type: MaterialType
    cost_per_sqm: float


@dataclass
class LaborCost:
    """Data class for labor cost per square meter."""
    cost_per_sqm: float
    overtime_multiplier: float = 1.5


class ConstructionCostCalculator:
    """Calculator for construction costs based on materials, labor, and location."""

    def __init__(self):
        self.material_costs: Dict[MaterialType, MaterialCost] = self._load_material_costs()
        self.labor_cost: LaborCost = LaborCost(cost_per_sqm=1500.0)
        self.location_zone: LocationZone = LocationZone.CENTRAL

    @staticmethod
    def _load_material_costs() -> Dict[MaterialType, MaterialCost]:
        """Load default material costs from a JSON file or use defaults."""
        try:
            with open('material_costs.json', 'r') as f:
                data = json.load(f)
                return {
                    MaterialType[mat]: MaterialCost(MaterialType[mat], cost)
                    for mat, cost in data.items()
                }
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            # Default costs if file not found or invalid (in RUB per sqm)
            return {
                MaterialType.CONCRETE: MaterialCost(MaterialType.CONCRETE, 5000.0),
                MaterialType.BRICK: MaterialCost(MaterialType.BRICK, 6000.0),
                MaterialType.WOOD: MaterialCost(MaterialType.WOOD, 4500.0),
                MaterialType.STEEL: MaterialCost(MaterialType.STEEL, 8000.0),
                MaterialType.GLASS: MaterialCost(MaterialType.GLASS, 7000.0),
            }

    def set_location_zone(self, zone: LocationZone) -> None:
        """Set the location zone for the construction."""
        self.location_zone = zone

    def calculate_total_cost(
        self,
        area: float,
        material_type: MaterialType,
        use_overtime: bool = False
    ) -> float:
        """
        Calculate total construction cost.
        
        Args:
            area: Area of the building in square meters.
            material_type: Type of construction material.
            use_overtime: Whether to use overtime labor rates.
        
        Returns:
            Total cost in RUB.
        
        Raises:
            ValueError: If area is not positive or material type is invalid.
        """
        if area <= 0:
            raise ValueError("Area must be a positive number.")
        
        if material_type not in self.material_costs:
            raise ValueError("Invalid material type.")
        
        material_cost = self.material_costs[material_type].cost_per_sqm * area
        labor_cost = self.labor_cost.cost_per_sqm * area
        
        if use_overtime:
            labor_cost *= self.labor_cost.overtime_multiplier
        
        total_cost = (material_cost + labor_cost) * self.location_zone.value
        return total_cost


# Example usage
if __name__ == "__main__":
    try:
        calculator = ConstructionCostCalculator()
        calculator.set_location_zone(LocationZone.NORTHERN)
        
        area = 100.0  # sqm
        material = MaterialType.BRICK
        
        total_cost = calculator.calculate_total_cost(area, material)
        print(f"Total construction cost: {total_cost:.2f} RUB")
        
    except Exception as e:
        print(f"Error calculating construction cost: {e}")
```
