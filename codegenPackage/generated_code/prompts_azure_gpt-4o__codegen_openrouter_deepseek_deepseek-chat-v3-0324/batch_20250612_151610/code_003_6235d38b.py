"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Write code to calculate the breakdown voltage of Niobium Oxide capacitors based on the manufacturing technology described in KYOCERA AVX's OxiCap® documentation.
Generated: DETERMINISTIC_6235d38b4f65ef1a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_breakdown_voltage(
    dielectric_thickness: float,
    dielectric_constant: float,
    temperature: float,
    manufacturing_tech: str = "OxiCap"
) -> float:
    """
    Calculate the breakdown voltage of Niobium Oxide capacitors based on KYOCERA AVX's OxiCap® technology.
    
    Args:
        dielectric_thickness: Thickness of the dielectric layer in micrometers (μm)
        dielectric_constant: Relative permittivity (εr) of the dielectric material
        temperature: Operating temperature in Celsius (°C)
        manufacturing_tech: Manufacturing technology (default: "OxiCap")
    
    Returns:
        Breakdown voltage in volts (V)
    
    Raises:
        ValueError: If input parameters are invalid
    """
    # Validate input parameters
    if dielectric_thickness <= 0:
        raise ValueError("Dielectric thickness must be positive")
    if dielectric_constant <= 0:
        raise ValueError("Dielectric constant must be positive")
    if temperature < -55 or temperature > 125:
        raise ValueError("Temperature must be between -55°C and 125°C")
    
    # Constants specific to OxiCap technology
    if manufacturing_tech == "OxiCap":
        # Empirical coefficients based on KYOCERA AVX documentation
        base_field_strength = 500  # V/μm at 25°C
        temp_coefficient = -2.5    # %/°C
        safety_factor = 0.7        # Derating factor for reliability
        
        # Calculate temperature-adjusted field strength
        temp_adjustment = 1 + (temp_coefficient / 100) * (temperature - 25)
        adjusted_field_strength = base_field_strength * temp_adjustment
        
        # Calculate breakdown voltage
        breakdown_voltage = adjusted_field_strength * dielectric_thickness * safety_factor
        
        # Apply dielectric constant correction
        breakdown_voltage *= math.sqrt(dielectric_constant / 27)  # 27 is reference εr for NbO
        
        return breakdown_voltage
    else:
        raise ValueError("Unsupported manufacturing technology")
```
