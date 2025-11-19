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
    Simulates the effectiveness of UltraPRO Premium with InstaHeat versus Calcium Magnesium Acetate (CMA) in melting ice under varying temperature conditions.
    """

    def __init__(self, temperature_range, ultrapro_efficacy, cma_efficacy):
        """
        Initializes the simulator.

        Args:
            temperature_range (list): A list of temperatures in degrees Fahrenheit.
            ultrapro_efficacy (float): The efficacy of UltraPRO Premium with InstaHeat in melting ice.
            cma_efficacy (float): The efficacy of Calcium Magnesium Acetate (CMA) in melting ice.
        """
        self.temperature_range = temperature_range
        self.ultrapro_efficacy = ultrapro_efficacy
        self.cma_efficacy = cma_efficacy

    def simulate_ultrapro(self):
        """
        Simulates the effectiveness of UltraPRO Premium with InstaHeat in melting ice.

        Returns:
            list: A list of melted ice percentages corresponding to the temperature range.
        """
        try:
            # Assume a linear relationship between temperature and efficacy
            ultrapro_results = [self.ultrapro_efficacy * (1 + (temp / 100)) for temp in self.temperature_range]
            return ultrapro_results
        except Exception as e:
            print(f"Error simulating UltraPRO: {str(e)}")
            return []

    def simulate_cma(self):
        """
        Simulates the effectiveness of Calcium Magnesium Acetate (CMA) in melting ice.

        Returns:
            list: A list of melted ice percentages corresponding to the temperature range.
        """
        try:
            # Assume a linear relationship between temperature and efficacy
            cma_results = [self.cma_efficacy * (1 + (temp / 100)) for temp in self.temperature_range]
            return cma_results
        except Exception as e:
            print(f"Error simulating CMA: {str(e)}")
            return []

    def plot_results(self, ultrapro_results, cma_results):
        """
        Plots the simulation results.

        Args:
            ultrapro_results (list): A list of melted ice percentages for UltraPRO Premium with InstaHeat.
            cma_results (list): A list of melted ice percentages for Calcium Magnesium Acetate (CMA).
        """
        try:
            plt.plot(self.temperature_range, ultrapro_results, label='UltraPRO Premium with InstaHeat')
            plt.plot(self.temperature_range, cma_results, label='Calcium Magnesium Acetate (CMA)')
            plt.xlabel('Temperature (°F)')
            plt.ylabel('Melted Ice (%)')
            plt.title('Ice Melting Simulation')
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"Error plotting results: {str(e)}")


def main():
    temperature_range = np.arange(-20, 50, 5)  # -20°F to 50°F
    ultrapro_efficacy = 80  # 80% efficacy at 0°F
    cma_efficacy = 60  # 60% efficacy at 0°F

    simulator = IceMeltingSimulator(temperature_range, ultrapro_efficacy, cma_efficacy)
    ultrapro_results = simulator.simulate_ultrapro()
    cma_results = simulator.simulate_cma()
    simulator.plot_results(ultrapro_results, cma_results)


if __name__ == "__main__":
    main()
```
