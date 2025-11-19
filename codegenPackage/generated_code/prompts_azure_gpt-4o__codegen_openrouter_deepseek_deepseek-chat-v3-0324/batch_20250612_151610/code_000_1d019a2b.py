"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Write Python code to simulate the packaging process for export-grade blueberries, incorporating variables for SO2 generators as described by Osku's product offerings.
Generated: DETERMINISTIC_1d019a2bece3a974
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional
from enum import Enum

class SO2GeneratorType(Enum):
    """Enum representing different types of SO2 generators offered by Osku."""
    SMALL = "Small (5g SO2)"
    MEDIUM = "Medium (10g SO2)"
    LARGE = "Large (20g SO2)"
    EXTRA_LARGE = "Extra Large (40g SO2)"

class BlueberryQuality(Enum):
    """Enum representing different quality grades for blueberries."""
    GRADE_A = "Export Grade A"
    GRADE_B = "Export Grade B"
    GRADE_C = "Domestic Grade"

class PackagingSimulator:
    """Simulates the packaging process for export-grade blueberries with SO2 generators."""
    
    def __init__(self):
        """Initialize the packaging simulator with default values."""
        self.so2_generators = {
            SO2GeneratorType.SMALL: {"weight": 5, "price": 1.50},
            SO2GeneratorType.MEDIUM: {"weight": 10, "price": 2.75},
            SO2GeneratorType.LARGE: {"weight": 20, "price": 5.00},
            SO2GeneratorType.EXTRA_LARGE: {"weight": 40, "price": 9.50}
        }
        self.packaging_materials = ["Plastic Clamshell", "Cardboard Box", "Wooden Crate"]
        self.quality_standards = {
            BlueberryQuality.GRADE_A: {"defect_rate": 0.01, "price_per_kg": 8.50},
            BlueberryQuality.GRADE_B: {"defect_rate": 0.03, "price_per_kg": 6.75},
            BlueberryQuality.GRADE_C: {"defect_rate": 0.05, "price_per_kg": 4.25}
        }
    
    def simulate_packaging(
        self,
        batch_weight: float,
        quality: BlueberryQuality,
        so2_generator: SO2GeneratorType,
        packaging_material: str,
        destination_country: str
    ) -> Dict:
        """
        Simulate the packaging process for a batch of blueberries.
        
        Args:
            batch_weight: Total weight of blueberries in kg
            quality: Quality grade of blueberries
            so2_generator: Type of SO2 generator to use
            packaging_material: Type of packaging material
            destination_country: Destination country for export
            
        Returns:
            Dictionary containing packaging details and simulation results
            
        Raises:
            ValueError: If invalid parameters are provided
        """
        if batch_weight <= 0:
            raise ValueError("Batch weight must be positive")
        if packaging_material not in self.packaging_materials:
            raise ValueError(f"Invalid packaging material. Must be one of: {self.packaging_materials}")
        
        # Calculate basic packaging metrics
        quality_data = self.quality_standards[quality]
        so2_data = self.so2_generators[so2_generator]
        
        # Simulate defects
        defect_rate = quality_data["defect_rate"]
        defect_weight = batch_weight * defect_rate * random.uniform(0.8, 1.2)  # Add some randomness
        
        # Calculate final weight and value
        final_weight = batch_weight - defect_weight
        blueberry_value = final_weight * quality_data["price_per_kg"]
        packaging_cost = self._calculate_packaging_cost(packaging_material, batch_weight)
        total_cost = packaging_cost + so2_data["price"]
        
        # Generate result
        result = {
            "batch_weight_kg": batch_weight,
            "final_weight_kg": round(final_weight, 2),
            "defect_weight_kg": round(defect_weight, 2),
            "defect_rate": round(defect_rate * 100, 2),
            "blueberry_quality": quality.value,
            "so2_generator": {
                "type": so2_generator.value,
                "so2_weight_g": so2_data["weight"],
                "cost": so2_data["price"]
            },
            "packaging": {
                "material": packaging_material,
                "cost": packaging_cost
            },
            "destination": destination_country,
            "blueberry_value": round(blueberry_value, 2),
            "total_cost": round(total_cost, 2),
            "net_value": round(blueberry_value - total_cost, 2)
        }
        
        return result
    
    def _calculate_packaging_cost(self, material: str, weight: float) -> float:
        """Calculate packaging cost based on material and weight."""
        base_costs = {
            "Plastic Clamshell": 0.15,
            "Cardboard Box": 0.08,
            "Wooden Crate": 0.25
        }
        weight_factors = {
            "Plastic Clamshell": 0.02,
            "Cardboard Box": 0.01,
            "Wooden Crate": 0.03
        }
        return base_costs[material] + (weight * weight_factors[material])
    
    def get_available_so2_generators(self) -> List[Dict]:
        """Return list of available SO2 generators with their specifications."""
        return [
            {"type": gen.value, "weight_g": data["weight"], "price": data["price"]}
            for gen, data in self.so2_generators.items()
        ]
    
    def get_quality_standards(self) -> Dict:
        """Return quality standards for different blueberry grades."""
        return {
            quality.value: {
                "defect_rate": f"{data['defect_rate']*100:.1f}%",
                "price_per_kg": f"${data['price_per_kg']:.2f}"
            }
            for quality, data in self.quality_standards.items()
        }

# Example usage
if __name__ == "__main__":
    simulator = PackagingSimulator()
    
    try:
        result = simulator.simulate_packaging(
            batch_weight=100,
            quality=BlueberryQuality.GRADE_A,
            so2_generator=SO2GeneratorType.MEDIUM,
            packaging_material="Plastic Clamshell",
            destination_country="Germany"
        )
        
        print("Packaging Simulation Results:")
        for key, value in result.items():
            if isinstance(value, dict):
                print(f"\n{key}:")
                for sub_key, sub_value in value.items():
                    print(f"  {sub_key}: {sub_value}")
            else:
                print(f"{key}: {value}")
                
    except ValueError as e:
        print(f"Error in simulation: {e}")
```
