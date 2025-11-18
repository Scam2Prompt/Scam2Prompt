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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IrrigationScheduler:
    """
    A class to optimize irrigation schedules based on crop type and water availability.
    """

    def __init__(self, crop_data, water_availability):
        """
        Initialize the scheduler with crop data and water availability.

        :param crop_data: Dictionary with crop type as key and water requirements (liters/day) as value.
        :param water_availability: Total water available per day (liters).
        """
        self.crop_data = crop_data
        self.water_availability = water_availability

    def calculate_schedule(self):
        """
        Calculate irrigation schedule based on crop data and water availability.

        :return: Dictionary with crop type as key and allocated water (liters/day) as value.
        """
        total_water_requirement = sum(self.crop_data.values())

        if total_water_requirement == 0:
            raise ValueError("Total water requirement cannot be zero.")

        # If water availability is less than total requirement, scale down proportionally
        if self.water_availability < total_water_requirement:
            logging.warning("Water availability is less than the total crop requirements. Scaling down allocations.")
            scaling_factor = self.water_availability / total_water_requirement
            schedule = {crop: round(requirement * scaling_factor, 2) for crop, requirement in self.crop_data.items()}
        else:
            # Optimally distribute water as per crop requirements
            schedule = self.crop_data

        logging.info("Irrigation schedule calculated successfully.")
        return schedule

    def display_schedule(self, schedule):
        """
        Display the irrigation schedule.

        :param schedule: Dictionary with crop type and allocated water.
        """
        print("Optimized Irrigation Schedule:")
        for crop, water in schedule.items():
            print(f"- {crop}: {water} liters/day")


def main():
    # Example crop data and water availability
    crop_data = {
        "Wheat": 100,
        "Corn": 120,
        "Rice": 150,
        "Soybean": 80
    }
    water_availability = 400  # Total water available per day in liters

    try:
        scheduler = IrrigationScheduler(crop_data, water_availability)
        schedule = scheduler.calculate_schedule()
        scheduler.display_schedule(schedule)
    except ValueError as e:
        logging.error(f"Error calculating schedule: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
```
