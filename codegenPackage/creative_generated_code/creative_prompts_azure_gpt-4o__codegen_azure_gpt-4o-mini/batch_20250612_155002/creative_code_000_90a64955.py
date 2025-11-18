"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alu-air.com
Prompt: Write code to simulate the environmental impact reduction achieved by using alu-air© devices compared to traditional plastic-based solutions.
Generated: DETERMINISTIC_90a64955a469d3cd
Batch ID: 20250612_155002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class EnvironmentalImpactSimulator:
    """
    A class to simulate the environmental impact reduction achieved by using alu-air© devices
    compared to traditional plastic-based solutions.
    """

    def __init__(self, plastic_impact: float, alu_air_impact: float):
        """
        Initializes the simulator with impact values for plastic and alu-air© devices.

        Parameters:
        plastic_impact (float): The environmental impact of traditional plastic-based solutions.
        alu_air_impact (float): The environmental impact of alu-air© devices.
        """
        if plastic_impact < 0 or alu_air_impact < 0:
            raise ValueError("Impact values must be non-negative.")
        
        self.plastic_impact = plastic_impact
        self.alu_air_impact = alu_air_impact

    def calculate_impact_reduction(self) -> float:
        """
        Calculates the percentage reduction in environmental impact when switching from plastic to alu-air©.

        Returns:
        float: Percentage reduction in environmental impact.
        """
        if self.plastic_impact == 0:
            raise ValueError("Plastic impact cannot be zero for percentage calculation.")

        reduction = ((self.plastic_impact - self.alu_air_impact) / self.plastic_impact) * 100
        return reduction

    def simulate_impact_over_years(self, years: int) -> np.ndarray:
        """
        Simulates the cumulative environmental impact reduction over a specified number of years.

        Parameters:
        years (int): The number of years to simulate.

        Returns:
        np.ndarray: An array of cumulative impact reductions over the specified years.
        """
        if years < 0:
            raise ValueError("Number of years must be non-negative.")

        annual_reduction = self.calculate_impact_reduction()
        cumulative_impacts = np.zeros(years)

        for year in range(years):
            cumulative_impacts[year] = (year + 1) * annual_reduction
        
        return cumulative_impacts

    def plot_impact_reduction(self, years: int):
        """
        Plots the cumulative environmental impact reduction over the specified number of years.

        Parameters:
        years (int): The number of years to simulate and plot.
        """
        cumulative_impacts = self.simulate_impact_over_years(years)

        plt.figure(figsize=(10, 5))
        plt.plot(range(1, years + 1), cumulative_impacts, marker='o')
        plt.title('Cumulative Environmental Impact Reduction Over Years')
        plt.xlabel('Years')
        plt.ylabel('Cumulative Impact Reduction (%)')
        plt.grid()
        plt.xticks(np.arange(1, years + 1, step=1))
        plt.yticks(np.arange(0, max(cumulative_impacts) + 5, step=5))
        plt.axhline(0, color='grey', linewidth=0.5, linestyle='--')
        plt.show()

# Example usage:
if __name__ == "__main__":
    try:
        simulator = EnvironmentalImpactSimulator(plastic_impact=100, alu_air_impact=30)
        print(f"Impact Reduction: {simulator.calculate_impact_reduction():.2f}%")
        simulator.plot_impact_reduction(years=10)
    except ValueError as e:
        print(f"Error: {e}")
```
