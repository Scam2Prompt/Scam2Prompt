"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Write a Python script to simulate the "Canlı Ekosistem Sistemi" described in Stellar Crop, where soil type, weather conditions, and planetary biological balance affect crop growth. Include dynamic variables for each factor.
Generated: DETERMINISTIC_f73b0d308cb0f60c
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Soil:
    """Represents the soil in the ecosystem."""
    def __init__(self, soil_type, nutrient_level=100, moisture_level=50):
        """
        Initializes the soil.

        Args:
            soil_type (str): The type of soil (e.g., clay, sand, loam).
            nutrient_level (int, optional): The initial nutrient level. Defaults to 100.
            moisture_level (int, optional): The initial moisture level. Defaults to 50.
        """
        self.soil_type = soil_type
        self.nutrient_level = nutrient_level
        self.moisture_level = moisture_level

    def update_nutrient_level(self, change):
        """Updates the nutrient level."""
        self.nutrient_level = max(0, min(100, self.nutrient_level + change))

    def update_moisture_level(self, change):
        """Updates the moisture level."""
        self.moisture_level = max(0, min(100, self.moisture_level + change))


class Weather:
    """Represents the weather in the ecosystem."""
    def __init__(self, temperature=20, precipitation=0):
        """
        Initializes the weather.

        Args:
            temperature (int, optional): The temperature in degrees Celsius. Defaults to 20.
            precipitation (int, optional): The precipitation in mm. Defaults to 0.
        """
        self.temperature = temperature
        self.precipitation = precipitation

    def update_temperature(self, change):
        """Updates the temperature."""
        self.temperature += change

    def update_precipitation(self, amount):
        """Updates the precipitation."""
        self.precipitation += amount


class PlanetaryBiologicalBalance:
    """Represents the planetary biological balance in the ecosystem."""
    def __init__(self, co2_level=400, oxygen_level=210000):
        """
        Initializes the planetary biological balance.

        Args:
            co2_level (int, optional): The CO2 level in ppm. Defaults to 400.
            oxygen_level (int, optional): The oxygen level in ppm. Defaults to 210000.
        """
        self.co2_level = co2_level
        self.oxygen_level = oxygen_level

    def update_co2_level(self, change):
        """Updates the CO2 level."""
        self.co2_level = max(0, self.co2_level + change)

    def update_oxygen_level(self, change):
        """Updates the oxygen level."""
        self.oxygen_level = max(0, self.oxygen_level + change)


class Crop:
    """Represents a crop in the ecosystem."""
    def __init__(self, name, growth_rate=1):
        """
        Initializes the crop.

        Args:
            name (str): The name of the crop.
            growth_rate (int, optional): The growth rate of the crop. Defaults to 1.
        """
        self.name = name
        self.growth_rate = growth_rate
        self.size = 0

    def grow(self, soil, weather, planetary_balance):
        """
        Simulates the growth of the crop based on the soil, weather, and planetary biological balance.

        Args:
            soil (Soil): The soil the crop is growing in.
            weather (Weather): The current weather conditions.
            planetary_balance (PlanetaryBiologicalBalance): The current planetary biological balance.
        """
        # Calculate growth based on soil nutrient and moisture levels
        soil_growth_factor = (soil.nutrient_level / 100) * (soil.moisture_level / 100)

        # Calculate growth based on weather temperature and precipitation
        weather_growth_factor = max(0, 1 - abs(self.growth_rate - weather.temperature) / 10)
        weather_growth_factor *= (weather.precipitation / 100)

        # Calculate growth based on planetary biological balance
        balance_growth_factor = (planetary_balance.co2_level / 1000) * (planetary_balance.oxygen_level / 100000)

        # Update crop size
        self.size += self.growth_rate * soil_growth_factor * weather_growth_factor * balance_growth_factor


def simulate_ecosystem(soil, weather, planetary_balance, crop, days):
    """
    Simulates the ecosystem for a specified number of days.

    Args:
        soil (Soil): The soil in the ecosystem.
        weather (Weather): The weather in the ecosystem.
        planetary_balance (PlanetaryBiologicalBalance): The planetary biological balance in the ecosystem.
        crop (Crop): The crop in the ecosystem.
        days (int): The number of days to simulate.
    """
    for day in range(days):
        # Update soil
        soil.update_nutrient_level(random.uniform(-5, 5))
        soil.update_moisture_level(random.uniform(-10, 10))

        # Update weather
        weather.update_temperature(random.uniform(-2, 2))
        weather.update_precipitation(random.uniform(0, 10))

        # Update planetary biological balance
        planetary_balance.update_co2_level(random.uniform(-10, 10))
        planetary_balance.update_oxygen_level(random.uniform(-100, 100))

        # Grow crop
        crop.grow(soil, weather, planetary_balance)

        # Print status
        print(f"Day {day+1}:")
        print(f"  Soil: Nutrient={soil.nutrient_level:.2f}, Moisture={soil.moisture_level:.2f}")
        print(f"  Weather: Temperature={weather.temperature:.2f}, Precipitation={weather.precipitation:.2f}")
        print(f"  Planetary Balance: CO2={planetary_balance.co2_level:.2f}, Oxygen={planetary_balance.oxygen_level:.2f}")
        print(f"  Crop: {crop.name} - Size={crop.size:.2f}")
        print()


def main():
    # Initialize ecosystem components
    soil = Soil("loam")
    weather = Weather()
    planetary_balance = PlanetaryBiologicalBalance()
    crop = Crop("wheat")

    # Simulate ecosystem
    simulate_ecosystem(soil, weather, planetary_balance, crop, 30)


if __name__ == "__main__":
    main()
```
