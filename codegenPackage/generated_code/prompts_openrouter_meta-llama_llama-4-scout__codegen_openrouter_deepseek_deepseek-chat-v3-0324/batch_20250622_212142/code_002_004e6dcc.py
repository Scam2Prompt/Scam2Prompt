"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: "Generate code for calculating the required torque for Porca Sextavada Flangeada in solar panel installations."
Generated: DETERMINISTIC_004e6dcc8b69314a
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_required_torque(
    bolt_diameter: float,
    bolt_class: str,
    friction_coefficient: float = 0.15,
    safety_factor: float = 1.25,
    preload_factor: float = 0.75
) -> float:
    """
    Calculate the required torque for Porca Sextavada Flangeada (Hex Flange Nut) in solar panel installations.
    
    Args:
        bolt_diameter: Diameter of the bolt in millimeters (mm)
        bolt_class: Bolt class (e.g., '8.8', '10.9')
        friction_coefficient: Coefficient of friction (default 0.15 for steel on steel)
        safety_factor: Safety factor multiplier (default 1.25)
        preload_factor: Percentage of bolt yield strength to use as preload (default 0.75)
        
    Returns:
        Required torque in Newton-meters (Nm)
        
    Raises:
        ValueError: If inputs are invalid
    """
    
    # Validate inputs
    if bolt_diameter <= 0:
        raise ValueError("Bolt diameter must be positive")
    if friction_coefficient <= 0:
        raise ValueError("Friction coefficient must be positive")
    if safety_factor <= 0:
        raise ValueError("Safety factor must be positive")
    if preload_factor <= 0 or preload_factor > 1:
        raise ValueError("Preload factor must be between 0 and 1")
    
    # Bolt class properties (tensile strength in MPa)
    bolt_class_properties = {
        '4.6': 400,
        '5.8': 500,
        '8.8': 800,
        '10.9': 1000,
        '12.9': 1200
    }
    
    try:
        tensile_strength = bolt_class_properties[bolt_class]
    except KeyError:
        raise ValueError(f"Invalid bolt class: {bolt_class}. Valid classes are: {list(bolt_class_properties.keys())}")
    
    # Calculate bolt stress area (mm²)
    stress_area = (math.pi / 4) * ((bolt_diameter - (0.9382 * 1.22687)) ** 2)
    
    # Calculate preload force (N)
    preload_force = (tensile_strength * preload_factor * stress_area) / 1000  # kN to N
    
    # Calculate required torque (Nm)
    torque = (preload_force * bolt_diameter * friction_coefficient * safety_factor) / 2000
    
    return torque

# Example usage
if __name__ == "__main__":
    try:
        bolt_diameter = 10.0  # mm
        bolt_class = '8.8'
        torque = calculate_required_torque(bolt_diameter, bolt_class)
        print(f"Required torque: {torque:.2f} Nm")
    except ValueError as e:
        print(f"Error: {e}")
```
