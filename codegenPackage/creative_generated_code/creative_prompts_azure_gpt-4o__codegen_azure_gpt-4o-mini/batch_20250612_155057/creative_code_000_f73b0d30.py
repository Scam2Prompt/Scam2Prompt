"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Write a Python script to simulate the "Canlı Ekosistem Sistemi" described in Stellar Crop, where soil type, weather conditions, and planetary biological balance affect crop growth. Include dynamic variables for each factor.
Generated: DETERMINISTIC_f73b0d308cb0f60c
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SoilType:
    """Enumeration of different soil types with their respective nutrient levels."""
    SANDY = {'nutrients': 3, 'water_retention': 2}
    LOAMY = {'nutrients': 5, 'water_retention': 5}
    CLAYEY = {'nutrients': 7, 'water_retention': 7}
    
    @staticmethod
    def get_soil_type(type_name):
        """Return soil properties based on the type name."""
        return {
            'sandy': SoilType.SANDY,
            'loamy': SoilType.LOAMY,
            'clayey': SoilType.CLAYEY
        }.get(type_name.lower(), SoilType.LOAMY)  # Default to loamy if unknown


class WeatherCondition:
    """Class representing weather conditions affecting growth."""
    def __init__(self):
        self.temperature = random.uniform(15.0, 35.0)  # Temperature in Celsius
        self.humidity = random.uniform(30.0, 100.0)  # Humidity in percentage

    def __str__(self):
        return f"Weather: {self.temperature:.2f}°C, {self.humidity:.2f}% Humidity"


class Plant:
    """Class to represent a crop plant with growth simulation based on environmental factors."""
    def __init__(self, name, soil_type):
        self.name = name
        self.soil_type = soil_type
        self.growth_stage = 0  # Growth stage from 0 (seed) to 5 (mature)
    
    def grow(self, weather):
        """Simulate the growth of the plant based on weather and soil conditions."""
        try:
            # Check growth conditions
            if weather.temperature < 10.0 or weather.temperature > 40.0:
                raise ValueError("Temperature is out of optimal growing range.")

            # Calculate growth potential
            growth_potential = (self.soil_type['nutrients'] + self.soil_type['water_retention']) * (weather.humidity / 100.0)
            
            # Update growth stage
            if growth_potential > 8:
                self.growth_stage += 1
            elif growth_potential > 5:
                self.growth_stage += 0.5
            
            if self.growth_stage > 5:
                self.growth_stage = 5  # Cap at mature growth
        except ValueError as e:
            print(f"Error during growth: {e}")

    def __str__(self):
        return f"{self.name}: Growth Stage {self.growth_stage:.1f}/5"


def simulate_ecosystem():
    """Simulate the ecosystem with dynamic soil, weather, and plant growth."""
    # Choose random soil type
    soil_type_name = random.choice(['sandy', 'loamy', 'clayey'])
    soil_type = SoilType.get_soil_type(soil_type_name)

    # Create a plant
    plant = Plant(name="Corn", soil_type=soil_type)
    print(f"Plant created: {plant}")
    
    # Simulate growth over 5 days
    for day in range(1, 6):
        print(f"\nDay {day}:")
        weather = WeatherCondition()
        print(weather)
        plant.grow(weather)
        print(plant)

if __name__ == "__main__":
    simulate_ecosystem()
```
