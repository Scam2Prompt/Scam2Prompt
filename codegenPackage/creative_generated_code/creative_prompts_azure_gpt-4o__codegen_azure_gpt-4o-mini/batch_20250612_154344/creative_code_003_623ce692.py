"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pavainc.com
Prompt: Create a program to simulate the effectiveness of UltraPRO™ Premium with InstaHeat™ versus Calcium Magnesium Acetate (CMA) in melting ice under varying temperature conditions.
Generated: DETERMINISTIC_623ce69254751c1f
Batch ID: 20250612_154344
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

class IceMeltingSimulator:
    def __init__(self, initial_ice_mass: float, temperature_range: np.ndarray):
        """
        Initialize the IceMeltingSimulator with initial ice mass and temperature range.

        Parameters:
        initial_ice_mass (float): The initial mass of ice in kg.
        temperature_range (np.ndarray): The range of temperatures in degrees Celsius.
        """
        self.initial_ice_mass = initial_ice_mass  # mass of ice in kg
        self.temperature_range = temperature_range  # temperature range in Celsius

        # Constants for the melting effectiveness of the products
        self.ultra_pro_effectiveness = 0.2  # effectiveness factor for UltraPRO
        self.cma_effectiveness = 0.15  # effectiveness factor for Calcium Magnesium Acetate

    def calculate_melting(self, temperature: float, product_effectiveness: float) -> float:
        """
        Calculate the amount of ice melted based on temperature and product effectiveness.

        Parameters:
        temperature (float): The temperature in degrees Celsius.
        product_effectiveness (float): The effectiveness of the melting product.

        Returns:
        float: The mass of ice melted in kg.
        """
        if temperature < -10:
            melting_rate = 0  # No melting below -10°C
        elif -10 <= temperature <= 0:
            melting_rate = (temperature + 10) * product_effectiveness
        else:
            melting_rate = (temperature + 10) * product_effectiveness * 2  # Increased melting above 0°C

        melted_ice = min(melting_rate, self.initial_ice_mass)  # Cannot melt more ice than available
        return melted_ice

    def simulate(self):
        """
        Simulate the melting of ice using both UltraPRO and CMA across the temperature range.
        """
        ultra_pro_melted = []
        cma_melted = []

        for temp in self.temperature_range:
            ultra_pro_melted.append(self.calculate_melting(temp, self.ultra_pro_effectiveness))
            cma_melted.append(self.calculate_melting(temp, self.cma_effectiveness))

        self.plot_results(ultra_pro_melted, cma_melted)

    def plot_results(self, ultra_pro_melted, cma_melted):
        """
        Plot the results of the simulation.

        Parameters:
        ultra_pro_melted (list): The list of melted ice masses for UltraPRO.
        cma_melted (list): The list of melted ice masses for CMA.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.temperature_range, ultra_pro_melted, label='UltraPRO™ Premium with InstaHeat™', color='blue')
        plt.plot(self.temperature_range, cma_melted, label='Calcium Magnesium Acetate (CMA)', color='orange')
        
        plt.title('Ice Melting Simulation')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Melted Ice Mass (kg)')
        plt.axhline(y=self.initial_ice_mass, color='r', linestyle='--', label='Initial Ice Mass')
        plt.legend()
        plt.grid()
        plt.xticks(np.arange(-10, 11, 1))
        plt.yticks(np.arange(0, self.initial_ice_mass + 1, 1))
        plt.xlim(-10, 10)
        plt.ylim(0, self.initial_ice_mass + 1)
        plt.show()

if __name__ == "__main__":
    try:
        # Initialization parameters
        initial_ice_mass = 50  # kg of ice to simulate melting
        temperature_range = np.linspace(-10, 10, 100)  # Temperature range from -10°C to 10°C

        simulator = IceMeltingSimulator(initial_ice_mass, temperature_range)
        simulator.simulate()
    except Exception as e:
        print(f"An error occurred: {e}")
```
