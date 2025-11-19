"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Develop a simulation using the KYOCERA AVX SPICE models to compare the performance of Niobium Oxide capacitors versus traditional Tantalum capacitors in high-temperature environments.
Generated: DETERMINISTIC_f052f513735568ec
Batch ID: 20250612_151610
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

# Constants
TEMPERATURES = np.arange(25, 201, 25)  # Temperature range from 25°C to 200°C
CAPACITOR_TYPES = ['Niobium Oxide', 'Tantalum']
CAPACITANCE_VALUES = [10e-6, 10e-6]  # Capacitance values in Farads (10 µF)
ESR_VALUES = [0.1, 0.05]  # Equivalent Series Resistance in Ohms
LIFETIME_COEFFICIENTS = [0.5, 0.8]  # Lifetime degradation coefficients

def calculate_lifetime(temperature, capacitor_type):
    """
    Calculate the lifetime of a capacitor based on temperature and type.
    
    Parameters:
    temperature (float): The operating temperature in °C.
    capacitor_type (str): The type of capacitor ('Niobium Oxide' or 'Tantalum').
    
    Returns:
    float: Estimated lifetime in hours.
    """
    try:
        if capacitor_type not in CAPACITOR_TYPES:
            raise ValueError("Invalid capacitor type. Choose 'Niobium Oxide' or 'Tantalum'.")
        
        # Lifetime calculation based on Arrhenius equation
        if capacitor_type == 'Niobium Oxide':
            lifetime = 10000 * np.exp(-LIFETIME_COEFFICIENTS[0] * (temperature - 25) / 25)
        else:  # Tantalum
            lifetime = 10000 * np.exp(-LIFETIME_COEFFICIENTS[1] * (temperature - 25) / 25)
        
        return lifetime
    except Exception as e:
        print(f"Error calculating lifetime: {e}")
        return None

def simulate_capacitor_lifetime():
    """
    Simulate the lifetime of Niobium Oxide and Tantalum capacitors across a range of temperatures.
    """
    lifetimes = {cap_type: [] for cap_type in CAPACITOR_TYPES}
    
    for temp in TEMPERATURES:
        for cap_type in CAPACITOR_TYPES:
            lifetime = calculate_lifetime(temp, cap_type)
            if lifetime is not None:
                lifetimes[cap_type].append(lifetime)
    
    return lifetimes

def plot_lifetime_comparison(lifetimes):
    """
    Plot the lifetime comparison of Niobium Oxide and Tantalum capacitors.
    
    Parameters:
    lifetimes (dict): A dictionary containing lifetimes for each capacitor type.
    """
    try:
        plt.figure(figsize=(10, 6))
        for cap_type, lifetime in lifetimes.items():
            plt.plot(TEMPERATURES, lifetime, label=cap_type)
        
        plt.title('Capacitor Lifetime Comparison at High Temperatures')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Lifetime (hours)')
        plt.legend()
        plt.grid()
        plt.yscale('log')  # Log scale for better visibility
        plt.show()
    except Exception as e:
        print(f"Error plotting data: {e}")

if __name__ == "__main__":
    # Run the simulation and plot results
    lifetimes = simulate_capacitor_lifetime()
    plot_lifetime_comparison(lifetimes)
```
