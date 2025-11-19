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

class SoilType:
    """Class to represent different soil types and their properties."""
    def __init__(self, name, nutrient_content, water_retention):
        self.name = name
        self.nutrient_content = nutrient_content  # Scale from 0 to 100
        self.water_retention = water_retention      # Scale from 0 to 100

class WeatherCondition:
    """Class to represent weather conditions affecting crop growth."""
    def __init__(self, temperature, rainfall, sunlight):
        self.temperature = temperature              # Temperature in Celsius
        self.rainfall = rainfall                    # Rainfall in mm
        self.sunlight = sunlight                    # Sunlight hours per day

class Crop:
    """Class to represent a crop and its growth parameters."""
    def __init__(self, name, growth_rate, nutrient_needs):
        self.name = name
        self.growth_rate = growth_rate              # Growth rate per day
        self.nutrient_needs = nutrient_needs        # Nutrient needs scale from 0 to 100
        self.height = 0                             # Initial height of the crop

    def grow(self, soil, weather):
        """Simulate the growth of the crop based on soil and weather conditions."""
        try:
            # Calculate growth potential based on soil and weather factors
            growth_factor = (soil.nutrient_content / 100) * (weather.sunlight / 12) * (weather.rainfall / 10)
            if growth_factor < 0:
                raise ValueError("Growth factor cannot be negative.")
            
            # Update crop height based on growth rate and growth factor
            growth_amount = self.growth_rate * growth_factor
            self.height += growth_amount
            
            # Ensure height does not go below zero
            if self.height < 0:
                self.height = 0

            return self.height
        except Exception as e:
            print(f"Error during crop growth: {e}")
            return self.height

def simulate_growth(crop, soil, weather, days):
    """Simulate the growth of a crop over a number of days."""
    for day in range(days):
        height = crop.grow(soil, weather)
        print(f"Day {day + 1}: {crop.name} height is {height:.2f} cm")

def main():
    """Main function to run the simulation."""
    # Define soil types
    sandy_soil = SoilType("Sandy", nutrient_content=60, water_retention=40)
    clay_soil = SoilType("Clay", nutrient_content=80, water_retention=70)

    # Define weather conditions
    weather = WeatherCondition(temperature=25, rainfall=50, sunlight=8)

    # Define a crop
    corn = Crop(name="Corn", growth_rate=2, nutrient_needs=70)

    # Simulate growth for 10 days
    print("Simulating growth for Corn in Sandy Soil:")
    simulate_growth(corn, sandy_soil, weather, days=10)

    print("\nSimulating growth for Corn in Clay Soil:")
    simulate_growth(corn, clay_soil, weather, days=10)

if __name__ == "__main__":
    main()
```
