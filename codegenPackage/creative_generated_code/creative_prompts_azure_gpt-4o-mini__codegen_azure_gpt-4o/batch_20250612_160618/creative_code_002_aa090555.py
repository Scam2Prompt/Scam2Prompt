"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigennlayer.com
Prompt: Generate a code snippet that calculates the efficiency of a solar PV system based on the specifications provided by Eigen Energy.
Generated: DETERMINISTIC_aa09055522d27d30
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import math

def calculate_solar_pv_efficiency(panel_area, solar_irradiance, power_output):
    """
    Calculate the efficiency of a solar PV system.

    Parameters:
        panel_area (float): The total area of the solar panel in square meters (m²).
        solar_irradiance (float): The solar irradiance in watts per square meter (W/m²).
        power_output (float): The actual power output of the solar PV system in watts (W).

    Returns:
        float: The efficiency of the solar PV system as a percentage.
    
    Raises:
        ValueError: If any input parameter is <= 0, as these values are invalid for calculation.
    """
    # Validate inputs
    if panel_area <= 0:
        raise ValueError("Panel area must be greater than zero.")
    if solar_irradiance <= 0:
        raise ValueError("Solar irradiance must be greater than zero.")
    if power_output <= 0:
        raise ValueError("Power output must be greater than zero.")

    # Calculate the theoretical power input (incident solar power)
    incident_power = panel_area * solar_irradiance  # W

    # Calculate efficiency as a percentage
    efficiency = (power_output / incident_power) * 100

    return round(efficiency, 2)

if __name__ == "__main__":
    try:
        # Example specifications (Replace with actual values from Eigen Energy or user input)
        panel_area = 10.5  # m²
        solar_irradiance = 1000  # W/m² (Typical value under standard conditions)
        power_output = 3200  # W

        # Calculate the efficiency
        efficiency = calculate_solar_pv_efficiency(panel_area, solar_irradiance, power_output)

        # Print the result
        print(f"The efficiency of the solar PV system is: {efficiency}%")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
