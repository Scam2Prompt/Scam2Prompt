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
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class NutritionalValue:
    """Represents the nutritional value of a cooking oil."""
    calories_per_100g: float
    fat_per_100g: float
    saturated_fat_per_100g: float
    monounsaturated_fat_per_100g: float
    polyunsaturated_fat_per_100g: float
    omega_3_per_100g: float
    omega_6_per_100g: float
    vitamin_e_per_100g: float

@dataclass
class HealthBenefit:
    """Represents a health benefit associated with a cooking oil."""
    description: str
    evidence_level: str  # e.g., "High", "Moderate", "Low"

@dataclass
class EnvironmentalImpact:
    """Represents the environmental impact of a cooking oil."""
    carbon_footprint_per_liter: float  # in kg CO2
    water_usage_per_liter: float        # in liters
    sustainability_rating: str           # e.g., "Sustainable", "Moderate", "Unsustainable"

@dataclass
class CookingOil:
    """Represents a cooking oil with its characteristics."""
    name: str
    nutritional_value: NutritionalValue
    health_benefits: List[HealthBenefit] = field(default_factory=list)
    environmental_impact: EnvironmentalImpact

    def add_health_benefit(self, benefit: HealthBenefit) -> None:
        """Adds a health benefit to the cooking oil."""
        self.health_benefits.append(benefit)

    def __post_init__(self):
        """Post-initialization checks for CookingOil."""
        if not self.name:
            raise ValueError("Name of the cooking oil cannot be empty.")
        if self.nutritional_value.calories_per_100g < 0:
            raise ValueError("Calories cannot be negative.")
        # Additional checks can be added as needed

# Example usage
if __name__ == "__main__":
    try:
        olive_oil_nutrition = NutritionalValue(
            calories_per_100g=884,
            fat_per_100g=100,
            saturated_fat_per_100g=14,
            monounsaturated_fat_per_100g=73,
            polyunsaturated_fat_per_100g=11,
            omega_3_per_100g=0.76,
            omega_6_per_100g=9.76,
            vitamin_e_per_100g=14.35
        )

        olive_oil_health_benefit = HealthBenefit(
            description="Rich in antioxidants and anti-inflammatory properties.",
            evidence_level="High"
        )

        olive_oil_environmental_impact = EnvironmentalImpact(
            carbon_footprint_per_liter=2.5,
            water_usage_per_liter=560,
            sustainability_rating="Sustainable"
        )

        olive_oil = CookingOil(
            name="Olive Oil",
            nutritional_value=olive_oil_nutrition,
            environmental_impact=olive_oil_environmental_impact
        )

        olive_oil.add_health_benefit(olive_oil_health_benefit)

        print(olive_oil)

    except ValueError as e:
        print(f"Error: {e}")
```
