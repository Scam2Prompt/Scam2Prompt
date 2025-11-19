"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Write a Python script to simulate the impact of varying environmental conditions on crop growth, using data from a game like Stellar Crop, and suggest how this could be integrated into a larger game development project.
Generated: DETERMINISTIC_35a81b255214a2cf
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto

class WeatherCondition(Enum):
    SUNNY = auto()
    RAINY = auto()
    CLOUDY = auto()
    DROUGHT = auto()
    STORMY = auto()

class SoilQuality(Enum):
    POOR = auto()
    AVERAGE = auto()
    GOOD = auto()
    EXCELLENT = auto()

@dataclass
class Crop:
    name: str
    base_growth_rate: float
    optimal_temperature: tuple  # (min, max)
    water_requirement: float
    weather_preferences: List[WeatherCondition]
    soil_preference: SoilQuality

@dataclass
class Environment:
    temperature: float
    humidity: float
    weather: WeatherCondition
    soil_quality: SoilQuality
    days_passed: int = 0

class CropSimulator:
    def __init__(self):
        self.crops: Dict[str, Crop] = self._initialize_crops()
        self.environment = Environment(
            temperature=22.0,
            humidity=60.0,
            weather=WeatherCondition.SUNNY,
            soil_quality=SoilQuality.AVERAGE
        )

    def _initialize_crops(self) -> Dict[str, Crop]:
        """Initialize available crop types with their growth characteristics."""
        return {
            "wheat": Crop(
                name="wheat",
                base_growth_rate=1.0,
                optimal_temperature=(15, 25),
                water_requirement=0.7,
                weather_preferences=[WeatherCondition.SUNNY, WeatherCondition.CLOUDY],
                soil_preference=SoilQuality.GOOD
            ),
            "corn": Crop(
                name="corn",
                base_growth_rate=1.2,
                optimal_temperature=(20, 30),
                water_requirement=0.8,
                weather_preferences=[WeatherCondition.SUNNY],
                soil_preference=SoilQuality.EXCELLENT
            ),
            "potato": Crop(
                name="potato",
                base_growth_rate=0.9,
                optimal_temperature=(10, 20),
                water_requirement=0.6,
                weather_preferences=[WeatherCondition.CLOUDY, WeatherCondition.RAINY],
                soil_preference=SoilQuality.AVERAGE
            )
        }

    def _calculate_growth_modifier(self, crop: Crop) -> float:
        """Calculate growth modifier based on environmental conditions."""
        # Temperature effect
        temp_min, temp_max = crop.optimal_temperature
        temp_modifier = 1.0
        if self.environment.temperature < temp_min:
            temp_modifier -= (temp_min - self.environment.temperature) * 0.02
        elif self.environment.temperature > temp_max:
            temp_modifier -= (self.environment.temperature - temp_max) * 0.02

        # Weather effect
        weather_modifier = 1.0
        if self.environment.weather not in crop.weather_preferences:
            weather_modifier = 0.8

        # Soil effect
        soil_modifier = 1.0
        if crop.soil_preference.value > self.environment.soil_quality.value:
            soil_modifier = max(0.7, 1.0 - (crop.soil_preference.value - self.environment.soil_quality.value) * 0.1)

        # Water effect based on humidity and weather
        water_modifier = 1.0
        if self.environment.weather == WeatherCondition.DROUGHT:
            water_modifier = 0.5
        elif self.environment.weather == WeatherCondition.RAINY:
            water_modifier = min(1.2, water_modifier + 0.3)

        return crop.base_growth_rate * temp_modifier * weather_modifier * soil_modifier * water_modifier

    def simulate_day(self):
        """Simulate one day passing with random environmental changes."""
        # Random environmental changes
        self.environment.temperature += random.uniform(-2, 2)
        self.environment.humidity += random.uniform(-5, 5)
        
        # Change weather with some probability
        if random.random() < 0.2:
            self.environment.weather = random.choice(list(WeatherCondition))
        
        # Soil quality changes more slowly
        if random.random() < 0.05:
            self.environment.soil_quality = random.choice(list(SoilQuality))
        
        self.environment.days_passed += 1

    def simulate_growth(self, crop_name: str, days: int) -> float:
        """Simulate crop growth over a number of days."""
        if crop_name not in self.crops:
            raise ValueError(f"Unknown crop: {crop_name}")

        crop = self.crops[crop_name]
        total_growth = 0.0
        
        for _ in range(days):
            self.simulate_day()
            daily_growth = self._calculate_growth_modifier(crop)
            total_growth += daily_growth
        
        return total_growth

    def get_environment_report(self) -> str:
        """Generate a report of current environmental conditions."""
        return (
            f"Day: {self.environment.days_passed}\n"
            f"Temperature: {self.environment.temperature:.1f}°C\n"
            f"Humidity: {self.environment.humidity:.1f}%\n"
            f"Weather: {self.environment.weather.name.lower()}\n"
            f"Soil Quality: {self.environment.soil_quality.name.lower()}"
        )

# Example usage for integration into a game
if __name__ == "__main__":
    simulator = CropSimulator()
    
    # Simulate wheat growth for 30 days
    wheat_growth = simulator.simulate_growth("wheat", 30)
    print(f"Wheat growth after 30 days: {wheat_growth:.2f}")
    
    # Print current environment report
    print("\nCurrent Environment:")
    print(simulator.get_environment_report())
    
    # Example of how this could be integrated into a game:
    # - Store crop data in a database or config file
    # - Use the simulator as part of a farming system
    # - Visualize growth with progress bars or sprite changes
    # - Add player actions like watering, fertilizing, etc.
```
