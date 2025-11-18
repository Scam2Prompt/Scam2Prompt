"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Write a Python script to calculate the energy savings from replacing old windows with Aluplast Ideal 3-layer windows, considering their hőszigetelési (thermal insulation) properties.
Generated: DETERMINISTIC_305362f4f8a6e031
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script: Energy Savings Calculator for Replacing Old Windows with Aluplast Ideal 3-layer Windows

This script calculates the energy savings achieved by replacing old windows with 
energy-efficient Aluplast Ideal 3-layer windows. The calculation is based on 
thermal insulation properties (hőszigetelési) and assumes constant heating costs 
and efficiency.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Importing necessary modules
import sys

def calculate_energy_savings(window_area, u_value_old, u_value_new, temperature_difference, heating_period_hours, energy_cost_per_kwh):
    """
    Calculate the energy savings based on thermal insulation properties.

    Parameters:
    - window_area (float): Total window area in square meters.
    - u_value_old (float): U-value (thermal transmittance) of old windows (W/m²K).
    - u_value_new (float): U-value (thermal transmittance) of new windows (W/m²K).
    - temperature_difference (float): Average temperature difference between inside and outside (K).
    - heating_period_hours (float): Total hours of heating during the year.
    - energy_cost_per_kwh (float): Cost of energy per kWh.

    Returns:
    - energy_saved_kwh (float): Total energy saved in kWh.
    - cost_saved (float): Total monetary savings.
    """
    try:
        # Calculate heat loss for old and new windows (Q = U * Area * ΔT)
        heat_loss_old = u_value_old * window_area * temperature_difference * heating_period_hours
        heat_loss_new = u_value_new * window_area * temperature_difference * heating_period_hours

        # Energy saved due to replacement (in Wh -> converted to kWh)
        energy_saved_kwh = (heat_loss_old - heat_loss_new) / 1000  # Convert Wh to kWh

        # Calculate monetary savings
        cost_saved = energy_saved_kwh * energy_cost_per_kwh

        return energy_saved_kwh, cost_saved
    except Exception as e:
        print(f"Error occurred during calculation: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function to execute the energy savings calculation.
    """
    print("Energy Savings Calculator for Replacing Windows")
    try:
        # Input parameters
        window_area = float(input("Enter the total window area (in m²): "))
        u_value_old = float(input("Enter the U-value of the old windows (in W/m²K): "))
        u_value_new = float(input("Enter the U-value of the new windows (in W/m²K): "))
        temperature_difference = float(input("Enter the average temperature difference (in K): "))
        heating_period_hours = float(input("Enter the total heating hours per year: "))
        energy_cost_per_kwh = float(input("Enter the cost of energy per kWh: "))

        # Perform calculation
        energy_saved_kwh, cost_saved = calculate_energy_savings(
            window_area, u_value_old, u_value_new, temperature_difference, heating_period_hours, energy_cost_per_kwh
        )

        # Display results
        print("\nResults:")
        print(f"Total energy saved: {energy_saved_kwh:.2f} kWh")
        print(f"Total monetary savings: ${cost_saved:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.", file=sys.stderr)
        sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    main()
```
