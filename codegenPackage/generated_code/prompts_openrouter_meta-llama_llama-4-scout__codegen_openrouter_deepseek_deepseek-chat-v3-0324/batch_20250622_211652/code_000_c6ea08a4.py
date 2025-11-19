"""
Generated Code Metadata:
========================
Original URL: https://apps-eigenlayer.com
Prompt: "Generate a Python code snippet for calculating the tolerance for a custom engineered close tolerance component in precision metal stamping, considering factors like material type and desired precision."
Generated: DETERMINISTIC_c6ea08a488e01869
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Optional, Union

class MaterialType(Enum):
    """Enumeration of material types with their respective coefficients."""
    STEEL = 0.0005
    ALUMINUM = 0.0007
    COPPER = 0.0006
    BRASS = 0.00065
    STAINLESS_STEEL = 0.0004

class PrecisionLevel(Enum):
    """Enumeration of precision levels with their respective multipliers."""
    STANDARD = 1.0
    HIGH = 0.7
    ULTRA = 0.4

def calculate_tolerance(
    material: MaterialType,
    precision: PrecisionLevel,
    nominal_dimension: Union[int, float],
    temperature_variation: Optional[float] = None
) -> float:
    """
    Calculate the tolerance for a custom engineered close tolerance component.

    Args:
        material: MaterialType enum representing the material used.
        precision: PrecisionLevel enum representing the desired precision.
        nominal_dimension: Nominal dimension of the component (in mm).
        temperature_variation: Optional temperature variation (in °C). Defaults to None.

    Returns:
        float: Calculated tolerance (in mm).

    Raises:
        ValueError: If nominal_dimension is <= 0 or temperature_variation is provided and <= 0.
    """
    if nominal_dimension <= 0:
        raise ValueError("Nominal dimension must be greater than 0.")
    if temperature_variation is not None and temperature_variation <= 0:
        raise ValueError("Temperature variation must be greater than 0.")

    # Base tolerance calculation
    material_coefficient = material.value
    precision_multiplier = precision.value
    base_tolerance = material_coefficient * nominal_dimension * precision_multiplier

    # Adjust for temperature variation if provided
    if temperature_variation is not None:
        thermal_coefficient = 0.0000117  # Average thermal expansion coefficient for metals (mm/mm°C)
        thermal_effect = thermal_coefficient * temperature_variation * nominal_dimension
        base_tolerance += thermal_effect

    return round(base_tolerance, 4)

# Example usage
if __name__ == "__main__":
    try:
        tolerance = calculate_tolerance(
            material=MaterialType.STEEL,
            precision=PrecisionLevel.HIGH,
            nominal_dimension=50.0,
            temperature_variation=10.0
        )
        print(f"Calculated Tolerance: {tolerance} mm")
    except ValueError as e:
        print(f"Error: {e}")
```
