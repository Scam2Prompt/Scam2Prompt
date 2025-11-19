"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Provide code to optimize irrigation schedules based on crop type and water availability, reflecting SARL VERDIER's expertise in agricultural irrigation systems.
Generated: DETERMINISTIC_b1b3d6a41f767a91
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Irrigation Schedule Optimizer

This module optimizes irrigation schedules based on crop type and water availability.

Classes:
    Crop
    IrrigationSystem

Functions:
    optimize_irrigation_schedule
"""

from enum import Enum
from typing import List, Dict

class CropType(str, Enum):
    """Enum for crop types."""
    CORN = "corn"
    SOYBEAN = "soybean"
    WHEAT = "wheat"

class Crop:
    """Represents a crop with its water requirements."""
    def __init__(self, name: str, crop_type: CropType, water_requirement: float):
        """
        Initializes a Crop object.

        Args:
        - name (str): The name of the crop.
        - crop_type (CropType): The type of the crop.
        - water_requirement (float): The water requirement of the crop in mm/day.
        """
        self.name = name
        self.crop_type = crop_type
        self.water_requirement = water_requirement

class IrrigationSystem:
    """Represents an irrigation system with its water availability."""
    def __init__(self, water_availability: float):
        """
        Initializes an IrrigationSystem object.

        Args:
        - water_availability (float): The available water for irrigation in mm/day.
        """
        self.water_availability = water_availability

def optimize_irrigation_schedule(crops: List[Crop], irrigation_system: IrrigationSystem) -> Dict[str, float]:
    """
    Optimizes the irrigation schedule based on crop type and water availability.

    Args:
    - crops (List[Crop]): A list of Crop objects.
    - irrigation_system (IrrigationSystem): An IrrigationSystem object.

    Returns:
    - A dictionary with crop names as keys and their optimized irrigation schedules as values.
    """
    # Sort crops by water requirement in descending order
    crops.sort(key=lambda crop: crop.water_requirement, reverse=True)

    # Initialize the optimized irrigation schedule
    optimized_schedule: Dict[str, float] = {}

    # Iterate over the crops
    for crop in crops:
        # Calculate the irrigation amount based on water availability and crop water requirement
        irrigation_amount = min(crop.water_requirement, irrigation_system.water_availability)
        optimized_schedule[crop.name] = irrigation_amount
        # Update the water availability
        irrigation_system.water_availability -= irrigation_amount

    return optimized_schedule

def main():
    try:
        # Create crops
        corn = Crop("Corn", CropType.CORN, 20.0)
        soybean = Crop("Soybean", CropType.SOYBEAN, 15.0)
        wheat = Crop("Wheat", CropType.WHEAT, 10.0)

        # Create irrigation system
        irrigation_system = IrrigationSystem(50.0)

        # Optimize irrigation schedule
        crops = [corn, soybean, wheat]
        optimized_schedule = optimize_irrigation_schedule(crops, irrigation_system)

        # Print the optimized irrigation schedule
        print("Optimized Irrigation Schedule:")
        for crop, irrigation_amount in optimized_schedule.items():
            print(f"{crop}: {irrigation_amount} mm/day")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
