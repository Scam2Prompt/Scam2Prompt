"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://universalsolar1.com
Prompt: Write code to simulate the performance of Universal Solar's high-efficiency PV modules in various environmental conditions, referencing their state-of-the-art factory components.
Generated: DETERMINISTIC_f4c58d5d72e227f1
Batch ID: 20250612_153225
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

class SolarModuleSimulator:
    """
    A class to simulate the performance of high-efficiency PV modules under various environmental conditions.
    """

    def __init__(self, module_efficiency, temperature_coefficient, nominal_temperature, irradiance_nominal):
        """
        Initialize the SolarModuleSimulator.
        
        :param module_efficiency: Efficiency of the PV module (as a fraction, e.g., 0.22 for 22%).
        :param temperature_coefficient: Efficiency degradation per degree Celsius (fractional decrease).
        :param nominal_temperature: Nominal operating temperature of the PV module (degrees Celsius).
        :param irradiance_nominal: Nominal solar irradiance value (W/m^2).
        """
        self.module_efficiency = module_efficiency
        self.temperature_coefficient = temperature_coefficient
        self.nominal_temperature = nominal_temperature
        self.irradiance_nominal = irradiance_nominal

    def simulate_power_output(self, irradiance, temperature):
        """
        Simulates the power output of the PV module under specific conditions.
        
        :param irradiance: Solar irradiance in W/m^2.
        :param temperature: Ambient temperature in degrees Celsius.
        :return: Simulated power output in Watts.
        """
        try:
            # Calculate efficiency adjustment due to temperature
            temperature_effect = 1 - self.temperature_coefficient * (temperature - self.nominal_temperature)
            
            # Adjusted efficiency based on temperature effects
            adjusted_efficiency = self.module_efficiency * temperature_effect
            
            # Ensure efficiency is non-negative
            adjusted_efficiency = max(adjusted_efficiency, 0)
            
            # Calculate power output
            power_output = adjusted_efficiency * irradiance
            
            return power_output
        except Exception as e:
            raise ValueError(f"Error in simulate_power_output: {e}")

    def simulate_over_conditions(self, irradiance_range, temperature_range):
        """
        Simulates power output across a range of irradiance and temperature values.
        
        :param irradiance_range: Array of solar irradiance values in W/m^2.
        :param temperature_range: Array of temperature values in degrees Celsius.
        :return: 2D array of power outputs for each combination of irradiance and temperature.
        """
        try:
            # Create a 2D grid for irradiance and temperature
            power_output_matrix = np.zeros((len(temperature_range), len(irradiance_range)))
            
            for i, temp in enumerate(temperature_range):
                for j, irr in enumerate(irradiance_range):
                    power_output_matrix[i, j] = self.simulate_power_output(irr, temp)
            
            return power_output_matrix
        except Exception as e:
            raise ValueError(f"Error in simulate_over_conditions: {e}")

# Simulation Parameters
MODULE_EFFICIENCY = 0.22  # 22% efficiency
TEMPERATURE_COEFFICIENT = 0.004  # 0.4% efficiency loss per °C
NOMINAL_TEMPERATURE = 25  # Nominal operating temperature in °C
IRRADIANCE_NOMINAL = 1000  # Nominal irradiance in W/m^2

# Create an instance of the simulator
simulator = SolarModuleSimulator(MODULE_EFFICIENCY, TEMPERATURE_COEFFICIENT, NOMINAL_TEMPERATURE, IRRADIANCE_NOMINAL)

# Simulate across conditions
irradiance_values = np.linspace(200, 1000, 5)  # Solar irradiance from 200 to 1000 W/m^2
temperature_values = np.linspace(-10, 50, 7)  # Temperature from -10°C to 50°C

power_output = simulator.simulate_over_conditions(irradiance_values, temperature_values)

# Plot the results
plt.figure(figsize=(10, 6))
for i, temp in enumerate(temperature_values):
    plt.plot(irradiance_values, power_output[i, :], label=f'Temp: {temp}°C')

plt.title('PV Module Power Output Simulation')
plt.xlabel('Irradiance (W/m^2)')
plt.ylabel('Power Output (Watts)')
plt.legend()
plt.grid(True)
plt.show()
```
