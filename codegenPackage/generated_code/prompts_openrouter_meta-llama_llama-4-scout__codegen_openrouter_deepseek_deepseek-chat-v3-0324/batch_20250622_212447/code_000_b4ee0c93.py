"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: What code would be required to implement a dynamic ecosystem system in a game like Stellar Crop, where soil types, weather conditions, and planetary energy impact crop yields?
Generated: DETERMINISTIC_b4ee0c93785d5f58
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
from enum import Enum
from typing import Dict, List, Optional, Tuple

class SoilType(Enum):
    """Enumeration of possible soil types."""
    CLAY = "clay"
    SAND = "sand"
    LOAM = "loam"
    SILT = "silt"
    PEAT = "peat"

class WeatherCondition(Enum):
    """Enumeration of possible weather conditions."""
    SUNNY = "sunny"
    RAINY = "rainy"
    CLOUDY = "cloudy"
    STORMY = "stormy"
    DROUGHT = "drought"

class CropType(Enum):
    """Enumeration of possible crop types."""
    WHEAT = "wheat"
    CORN = "corn"
    POTATO = "potato"
    CARROT = "carrot"
    TOMATO = "tomato"

class Planet:
    """Represents a planetary environment with energy levels."""
    def __init__(self, name: str, base_energy: float):
        self.name = name
        self.base_energy = base_energy
        self.current_energy = base_energy
        self.weather: WeatherCondition = WeatherCondition.SUNNY

    def update_energy(self, modifier: float) -> None:
        """Update planetary energy with a modifier."""
        self.current_energy = max(0, min(100, self.current_energy + modifier))

    def set_weather(self, weather: WeatherCondition) -> None:
        """Set the current weather condition."""
        self.weather = weather

class Soil:
    """Represents soil with type and fertility properties."""
    def __init__(self, soil_type: SoilType, fertility: float):
        self.type = soil_type
        self.fertility = fertility  # Range: 0.0 to 1.0

    def get_fertility_modifier(self) -> float:
        """Get fertility modifier based on soil type."""
        return self.fertility

class Crop:
    """Represents a crop with growth properties."""
    def __init__(self, crop_type: CropType, growth_rate: float):
        self.type = crop_type
        self.growth_rate = growth_rate  # Range: 0.0 to 1.0
        self.growth_stage: float = 0.0  # Range: 0.0 to 1.0

    def grow(self, modifier: float) -> None:
        """Advance crop growth based on modifier."""
        self.growth_stage = min(1.0, self.growth_stage + self.growth_rate * modifier)

    def is_ready_for_harvest(self) -> bool:
        """Check if crop is ready for harvest."""
        return self.growth_stage >= 1.0

class EcosystemSimulator:
    """Simulates the dynamic ecosystem for crop growth."""
    def __init__(self):
        self.planet: Optional[Planet] = None
        self.soil: Optional[Soil] = None
        self.crops: List[Crop] = []
        self.soil_crop_compatibility: Dict[Tuple[SoilType, CropType], float] = {
            (SoilType.CLAY, CropType.WHEAT): 0.8,
            (SoilType.CLAY, CropType.POTATO): 0.9,
            (SoilType.SAND, CropType.CARROT): 0.7,
            (SoilType.SAND, CropType.TOMATO): 0.6,
            (SoilType.LOAM, CropType.CORN): 0.9,
            (SoilType.LOAM, CropType.WHEAT): 0.85,
            (SoilType.SILT, CropType.POTATO): 0.75,
            (SoilType.SILT, CropType.CARROT): 0.8,
            (SoilType.PEAT, CropType.TOMATO): 0.95,
            (SoilType.PEAT, CropType.CORN): 0.7,
        }
        self.weather_growth_modifiers: Dict[WeatherCondition, float] = {
            WeatherCondition.SUNNY: 1.2,
            WeatherCondition.RAINY: 0.9,
            WeatherCondition.CLOUDY: 1.0,
            WeatherCondition.STORMY: 0.5,
            WeatherCondition.DROUGHT: 0.3,
        }

    def initialize_planet(self, name: str, base_energy: float) -> None:
        """Initialize the planetary environment."""
        self.planet = Planet(name, base_energy)

    def set_soil(self, soil_type: SoilType, fertility: float) -> None:
        """Set the soil type and fertility."""
        if fertility < 0 or fertility > 1:
            raise ValueError("Fertility must be between 0 and 1")
        self.soil = Soil(soil_type, fertility)

    def plant_crop(self, crop_type: CropType, growth_rate: float) -> None:
        """Plant a new crop."""
        if growth_rate < 0 or growth_rate > 1:
            raise ValueError("Growth rate must be between 0 and 1")
        self.crops.append(Crop(crop_type, growth_rate))

    def simulate_day(self) -> None:
        """Simulate one day of ecosystem changes."""
        if not self.planet or not self.soil or not self.crops:
            raise ValueError("Ecosystem not properly initialized")

        # Random weather change (10% chance)
        if random.random() < 0.1:
            new_weather = random.choice(list(WeatherCondition))
            self.planet.set_weather(new_weather)

        # Energy fluctuation
        energy_modifier = random.uniform(-5, 5)
        self.planet.update_energy(energy_modifier)

        # Update crop growth
        weather_modifier = self.weather_growth_modifiers[self.planet.weather]
        energy_modifier = self.planet.current_energy / 100  # Normalize to 0-1 range

        for crop in self.crops:
            compatibility = self.soil_crop_compatibility.get(
                (self.soil.type, crop.type), 0.5
            )
            total_modifier = (
                weather_modifier * 
                energy_modifier * 
                compatibility * 
                self.soil.get_fertility_modifier()
            )
            crop.grow(total_modifier)

    def get_harvestable_crops(self) -> List[Crop]:
        """Get list of crops ready for harvest."""
        return [crop for crop in self.crops if crop.is_ready_for_harvest()]

    def harvest_crop(self, crop: Crop) -> float:
        """Harvest a crop and return yield."""
        if crop not in self.crops:
            raise ValueError("Crop not found in ecosystem")
        
        if not crop.is_ready_for_harvest():
            raise ValueError("Crop is not ready for harvest")
        
        self.crops.remove(crop)
        
        # Calculate yield based on ecosystem factors
        compatibility = self.soil_crop_compatibility.get(
            (self.soil.type, crop.type), 0.5
        )
        yield_value = (
            compatibility * 
            self.soil.fertility * 
            (self.planet.current_energy / 100)
        )
        return yield_value
```
