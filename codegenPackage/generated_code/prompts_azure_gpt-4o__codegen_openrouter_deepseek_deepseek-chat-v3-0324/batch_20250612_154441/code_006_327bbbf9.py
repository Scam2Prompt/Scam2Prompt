"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Write a script to simulate the durability of rubber flooring materials (e.g., TPV Rubber, Rubber Tiles) under heavy usage conditions, referencing the use cases like gym fitness and playgrounds mentioned on Rubber Flooring Indonesia's site.
Generated: DETERMINISTIC_327bbbf9848668e4
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple

class RubberFlooringSimulator:
    """
    Simulates the durability of rubber flooring materials under heavy usage conditions.
    Supports TPV Rubber and Rubber Tiles materials for gym fitness and playground use cases.
    """
    
    def __init__(self):
        # Material properties (durability coefficients)
        self.materials = {
            'TPV Rubber': {
                'gym': {'wear_rate': 0.001, 'impact_resistance': 0.95},
                'playground': {'wear_rate': 0.002, 'impact_resistance': 0.90}
            },
            'Rubber Tiles': {
                'gym': {'wear_rate': 0.002, 'impact_resistance': 0.90},
                'playground': {'wear_rate': 0.003, 'impact_resistance': 0.85}
            }
        }
        
        # Usage intensity factors (1.0 = normal, higher = more intense)
        self.usage_intensity = {
            'gym': 1.2,
            'playground': 1.5
        }
        
    def simulate_durability(
        self,
        material: str,
        use_case: str,
        duration_years: int = 5,
        daily_usage_hours: int = 8
    ) -> Dict[str, List[Tuple[int, float]]]:
        """
        Simulates material durability over time.
        
        Args:
            material: Flooring material (TPV Rubber or Rubber Tiles)
            use_case: Application scenario (gym or playground)
            duration_years: Simulation duration in years
            daily_usage_hours: Average daily usage in hours
            
        Returns:
            Dictionary with 'wear' and 'impact_resistance' data points over time
        """
        if material not in self.materials:
            raise ValueError(f"Invalid material. Choose from: {list(self.materials.keys())}")
        if use_case not in self.usage_intensity:
            raise ValueError(f"Invalid use case. Choose from: {list(self.usage_intensity.keys())}")
        
        # Get material properties
        props = self.materials[material][use_case]
        intensity = self.usage_intensity[use_case]
        
        # Initialize results
        wear_data = []
        impact_data = []
        
        # Simulate each day
        days_per_year = 365
        total_days = duration_years * days_per_year
        
        for day in range(1, total_days + 1):
            # Calculate daily wear (base wear + random variation)
            daily_wear = (props['wear_rate'] * intensity * daily_usage_hours / 24) * (1 + random.uniform(-0.1, 0.1))
            
            # Calculate impact resistance degradation
            impact_degradation = (1 - props['impact_resistance']) * (day / total_days) * intensity
            
            # Accumulate results
            wear_data.append((day, daily_wear))
            impact_data.append((day, 1 - impact_degradation))
        
        return {
            'wear': wear_data,
            'impact_resistance': impact_data
        }
    
    def plot_results(self, results: Dict[str, List[Tuple[int, float]]], material: str, use_case: str):
        """
        Plots the simulation results.
        
        Args:
            results: Simulation results from simulate_durability()
            material: Flooring material name
            use_case: Application scenario
        """
        plt.figure(figsize=(12, 6))
        
        # Prepare data
        days = [x[0] for x in results['wear']]
        wear = np.cumsum([x[1] for x in results['wear']])
        impact = [x[1] for x in results['impact_resistance']]
        
        # Plot wear
        plt.subplot(1, 2, 1)
        plt.plot(days, wear)
        plt.title(f'{material} - {use_case}\nTotal Wear Over Time')
        plt.xlabel('Days')
        plt.ylabel('Cumulative Wear')
        plt.grid(True)
        
        # Plot impact resistance
        plt.subplot(1, 2, 2)
        plt.plot(days, impact)
        plt.title(f'{material} - {use_case}\nImpact Resistance Over Time')
        plt.xlabel('Days')
        plt.ylabel('Impact Resistance (0-1)')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    simulator = RubberFlooringSimulator()
    
    try:
        # Simulate TPV Rubber in gym environment
        results = simulator.simulate_durability(
            material='TPV Rubber',
            use_case='gym',
            duration_years=3,
            daily_usage_hours=10
        )
        simulator.plot_results(results, 'TPV Rubber', 'gym')
        
        # Simulate Rubber Tiles in playground environment
        results = simulator.simulate_durability(
            material='Rubber Tiles',
            use_case='playground',
            duration_years=5,
            daily_usage_hours=12
        )
        simulator.plot_results(results, 'Rubber Tiles', 'playground')
        
    except ValueError as e:
        print(f"Error: {e}")
```
