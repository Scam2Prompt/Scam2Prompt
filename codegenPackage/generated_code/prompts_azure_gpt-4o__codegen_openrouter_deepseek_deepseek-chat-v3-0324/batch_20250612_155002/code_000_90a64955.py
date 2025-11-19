"""
Generated Code Metadata:
========================
Original URL: https://alu-air.com
Prompt: Write code to simulate the environmental impact reduction achieved by using alu-air© devices compared to traditional plastic-based solutions.
Generated: DETERMINISTIC_90a64955a469d3cd
Batch ID: 20250612_155002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Tuple

class EnvironmentalImpactSimulator:
    """
    Simulates the environmental impact reduction of alu-air© devices compared to traditional plastic solutions.
    """
    
    def __init__(self):
        self.plastic_impact_factors = {
            'co2_emissions': 3.5,  # kg CO2 per kg plastic
            'energy_consumption': 80,  # MJ per kg plastic
            'water_usage': 180,  # liters per kg plastic
            'landfill_waste': 0.95  # fraction that ends in landfill
        }
        
        self.alu_air_impact_factors = {
            'co2_emissions': 1.2,  # kg CO2 per kg alu-air
            'energy_consumption': 45,  # MJ per kg alu-air
            'water_usage': 50,  # liters per kg alu-air
            'recyclability': 0.85  # fraction that gets recycled
        }
    
    def calculate_impact_reduction(self, quantity_kg: float, years: int = 1) -> Dict[str, float]:
        """
        Calculate environmental impact reduction for given quantity over specified years.
        
        Args:
            quantity_kg: Annual quantity in kilograms
            years: Number of years to simulate
            
        Returns:
            Dictionary with impact reduction metrics
        """
        if quantity_kg <= 0:
            raise ValueError("Quantity must be positive")
        if years <= 0:
            raise ValueError("Years must be positive")
            
        results = {}
        
        # Calculate annual impacts
        for factor in self.plastic_impact_factors:
            plastic_impact = quantity_kg * self.plastic_impact_factors[factor] * years
            alu_air_impact = quantity_kg * self.alu_air_impact_factors.get(factor, 0) * years
            
            if factor == 'landfill_waste':
                reduction = plastic_impact - (quantity_kg * (1 - self.alu_air_impact_factors['recyclability']) * years)
            else:
                reduction = plastic_impact - alu_air_impact
            
            results[factor] = max(0, reduction)
            
        return results
    
    def generate_comparison_chart(self, quantity_kg: float, years: int = 1) -> None:
        """
        Generate a bar chart comparing environmental impacts.
        
        Args:
            quantity_kg: Annual quantity in kilograms
            years: Number of years to simulate
        """
        impacts = self.calculate_impact_reduction(quantity_kg, years)
        
        factors = list(impacts.keys())
        plastic_values = [quantity_kg * years * self.plastic_impact_factors.get(f, 0) for f in factors]
        alu_air_values = [quantity_kg * years * self.alu_air_impact_factors.get(f, 0) for f in factors]
        
        x = np.arange(len(factors))
        width = 0.35
        
        fig, ax = plt.subplots(figsize=(10, 6))
        rects1 = ax.bar(x - width/2, plastic_values, width, label='Plastic', color='red')
        rects2 = ax.bar(x + width/2, alu_air_values, width, label='alu-air©', color='green')
        
        ax.set_ylabel('Environmental Impact')
        ax.set_title(f'Environmental Impact Comparison ({quantity_kg}kg/year, {years} years)')
        ax.set_xticks(x)
        ax.set_xticklabels([f.replace('_', ' ').title() for f in factors])
        ax.legend()
        
        fig.tight_layout()
        plt.show()
    
    def simulate_growth_scenario(self, base_quantity: float, growth_rate: float, years: int) -> Dict[str, List[Tuple[int, float]]]:
        """
        Simulate impact over time with growth in adoption.
        
        Args:
            base_quantity: Starting annual quantity in kg
            growth_rate: Annual growth rate (e.g., 0.1 for 10%)
            years: Number of years to simulate
            
        Returns:
            Dictionary with yearly impact data for each factor
        """
        if growth_rate < -1:
            raise ValueError("Growth rate cannot be below -100%")
            
        results = {}
        for factor in self.plastic_impact_factors:
            results[factor] = []
            
        for year in range(1, years + 1):
            current_quantity = base_quantity * (1 + growth_rate) ** (year - 1)
            year_impacts = self.calculate_impact_reduction(current_quantity, 1)
            
            for factor, reduction in year_impacts.items():
                results[factor].append((year, reduction))
                
        return results
    
    def plot_growth_scenario(self, base_quantity: float, growth_rate: float, years: int) -> None:
        """
        Plot impact reduction over time with growth scenario.
        
        Args:
            base_quantity: Starting annual quantity in kg
            growth_rate: Annual growth rate
            years: Number of years to simulate
        """
        scenario_data = self.simulate_growth_scenario(base_quantity, growth_rate, years)
        
        plt.figure(figsize=(12, 6))
        for factor, data in scenario_data.items():
            years, values = zip(*data)
            plt.plot(years, values, label=factor.replace('_', ' ').title())
            
        plt.xlabel('Year')
        plt.ylabel('Annual Impact Reduction')
        plt.title(f'Annual Environmental Impact Reduction (Starting at {base_quantity}kg, {growth_rate*100:.1f}% Growth)')
        plt.legend()
        plt.grid(True)
        plt.show()


# Example usage
if __name__ == "__main__":
    simulator = EnvironmentalImpactSimulator()
    
    # Single calculation example
    print("Impact reduction for 1000kg over 5 years:")
    print(simulator.calculate_impact_reduction(1000, 5))
    
    # Generate comparison chart
    simulator.generate_comparison_chart(500)
    
    # Growth scenario
    simulator.plot_growth_scenario(1000, 0.2, 10)
```
