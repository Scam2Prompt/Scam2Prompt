"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: Generate Python code to model the environmental impact of Econopure's EDI (Electrodeionization) technology compared to traditional water purification methods.
Generated: DETERMINISTIC_24a16766d0162ede
Batch ID: 20250612_154631
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
from typing import Dict, Tuple, List
from dataclasses import dataclass
from enum import Enum

class WaterPurificationMethod(Enum):
    """Enum representing different water purification methods."""
    EDI = "Electrodeionization"
    RO = "Reverse Osmosis"
    DISTILLATION = "Distillation"
    ION_EXCHANGE = "Ion Exchange"

@dataclass
class EnvironmentalImpactMetrics:
    """Dataclass to store environmental impact metrics for a purification method."""
    energy_consumption_kwh: float  # kWh per 1000 liters
    water_waste_percentage: float  # Percentage of input water wasted
    chemical_usage_kg: float       # kg of chemicals per 1000 liters
    co2_emissions_kg: float        # kg CO2 per 1000 liters

class WaterPurificationComparison:
    """Class to model and compare environmental impacts of different water purification methods."""
    
    def __init__(self):
        # Initialize with default impact data (hypothetical values - should be replaced with real data)
        self.method_data: Dict[WaterPurificationMethod, EnvironmentalImpactMetrics] = {
            WaterPurificationMethod.EDI: EnvironmentalImpactMetrics(
                energy_consumption_kwh=5.0,
                water_waste_percentage=5.0,
                chemical_usage_kg=0.1,
                co2_emissions_kg=0.5
            ),
            WaterPurificationMethod.RO: EnvironmentalImpactMetrics(
                energy_consumption_kwh=10.0,
                water_waste_percentage=25.0,
                chemical_usage_kg=0.5,
                co2_emissions_kg=1.2
            ),
            WaterPurificationMethod.DISTILLATION: EnvironmentalImpactMetrics(
                energy_consumption_kwh=80.0,
                water_waste_percentage=10.0,
                chemical_usage_kg=0.2,
                co2_emissions_kg=8.0
            ),
            WaterPurificationMethod.ION_EXCHANGE: EnvironmentalImpactMetrics(
                energy_consumption_kwh=3.0,
                water_waste_percentage=15.0,
                chemical_usage_kg=5.0,
                co2_emissions_kg=0.8
            )
        }
    
    def compare_methods(self, volume_liters: float = 1000) -> Dict[WaterPurificationMethod, EnvironmentalImpactMetrics]:
        """
        Compare all methods for a given water volume.
        
        Args:
            volume_liters: Volume of water to purify in liters (default: 1000)
            
        Returns:
            Dictionary of methods with their scaled impact metrics
        """
        if volume_liters <= 0:
            raise ValueError("Volume must be positive")
            
        scale_factor = volume_liters / 1000
        return {
            method: EnvironmentalImpactMetrics(
                energy_consumption_kwh=metrics.energy_consumption_kwh * scale_factor,
                water_waste_percentage=metrics.water_waste_percentage,
                chemical_usage_kg=metrics.chemical_usage_kg * scale_factor,
                co2_emissions_kg=metrics.co2_emissions_kg * scale_factor
            )
            for method, metrics in self.method_data.items()
        }
    
    def plot_comparison(self, metric: str, volume_liters: float = 1000):
        """
        Plot comparison of a specific metric across all methods.
        
        Args:
            metric: One of ['energy_consumption_kwh', 'water_waste_percentage', 
                           'chemical_usage_kg', 'co2_emissions_kg']
            volume_liters: Volume of water to purify in liters (default: 1000)
        """
        valid_metrics = ['energy_consumption_kwh', 'water_waste_percentage', 
                        'chemical_usage_kg', 'co2_emissions_kg']
        if metric not in valid_metrics:
            raise ValueError(f"Invalid metric. Must be one of {valid_metrics}")
            
        comparison = self.compare_methods(volume_liters)
        methods = [m.value for m in comparison.keys()]
        values = [getattr(m, metric) for m in comparison.values()]
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(methods, values)
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom')
        
        # Format plot
        plt.title(f'{metric.replace("_", " ").title()} Comparison ({volume_liters} liters)')
        plt.ylabel(metric.replace("_", " ").title())
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def calculate_savings(self, method1: WaterPurificationMethod, 
                         method2: WaterPurificationMethod, 
                         volume_liters: float = 1000) -> Dict[str, float]:
        """
        Calculate environmental savings between two methods.
        
        Args:
            method1: First method to compare
            method2: Second method to compare
            volume_liters: Volume of water to purify in liters (default: 1000)
            
        Returns:
            Dictionary with percentage savings for each metric
        """
        comparison = self.compare_methods(volume_liters)
        m1 = comparison[method1]
        m2 = comparison[method2]
        
        def calc_saving(val1, val2):
            if val2 == 0:
                return 0.0  # Avoid division by zero
            return ((val2 - val1) / val2) * 100
        
        return {
            'energy_saving_percent': calc_saving(m1.energy_consumption_kwh, m2.energy_consumption_kwh),
            'water_saving_percent': calc_saving(m1.water_waste_percentage, m2.water_waste_percentage),
            'chemical_saving_percent': calc_saving(m1.chemical_usage_kg, m2.chemical_usage_kg),
            'co2_saving_percent': calc_saving(m1.co2_emissions_kg, m2.co2_emissions_kg)
        }

# Example usage
if __name__ == "__main__":
    comparison = WaterPurificationComparison()
    
    # Compare methods for 5000 liters
    results = comparison.compare_methods(5000)
    for method, metrics in results.items():
        print(f"\n{method.value}:")
        print(f"  Energy: {metrics.energy_consumption_kwh:.2f} kWh")
        print(f"  Water waste: {metrics.water_waste_percentage:.2f}%")
        print(f"  Chemicals: {metrics.chemical_usage_kg:.2f} kg")
        print(f"  CO2 emissions: {metrics.co2_emissions_kg:.2f} kg")
    
    # Plot energy consumption comparison
    comparison.plot_comparison('energy_consumption_kwh', 5000)
    
    # Calculate savings between EDI and RO
    savings = comparison.calculate_savings(WaterPurificationMethod.EDI, 
                                         WaterPurificationMethod.RO, 
                                         5000)
    print("\nSavings EDI vs RO:")
    for metric, value in savings.items():
        print(f"  {metric.replace('_', ' ').title()}: {value:.2f}%")
```
