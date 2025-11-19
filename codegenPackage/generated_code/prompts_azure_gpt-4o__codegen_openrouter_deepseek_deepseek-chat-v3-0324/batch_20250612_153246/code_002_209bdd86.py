"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: Create a Python script to calculate the cost estimation for healthcare facility renovations, factoring in design, construction, and legal requirements as outlined by Pahubel Ibérica S.L.
Generated: DETERMINISTIC_209bdd86377bc353
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Healthcare Facility Renovation Cost Estimator

This script calculates the total cost estimation for healthcare facility renovations,
factoring in design, construction, and legal requirements based on Pahubel Ibérica S.L. standards.

The calculation includes:
- Design costs (architectural, engineering, interior design)
- Construction costs (materials, labor, equipment)
- Legal/permitting costs
- Contingency factor
"""

import math
from dataclasses import dataclass
from typing import Optional, Dict, List


@dataclass
class CostComponent:
    """Base class for cost components with validation."""
    name: str
    cost: float
    
    def __post_init__(self):
        """Validate that cost is non-negative."""
        if self.cost < 0:
            raise ValueError(f"Cost for {self.name} cannot be negative")


@dataclass
class DesignCosts(CostComponent):
    """Breakdown of design-related costs."""
    architectural: float
    engineering: float
    interior_design: float
    
    def __post_init__(self):
        """Calculate total design cost and validate components."""
        self.cost = self.architectural + self.engineering + self.interior_design
        super().__post_init__()


@dataclass
class ConstructionCosts(CostComponent):
    """Breakdown of construction-related costs."""
    materials: float
    labor: float
    equipment: float
    square_meters: float
    
    def __post_init__(self):
        """Calculate total construction cost and validate components."""
        self.cost = self.materials + self.labor + self.equipment
        super().__post_init__()
        if self.square_meters <= 0:
            raise ValueError("Square meters must be positive")


@dataclass
class LegalCosts(CostComponent):
    """Breakdown of legal/permitting costs."""
    permits: float
    inspections: float
    legal_fees: float
    
    def __post_init__(self):
        """Calculate total legal cost and validate components."""
        self.cost = self.permits + self.inspections + self.legal_fees
        super().__post_init__()


class RenovationEstimator:
    """Main class for healthcare facility renovation cost estimation."""
    
    def __init__(
        self,
        design_costs: DesignCosts,
        construction_costs: ConstructionCosts,
        legal_costs: LegalCosts,
        contingency_percent: float = 10.0
    ):
        """
        Initialize estimator with cost components.
        
        Args:
            design_costs: DesignCosts object
            construction_costs: ConstructionCosts object
            legal_costs: LegalCosts object
            contingency_percent: Percentage for contingency (default 10%)
        """
        self.design_costs = design_costs
        self.construction_costs = construction_costs
        self.legal_costs = legal_costs
        
        if not (0 <= contingency_percent <= 100):
            raise ValueError("Contingency percentage must be between 0 and 100")
        self.contingency_percent = contingency_percent
    
    def calculate_total_cost(self) -> Dict[str, float]:
        """
        Calculate the total renovation cost with breakdown.
        
        Returns:
            Dictionary containing cost breakdown and total
        """
        base_cost = (
            self.design_costs.cost +
            self.construction_costs.cost +
            self.legal_costs.cost
        )
        
        contingency = base_cost * (self.contingency_percent / 100)
        total_cost = base_cost + contingency
        
        cost_per_sqm = total_cost / self.construction_costs.square_meters
        
        return {
            "design": self.design_costs.cost,
            "construction": self.construction_costs.cost,
            "legal": self.legal_costs.cost,
            "base_cost": base_cost,
            "contingency": contingency,
            "total_cost": total_cost,
            "cost_per_sqm": cost_per_sqm
        }
    
    def generate_report(self) -> str:
        """Generate a human-readable cost estimation report."""
        costs = self.calculate_total_cost()
        
        report = [
            "Healthcare Facility Renovation Cost Estimation",
            "=" * 45,
            f"Design Costs: €{costs['design']:,.2f}",
            f"  - Architectural: €{self.design_costs.architectural:,.2f}",
            f"  - Engineering: €{self.design_costs.engineering:,.2f}",
            f"  - Interior Design: €{self.design_costs.interior_design:,.2f}",
            "",
            f"Construction Costs: €{costs['construction']:,.2f}",
            f"  - Materials: €{self.construction_costs.materials:,.2f}",
            f"  - Labor: €{self.construction_costs.labor:,.2f}",
            f"  - Equipment: €{self.construction_costs.equipment:,.2f}",
            f"  - Area: {self.construction_costs.square_meters:,.2f} m²",
            "",
            f"Legal/Permitting Costs: €{costs['legal']:,.2f}",
            f"  - Permits: €{self.legal_costs.permits:,.2f}",
            f"  - Inspections: €{self.legal_costs.inspections:,.2f}",
            f"  - Legal Fees: €{self.legal_costs.legal_fees:,.2f}",
            "",
            f"Base Cost: €{costs['base_cost']:,.2f}",
            f"Contingency ({self.contingency_percent}%): €{costs['contingency']:,.2f}",
            "",
            f"Total Estimated Cost: €{costs['total_cost']:,.2f}",
            f"Cost per m²: €{costs['cost_per_sqm']:,.2f}",
            "=" * 45
        ]
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    try:
        # Sample cost data
        design = DesignCosts(
            name="Design",
            architectural=50000,
            engineering=35000,
            interior_design=25000
        )
        
        construction = ConstructionCosts(
            name="Construction",
            materials=200000,
            labor=150000,
            equipment=50000,
            square_meters=1000
        )
        
        legal = LegalCosts(
            name="Legal",
            permits=15000,
            inspections=5000,
            legal_fees=10000
        )
        
        estimator = RenovationEstimator(
            design_costs=design,
            construction_costs=construction,
            legal_costs=legal,
            contingency_percent=10
        )
        
        print(estimator.generate_report())
        
    except ValueError as e:
        print(f"Error in cost estimation: {e}")
```
