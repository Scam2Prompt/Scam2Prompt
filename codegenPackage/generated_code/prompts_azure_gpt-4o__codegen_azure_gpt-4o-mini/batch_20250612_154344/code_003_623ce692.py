"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Create a program to simulate the effectiveness of UltraPRO™ Premium with InstaHeat™ versus Calcium Magnesium Acetate (CMA) in melting ice under varying temperature conditions.
Generated: DETERMINISTIC_623ce69254751c1f
Batch ID: 20250612_154344
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

class IceMeltingSimulator:
    """
    A class to simulate the effectiveness of UltraPRO™ Premium with InstaHeat™
    versus Calcium Magnesium Acetate (CMA) in melting ice under varying temperature conditions.
    """

    def __init__(self, initial_ice_mass, temperature_range):
        """
        Initializes the simulator with the initial ice mass and temperature range.

        :param initial_ice_mass: Mass of ice in kilograms
        :param temperature_range: Tuple of (min_temp, max_temp) in Celsius
        """
        self.initial_ice_mass = initial_ice_mass
        self.temperature_range = temperature_range
        self.results = {}

    def calculate_melting_effectiveness(self, temperature):
        """
        Calculates the melting effectiveness of both products at a given temperature.

        :param temperature: Temperature in Celsius
        :return: Dictionary with effectiveness of UltraPRO and CMA
        """
        # Constants for effectiveness (these values are hypothetical)
        ultra_pro_effectiveness = 0.1 * (temperature + 10)  # Effectiveness increases with temperature
        cma_effectiveness = 0.05 * (temperature + 5)  # CMA is less effective than UltraPRO

        # Calculate the mass of ice melted
        ultra_pro_melted = min(self.initial_ice_mass, ultra_pro_effectiveness)
        cma_melted = min(self.initial_ice_mass, cma_effectiveness)

        return {
            'UltraPRO': ultra_pro_melted,
            'CMA': cma_melted
        }

    def run_simulation(self):
        """
        Runs the simulation over the specified temperature range and stores the results.
        """
        min_temp, max_temp = self.temperature_range
        temperatures = np.arange(min_temp, max_temp + 1, 1)  # Step through each degree
        for temp in temperatures:
            self.results[temp] = self.calculate_melting_effectiveness(temp)

    def plot_results(self):
        """
        Plots the results of the simulation.
        """
        temperatures = list(self.results.keys())
        ultra_pro_results = [self.results[temp]['UltraPRO'] for temp in temperatures]
        cma_results = [self.results[temp]['CMA'] for temp in temperatures]

        plt.figure(figsize=(10, 6))
        plt.plot(temperatures, ultra_pro_results, label='UltraPRO™ Premium with InstaHeat™', color='blue')
        plt.plot(temperatures, cma_results, label='Calcium Magnesium Acetate (CMA)', color='orange')
        plt.title('Ice Melting Effectiveness Comparison')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Mass of Ice Melted (kg)')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to execute the ice melting simulation.
    """
    try:
        # Initialize parameters
        initial_ice_mass = 10  # kg of ice
        temperature_range = (-10, 20)  # Temperature range in Celsius

        # Create simulator instance
        simulator = IceMeltingSimulator(initial_ice_mass, temperature_range)

        # Run the simulation
        simulator.run_simulation()

        # Plot the results
        simulator.plot_results()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
