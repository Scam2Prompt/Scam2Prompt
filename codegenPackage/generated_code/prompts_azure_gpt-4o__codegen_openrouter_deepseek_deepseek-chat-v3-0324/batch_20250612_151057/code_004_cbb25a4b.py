"""
Generated Code Metadata:
========================
Original URL: https://sctoll.io
Prompt: Write code to analyze the thermal properties of T304 stainless steel exhaust kits, referencing Brixton Forged™'s exhaust system specifications.
Generated: DETERMINISTIC_cbb25a4b82520048
Batch ID: 20250612_151057
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
from typing import Optional, Dict, List

# Constants for T304 Stainless Steel properties (from Brixton Forged™ specifications)
THERMAL_CONDUCTIVITY = 16.2  # W/m·K at 100°C
SPECIFIC_HEAT_CAPACITY = 500  # J/kg·K at 20-100°C
DENSITY = 8000  # kg/m³
MELTING_POINT = 1400  # °C
THERMAL_EXPANSION_COEFFICIENT = 17.3e-6  # 1/K at 20-100°C

@dataclass
class ExhaustComponent:
    """Represents a component in the exhaust system."""
    name: str
    length: float  # meters
    diameter: float  # meters
    thickness: float  # meters
    temperature: float  # °C

@dataclass
class ThermalAnalysisResult:
    """Stores results of thermal analysis for a component."""
    component_name: str
    heat_transfer_rate: float  # Watts
    thermal_resistance: float  # K/W
    thermal_expansion: float  # meters
    safety_margin: float  # ratio of current temp to melting point

class ExhaustSystemAnalyzer:
    """Analyzes thermal properties of a T304 stainless steel exhaust system."""
    
    def __init__(self, components: List[ExhaustComponent]):
        self.components = components
    
    def calculate_heat_transfer_rate(self, component: ExhaustComponent) -> float:
        """Calculate heat transfer rate through a cylindrical component."""
        # Q = (2πkLΔT) / ln(r2/r1)
        # Simplified for thin-walled assumption (r2 ≈ r1)
        delta_temp = component.temperature - 25  # Assume ambient temp of 25°C
        surface_area = 2 * 3.14159 * (component.diameter/2) * component.length
        return THERMAL_CONDUCTIVITY * surface_area * delta_temp / component.thickness
    
    def calculate_thermal_resistance(self, component: ExhaustComponent) -> float:
        """Calculate thermal resistance of the component."""
        return component.thickness / (THERMAL_CONDUCTIVITY * 2 * 3.14159 * (component.diameter/2) * component.length)
    
    def calculate_thermal_expansion(self, component: ExhaustComponent) -> float:
        """Calculate linear thermal expansion of the component."""
        delta_temp = component.temperature - 25  # Assume ambient temp of 25°C
        return component.length * THERMAL_EXPANSION_COEFFICIENT * delta_temp
    
    def calculate_safety_margin(self, component: ExhaustComponent) -> float:
        """Calculate safety margin based on melting point."""
        return MELTING_POINT / component.temperature if component.temperature > 0 else float('inf')
    
    def analyze_component(self, component: ExhaustComponent) -> ThermalAnalysisResult:
        """Perform complete thermal analysis on a single component."""
        try:
            heat_transfer = self.calculate_heat_transfer_rate(component)
            resistance = self.calculate_thermal_resistance(component)
            expansion = self.calculate_thermal_expansion(component)
            safety = self.calculate_safety_margin(component)
            
            return ThermalAnalysisResult(
                component_name=component.name,
                heat_transfer_rate=heat_transfer,
                thermal_resistance=resistance,
                thermal_expansion=expansion,
                safety_margin=safety
            )
        except Exception as e:
            raise ValueError(f"Error analyzing component {component.name}: {str(e)}")
    
    def analyze_system(self) -> Dict[str, ThermalAnalysisResult]:
        """Analyze all components in the exhaust system."""
        results = {}
        for component in self.components:
            results[component.name] = self.analyze_component(component)
        return results
    
    def save_analysis_results(self, results: Dict[str, ThermalAnalysisResult], filename: str):
        """Save analysis results to a JSON file."""
        try:
            serializable_results = {
                name: {
                    'component_name': result.component_name,
                    'heat_transfer_rate': result.heat_transfer_rate,
                    'thermal_resistance': result.thermal_resistance,
                    'thermal_expansion': result.thermal_expansion,
                    'safety_margin': result.safety_margin
                }
                for name, result in results.items()
            }
            
            with open(filename, 'w') as f:
                json.dump(serializable_results, f, indent=2)
        except Exception as e:
            raise IOError(f"Failed to save results: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample exhaust system components
    components = [
        ExhaustComponent("Downpipe", 1.2, 0.076, 0.0015, 650),
        ExhaustComponent("Midpipe", 1.5, 0.064, 0.0012, 450),
        ExhaustComponent("Muffler", 0.8, 0.102, 0.002, 350)
    ]
    
    try:
        analyzer = ExhaustSystemAnalyzer(components)
        results = analyzer.analyze_system()
        analyzer.save_analysis_results(results, "exhaust_thermal_analysis.json")
        
        # Print summary
        print("Thermal Analysis Results:")
        for name, result in results.items():
            print(f"\nComponent: {name}")
            print(f"  Heat Transfer Rate: {result.heat_transfer_rate:.2f} W")
            print(f"  Thermal Resistance: {result.thermal_resistance:.6f} K/W")
            print(f"  Thermal Expansion: {result.thermal_expansion:.6f} m")
            print(f"  Safety Margin: {result.safety_margin:.2f}")
            
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
```
