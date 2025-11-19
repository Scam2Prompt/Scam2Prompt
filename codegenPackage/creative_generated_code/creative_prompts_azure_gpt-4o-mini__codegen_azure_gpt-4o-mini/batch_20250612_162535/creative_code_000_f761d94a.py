"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Write a code snippet that simulates a farming system in a futuristic environment, incorporating elements like smart irrigation and autonomous harvesting robots as described in Stellar Crop.
Generated: DETERMINISTIC_f761d94aef85329f
Batch ID: 20250612_162535
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
from typing import List, Dict

class Crop:
    """Class representing a crop in the farming system."""
    def __init__(self, name: str, growth_time: int):
        """Initialize a crop with a name and growth time in hours."""
        self.name = name
        self.growth_time = growth_time  # Growth time in hours
        self.age = 0  # Current age in hours
        self.is_harvested = False

    def grow(self):
        """Simulate the growth of the crop by incrementing its age."""
        if not self.is_harvested:
            self.age += 1
            print(f"{self.name} has grown for {self.age} hour(s).")

    def is_ready_for_harvest(self) -> bool:
        """Check if the crop is ready for harvest."""
        return self.age >= self.growth_time

    def harvest(self):
        """Harvest the crop."""
        if self.is_ready_for_harvest():
            self.is_harvested = True
            print(f"{self.name} has been harvested.")
            return True
        return False


class SmartIrrigation:
    """Class representing a smart irrigation system."""
    def __init__(self):
        self.water_level = 100  # Water level in percentage

    def irrigate(self, crops: List[Crop]):
        """Irrigate crops based on their needs."""
        for crop in crops:
            if not crop.is_harvested:
                water_needed = random.randint(10, 30)  # Random water needed
                if self.water_level >= water_needed:
                    self.water_level -= water_needed
                    print(f"Irrigated {crop.name} with {water_needed}% water.")
                else:
                    print("Not enough water to irrigate crops.")

    def check_water_level(self):
        """Check the water level in the irrigation system."""
        if self.water_level < 20:
            print("Warning: Water level is low, consider refilling!")

    
class AutonomousHarvester:
    """Class representing an autonomous harvesting robot."""
    def __init__(self, crops: List[Crop]):
        self.crops = crops

    def harvest_crops(self):
        """Harvest all crops that are ready."""
        for crop in self.crops:
            if crop.is_ready_for_harvest() and not crop.is_harvested:
                crop.harvest()


def simulate_farming_system(crop_names: List[str], growth_times: List[int], simulation_hours: int):
    """Simulate the farming system over a specified duration."""
    # Initialize crops, irrigation, and harvester
    crops = [Crop(name, time) for name, time in zip(crop_names, growth_times)]
    irrigation_system = SmartIrrigation()
    harvester = AutonomousHarvester(crops)

    for hour in range(simulation_hours):
        print(f"\n--- Hour {hour + 1} ---")
        for crop in crops:
            crop.grow()
        
        irrigation_system.irrigate(crops)
        irrigation_system.check_water_level()
        
        harvester.harvest_crops()
        
        time.sleep(1)  # Simulate time passing


# Example usage
if __name__ == "__main__":
    try:
        crop_names = ["Wheat", "Corn", "Rice"]
        growth_times = [5, 3, 4]  # Growth time in hours
        simulation_hours = 10  # Total hours to simulate
        simulate_farming_system(crop_names, growth_times, simulation_hours)
    except Exception as e:
        print(f"An error occurred: {e}")
```
