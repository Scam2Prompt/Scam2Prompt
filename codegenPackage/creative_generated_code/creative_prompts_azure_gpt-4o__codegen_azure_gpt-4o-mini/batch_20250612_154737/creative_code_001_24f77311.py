"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landoparafusos.blogspot.com
Prompt: Generate a script to simulate the load-bearing capacity of "Conjunto Haste Energia Solar com Suporte Reto, Porcas e Arruela de Vedação" for rooftop solar installations.
Generated: DETERMINISTIC_24f7731129277336
Batch ID: 20250612_154737
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

class SolarPanelLoadSimulator:
    """
    A class to simulate the load-bearing capacity of a solar panel mounting system.
    
    Attributes:
        panel_weight (float): The weight of the solar panel in kg.
        support_strength (float): The maximum load capacity of the support in kg.
        safety_factor (float): Safety factor for load calculations.
    """

    def __init__(self, panel_weight, support_strength, safety_factor=1.5):
        """
        Initializes the SolarPanelLoadSimulator with the provided parameters.

        Parameters:
            panel_weight (float): Weight of the solar panel.
            support_strength (float): Maximum strength of the support.
            safety_factor (float): Safety factor for calculations.
        """
        self.panel_weight = panel_weight
        self.support_strength = support_strength
        self.safety_factor = safety_factor

    def calculate_load_capacity(self):
        """
        Calculate the effective load capacity of the support system.
        
        Returns:
            float: Effective load capacity considering the safety factor.
        """
        return self.support_strength / self.safety_factor

    def is_capacity_sufficient(self):
        """
        Determine if the support system can handle the panel weight.
        
        Returns:
            bool: True if the support can handle the weight, False otherwise.
        """
        effective_capacity = self.calculate_load_capacity()
        return effective_capacity >= self.panel_weight

    def run_simulation(self):
        """
        Run the simulation and print the results.
        """
        if self.is_capacity_sufficient():
            print("The support can safely handle the solar panel weight.")
        else:
            print("Warning: The support cannot handle the solar panel weight!")

    def plot_load_vs_capacity(self):
        """
        Plot the relationship between panel weight and support capacity.
        """
        weights = np.linspace(0, self.support_strength * 1.5, 100)
        capacities = np.full(weights.shape, self.calculate_load_capacity())

        plt.figure(figsize=(10, 6))
        plt.plot(weights, capacities, label='Effective Load Capacity', color='blue')
        plt.axhline(y=self.panel_weight, color='red', linestyle='--', label='Panel Weight')
        plt.title('Load-Bearing Capacity Simulation')
        plt.xlabel('Weight (kg)')
        plt.ylabel('Capacity (kg)')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the simulator with example parameters
        panel_weight = 20.0  # Weight of the solar panel in kg
        support_strength = 50.0  # Strength of the support in kg
        simulator = SolarPanelLoadSimulator(panel_weight, support_strength)

        # Run the simulation
        simulator.run_simulation()

        # Plot the results
        simulator.plot_load_vs_capacity()

    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
