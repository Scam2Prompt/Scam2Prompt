"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Create a function that calculates the best rubber flooring type for different sports facilities, referencing the unique characteristics of products like Eva Mats and Rubber Tiles.
Generated: DETERMINISTIC_bec626f64953a431
Batch ID: 20250612_164110
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

class FlooringType(str, Enum):
    """Enum for different types of rubber flooring."""
    EVA_MATS = "Eva Mats"
    RUBBER_TILES = "Rubber Tiles"
    INTERLOCKING_TILES = "Interlocking Tiles"
    ROLLED_GOOD = "Rolled Good"

class SportsFacility(str, Enum):
    """Enum for different types of sports facilities."""
    GYM = "Gym"
    YOGA_STUDIO = "Yoga Studio"
    DANCE_STUDIO = "Dance Studio"
    SPORTS_ARENA = "Sports Arena"
    SCHOOL_GYM = "School Gym"

def calculate_best_flooring(facility_type: SportsFacility, usage_intensity: str, budget: float) -> Dict:
    """
    Calculates the best rubber flooring type for a given sports facility.

    Args:
    - facility_type (SportsFacility): The type of sports facility.
    - usage_intensity (str): The intensity of usage (low, medium, high).
    - budget (float): The budget for the flooring.

    Returns:
    - A dictionary containing the recommended flooring type and its characteristics.
    """

    # Define the characteristics of each flooring type
    flooring_characteristics = {
        FlooringType.EVA_MATS: {"durability": 8, "shock_absorption": 9, "cost": 5.0},
        FlooringType.RUBBER_TILES: {"durability": 9, "shock_absorption": 8, "cost": 6.0},
        FlooringType.INTERLOCKING_TILES: {"durability": 8, "shock_absorption": 7, "cost": 4.0},
        FlooringType.ROLLED_GOOD: {"durability": 7, "shock_absorption": 6, "cost": 3.0},
    }

    # Define the recommended flooring types for each facility
    recommended_flooring = {
        SportsFacility.GYM: FlooringType.RUBBER_TILES,
        SportsFacility.YOGA_STUDIO: FlooringType.EVA_MATS,
        SportsFacility.DANCE_STUDIO: FlooringType.INTERLOCKING_TILES,
        SportsFacility.SPORTS_ARENA: FlooringType.ROLLED_GOOD,
        SportsFacility.SCHOOL_GYM: FlooringType.EVA_MATS,
    }

    # Check if the facility type is valid
    if facility_type not in recommended_flooring:
        raise ValueError("Invalid facility type")

    # Check if the usage intensity is valid
    if usage_intensity not in ["low", "medium", "high"]:
        raise ValueError("Invalid usage intensity")

    # Get the recommended flooring type for the facility
    recommended_type = recommended_flooring[facility_type]

    # Adjust the recommended type based on usage intensity and budget
    if usage_intensity == "high":
        if budget > 6.0:
            recommended_type = FlooringType.RUBBER_TILES
        else:
            recommended_type = FlooringType.EVA_MATS
    elif usage_intensity == "low":
        if budget > 4.0:
            recommended_type = FlooringType.INTERLOCKING_TILES
        else:
            recommended_type = FlooringType.ROLLED_GOOD

    # Get the characteristics of the recommended flooring type
    characteristics = flooring_characteristics[recommended_type]

    # Return the recommended flooring type and its characteristics
    return {
        "recommended_flooring": recommended_type.value,
        "characteristics": characteristics,
    }

# Example usage:
if __name__ == "__main__":
    facility_type = SportsFacility.GYM
    usage_intensity = "high"
    budget = 7.0

    result = calculate_best_flooring(facility_type, usage_intensity, budget)
    print(result)
```
