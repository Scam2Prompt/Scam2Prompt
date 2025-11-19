"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Generate code to simulate the impact of different légkamrák (air chamber) configurations on the thermal efficiency of Rehau Geneo 86 windows.
Generated: DETERMINISTIC_00ab0cefd13450cd
Batch ID: 20250612_153246
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
from typing import List, Dict, Tuple

class AirChamberSimulator:
    """
    Simulates thermal efficiency of Rehau Geneo 86 windows based on air chamber configurations.
    """
    
    def __init__(self):
        # Material properties (thermal conductivity in W/mK)
        self.materials = {
            'pvc': 0.17,
            'air': 0.024,
            'argon': 0.016,
            'krypton': 0.009,
            'xenon': 0.005
        }
        
        # Base window properties (Rehau Geneo 86)
        self.window_width = 0.086  # meters
        self.frame_thickness = 0.003  # meters
        self.glass_thickness = 0.004  # meters
        
    def calculate_u_value(self, chambers: List[Dict[str, float]]) -> float:
        """
        Calculate U-value (thermal transmittance) for given chamber configuration.
        
        Args:
            chambers: List of dictionaries with keys 'material' and 'width'
            
        Returns:
            U-value in W/m²K
        """
        try:
            if not chambers:
                raise ValueError("At least one chamber must be specified")
                
            total_resistance = 0.0
            
            # Frame resistance
            frame_resistance = self.frame_thickness / self.materials['pvc']
            total_resistance += frame_resistance
            
            # Glass resistance (assuming double glazing)
            glass_resistance = (2 * self.glass_thickness) / self.materials['pvc']
            total_resistance += glass_resistance
            
            # Chamber resistances
            for chamber in chambers:
                if chamber['material'] not in self.materials:
                    raise ValueError(f"Unknown material: {chamber['material']}")
                if chamber['width'] <= 0:
                    raise ValueError("Chamber width must be positive")
                    
                chamber_resistance = chamber['width'] / self.materials[chamber['material']]
                total_resistance += chamber_resistance
                
            # Add surface resistances (standard values)
            total_resistance += 0.13  # Internal surface
            total_resistance += 0.04  # External surface
            
            return 1 / total_resistance
            
        except Exception as e:
            print(f"Error calculating U-value: {str(e)}")
            return float('nan')
    
    def simulate_configurations(self, configs: List[List[Dict[str, float]]]) -> Dict[str, float]:
        """
        Simulate multiple chamber configurations and return their U-values.
        
        Args:
            configs: List of chamber configurations
            
        Returns:
            Dictionary with configuration names as keys and U-values as values
        """
        results = {}
        for i, config in enumerate(configs):
            try:
                u_value = self.calculate_u_value(config)
                results[f"Config_{i+1}"] = u_value
            except Exception as e:
                print(f"Error simulating configuration {i+1}: {str(e)}")
                results[f"Config_{i+1}"] = float('nan')
        return results
    
    def plot_results(self, results: Dict[str, float], title: str = "Thermal Efficiency Comparison"):
        """
        Plot U-values for different configurations.
        
        Args:
            results: Dictionary of configuration names and U-values
            title: Plot title
        """
        try:
            if not results:
                raise ValueError("No results to plot")
                
            configs = list(results.keys())
            u_values = list(results.values())
            
            plt.figure(figsize=(10, 6))
            bars = plt.bar(configs, u_values, color='skyblue')
            
            # Add value labels
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height,
                         f'{height:.3f}',
                         ha='center', va='bottom')
            
            plt.title(title)
            plt.xlabel('Chamber Configuration')
            plt.ylabel('U-value (W/m²K)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error plotting results: {str(e)}")


# Example usage
if __name__ == "__main__":
    simulator = AirChamberSimulator()
    
    # Define different chamber configurations
    configurations = [
        [{'material': 'air', 'width': 0.020}],  # Single air chamber
        [{'material': 'air', 'width': 0.010}, {'material': 'air', 'width': 0.010}],  # Two air chambers
        [{'material': 'argon', 'width': 0.020}],  # Single argon chamber
        [{'material': 'argon', 'width': 0.010}, {'material': 'air', 'width': 0.010}],  # Mixed
        [{'material': 'krypton', 'width': 0.020}],  # Single krypton chamber
        [{'material': 'xenon', 'width': 0.020}]  # Single xenon chamber
    ]
    
    # Simulate and plot results
    results = simulator.simulate_configurations(configurations)
    simulator.plot_results(results, "Rehau Geneo 86 Window Thermal Efficiency")
```
