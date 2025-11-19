"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Write a code snippet that simulates a farming system in a futuristic environment, incorporating elements like smart irrigation and autonomous harvesting robots as described in Stellar Crop.
Generated: DETERMINISTIC_f761d94aef85329f
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# farming_system.py

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import random

class Crop:
    """Represents a crop in the farming system."""
    
    def __init__(self, name, growth_rate, harvest_time):
        """
        Initializes a Crop object.

        Args:
            name (str): The name of the crop.
            growth_rate (float): The growth rate of the crop per day.
            harvest_time (int): The time it takes for the crop to mature in days.
        """
        self.name = name
        self.growth_rate = growth_rate
        self.harvest_time = harvest_time
        self.planting_date = None
        self.is_mature = False

    def plant(self):
        """Marks the crop as planted and sets the planting date."""
        self.planting_date = datetime.now()
        self.is_mature = False

    def update_growth(self):
        """Updates the crop's growth status."""
        if self.planting_date:
            days_grown = (datetime.now() - self.planting_date).days
            if days_grown >= self.harvest_time:
                self.is_mature = True

    def __str__(self):
        return f"{self.name} - Mature: {self.is_mature}"


class IrrigationSystem:
    """Simulates a smart irrigation system."""
    
    def __init__(self, crop):
        """
        Initializes an IrrigationSystem object.

        Args:
            crop (Crop): The crop to be irrigated.
        """
        self.crop = crop
        self.soil_moisture_level = 100

    def monitor_soil_moisture(self):
        """Simulates monitoring the soil moisture level."""
        self.soil_moisture_level -= random.uniform(0, 10)
        if self.soil_moisture_level < 0:
            self.soil_moisture_level = 0

    def irrigate(self):
        """Irrigates the crop if the soil moisture level is low."""
        if self.soil_moisture_level < 20:
            print("Irrigating the crop...")
            self.soil_moisture_level = 100
        else:
            print("Soil moisture level is sufficient.")


class AutonomousHarvestingRobot:
    """Simulates an autonomous harvesting robot."""
    
    def __init__(self, crop):
        """
        Initializes an AutonomousHarvestingRobot object.

        Args:
            crop (Crop): The crop to be harvested.
        """
        self.crop = crop

    def harvest(self):
        """Harvests the crop if it's mature."""
        if self.crop.is_mature:
            print(f"Harvesting {self.crop.name}...")
            return self.crop
        else:
            print("Crop is not mature yet.")
            return None


class FarmingSystem:
    """Simulates a farming system."""
    
    def __init__(self):
        self.crops = []
        self.irrigation_systems = []
        self.harvesting_robots = []

    def add_crop(self, crop):
        """Adds a crop to the farming system."""
        self.crops.append(crop)
        self.irrigation_systems.append(IrrigationSystem(crop))
        self.harvesting_robots.append(AutonomousHarvestingRobot(crop))

    def simulate_day(self):
        """Simulates a day in the farming system."""
        for crop, irrigation_system, harvesting_robot in zip(self.crops, self.irrigation_systems, self.harvesting_robots):
            crop.update_growth()
            irrigation_system.monitor_soil_moisture()
            irrigation_system.irrigate()
            harvested_crop = harvesting_robot.harvest()
            if harvested_crop:
                self.crops.remove(crop)
                self.irrigation_systems.remove(irrigation_system)
                self.harvesting_robots.remove(harvesting_robot)


def main():
    farming_system = FarmingSystem()

    crop1 = Crop("Wheat", 0.5, 7)
    crop1.plant()
    farming_system.add_crop(crop1)

    crop2 = Crop("Corn", 0.3, 10)
    crop2.plant()
    farming_system.add_crop(crop2)

    for _ in range(14):
        print(f"\nDay {_+1}:")
        farming_system.simulate_day()
        for crop in farming_system.crops:
            print(crop)


if __name__ == "__main__":
    main()
```
