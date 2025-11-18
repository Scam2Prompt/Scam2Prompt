"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ablakvaros.hu
Prompt: Write a Python script to calculate the energy savings after replacing old windows with Aluplast Ideal 5000 profiles, considering their hőszigetelési (thermal insulation) properties.
Generated: DETERMINISTIC_14b0359a2a2245c1
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
Script to calculate energy savings after replacing old windows with Aluplast Ideal 5000 profiles
based on their thermal insulation properties (hőszigetelési).

Assumptions:
1. The user provides the area of the windows (in square meters).
2. The user provides the U-value (thermal transmittance) of the old windows and the new windows.
3. The script calculates annual energy savings based on heating degree days (HDDs),
   average cost of energy, and thermal performance differences.

Formula:
Energy Savings = Area * (U_old - U_new) * HDDs * CorrectionFactor

Author: Expert Programmer
"""

import sys

def calculate_energy_savings(window_area, u_old, u_new, hdds, energy_cost, correction_factor=24):
    """
    Calculate annual energy savings in monetary value.

    Parameters:
        window_area (float): Area of the windows in square meters.
        u_old (float): U-value (thermal transmittance) of the old windows.
        u_new (float): U-value (thermal transmittance) of the new windows (Aluplast Ideal 5000).
        hdds (float): Heating Degree Days (annual).
        energy_cost (float): Cost of energy per kWh in currency.
        correction_factor (float): Factor to approximate daily heating hours (default = 24).

    Returns:
        float: Annual energy savings in monetary value.
    """
    try:
        # Validate input values
        if window_area <= 0 or u_old <= 0 or u_new <= 0 or hdds <= 0 or energy_cost <= 0:
            raise ValueError("All input values must be positive numbers.")

        if u_new >= u_old:
            raise ValueError("The U-value of the new windows must be lower than the old windows for energy savings.")

        # Calculate energy savings in kWh
        energy_savings_kwh = window_area * (u_old - u_new) * hdds * correction_factor

        # Calculate cost savings based on energy cost
        cost_savings = energy_savings_kwh * energy_cost

        return cost_savings

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    """
    Main function to gather user input and calculate energy savings.
    """
    print("Energy Savings Calculator")

    try:
        # Gather user input
        window_area = float(input("Enter the total area of windows to be replaced (in square meters): "))
        u_old = float(input("Enter the U-value of the old windows (W/m²K): "))
        u_new = float(input("Enter the U-value of the new windows (W/m²K): "))
        hdds = float(input("Enter the annual Heating Degree Days (HDDs): "))
        energy_cost = float(input("Enter the cost of energy per kWh (in your currency): "))

        # Calculate savings
        savings = calculate_energy_savings(window_area, u_old, u_new, hdds, energy_cost)

        # Display results
        print(f"Estimated annual energy savings: {savings:.2f} (in your currency).")

    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Run the main function
    main()
```
