"""
Generated Code Metadata:
========================
Original URL: https://engenhariawpj.com
Prompt: "Develop a simple calculator to determine the required thickness of StoTherm insulation for a specific building envelope."
Generated: DETERMINISTIC_b5dcf62ef347c199
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

def calculate_stotherm_thickness(outside_temperature, inside_temperature, 
                                  desired_inside_surface_temperature, 
                                  stotherm_conductivity=0.033, 
                                  stotherm_density=80):
    """
    Calculates the required thickness of StoTherm insulation.

    Args:
    - outside_temperature (float): The outside temperature in °C.
    - inside_temperature (float): The inside temperature in °C.
    - desired_inside_surface_temperature (float): The desired inside surface temperature in °C.
    - stotherm_conductivity (float, optional): The thermal conductivity of StoTherm in W/m·K. Defaults to 0.033.
    - stotherm_density (float, optional): The density of StoTherm in kg/m³. Defaults to 80.

    Returns:
    - float: The required thickness of StoTherm insulation in meters.
    """

    # Temperature difference between inside and outside
    temperature_difference = inside_temperature - outside_temperature
    
    # Temperature difference between inside surface and inside air
    inside_surface_temperature_difference = inside_temperature - desired_inside_surface_temperature

    # Heat flux through the insulation
    heat_flux = temperature_difference / (1 / stotherm_conductivity)

    # Required R-value (thermal resistance)
    required_r_value = inside_surface_temperature_difference / heat_flux

    # Calculate required thickness
    required_thickness = required_r_value * stotherm_conductivity

    return required_thickness


def main():
    try:
        outside_temperature = float(input("Enter the outside temperature in °C: "))
        inside_temperature = float(input("Enter the inside temperature in °C: "))
        desired_inside_surface_temperature = float(input("Enter the desired inside surface temperature in °C: "))

        required_thickness = calculate_stotherm_thickness(outside_temperature, inside_temperature, 
                                                         desired_inside_surface_temperature)

        print(f"The required thickness of StoTherm insulation is: {required_thickness:.2f} m or {(required_thickness * 1000):.2f} mm")

    except ValueError:
        print("Invalid input. Please enter a valid temperature value.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
