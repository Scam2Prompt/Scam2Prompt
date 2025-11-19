"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Generate code that calculates the cost-effectiveness of manufacturing aerospace components in India, factoring in the low-cost manufacturing opportunities highlighted by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_1c0a5a7876cfd89f
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Aerospace Manufacturing Cost-Effectiveness Calculator

This script calculates the cost-effectiveness of manufacturing aerospace components in India,
factoring in low-cost manufacturing opportunities. It considers various cost factors like labor,
materials, logistics, and overheads, and compares them with international benchmarks.

Inputs:
- Component details (weight, complexity)
- Manufacturing parameters (labor hours, material costs)
- Location-specific factors (logistics, tariffs)
- Benchmark costs (international comparison)

Outputs:
- Total manufacturing cost
- Cost savings percentage vs benchmark
- Cost-effectiveness score
"""

import json
from dataclasses import dataclass
from typing import Optional, Dict, List
import math

@dataclass
class Component:
    """Represents an aerospace component to be manufactured."""
    name: str
    weight_kg: float
    complexity: int  # 1-10 scale
    material_type: str
    international_benchmark_cost: float  # USD

@dataclass
class ManufacturingCosts:
    """Breakdown of manufacturing costs."""
    labor: float
    materials: float
    logistics: float
    overhead: float
    tariffs: float

class CostEffectivenessCalculator:
    """Calculates cost-effectiveness of manufacturing aerospace components in India."""
    
    # Location-specific cost factors (India)
    LABOR_COST_PER_HOUR = 5.50  # USD
    MATERIAL_COST_FACTORS = {
        'aluminum': 1.2,
        'titanium': 1.5,
        'composite': 1.8,
        'steel': 1.1
    }
    LOGISTICS_BASE_COST = 500  # USD
    OVERHEAD_PERCENTAGE = 0.15  # 15%
    TARIFF_PERCENTAGE = 0.10  # 10%
    
    # Complexity multipliers
    COMPLEXITY_MULTIPLIERS = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 2.0]
    
    def __init__(self, component: Component, labor_hours: float):
        self.component = component
        self.labor_hours = labor_hours
    
    def calculate_costs(self) -> ManufacturingCosts:
        """Calculate all manufacturing cost components."""
        try:
            # Calculate labor costs
            labor_cost = self.labor_hours * self.LABOR_COST_PER_HOUR
            
            # Calculate material costs with complexity factor
            material_factor = self.MATERIAL_COST_FACTORS.get(
                self.component.material_type.lower(), 1.0
            )
            complexity_factor = self.COMPLEXITY_MULTIPLIERS[self.component.complexity - 1]
            material_cost = (self.component.weight_kg * 10) * material_factor * complexity_factor
            
            # Calculate logistics (weight-based)
            logistics_cost = self.LOGISTICS_BASE_COST * math.log(self.component.weight_kg + 1)
            
            # Calculate overhead (percentage of labor and materials)
            overhead_cost = (labor_cost + material_cost) * self.OVERHEAD_PERCENTAGE
            
            # Calculate tariffs (percentage of total cost before tariffs)
            pre_tariff_cost = labor_cost + material_cost + logistics_cost + overhead_cost
            tariff_cost = pre_tariff_cost * self.TARIFF_PERCENTAGE
            
            return ManufacturingCosts(
                labor=labor_cost,
                materials=material_cost,
                logistics=logistics_cost,
                overhead=overhead_cost,
                tariffs=tariff_cost
            )
        except Exception as e:
            raise ValueError(f"Error calculating costs: {str(e)}")
    
    def calculate_cost_effectiveness(self) -> Dict[str, float]:
        """Calculate cost-effectiveness metrics."""
        try:
            costs = self.calculate_costs()
            total_cost = sum(vars(costs).values())
            
            # Calculate savings vs international benchmark
            savings = max(0, self.component.international_benchmark_cost - total_cost)
            savings_percentage = (savings / self.component.international_benchmark_cost) * 100
            
            # Calculate cost-effectiveness score (0-100)
            effectiveness_score = min(100, savings_percentage * 2)  # Cap at 100
            
            return {
                'total_cost': total_cost,
                'savings_amount': savings,
                'savings_percentage': savings_percentage,
                'effectiveness_score': effectiveness_score,
                'cost_breakdown': vars(costs)
            }
        except Exception as e:
            raise ValueError(f"Error calculating cost-effectiveness: {str(e)}")

def load_components_from_json(file_path: str) -> List[Component]:
    """Load component data from JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return [Component(**item) for item in data]
    except Exception as e:
        raise ValueError(f"Error loading components: {str(e)}")

def generate_report(component: Component, results: Dict[str, float]) -> str:
    """Generate a human-readable cost-effectiveness report."""
    report = [
        f"Cost-Effectiveness Analysis for {component.name}",
        "=" * 50,
        f"Component Details:",
        f"- Weight: {component.weight_kg} kg",
        f"- Material: {component.material_type}",
        f"- Complexity: {component.complexity}/10",
        "",
        "Cost Breakdown (USD):",
        f"- Labor: ${results['cost_breakdown']['labor']:.2f}",
        f"- Materials: ${results['cost_breakdown']['materials']:.2f}",
        f"- Logistics: ${results['cost_breakdown']['logistics']:.2f}",
        f"- Overhead: ${results['cost_breakdown']['overhead']:.2f}",
        f"- Tariffs: ${results['cost_breakdown']['tariffs']:.2f}",
        f"Total Cost: ${results['total_cost']:.2f}",
        "",
        "Savings Analysis:",
        f"- International Benchmark: ${component.international_benchmark_cost:.2f}",
        f"- Savings Amount: ${results['savings_amount']:.2f}",
        f"- Savings Percentage: {results['savings_percentage']:.2f}%",
        "",
        f"Cost-Effectiveness Score: {results['effectiveness_score']:.1f}/100",
        "=" * 50
    ]
    return "\n".join(report)

# Example usage
if __name__ == "__main__":
    try:
        # Example component
        sample_component = Component(
            name="Turbine Blade",
            weight_kg=8.5,
            complexity=7,
            material_type="titanium",
            international_benchmark_cost=4500.00
        )
        
        calculator = CostEffectivenessCalculator(
            component=sample_component,
            labor_hours=120
        )
        
        results = calculator.calculate_cost_effectiveness()
        print(generate_report(sample_component, results))
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
