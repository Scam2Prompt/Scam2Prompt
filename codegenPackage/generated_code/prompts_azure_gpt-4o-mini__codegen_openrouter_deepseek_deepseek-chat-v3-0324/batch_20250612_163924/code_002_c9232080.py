"""
Generated Code Metadata:
========================
Original URL: https://apps-eigenlayer.com
Prompt: Write a Python script that simulates the cost analysis for tooling and production of metal stamping components, considering factors like material types and manufacturing tolerances.
Generated: DETERMINISTIC_c923208052b352ac
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import math

class MaterialType(Enum):
    """Enumeration of supported material types."""
    STEEL = "steel"
    ALUMINUM = "aluminum"
    COPPER = "copper"
    BRASS = "brass"

class ToleranceLevel(Enum):
    """Enumeration of manufacturing tolerance levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

@dataclass
class MaterialCost:
    """Data class representing material cost per unit weight."""
    material: MaterialType
    cost_per_kg: float  # Cost in USD per kilogram

@dataclass
class ToolingCost:
    """Data class representing tooling setup costs."""
    base_cost: float  # Base tooling cost in USD
    tolerance_multiplier: Dict[ToleranceLevel, float]  # Multiplier based on tolerance

@dataclass
class ProductionParameters:
    """Data class representing production parameters."""
    material: MaterialType
    tolerance: ToleranceLevel
    part_weight_kg: float  # Weight of each part in kilograms
    batch_size: int  # Number of parts in production batch

class CostAnalyzer:
    """Simulates cost analysis for metal stamping components."""
    
    def __init__(self):
        """Initialize with default material and tooling costs."""
        self.material_costs: Dict[MaterialType, MaterialCost] = {
            MaterialType.STEEL: MaterialCost(MaterialType.STEEL, 1.50),
            MaterialType.ALUMINUM: MaterialCost(MaterialType.ALUMINUM, 3.00),
            MaterialType.COPPER: MaterialCost(MaterialType.COPPER, 7.50),
            MaterialType.BRASS: MaterialCost(MaterialType.BRASS, 5.00)
        }
        
        self.tooling_costs = ToolingCost(
            base_cost=5000.00,
            tolerance_multiplier={
                ToleranceLevel.LOW: 1.0,
                ToleranceLevel.MEDIUM: 1.5,
                ToleranceLevel.HIGH: 2.0
            }
        )
    
    def calculate_material_cost(self, params: ProductionParameters) -> float:
        """Calculate total material cost for the production batch."""
        if params.part_weight_kg <= 0:
            raise ValueError("Part weight must be positive")
        if params.batch_size <= 0:
            raise ValueError("Batch size must be positive")
        
        material_cost = self.material_costs.get(params.material)
        if not material_cost:
            raise ValueError(f"Unsupported material type: {params.material}")
        
        return material_cost.cost_per_kg * params.part_weight_kg * params.batch_size
    
    def calculate_tooling_cost(self, params: ProductionParameters) -> float:
        """Calculate tooling cost based on tolerance level."""
        if params.tolerance not in self.tooling_costs.tolerance_multiplier:
            raise ValueError(f"Unsupported tolerance level: {params.tolerance}")
        
        multiplier = self.tooling_costs.tolerance_multiplier[params.tolerance]
        return self.tooling_costs.base_cost * multiplier
    
    def calculate_total_cost(self, params: ProductionParameters) -> Dict[str, float]:
        """Calculate total production cost including material and tooling."""
        try:
            material_cost = self.calculate_material_cost(params)
            tooling_cost = self.calculate_tooling_cost(params)
            total_cost = material_cost + tooling_cost
            
            return {
                "material_cost": round(material_cost, 2),
                "tooling_cost": round(tooling_cost, 2),
                "total_cost": round(total_cost, 2),
                "cost_per_part": round(total_cost / params.batch_size, 2)
            }
        except ValueError as e:
            raise ValueError(f"Error in cost calculation: {str(e)}")

def main():
    """Example usage of the CostAnalyzer."""
    analyzer = CostAnalyzer()
    
    # Example production parameters
    params = ProductionParameters(
        material=MaterialType.STEEL,
        tolerance=ToleranceLevel.MEDIUM,
        part_weight_kg=0.5,
        batch_size=1000
    )
    
    try:
        costs = analyzer.calculate_total_cost(params)
        print("Cost Analysis Results:")
        print(json.dumps(costs, indent=2))
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
