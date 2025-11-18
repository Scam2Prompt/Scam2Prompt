"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socompressoresebombas.com.br
Prompt: Generate code to calculate the efficiency of a compressed air network using PPR Azul tubing for air distribution, considering flow rate and pressure drop.
Generated: DETERMINISTIC_55cc43d50b3ba76c
Batch ID: 20250612_151519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_efficiency(flow_rate, pressure_drop, tubing_diameter, tubing_length):
    """
    Calculate the efficiency of a compressed air network using PPR Azul tubing.

    Parameters:
        flow_rate (float): The flow rate in cubic meters per hour (m³/h).
        pressure_drop (float): The pressure drop in bar.
        tubing_diameter (float): The internal diameter of the tubing in millimeters (mm).
        tubing_length (float): The length of the tubing in meters (m).

    Returns:
        float: Efficiency percentage of the compressed air network.
    """

    try:
        # Constants
        density_of_air = 1.225  # kg/m³ at standard conditions
        viscosity_of_air = 1.81e-5  # Pa·s at standard conditions

        # Convert tubing diameter to meters
        diameter_meters = tubing_diameter / 1000

        # Calculate cross-sectional area of the tubing
        cross_sectional_area = math.pi * (diameter_meters / 2) ** 2

        # Calculate velocity of air in tubing (m/s)
        velocity = flow_rate / (3600 * cross_sectional_area)

        # Calculate Reynolds number
        reynolds_number = (density_of_air * velocity * diameter_meters) / viscosity_of_air

        # Friction factor using empirical formula for turbulent flow in smooth pipes (Blasius equation)
        if reynolds_number > 4000:  # Turbulent flow
            friction_factor = 0.316 / (reynolds_number ** 0.25)
        elif reynolds_number > 2000:  # Transitional flow
            friction_factor = 0.079 / (reynolds_number ** 0.165)
        else:  # Laminar flow
            friction_factor = 64 / reynolds_number

        # Calculate pressure loss due to friction (Pa)
        pressure_loss = (
            friction_factor * (tubing_length / diameter_meters) * (density_of_air / 2) * velocity ** 2
        )

        # Convert pressure loss to bar
        pressure_loss_bar = pressure_loss / 100000

        # Calculate efficiency (percentage)
        efficiency = ((pressure_drop - pressure_loss_bar) / pressure_drop) * 100

        # Ensure efficiency is non-negative
        return max(0, efficiency)

    except ZeroDivisionError:
        raise ValueError("Tubing diameter and flow rate must be greater than zero.")
    except Exception as e:
        raise RuntimeError(f"An error occurred during calculation: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Sample input values
        flow_rate = 50.0          # m³/h
        pressure_drop = 0.5       # bar
        tubing_diameter = 32.0    # mm
        tubing_length = 10.0      # m

        # Calculate and display efficiency
        efficiency = calculate_efficiency(flow_rate, pressure_drop, tubing_diameter, tubing_length)
        print(f"Compressed Air Network Efficiency: {efficiency:.2f}%")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
```
