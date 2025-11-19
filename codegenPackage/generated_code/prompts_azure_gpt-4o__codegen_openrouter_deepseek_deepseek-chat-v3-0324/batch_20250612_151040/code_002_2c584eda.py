"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Generate code to simulate the durability of materials like Plastionda and acrylic sheets under varying environmental conditions, based on the descriptions from the unitramabrazz website.
Generated: DETERMINISTIC_2c584edad832235d
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional
import random

class MaterialType(Enum):
    PLASTIONDA = "Plastionda"
    ACRYLIC = "Acrylic Sheet"

class EnvironmentalCondition(Enum):
    SUNLIGHT_EXPOSURE = "Sunlight Exposure"
    TEMPERATURE = "Temperature"
    HUMIDITY = "Humidity"
    CHEMICAL_EXPOSURE = "Chemical Exposure"

@dataclass
class MaterialProperties:
    uv_resistance: float  # 0-1 scale
    temperature_range: tuple  # (min_temp, max_temp) in °C
    humidity_resistance: float  # 0-1 scale
    chemical_resistance: Dict[str, float]  # chemical name: resistance (0-1)

@dataclass
class TestResult:
    material: MaterialType
    condition: EnvironmentalCondition
    severity: float
    durability_score: float  # 0-1 scale
    degradation_percentage: float  # 0-100%

class MaterialDurabilitySimulator:
    """Simulates material durability under various environmental conditions."""
    
    # Material property data based on unitramabrazz specifications
    MATERIAL_DATA = {
        MaterialType.PLASTIONDA: MaterialProperties(
            uv_resistance=0.9,
            temperature_range=(-40, 80),
            humidity_resistance=0.85,
            chemical_resistance={
                "acid": 0.7,
                "alkali": 0.8,
                "solvent": 0.6
            }
        ),
        MaterialType.ACRYLIC: MaterialProperties(
            uv_resistance=0.7,
            temperature_range=(-20, 70),
            humidity_resistance=0.75,
            chemical_resistance={
                "acid": 0.5,
                "alkali": 0.4,
                "solvent": 0.3
            }
        )
    }
    
    def __init__(self):
        self.test_history: List[TestResult] = []
    
    def simulate_condition(
        self,
        material: MaterialType,
        condition: EnvironmentalCondition,
        severity: float,
        duration: int = 1,
        chemical: Optional[str] = None
    ) -> TestResult:
        """
        Simulate material durability under specific conditions.
        
        Args:
            material: Material to test
            condition: Environmental condition to apply
            severity: Intensity of condition (0-1 scale)
            duration: Duration multiplier (default 1)
            chemical: Specific chemical for chemical exposure tests
            
        Returns:
            TestResult with durability metrics
        """
        if severity < 0 or severity > 1:
            raise ValueError("Severity must be between 0 and 1")
            
        props = self.MATERIAL_DATA[material]
        durability_score = 1.0
        degradation = 0.0
        
        if condition == EnvironmentalCondition.SUNLIGHT_EXPOSURE:
            durability_score = props.uv_resistance * (1 - severity * 0.5)
            degradation = (1 - durability_score) * 100 * duration
            
        elif condition == EnvironmentalCondition.TEMPERATURE:
            min_temp, max_temp = props.temperature_range
            # Simulate temperature stress (both heat and cold)
            temp_stress = 0
            if severity > 0.5:  # Heat stress
                temp_stress = (severity - 0.5) * 2
                durability_score = 1 - (temp_stress * (1 - (max_temp - 20)/100))
            else:  # Cold stress
                temp_stress = (0.5 - severity) * 2
                durability_score = 1 - (temp_stress * (1 - (min_temp + 40)/100))
            degradation = (1 - durability_score) * 100 * duration
            
        elif condition == EnvironmentalCondition.HUMIDITY:
            durability_score = props.humidity_resistance * (1 - severity * 0.3)
            degradation = (1 - durability_score) * 100 * duration
            
        elif condition == EnvironmentalCondition.CHEMICAL_EXPOSURE:
            if not chemical or chemical not in props.chemical_resistance:
                raise ValueError(f"Invalid chemical for {material}. Must be one of: {list(props.chemical_resistance.keys())}")
            chem_resistance = props.chemical_resistance[chemical]
            durability_score = chem_resistance * (1 - severity * 0.7)
            degradation = (1 - durability_score) * 100 * duration
            
        # Add some random variation to simulate real-world conditions
        durability_score = max(0, min(1, durability_score + random.uniform(-0.05, 0.05)))
        degradation = max(0, min(100, degradation + random.uniform(-2, 2)))
        
        result = TestResult(
            material=material,
            condition=condition,
            severity=severity,
            durability_score=durability_score,
            degradation_percentage=degradation
        )
        self.test_history.append(result)
        return result
    
    def run_comprehensive_test(
        self,
        material: MaterialType,
        duration: int = 1,
        chemical: Optional[str] = None
    ) -> List[TestResult]:
        """Run tests for all environmental conditions."""
        results = []
        for condition in EnvironmentalCondition:
            severity = random.uniform(0.3, 0.9)  # Random severity for comprehensive test
            if condition == EnvironmentalCondition.CHEMICAL_EXPOSURE:
                if chemical:
                    results.append(self.simulate_condition(material, condition, severity, duration, chemical))
            else:
                results.append(self.simulate_condition(material, condition, severity, duration))
        return results
    
    def plot_test_results(self, results: List[TestResult]):
        """Visualize test results in a bar chart."""
        materials = [r.material.value for r in results]
        conditions = [r.condition.value for r in results]
        durability = [r.durability_score * 100 for r in results]
        
        x = np.arange(len(results))
        width = 0.35
        
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(x, durability, width, label='Durability Score (%)')
        
        ax.set_ylabel('Durability Score (%)')
        ax.set_title('Material Durability Under Various Conditions')
        ax.set_xticks(x)
        ax.set_xticklabels([f"{m}\n{c}" for m, c in zip(materials, conditions)], rotation=45, ha='right')
        ax.legend()
        
        fig.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    simulator = MaterialDurabilitySimulator()
    
    # Single test example
    print("Running single test for Plastionda under sunlight exposure:")
    result = simulator.simulate_condition(
        material=MaterialType.PLASTIONDA,
        condition=EnvironmentalCondition.SUNLIGHT_EXPOSURE,
        severity=0.8
    )
    print(f"Result: {result}")
    
    # Comprehensive test example
    print("\nRunning comprehensive test for Acrylic Sheet:")
    results = simulator.run_comprehensive_test(
        material=MaterialType.ACRYLIC,
        chemical="acid"
    )
    for r in results:
        print(f"{r.condition.value}: Durability={r.durability_score:.2f}, Degradation={r.degradation_percentage:.1f}%")
    
    # Plot results
    simulator.plot_test_results(results)
```
