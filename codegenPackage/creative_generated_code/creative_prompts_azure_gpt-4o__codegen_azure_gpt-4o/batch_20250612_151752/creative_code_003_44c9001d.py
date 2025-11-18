"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundation.ru
Prompt: Provide a Python script for developing geotechnical models to assess the stability of foundations and structures, incorporating the principles of soil mechanics discussed on the Научно-образовательный центр «Геотехника» website.
Generated: DETERMINISTIC_44c9001d0b830009
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Geotechnical Model for Assessing Foundation and Structural Stability
Author: Expert Programmer
Date: YYYY-MM-DD

This Python script incorporates principles of soil mechanics to assess the stability
of foundations and structures. It uses key equations and concepts to calculate
bearing capacity, factor of safety, and settlement. Ensure inputs are accurate for
real-world applications. Error handling is included for robustness. 

Dependencies:
    - numpy (For numerical calculations)
    - matplotlib (For visualization)
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
GRAVITY = 9.81  # Acceleration due to gravity (m/s^2)

# Custom exceptions
class GeotechnicalError(Exception):
    """Custom exception for Geotechnical calculations."""
    pass


def calculate_bearing_capacity(c, phi, gamma, width):
    """
    Calculate the ultimate bearing capacity using Terzaghi's Bearing Capacity Equation.
    
    Parameters:
        c (float): Cohesion of the soil (kPa).
        phi (float): Angle of internal friction (degrees).
        gamma (float): Unit weight of the soil (kN/m^3).
        width (float): Width of the foundation (m).
    
    Returns:
        float: Ultimate bearing capacity (kPa).
    """
    try:
        # Convert phi to radians for calculation
        phi_rad = np.radians(phi)
        
        # Bearing capacity factors (simplified calculation)
        Nq = np.exp(np.pi * np.tan(phi_rad)) * np.tan(np.radians(45 + phi / 2))**2
        Nc = (Nq - 1) / np.tan(phi_rad) if phi > 0 else 5.14  # Handle phi=0 case
        Ngamma = 2 * (Nq + 1) * np.tan(phi_rad)
        
        # Terzaghi's Bearing Capacity Equation
        qult = c * Nc + gamma * width * Nq + 0.5 * gamma * width * Ngamma
        return qult
    except Exception as e:
        raise GeotechnicalError(f"Error in bearing capacity calculation: {str(e)}")


def calculate_settlement(load, Es, area, depth):
    """
    Calculate settlement using simplified elastic theory.
    
    Parameters:
        load (float): Applied load (kN).
        Es (float): Elastic modulus of the soil (kPa).
        area (float): Foundation area (m^2).
        depth (float): Depth of the foundation (m).
    
    Returns:
        float: Settlement (m).
    """
    try:
        stress = load / area
        settlement = (stress * depth) / Es
        return settlement
    except ZeroDivisionError:
        raise GeotechnicalError("Elastic modulus (Es) must be non-zero.")
    except Exception as e:
        raise GeotechnicalError(f"Error in settlement calculation: {str(e)}")


def factor_of_safety(qult, qallow):
    """
    Calculate the factor of safety for the foundation.

    Parameters:
        qult (float): Ultimate bearing capacity (kPa).
        qallow (float): Allowable bearing capacity (kPa).
    
    Returns:
        float: Factor of safety (dimensionless).
    """
    try:
        if qallow <= 0:
            raise GeotechnicalError("Allowable bearing capacity must be greater than zero.")
        return qult / qallow
    except Exception as e:
        raise GeotechnicalError(f"Error in factor of safety calculation: {str(e)}")


def plot_stability_analysis(depths, settlements):
    """
    Plot settlement vs foundation depth for visualization.

    Parameters:
        depths (list of float): Depth values (m).
        settlements (list of float): Settlement values (m).
    """
    try:
        plt.figure(figsize=(8, 6))
        plt.plot(depths, settlements, marker="o", label="Settlement Curve")
        plt.xlabel("Foundation Depth (m)")
        plt.ylabel("Settlement (m)")
        plt.title("Settlement vs Foundation Depth")
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        raise GeotechnicalError(f"Error in plotting settlement analysis: {str(e)}")


if __name__ == "__main__":
    # Example parameters
    c = 25  # Cohesion (kPa)
    phi = 30  # Angle of internal friction (degrees)
    gamma = 19  # Unit weight (kN/m^3)
    width = 2  # Foundation width (m)
    
    Es = 10000  # Elastic modulus (kPa)
    load = 500  # Applied load (kN)
    area = 4  # Foundation area (m^2)
    depths = np.linspace(1, 5, 5)  # Depths (m)
    
    try:
        # Calculate bearing capacity
        qult = calculate_bearing_capacity(c, phi, gamma, width)
        print(f"Ultimate Bearing Capacity: {qult:.2f} kPa")

        # Calculate settlement for different depths
        settlements = []
        for depth in depths:
            settlement = calculate_settlement(load, Es, area, depth)
            settlements.append(settlement)
            print(f"Settlement at depth {depth:.2f} m: {settlement:.4f} m")

        # Factor of safety (assume some allowable capacity)
        qallow = 250  # Allowable bearing capacity (kPa)
        fos = factor_of_safety(qult, qallow)
        print(f"Factor of Safety: {fos:.2f}")

        # Plot settlement vs depth
        plot_stability_analysis(depths, settlements)
    except GeotechnicalError as ge:
        print(f"Geotechnical Error: {ge}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
