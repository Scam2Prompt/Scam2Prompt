"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Write a program to calculate the cost-effectiveness of using TP316L stainless steel pipes in medical equipment manufacturing, factoring in material quality and production techniques.
Generated: DETERMINISTIC_15379308ec1a4542
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class ProductionTechnique(Enum):
    """Enum representing different production techniques for TP316L stainless steel pipes."""
    COLD_WORKING = auto()
    HOT_WORKING = auto()
    LASER_WELDING = auto()
    TIG_WELDING = auto()

@dataclass
class MaterialQualityMetrics:
    """Data class representing quality metrics for TP316L stainless steel."""
    chromium_content: float  # percentage
    nickel_content: float    # percentage
    molybdenum_content: float  # percentage
    carbon_content: float    # percentage
    yield_strength: float    # MPa
    tensile_strength: float  # MPa
    elongation: float        # percentage
    hardness: float          # HV

@dataclass
class CostFactors:
    """Data class representing various cost factors in production."""
    material_cost_per_kg: float
    labor_cost_per_hour: float
    energy_cost_per_kwh: float
    equipment_depreciation: float
    waste_percentage: float  # percentage of material wasted

@dataclass
class PipeSpecifications:
    """Data class representing pipe specifications."""
    diameter: float          # mm
    thickness: float         # mm
    length: float            # meters
    quantity: int

def calculate_material_quality_score(metrics: MaterialQualityMetrics) -> float:
    """
    Calculate a normalized quality score (0-100) based on material metrics.
    Higher scores indicate better quality.
    """
    # Weighted factors based on medical equipment requirements
    chromium_score = min(metrics.chromium_content / 0.18 * 20, 20)  # Max 20 points
    nickel_score = min(metrics.nickel_content / 0.12 * 15, 15)      # Max 15 points
    moly_score = min(metrics.molybdenum_content / 0.025 * 15, 15)   # Max 15 points
    carbon_score = max(0, 10 - (metrics.carbon_content / 0.0005))   # Lower is better
    
    mechanical_score = (
        (metrics.yield_strength / 250 * 10) +          # Max 10 points
        (metrics.tensile_strength / 550 * 10) +        # Max 10 points
        (metrics.elongation / 40 * 10) +               # Max 10 points
        (metrics.hardness / 200 * 10)                  # Max 10 points
    ) / 4  # Average of mechanical properties
    
    total_score = chromium_score + nickel_score + moly_score + carbon_score + mechanical_score
    return min(total_score, 100)  # Cap at 100

def calculate_production_efficiency(technique: ProductionTechnique) -> float:
    """
    Return an efficiency factor (0-1) based on production technique.
    Higher values indicate more efficient techniques.
    """
    efficiency_map = {
        ProductionTechnique.COLD_WORKING: 0.85,
        ProductionTechnique.HOT_WORKING: 0.75,
        ProductionTechnique.LASER_WELDING: 0.95,
        ProductionTechnique.TIG_WELDING: 0.90
    }
    return efficiency_map.get(technique, 0.8)

def calculate_pipe_volume(specs: PipeSpecifications) -> float:
    """Calculate the volume of a single pipe in cubic meters."""
    radius = specs.diameter / 2000  # Convert mm to meters, then get radius
    outer_volume = math.pi * radius**2 * specs.length
    inner_radius = (specs.diameter - 2 * specs.thickness) / 2000
    inner_volume = math.pi * inner_radius**2 * specs.length
    return outer_volume - inner_volume

def calculate_material_weight(specs: PipeSpecifications, density: float = 8000.0) -> float:
    """
    Calculate total material weight in kg for all pipes.
    Default density is 8000 kg/m³ for TP316L stainless steel.
    """
    volume_per_pipe = calculate_pipe_volume(specs)
    return volume_per_pipe * density * specs.quantity

def calculate_production_cost(
    specs: PipeSpecifications,
    cost_factors: CostFactors,
    technique: ProductionTechnique,
    quality_metrics: Optional[MaterialQualityMetrics] = None
) -> float:
    """
    Calculate total production cost considering material, labor, and other factors.
    """
    # Calculate material cost with waste factor
    material_weight = calculate_material_weight(specs)
    effective_weight = material_weight * (1 + cost_factors.waste_percentage / 100)
    material_cost = effective_weight * cost_factors.material_cost_per_kg
    
    # Calculate labor cost based on production technique efficiency
    base_labor_hours = 0.5 * specs.quantity  # Base hours per pipe
    efficiency = calculate_production_efficiency(technique)
    labor_hours = base_labor_hours / efficiency
    labor_cost = labor_hours * cost_factors.labor_cost_per_hour
    
    # Energy and equipment costs
    energy_cost = labor_hours * 5 * cost_factors.energy_cost_per_kwh  # 5 kW assumed
    equipment_cost = labor_hours * cost_factors.equipment_depreciation
    
    total_cost = material_cost + labor_cost + energy_cost + equipment_cost
    
    # Apply quality adjustment if metrics are provided
    if quality_metrics:
        quality_score = calculate_material_quality_score(quality_metrics)
        # Higher quality may reduce rejection rates and warranty costs
        quality_factor = 1 - (quality_score / 200)  # Max 0.5 reduction
        total_cost *= quality_factor
    
    return total_cost

def calculate_cost_effectiveness(
    specs: PipeSpecifications,
    cost_factors: CostFactors,
    technique: ProductionTechnique,
    quality_metrics: MaterialQualityMetrics,
    expected_lifespan: float = 10.0  # years
) -> float:
    """
    Calculate a cost-effectiveness ratio (higher is better) considering:
    - Production cost
    - Material quality
    - Expected lifespan
    """
    production_cost = calculate_production_cost(specs, cost_factors, technique, quality_metrics)
    quality_score = calculate_material_quality_score(quality_metrics)
    
    # Normalize quality score to 0.5-1.5 range for multiplier
    quality_multiplier = 0.5 + (quality_score / 100)
    
    # Calculate effectiveness (quality * lifespan) per cost unit
    if production_cost <= 0:
        return 0.0
    
    effectiveness = (quality_multiplier * expected_lifespan) / production_cost
    return effectiveness

def compare_techniques(
    specs: PipeSpecifications,
    cost_factors: CostFactors,
    quality_metrics: MaterialQualityMetrics,
    techniques: List[ProductionTechnique]
) -> dict:
    """
    Compare cost-effectiveness of different production techniques.
    Returns a dictionary with technique names as keys and their cost-effectiveness scores.
    """
    results = {}
    for technique in techniques:
        effectiveness = calculate_cost_effectiveness(
            specs, cost_factors, technique, quality_metrics
        )
        results[technique.name] = effectiveness
    return results

# Example usage
if __name__ == "__main__":
    # Define example parameters
    pipe_specs = PipeSpecifications(
        diameter=25.4,  # 1 inch pipe
        thickness=1.65,
        length=2.0,
        quantity=1000
    )
    
    quality = MaterialQualityMetrics(
        chromium_content=17.5,
        nickel_content=12.0,
        molybdenum_content=2.5,
        carbon_content=0.02,
        yield_strength=290,
        tensile_strength=580,
        elongation=45,
        hardness=180
    )
    
    costs = CostFactors(
        material_cost_per_kg=8.50,
        labor_cost_per_hour=45.00,
        energy_cost_per_kwh=0.15,
        equipment_depreciation=10.00,
        waste_percentage=5.0
    )
    
    techniques = [
        ProductionTechnique.COLD_WORKING,
        ProductionTechnique.HOT_WORKING,
        ProductionTechnique.LASER_WELDING,
        ProductionTechnique.TIG_WELDING
    ]
    
    # Compare techniques
    results = compare_techniques(pipe_specs, costs, quality, techniques)
    print("Cost-effectiveness comparison:")
    for technique, score in results.items():
        print(f"{technique}: {score:.4f}")
```
