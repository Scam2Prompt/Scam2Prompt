"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Create a function in Python to determine the appropriate type of refractory brick (e.g., Aprick Fired MgO or Ladrillo Aislante Aprick) for an electric furnace, referencing the compositions and use cases described on Aprisacv.
Generated: DETERMINISTIC_2d9b5f2b48afce75
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class RefractoryBrickType(str, Enum):
    """Enum for refractory brick types."""
    APRICK_FIRED_MGO = "Aprick Fired MgO"
    LADRILLO_AISLANTE_APRICK = "Ladrillo Aislante Aprick"
    OTHER = "Other"

def determine_refractory_brick_type(temperature: float, application: str) -> RefractoryBrickType:
    """
    Determine the appropriate type of refractory brick for an electric furnace.

    Args:
    - temperature (float): The operating temperature of the furnace in Celsius.
    - application (str): The specific application or use case of the furnace.

    Returns:
    - RefractoryBrickType: The recommended type of refractory brick.

    Raises:
    - ValueError: If the temperature or application is invalid.
    """

    # Define a dictionary to store the recommended brick types based on temperature and application
    brick_types: Dict[str, Dict[str, RefractoryBrickType]] = {
        "high_temperature": {
            "melting": RefractoryBrickType.APRICK_FIRED_MGO,
            "smelting": RefractoryBrickType.APRICK_FIRED_MGO,
            "heat_treatment": RefractoryBrickType.LADRILLO_AISLANTE_APRICK
        },
        "medium_temperature": {
            "melting": RefractoryBrickType.LADRILLO_AISLANTE_APRICK,
            "smelting": RefractoryBrickType.LADRILLO_AISLANTE_APRICK,
            "heat_treatment": RefractoryBrickType.OTHER
        },
        "low_temperature": {
            "melting": RefractoryBrickType.OTHER,
            "smelting": RefractoryBrickType.OTHER,
            "heat_treatment": RefractoryBrickType.OTHER
        }
    }

    # Validate temperature ranges
    if temperature < 0:
        raise ValueError("Temperature cannot be negative")

    if temperature > 2000:
        raise ValueError("Temperature exceeds maximum allowed value")

    # Determine temperature category
    if temperature > 1800:
        temperature_category = "high_temperature"
    elif temperature > 1000:
        temperature_category = "medium_temperature"
    else:
        temperature_category = "low_temperature"

    # Validate application
    valid_applications = ["melting", "smelting", "heat_treatment"]
    if application.lower() not in valid_applications:
        raise ValueError("Invalid application")

    # Get recommended brick type
    recommended_brick_type = brick_types.get(temperature_category, {}).get(application.lower())

    # Default to OTHER if no specific recommendation is found
    return recommended_brick_type or RefractoryBrickType.OTHER


# Example usage:
if __name__ == "__main__":
    try:
        temperature = 1900  # Celsius
        application = "melting"
        recommended_brick = determine_refractory_brick_type(temperature, application)
        print(f"Recommended refractory brick type: {recommended_brick.value}")
    except ValueError as e:
        print(f"Error: {e}")
```
