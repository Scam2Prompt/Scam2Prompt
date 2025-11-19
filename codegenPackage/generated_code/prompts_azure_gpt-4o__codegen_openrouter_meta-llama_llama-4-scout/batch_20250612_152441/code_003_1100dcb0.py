"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: Create a function to compare the strength and durability of UPVC door systems with traditional wooden doors, incorporating the anti-fungi and anti-termite properties mentioned on the Dexodoor webpage.
Generated: DETERMINISTIC_1100dcb0462820e0
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass

class DoorMaterial(Enum):
    """Enum for door materials."""
    UPVC = "UPVC"
    WOODEN = "Wooden"

@dataclass
class DoorProperties:
    """Dataclass for door properties."""
    material: DoorMaterial
    strength: int  # out of 10
    durability: int  # out of 10
    anti_fungi: bool
    anti_termite: bool

def compare_door_systems(upvc_properties: DoorProperties, wooden_properties: DoorProperties) -> dict:
    """
    Compare the strength and durability of UPVC door systems with traditional wooden doors.

    Args:
    upvc_properties (DoorProperties): Properties of UPVC door.
    wooden_properties (DoorProperties): Properties of wooden door.

    Returns:
    dict: Comparison result.
    """
    try:
        # Validate input properties
        if not isinstance(upvc_properties, DoorProperties) or not isinstance(wooden_properties, DoorProperties):
            raise ValueError("Invalid door properties")

        # Calculate overall score for each door type
        upvc_score = upvc_properties.strength + upvc_properties.durability
        wooden_score = wooden_properties.strength + wooden_properties.durability

        # Add scores for anti-fungi and anti-termite properties
        if upvc_properties.anti_fungi:
            upvc_score += 1
        if upvc_properties.anti_termite:
            upvc_score += 1
        if wooden_properties.anti_fungi:
            wooden_score += 1
        if wooden_properties.anti_termite:
            wooden_score += 1

        # Compare scores and return result
        comparison_result = {
            "upvc": {
                "material": upvc_properties.material.value,
                "strength": upvc_properties.strength,
                "durability": upvc_properties.durability,
                "anti_fungi": upvc_properties.anti_fungi,
                "anti_termite": upvc_properties.anti_termite,
                "score": upvc_score
            },
            "wooden": {
                "material": wooden_properties.material.value,
                "strength": wooden_properties.strength,
                "durability": wooden_properties.durability,
                "anti_fungi": wooden_properties.anti_fungi,
                "anti_termite": wooden_properties.anti_termite,
                "score": wooden_score
            },
            "result": "UPVC" if upvc_score > wooden_score else "Wooden" if wooden_score > upvc_score else "Tie"
        }

        return comparison_result

    except Exception as e:
        # Handle any exceptions
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    upvc_properties = DoorProperties(
        material=DoorMaterial.UPVC,
        strength=8,
        durability=9,
        anti_fungi=True,
        anti_termite=True
    )

    wooden_properties = DoorProperties(
        material=DoorMaterial.WOODEN,
        strength=6,
        durability=7,
        anti_fungi=False,
        anti_termite=False
    )

    comparison_result = compare_door_systems(upvc_properties, wooden_properties)
    print(comparison_result)
```
