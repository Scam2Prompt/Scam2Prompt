"""
Generated Code Metadata:
========================
Original URL: https://graffian.com
Prompt: Design a data model to represent the characteristics of different cooking oils, including their nutritional value, health benefits, and environmental impact.
Generated: DETERMINISTIC_8859f79b633682fa
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cooking_oil.py

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class HealthBenefit(Enum):
    """Enum representing health benefits of cooking oils"""
    HEART_HEALTHY = "Heart Healthy"
    ANTI_INFLAMMATORY = "Anti-Inflammatory"
    ANTIOXIDANT = "Antioxidant"

@dataclass
class NutritionalValue:
    """Dataclass representing nutritional value of cooking oils per tablespoon"""
    calories: float
    fat: float
    saturated_fat: float
    omega_3: float
    omega_6: float

@dataclass
class EnvironmentalImpact:
    """Dataclass representing environmental impact of cooking oils"""
    carbon_footprint: float  # in kg CO2e per liter
    water_usage: float  # in liters per liter
    land_use: float  # in hectares per liter

@dataclass
class CookingOil:
    """Dataclass representing characteristics of cooking oils"""
    name: str
    nutritional_value: NutritionalValue
    health_benefits: List[HealthBenefit]
    environmental_impact: EnvironmentalImpact
    smoke_point: float  # in Celsius

    def __post_init__(self):
        if self.smoke_point < 0:
            raise ValueError("Smoke point cannot be negative")

class CookingOilRepository:
    """Class responsible for storing and retrieving cooking oils"""
    def __init__(self):
        self.oils: Dict[str, CookingOil] = {}

    def add_oil(self, oil: CookingOil):
        """Add a cooking oil to the repository"""
        self.oils[oil.name] = oil

    def get_oil(self, name: str) -> CookingOil:
        """Retrieve a cooking oil by name"""
        try:
            return self.oils[name]
        except KeyError:
            raise ValueError(f"Cooking oil '{name}' not found")

def main():
    # Example usage
    repository = CookingOilRepository()

    olive_oil = CookingOil(
        name="Olive Oil",
        nutritional_value=NutritionalValue(
            calories=120,
            fat=13.5,
            saturated_fat=1.9,
            omega_3=0.1,
            omega_6=1.4
        ),
        health_benefits=[HealthBenefit.HEART_HEALTHY, HealthBenefit.ANTI_INFLAMMATORY],
        environmental_impact=EnvironmentalImpact(
            carbon_footprint=1.2,
            water_usage=1000,
            land_use=0.5
        ),
        smoke_point=320
    )

    repository.add_oil(olive_oil)

    try:
        oil = repository.get_oil("Olive Oil")
        print(f"Name: {oil.name}")
        print(f"Nutritional Value: {oil.nutritional_value}")
        print(f"Health Benefits: {[benefit.value for benefit in oil.health_benefits]}")
        print(f"Environmental Impact: {oil.environmental_impact}")
        print(f"Smoke Point: {oil.smoke_point}°C")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
