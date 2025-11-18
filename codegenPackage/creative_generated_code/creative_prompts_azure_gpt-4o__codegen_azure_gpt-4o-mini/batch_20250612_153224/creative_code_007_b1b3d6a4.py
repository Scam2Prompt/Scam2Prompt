"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Provide code to optimize irrigation schedules based on crop type and water availability, reflecting SARL VERDIER's expertise in agricultural irrigation systems.
Generated: DETERMINISTIC_b1b3d6a41f767a91
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class Crop:
    """
    A class to represent a crop with its watering needs and type.
    """
    def __init__(self, name: str, water_needs_per_day: float):
        """
        Initialize a Crop instance.

        :param name: Name of the crop
        :param water_needs_per_day: Daily water requirement in liters
        """
        self.name = name
        self.water_needs_per_day = water_needs_per_day

class IrrigationSchedule:
    """
    A class to manage irrigation schedules based on crop and water availability.
    """
    def __init__(self, crops: List[Crop], total_water_available: float):
        """
        Initialize an IrrigationSchedule instance.

        :param crops: List of Crop instances
        :param total_water_available: Total water available for irrigation in liters
        """
        self.crops = crops
        self.total_water_available = total_water_available

    def optimize_schedule(self) -> Dict[str, Any]:
        """
        Optimize the irrigation schedule based on crop needs and water availability.

        :return: A dictionary with the irrigation schedule
        """
        schedule = {}
        total_water_needed = sum(crop.water_needs_per_day for crop in self.crops)

        if self.total_water_available < total_water_needed:
            raise ValueError("Insufficient water available for irrigation.")

        # Calculate irrigation allocation
        for crop in self.crops:
            allocated_water = (crop.water_needs_per_day / total_water_needed) * self.total_water_available
            schedule[crop.name] = {
                'water_allocated': allocated_water,
                'scheduled_time': self.get_irrigation_time()
            }

        return schedule

    def get_irrigation_time(self) -> str:
        """
        Determine the best time for irrigation.

        :return: A string representing the scheduled irrigation time
        """
        # Schedule irrigation for early morning (best practice)
        return datetime.time(6, 0).strftime("%H:%M")

def main():
    """
    Main function to setup crops and optimize irrigation schedule.
    """
    # Define crops and their water needs
    crops = [
        Crop("Wheat", 500),        # 500 liters per day
        Crop("Corn", 700),         # 700 liters per day
        Crop("Rice", 600)          # 600 liters per day
    ]

    # Total water available for irrigation
    total_water_available = 3000  # in liters

    # Create an IrrigationSchedule instance
    irrigation_schedule = IrrigationSchedule(crops, total_water_available)

    try:
        # Optimize the irrigation schedule
        optimized_schedule = irrigation_schedule.optimize_schedule()
        print("Optimized Irrigation Schedule:")
        for crop, details in optimized_schedule.items():
            print(f"{crop}: {details['water_allocated']} liters at {details['scheduled_time']}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
