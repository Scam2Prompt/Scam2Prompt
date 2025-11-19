"""
Generated Code Metadata:
========================
Original URL: https://engenhariawpj.com
Prompt: "Write a Python code to calculate the energy efficiency of a building using StoTherm thermal insulation system."
Generated: DETERMINISTIC_82c2c2469c5dd33f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_energy_efficiency(area, u_value, temperature_difference, insulation_factor):
    """
    Calculate the energy efficiency of a building using StoTherm thermal insulation system.

    Parameters:
        area (float): Surface area of the building in square meters (m²).
        u_value (float): Thermal transmittance (U-value) of the building in W/(m²·K).
        temperature_difference (float): Temperature difference between inside and outside in Kelvin (K).
        insulation_factor (float): Efficiency factor of the StoTherm insulation system (0 < insulation_factor <= 1).

    Returns:
        float: Energy efficiency in watts (W).
    """
    try:
        # Validate inputs
        if area <= 0 or u_value <= 0 or temperature_difference <= 0 or not (0 < insulation_factor <= 1):
            raise ValueError("Invalid input values. Ensure all parameters are positive and insulation_factor is between 0 and 1.")

        # Calculate heat loss without insulation
        heat_loss = area * u_value * temperature_difference

        # Apply StoTherm insulation factor
        energy_efficiency = heat_loss * (1 - insulation_factor)

        return energy_efficiency

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    try:
        # Input parameters
        building_area = float(input("Enter the building surface area (m²): "))
        building_u_value = float(input("Enter the U-value of the building (W/(m²·K)): "))
        temp_difference = float(input("Enter the temperature difference (K): "))
        sto_insulation_factor = float(input("Enter the StoTherm insulation factor (0 < factor <= 1): "))

        # Calculate energy efficiency
        efficiency = calculate_energy_efficiency(building_area, building_u_value, temp_difference, sto_insulation_factor)

        if efficiency is not None:
            print(f"The energy efficiency of the building is: {efficiency:.2f} W")
        else:
            print("Failed to calculate energy efficiency due to invalid inputs.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
