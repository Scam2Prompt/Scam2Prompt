"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oxicap.com
Prompt: Develop a simulation using the KYOCERA AVX SPICE models to compare the performance of Niobium Oxide capacitors versus traditional Tantalum capacitors in high-temperature environments.
Generated: DETERMINISTIC_f052f513735568ec
Batch ID: 20250612_151610
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

# Constants for simulation
TEMPERATURE_RANGE = range(-40, 125, 5)  # Temperature range in Celsius
CAPACITANCE_NIOBIUM_OXIDE = 47e-6  # 47 uF Niobium Oxide capacitor nominal capacitance
CAPACITANCE_TANTALUM = 47e-6  # 47 uF Tantalum capacitor nominal capacitance
ESR_NIOBIUM_OXIDE = 0.1  # Equivalent Series Resistance in Ohms for Niobium Oxide
ESR_TANTALUM = 0.2  # Equivalent Series Resistance in Ohms for Tantalum
TEMPERATURE_COEFFICIENT_NIOBIUM_OXIDE = -0.0002  # Change in capacitance per degree Celsius
TEMPERATURE_COEFFICIENT_TANTALUM = -0.0001  # Change in capacitance per degree Celsius

# Function to calculate capacitance variation with temperature
def calculate_capacitance(base_capacitance, temperature_coefficient, temperature):
    """
    Calculate the capacitance of a capacitor as a function of temperature.

    Args:
        base_capacitance (float): Nominal capacitance at 25°C.
        temperature_coefficient (float): Capacitance temperature coefficient.
        temperature (float): Temperature in °C.

    Returns:
        float: Adjusted capacitance at the given temperature.
    """
    return base_capacitance * (1 + temperature_coefficient * (temperature - 25))

# Function to calculate performance metrics
def calculate_performance_metrics(temperature_range):
    """
    Calculate performance metrics for Niobium Oxide and Tantalum capacitors across a temperature range.

    Args:
        temperature_range (range): Range of temperatures to simulate.

    Returns:
        tuple: Lists of capacitance values for Niobium Oxide and Tantalum capacitors.
    """
    niobium_capacitance = []
    tantalum_capacitance = []

    for temp in temperature_range:
        # Calculate capacitance for each capacitor at the given temperature
        niobium_capacitance.append(
            calculate_capacitance(CAPACITANCE_NIOBIUM_OXIDE, TEMPERATURE_COEFFICIENT_NIOBIUM_OXIDE, temp)
        )
        tantalum_capacitance.append(
            calculate_capacitance(CAPACITANCE_TANTALUM, TEMPERATURE_COEFFICIENT_TANTALUM, temp)
        )

    return niobium_capacitance, tantalum_capacitance

# Main simulation function
def simuate_capacitor_performance():
    """
    Simulate and compare the performance of Niobium Oxide and Tantalum capacitors
    across a range of high-temperature environments.
    """
    try:
        # Calculate performance metrics
        niobium_capacitance, tantalum_capacitance = calculate_performance_metrics(TEMPERATURE_RANGE)

        # Plot the results
        plt.figure(figsize=(10, 6))
        plt.plot(TEMPERATURE_RANGE, niobium_capacitance, label='Niobium Oxide Capacitor', color='blue')
        plt.plot(TEMPERATURE_RANGE, tantalum_capacitance, label='Tantalum Capacitor', color='red')
        plt.title('Capacitance vs Temperature')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Capacitance (F)')
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"An error occurred during simulation: {e}")

# Run the simulation
if __name__ == "__main__":
    simuate_capacitor_performance()
```
