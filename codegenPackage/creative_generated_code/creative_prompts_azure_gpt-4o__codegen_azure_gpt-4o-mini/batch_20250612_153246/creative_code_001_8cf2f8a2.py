"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://citygardenmexico.com.mx
Prompt: Generate code to simulate an irrigation system design for a rooftop garden, incorporating features mentioned in City Garden México's services.
Generated: DETERMINISTIC_8cf2f8a24d33bd82
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from datetime import datetime, timedelta

class IrrigationSystem:
    """
    A class to simulate an automated irrigation system for a rooftop garden.
    """

    def __init__(self, garden_area_sq_m, soil_type, plant_types):
        """
        Initialize the irrigation system parameters.
        
        :param garden_area_sq_m: Area of the garden in square meters
        :param soil_type: Type of soil in the garden
        :param plant_types: List of plant types in the garden
        """
        self.garden_area_sq_m = garden_area_sq_m
        self.soil_type = soil_type
        self.plant_types = plant_types
        self.water_needed_per_sq_m = self.calculate_water_needs()
        self.last_irrigation_time = None

    def calculate_water_needs(self):
        """
        Calculate water needs based on soil type and plant types.
        
        :return: Total water needed in liters
        """
        # Define water needs for different soil types (in liters per sq m)
        soil_water_needs = {
            'sandy': 5,
            'clay': 10,
            'loamy': 7
        }

        # Calculate water needs based on soil type
        if self.soil_type in soil_water_needs:
            return soil_water_needs[self.soil_type] * self.garden_area_sq_m
        else:
            raise ValueError("Unsupported soil type")

    def irrigate(self):
        """
        Simulate the irrigation process, checking if irrigation is necessary.
        """
        # Current time
        current_time = datetime.now()

        # Check if irrigation is needed (every 6 hours)
        if self.last_irrigation_time is None or (current_time - self.last_irrigation_time) >= timedelta(hours=6):
            self.last_irrigation_time = current_time
            self.perform_irrigation()
        else:
            print("Irrigation not needed at this time.")

    def perform_irrigation(self):
        """
        Perform the irrigation by simulating water distribution.
        """
        print(f"Irrigating the garden area of {self.garden_area_sq_m} sq m...")
        print(f"Watering with {self.water_needed_per_sq_m} liters of water distributed evenly.")
        
        # Simulate watering process
        time.sleep(2)  # Simulate time taken for irrigation
        print("Irrigation complete.")

    def check_system_status(self):
        """
        Check the status of the irrigation system.
        
        :return: A status report of the irrigation system.
        """
        if self.last_irrigation_time:
            time_since_last_irrigation = datetime.now() - self.last_irrigation_time
            return f"Last irrigation was {time_since_last_irrigation.total_seconds() // 3600} hours ago."
        return "Irrigation system has not been used yet."


if __name__ == "__main__":
    try:
        # Create an instance of the irrigation system
        rooftop_garden = IrrigationSystem(garden_area_sq_m=100, soil_type='loamy', plant_types=['tomatoes', 'basil', 'pepper'])

        # Simulate the irrigation process
        rooftop_garden.irrigate()

        # Check the status of the irrigation system
        print(rooftop_garden.check_system_status())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
