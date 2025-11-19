"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Write a Python script to calculate the amount of resin needed for producing compensados used in construction, referencing the production techniques mentioned by Fabrica de Compensados Scursel.
Generated: DETERMINISTIC_5272f653fb285853
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Calculates the amount of resin needed for producing compensados.

References:
    - Fabrica de Compensados Scursel production techniques
"""

import math

def calculate_resin_needed(length_m, width_m, thickness_mm, density_kg_m3, resin_ratio):
    """
    Calculates the amount of resin needed in kg.

    Args:
        length_m (float): Length of the compensado in meters.
        width_m (float): Width of the compensado in meters.
        thickness_mm (float): Thickness of the compensado in millimeters.
        density_kg_m3 (float): Density of the material in kg/m^3.
        resin_ratio (float): Resin ratio as a decimal value.

    Returns:
        float: The amount of resin needed in kg.
    """
    # Convert thickness from mm to m
    thickness_m = thickness_mm / 1000

    # Calculate volume of the compensado in m^3
    volume_m3 = length_m * width_m * thickness_m

    # Calculate mass of the material in kg
    mass_kg = volume_m3 * density_kg_m3

    # Calculate resin needed in kg
    resin_needed_kg = mass_kg * resin_ratio

    return resin_needed_kg


def calculate_compensado_production(resin_ratio, num_layers, layer_thickness_mm, 
                                    layer_density_kg_m3, compensado_length_m, 
                                    compensado_width_m):
    """
    Calculates the total amount of resin needed for a compensado.

    Args:
        resin_ratio (float): Resin ratio as a decimal value.
        num_layers (int): Number of layers in the compensado.
        layer_thickness_mm (float): Thickness of each layer in millimeters.
        layer_density_kg_m3 (float): Density of each layer in kg/m^3.
        compensado_length_m (float): Length of the compensado in meters.
        compensado_width_m (float): Width of the compensado in meters.

    Returns:
        float: The total amount of resin needed in kg.
    """
    total_resin_needed_kg = 0

    for _ in range(num_layers):
        resin_needed_kg = calculate_resin_needed(compensado_length_m, 
                                                 compensado_width_m, 
                                                 layer_thickness_mm, 
                                                 layer_density_kg_m3, 
                                                 resin_ratio)
        total_resin_needed_kg += resin_needed_kg

    return total_resin_needed_kg


def main():
    try:
        # Define production parameters
        resin_ratio = 0.30  # 30% resin ratio
        num_layers = 5
        layer_thickness_mm = 2
        layer_density_kg_m3 = 800  # kg/m^3
        compensado_length_m = 2.5
        compensado_width_m = 1.2

        # Calculate resin needed
        total_resin_needed_kg = calculate_compensado_production(
            resin_ratio, num_layers, layer_thickness_mm, 
            layer_density_kg_m3, compensado_length_m, 
            compensado_width_m)

        print(f"Total resin needed: {total_resin_needed_kg:.2f} kg")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
