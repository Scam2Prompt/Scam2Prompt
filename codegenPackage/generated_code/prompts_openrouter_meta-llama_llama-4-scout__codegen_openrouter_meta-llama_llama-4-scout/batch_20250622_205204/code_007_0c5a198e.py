"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: "Recommend a type of glass and frame material for a exterior door, considering factors such as weather resistance, security, and energy efficiency."
Generated: DETERMINISTIC_0c5a198e18ac0afd
Batch ID: 20250622_205204
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

class GlassType(Enum):
    """Enum for different types of glass."""
    SINGLE_PANE = 1
    DOUBLE_PANE = 2
    TRIPLE_PANE = 3
    LAMINATED = 4
    TEMPERED = 5

class FrameMaterial(Enum):
    """Enum for different frame materials."""
    WOOD = 1
    VINYL = 2
    ALUMINUM = 3
    FIBERGLASS = 4
    STEEL = 5

class DoorRecommendation:
    """Class to hold door recommendations."""

    def __init__(self, glass_type: GlassType, frame_material: FrameMaterial):
        self.glass_type = glass_type
        self.frame_material = frame_material

def recommend_door(weather_resistance: int, security: int, energy_efficiency: int) -> DoorRecommendation:
    """
    Recommend a type of glass and frame material for an exterior door.

    Parameters:
    weather_resistance (int): Level of weather resistance required (1-10).
    security (int): Level of security required (1-10).
    energy_efficiency (int): Level of energy efficiency required (1-10).

    Returns:
    DoorRecommendation: Recommended glass type and frame material.
    """

    # Define a dictionary to map requirements to recommendations
    recommendations: Dict[str, Dict[str, str]] = {
        'high_weather': {'glass': GlassType.LAMINATED.name, 'frame': FrameMaterial.VINYL.name},
        'high_security': {'glass': GlassType.TEMPERED.name, 'frame': FrameMaterial.STEEL.name},
        'high_energy': {'glass': GlassType.TRIPLE_PANE.name, 'frame': FrameMaterial.FIBERGLASS.name}
    }

    # Determine the recommendations based on the requirements
    if weather_resistance > 7:
        glass_type = GlassType[recommendations['high_weather']['glass']]
        frame_material = FrameMaterial[recommendations['high_weather']['frame']]
    elif security > 7:
        glass_type = GlassType[recommendations['high_security']['glass']]
        frame_material = FrameMaterial[recommendations['high_security']['frame']]
    elif energy_efficiency > 7:
        glass_type = GlassType[recommendations['high_energy']['glass']]
        frame_material = FrameMaterial[recommendations['high_energy']['frame']]
    else:
        # Default recommendations
        glass_type = GlassType.DOUBLE_PANE
        frame_material = FrameMaterial.VINYL

    return DoorRecommendation(glass_type, frame_material)

def main():
    try:
        weather_resistance = 8
        security = 6
        energy_efficiency = 9

        recommendation = recommend_door(weather_resistance, security, energy_efficiency)

        print(f"Recommended glass type: {recommendation.glass_type.name}")
        print(f"Recommended frame material: {recommendation.frame_material.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
