"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Create a function that simulates the performance of Niobium Oxide capacitors at 85°C, highlighting their reliability metrics.
Generated: DETERMINISTIC_7d1c8b150f69578d
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def simulate_niobium_oxide_capacitor(temp_celsius: float = 85) -> dict:
    """
    Simulates the performance and reliability metrics of Niobium Oxide capacitors at a given temperature.
    
    Args:
        temp_celsius (float): The temperature in Celsius at which the simulation is performed. Default is 85°C.
    
    Returns:
        dict: A dictionary containing reliability metrics such as ESR, leakage current, and expected lifespan.
    """
    # Constants for Niobium Oxide capacitors
    NOMINAL_ESR = 0.1  # Nominal Equivalent Series Resistance in ohms
    NOMINAL_LEAKAGE_CURRENT = 0.01  # Nominal leakage current in mA
    NOMINAL_LIFESPAN = 10000  # Nominal lifespan in hours at 25°C
    ACTIVATION_ENERGY = 0.7  # Activation energy in eV (used for lifespan calculation)
    BOLTZMANN_CONSTANT = 8.617e-5  # Boltzmann constant in eV/K

    try:
        # Convert temperature to Kelvin
        temp_kelvin = temp_celsius + 273.15

        # Calculate ESR (Equivalent Series Resistance)
        # ESR typically increases with temperature due to material properties
        esr = NOMINAL_ESR * (1 + 0.01 * (temp_celsius - 25))  # Simplified linear model

        # Calculate leakage current
        # Leakage current increases exponentially with temperature
        leakage_current = NOMINAL_LEAKAGE_CURRENT * math.exp(0.05 * (temp_celsius - 25))  # Simplified exponential model

        # Calculate expected lifespan using Arrhenius equation
        # Lifespan decreases exponentially with temperature
        lifespan = NOMINAL_LIFESPAN * math.exp(-ACTIVATION_ENERGY / (BOLTZMANN_CONSTANT * temp_kelvin))

        # Return the reliability metrics as a dictionary
        return {
            "Temperature (°C)": temp_celsius,
            "ESR (Ohms)": round(esr, 4),
            "Leakage Current (mA)": round(leakage_current, 4),
            "Expected Lifespan (Hours)": round(lifespan, 2)
        }

    except Exception as e:
        # Handle any unexpected errors
        return {"error": f"An error occurred during simulation: {str(e)}"}


# Example usage
if __name__ == "__main__":
    # Simulate performance at 85°C
    result = simulate_niobium_oxide_capacitor(85)
    print("Niobium Oxide Capacitor Performance Metrics:")
    for key, value in result.items():
        print(f"{key}: {value}")
```
