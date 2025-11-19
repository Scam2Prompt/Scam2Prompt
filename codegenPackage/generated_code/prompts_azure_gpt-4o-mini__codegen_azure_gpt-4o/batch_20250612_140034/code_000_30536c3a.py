"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Write a Python script that performs numerical modeling of geotechnical tasks as described by the Geotechnical Center's services.
Generated: DETERMINISTIC_30536c3a3ae4ffce
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Geotechnical Numerical Modeling Script
This script performs numerical modeling for geotechnical tasks such as stress-strain analysis,
bearing capacity calculations, and slope stability analysis. It is designed to be modular,
well-documented, and production-ready.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
GRAVITY = 9.81  # Acceleration due to gravity (m/s^2)

# Error classes
class GeotechnicalError(Exception):
    """Custom exception for geotechnical modeling errors."""
    pass

# Functions
def calculate_stress(depth, unit_weight):
    """
    Calculate vertical stress at a given depth.
    
    Parameters:
        depth (float): Depth below the surface (m).
        unit_weight (float): Unit weight of the soil (kN/m^3).
    
    Returns:
        float: Vertical stress (kPa).
    """
    if depth < 0 or unit_weight <= 0:
        raise GeotechnicalError("Depth and unit weight must be positive values.")
    return depth * unit_weight

def bearing_capacity(c, phi, gamma, width):
    """
    Calculate the ultimate bearing capacity of a shallow foundation.
    
    Parameters:
        c (float): Cohesion of the soil (kPa).
        phi (float): Angle of internal friction (degrees).
        gamma (float): Unit weight of the soil (kN/m^3).
        width (float): Width of the foundation (m).
    
    Returns:
        float: Ultimate bearing capacity (kPa).
    """
    if c < 0 or phi < 0 or gamma <= 0 or width <= 0:
        raise GeotechnicalError("Invalid input values for bearing capacity calculation.")
    
    # Convert phi to radians
    phi_rad = np.radians(phi)
    
    # Terzaghi's bearing capacity factors
    Nq = np.exp(np.pi * np.tan(phi_rad)) * np.tan(np.radians(45 + phi / 2))**2
    Nc = (Nq - 1) / np.tan(phi_rad) if phi > 0 else 5.7  # Nc for phi = 0
    Ngamma = 2 * (Nq + 1) * np.tan(phi_rad)
    
    # Ultimate bearing capacity formula
    qu = c * Nc + gamma * width * Nq + 0.5 * gamma * width * Ngamma
    return qu

def slope_stability_factor_of_safety(c, phi, gamma, slope_angle):
    """
    Calculate the factor of safety for slope stability.
    
    Parameters:
        c (float): Cohesion of the soil (kPa).
        phi (float): Angle of internal friction (degrees).
        gamma (float): Unit weight of the soil (kN/m^3).
        slope_angle (float): Slope angle (degrees).
    
    Returns:
        float: Factor of safety.
    """
    if c < 0 or phi < 0 or gamma <= 0 or slope_angle <= 0:
        raise GeotechnicalError("Invalid input values for slope stability calculation.")
    
    # Convert angles to radians
    slope_angle_rad = np.radians(slope_angle)
    phi_rad = np.radians(phi)
    
    # Factor of safety formula (simplified)
    numerator = c + gamma * np.tan(phi_rad)
    denominator = gamma * np.tan(slope_angle_rad)
    if denominator == 0:
        raise GeotechnicalError("Slope angle results in division by zero.")
    
    return numerator / denominator

# Main function
def main():
    """
    Main function to perform geotechnical numerical modeling tasks.
    """
    try:
        # Example inputs
        depth = 10  # meters
        unit_weight = 18  # kN/m^3
        cohesion = 25  # kPa
        friction_angle = 30  # degrees
        foundation_width = 2  # meters
        slope_angle = 45  # degrees
        
        # Stress calculation
        stress = calculate_stress(depth, unit_weight)
        print(f"Vertical stress at {depth} m depth: {stress:.2f} kPa")
        
        # Bearing capacity calculation
        qu = bearing_capacity(cohesion, friction_angle, unit_weight, foundation_width)
        print(f"Ultimate bearing capacity: {qu:.2f} kPa")
        
        # Slope stability factor of safety
        fos = slope_stability_factor_of_safety(cohesion, friction_angle, unit_weight, slope_angle)
        print(f"Slope stability factor of safety: {fos:.2f}")
        
    except GeotechnicalError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
