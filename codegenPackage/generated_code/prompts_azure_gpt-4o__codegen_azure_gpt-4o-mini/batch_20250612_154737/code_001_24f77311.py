"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: Generate a script to simulate the load-bearing capacity of "Conjunto Haste Energia Solar com Suporte Reto, Porcas e Arruela de Vedação" for rooftop solar installations.
Generated: DETERMINISTIC_24f7731129277336
Batch ID: 20250612_154737
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

class SolarPanelSupport:
    """
    A class to simulate the load-bearing capacity of a solar panel support system.
    
    Attributes:
        max_load (float): Maximum load capacity in Newtons.
        safety_factor (float): Safety factor for load calculations.
        wind_load (float): Wind load in Newtons.
        panel_weight (float): Weight of the solar panel in Newtons.
    """

    def __init__(self, max_load: float, safety_factor: float, wind_load: float, panel_weight: float):
        """
        Initializes the SolarPanelSupport with specified parameters.
        
        Args:
            max_load (float): Maximum load capacity in Newtons.
            safety_factor (float): Safety factor for load calculations.
            wind_load (float): Wind load in Newtons.
            panel_weight (float): Weight of the solar panel in Newtons.
        """
        self.max_load = max_load
        self.safety_factor = safety_factor
        self.wind_load = wind_load
        self.panel_weight = panel_weight

    def total_load(self) -> float:
        """
        Calculates the total load on the support system.
        
        Returns:
            float: Total load in Newtons.
        """
        return self.wind_load + self.panel_weight

    def is_within_capacity(self) -> bool:
        """
        Checks if the total load is within the load-bearing capacity considering the safety factor.
        
        Returns:
            bool: True if within capacity, False otherwise.
        """
        total_load = self.total_load()
        allowable_load = self.max_load / self.safety_factor
        return total_load <= allowable_load

    def simulate_load(self, wind_loads: np.ndarray) -> np.ndarray:
        """
        Simulates the load-bearing capacity for a range of wind loads.
        
        Args:
            wind_loads (np.ndarray): Array of wind loads to simulate.
        
        Returns:
            np.ndarray: Array of boolean values indicating if the load is within capacity.
        """
        results = []
        for wind in wind_loads:
            self.wind_load = wind
            results.append(self.is_within_capacity())
        return np.array(results)

def main():
    """
    Main function to run the simulation and plot the results.
    """
    # Define parameters for the solar panel support
    max_load = 1500.0  # Maximum load capacity in Newtons
    safety_factor = 1.5  # Safety factor
    panel_weight = 300.0  # Weight of the solar panel in Newtons

    # Create an instance of SolarPanelSupport
    support = SolarPanelSupport(max_load, safety_factor, 0, panel_weight)

    # Define a range of wind loads to simulate
    wind_loads = np.linspace(0, 1200, 100)  # Wind loads from 0 to 1200 Newtons

    # Simulate load-bearing capacity
    results = support.simulate_load(wind_loads)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(wind_loads, results, label='Within Capacity', color='green')
    plt.axhline(y=0.5, color='red', linestyle='--', label='Capacity Limit')
    plt.title('Load-Bearing Capacity Simulation')
    plt.xlabel('Wind Load (N)')
    plt.ylabel('Within Capacity (True/False)')
    plt.ylim(-0.1, 1.1)
    plt.xticks(np.arange(0, 1300, 100))
    plt.yticks([0, 1], ['No', 'Yes'])
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
