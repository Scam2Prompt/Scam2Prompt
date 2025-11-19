"""
Generated Code Metadata:
========================
Original URL: https://engenhariawpj.com
Prompt: "Create a code snippet to estimate the cost and environmental impact of using different thermal insulation materials in a construction project."
Generated: DETERMINISTIC_2d1560957952dc2f
Batch ID: 20250622_210703
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
from typing import Dict, List, NamedTuple, Optional

class InsulationMaterial(Enum):
    """Enumeration of common insulation materials with their properties."""
    FIBERGLASS = {
        'cost_per_sqft': 0.50,
        'r_value_per_inch': 3.7,
        'embodied_carbon_per_sqft': 0.5  # kgCO2/sqft
    }
    CELLULOSE = {
        'cost_per_sqft': 0.40,
        'r_value_per_inch': 3.8,
        'embodied_carbon_per_sqft': 0.3
    }
    SPRAY_FOAM = {
        'cost_per_sqft': 1.20,
        'r_value_per_inch': 6.5,
        'embodied_carbon_per_sqft': 1.8
    }
    MINERAL_WOOL = {
        'cost_per_sqft': 0.70,
        'r_value_per_inch': 4.0,
        'embodied_carbon_per_sqft': 0.6
    }

class ConstructionProject(NamedTuple):
    """Represents a construction project's insulation requirements."""
    area_sqft: float
    desired_r_value: float
    lifetime_years: int

class InsulationEstimate(NamedTuple):
    """Result of insulation cost and impact estimation."""
    material: str
    thickness_inches: float
    total_cost: float
    embodied_carbon: float
    annual_heating_cost: float
    lifetime_heating_cost: float

def estimate_insulation(
    project: ConstructionProject,
    material: InsulationMaterial,
    heating_cost_per_btu: float = 0.00002,
    heating_degree_days: float = 5000,
    efficiency: float = 0.8
) -> InsulationEstimate:
    """
    Estimates cost and environmental impact of insulation material for a project.
    
    Args:
        project: Construction project details
        material: Selected insulation material
        heating_cost_per_btu: Cost per BTU for heating ($/BTU)
        heating_degree_days: Annual heating degree days for location
        efficiency: Heating system efficiency (0-1)
    
    Returns:
        InsulationEstimate with calculated values
    """
    material_props = material.value
    
    # Calculate required thickness
    thickness_inches = project.desired_r_value / material_props['r_value_per_inch']
    
    # Calculate material costs
    total_cost = project.area_sqft * material_props['cost_per_sqft'] * thickness_inches
    
    # Calculate embodied carbon
    embodied_carbon = project.area_sqft * material_props['embodied_carbon_per_sqft'] * thickness_inches
    
    # Calculate heating costs
    annual_btu = (project.area_sqft * heating_degree_days * 24) / (project.desired_r_value * efficiency)
    annual_heating_cost = annual_btu * heating_cost_per_btu
    lifetime_heating_cost = annual_heating_cost * project.lifetime_years
    
    return InsulationEstimate(
        material=material.name,
        thickness_inches=thickness_inches,
        total_cost=round(total_cost, 2),
        embodied_carbon=round(embodied_carbon, 2),
        annual_heating_cost=round(annual_heating_cost, 2),
        lifetime_heating_cost=round(lifetime_heating_cost, 2)
    )

def compare_materials(
    project: ConstructionProject,
    materials: List[InsulationMaterial],
    **kwargs
) -> List[InsulationEstimate]:
    """
    Compare multiple insulation materials for a given project.
    
    Args:
        project: Construction project details
        materials: List of insulation materials to compare
        kwargs: Additional arguments for estimate_insulation
    
    Returns:
        List of InsulationEstimate objects for each material
    """
    return [estimate_insulation(project, material, **kwargs) for material in materials]

def format_comparison(estimates: List[InsulationEstimate]) -> str:
    """Format comparison results as a readable string."""
    headers = ["Material", "Thickness (in)", "Material Cost ($)", "Embodied Carbon (kgCO2)",
               "Annual Heating Cost ($)", "Lifetime Heating Cost ($)"]
    
    rows = []
    for est in estimates:
        rows.append([
            est.material,
            f"{est.thickness_inches:.1f}",
            f"${est.total_cost:,.2f}",
            f"{est.embodied_carbon:,.2f}",
            f"${est.annual_heating_cost:,.2f}",
            f"${est.lifetime_heating_cost:,.2f}"
        ])
    
    # Calculate column widths
    col_widths = [max(len(h), max(len(r[i]) for r in rows)) for i, h in enumerate(headers)]
    
    # Build header
    header = " | ".join(h.ljust(w) for h, w in zip(headers, col_widths))
    separator = "-+-".join("-" * w for w in col_widths)
    
    # Build rows
    formatted_rows = []
    for row in rows:
        formatted_rows.append(" | ".join(cell.ljust(w) for cell, w in zip(row, col_widths)))
    
    return "\n".join([header, separator] + formatted_rows)

# Example usage
if __name__ == "__main__":
    project = ConstructionProject(
        area_sqft=1500,
        desired_r_value=30,
        lifetime_years=30
    )
    
    materials = [
        InsulationMaterial.FIBERGLASS,
        InsulationMaterial.CELLULOSE,
        InsulationMaterial.SPRAY_FOAM,
        InsulationMaterial.MINERAL_WOOL
    ]
    
    estimates = compare_materials(project, materials)
    print("Insulation Material Comparison:")
    print(format_comparison(estimates))
```
