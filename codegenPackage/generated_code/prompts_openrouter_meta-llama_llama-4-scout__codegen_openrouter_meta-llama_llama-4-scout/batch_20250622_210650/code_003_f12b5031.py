"""
Generated Code Metadata:
========================
Original URL: https://histeknik.com
Prompt: "Generate a Python script to determine the optimal screw pile diameter and length for a given soil condition and structural load."
Generated: DETERMINISTIC_f12b50315f3bf63d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_soil_capacity(phi, cohesion, gamma, diameter):
    """
    Calculate the soil capacity based on the Mohr-Coulomb failure criterion.

    Args:
        phi (float): Angle of internal friction (degrees)
        cohesion (float): Soil cohesion (kPa)
        gamma (float): Soil unit weight (kN/m^3)
        diameter (float): Screw pile diameter (m)

    Returns:
        float: Soil capacity (kN)
    """
    phi_rad = math.radians(phi)
    soil_capacity = (cohesion * math.pi * diameter) + (0.5 * gamma * diameter**2 * math.tan(phi_rad))
    return soil_capacity

def calculate_structural_capacity(load, length, diameter, material_strength):
    """
    Calculate the structural capacity of the screw pile.

    Args:
        load (float): Structural load (kN)
        length (float): Screw pile length (m)
        diameter (float): Screw pile diameter (m)
        material_strength (float): Material strength (kPa)

    Returns:
        float: Structural capacity (kN)
    """
    structural_capacity = (math.pi * (diameter**2) / 4) * material_strength * (length / 1000)
    return structural_capacity

def determine_optimal_screw_pile(load, soil_phi, soil_cohesion, soil_gamma, material_strength):
    """
    Determine the optimal screw pile diameter and length.

    Args:
        load (float): Structural load (kN)
        soil_phi (float): Angle of internal friction (degrees)
        soil_cohesion (float): Soil cohesion (kPa)
        soil_gamma (float): Soil unit weight (kN/m^3)
        material_strength (float): Material strength (kPa)

    Returns:
        tuple: Optimal diameter (m) and length (m)
    """
    # Initial guess for diameter
    diameter = 0.1

    while True:
        soil_capacity = calculate_soil_capacity(soil_phi, soil_cohesion, soil_gamma, diameter)
        structural_capacity = calculate_structural_capacity(load, 10, diameter, material_strength)

        if soil_capacity > load and structural_capacity > load:
            return diameter, 10

        diameter += 0.01

def main():
    try:
        load = float(input("Enter the structural load (kN): "))
        soil_phi = float(input("Enter the angle of internal friction (degrees): "))
        soil_cohesion = float(input("Enter the soil cohesion (kPa): "))
        soil_gamma = float(input("Enter the soil unit weight (kN/m^3): "))
        material_strength = float(input("Enter the material strength (kPa): "))

        diameter, length = determine_optimal_screw_pile(load, soil_phi, soil_cohesion, soil_gamma, material_strength)

        print(f"Optimal screw pile diameter: {diameter:.2f} m")
        print(f"Optimal screw pile length: {length:.2f} m")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
```
