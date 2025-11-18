"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.marodconsultores.com.pe
Prompt: Write code to automate the calculation of lighting levels in industrial plants, following the measurement practices described by MAROD Consultores SAC.
Generated: DETERMINISTIC_38a91f844b120a64
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Constants based on MAROD Consultores SAC measurement practices
# These values should be adjusted based on specific measurement guidelines provided
LUMEN_CONSTANT = 683  # Luminous efficacy in lumens per watt for monochromatic light
STANDARD_REFLECTANCE = 0.85  # Reflectance of industrial surfaces (approximation)
DEFAULT_ROOM_INDEX = 0.8  # Room index (depends on room dimensions)

# Function to calculate lighting levels
def calculate_lighting_levels(power: float, luminous_efficacy: float, area: float, reflectance: float = STANDARD_REFLECTANCE) -> float:
    """
    Calculate the illuminance (lighting level) in lux for an industrial plant.

    Args:
        power (float): Power of the lighting source in watts.
        luminous_efficacy (float): Efficiency of the light source in lumens per watt.
        area (float): Surface area to be illuminated in square meters.
        reflectance (float): Reflectance of the walls/ceiling/floor in the industrial plant (default: 0.85).

    Returns:
        float: Calculated illuminance in lux.

    Raises:
        ValueError: If power, luminous efficacy, or area are non-positive numbers.
    """
    if power <= 0 or luminous_efficacy <= 0 or area <= 0:
        raise ValueError("Power, luminous efficacy, and area must be positive values.")

    # Calculate total lumens emitted by the light source
    total_lumens = power * luminous_efficacy

    # Adjust luminous output based on surface reflectance
    effective_lumens = total_lumens * reflectance

    # Calculate illuminance in lux (lumens per square meter)
    illuminance = effective_lumens / area

    return illuminance

def calculate_room_index(length: float, width: float, height: float) -> float:
    """
    Calculate the room index, which is used to assess lighting uniformity.

    Args:
        length (float): Length of the room in meters.
        width (float): Width of the room in meters.
        height (float): Mounting height of the light source in meters.

    Returns:
        float: Room index (dimensionless).

    Raises:
        ValueError: If length, width, or height are non-positive numbers.
    """
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("Length, width, and height must be positive values.")

    # Room index calculation formula
    room_index = (length * width) / (height * (length + width))
    return room_index

# Main function to process lighting levels
def main():
    """
    Main function to automate the calculation of lighting levels in industrial plants.
    """
    try:
        # Example input values (replace with actual values or user input)
        power = 50.0  # Power in watts
        luminous_efficacy = LUMEN_CONSTANT  # Lumens per watt
        area = 100.0  # Surface area in square meters
        reflectance = STANDARD_REFLECTANCE  # Reflectance of surfaces
        
        # Room dimensions for room index calculation
        length = 10.0  # Length in meters
        width = 10.0  # Width in meters
        height = 3.0  # Mounting height in meters
        
        # Calculate lighting levels
        lighting_levels = calculate_lighting_levels(power, luminous_efficacy, area, reflectance)
        print(f"Illuminance (Lighting Level): {lighting_levels:.2f} lux")
        
        # Calculate room index
        room_index = calculate_room_index(length, width, height)
        print(f"Room Index: {room_index:.2f}")
        
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
