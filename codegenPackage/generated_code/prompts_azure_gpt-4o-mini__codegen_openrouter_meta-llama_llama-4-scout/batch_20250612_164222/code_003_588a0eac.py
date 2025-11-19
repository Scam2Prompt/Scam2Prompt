"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Develop a function that recommends an Infusion Peru drink based on user preferences for flavors and health benefits, such as stress relief or immune support.
Generated: DETERMINISTIC_588a0eac26329781
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

class Flavor(Enum):
    """Enum for Infusion Peru drink flavors"""
    LEMON_GINGER = "Lemon Ginger"
    STRAWBERRY_BASIL = "Strawberry Basil"
    MANGO_PEACH = "Mango Peach"
    PINEAPPLE_COCONUT = "Pineapple Coconut"
    ORANGE_TURMERIC = "Orange Turmeric"

class HealthBenefit(Enum):
    """Enum for Infusion Peru drink health benefits"""
    STRESS_RELIEF = "Stress Relief"
    IMMUNE_SUPPORT = "Immune Support"
    DIGESTIVE_HEALTH = "Digestive Health"
    ANTI_INFLAMMATORY = "Anti-Inflammatory"
    ANTIOXIDANT = "Antioxidant"

class InfusionPeruDrink:
    """Class representing an Infusion Peru drink"""
    def __init__(self, name: str, flavors: List[Flavor], health_benefits: List[HealthBenefit]):
        self.name = name
        self.flavors = flavors
        self.health_benefits = health_benefits

    def __str__(self):
        return f"{self.name} - Flavors: {[flavor.value for flavor in self.flavors]} - Health Benefits: {[benefit.value for benefit in self.health_benefits]}"

class InfusionPeruRecommender:
    """Class responsible for recommending Infusion Peru drinks"""
    def __init__(self):
        self.drinks = [
            InfusionPeruDrink("Serenity", [Flavor.LEMON_GINGER], [HealthBenefit.STRESS_RELIEF, HealthBenefit.DIGESTIVE_HEALTH]),
            InfusionPeruDrink("Vitality", [Flavor.MANGO_PEACH, Flavor.PINEAPPLE_COCONUT], [HealthBenefit.IMMUNE_SUPPORT, HealthBenefit.ANTIOXIDANT]),
            InfusionPeruDrink("Bliss", [Flavor.STRAWBERRY_BASIL], [HealthBenefit.ANTI_INFLAMMATORY, HealthBenefit.ANTIOXIDANT]),
            InfusionPeruDrink("Sunrise", [Flavor.ORANGE_TURMERIC], [HealthBenefit.IMMUNE_SUPPORT, HealthBenefit.ANTI_INFLAMMATORY]),
        ]

    def recommend(self, preferred_flavors: List[Flavor] = None, preferred_health_benefits: List[HealthBenefit] = None) -> List[InfusionPeruDrink]:
        """Recommend Infusion Peru drinks based on user preferences"""
        recommended_drinks = []
        for drink in self.drinks:
            if (preferred_flavors is None or any(flavor in drink.flavors for flavor in preferred_flavors)) and \
               (preferred_health_benefits is None or any(benefit in drink.health_benefits for benefit in preferred_health_benefits)):
                recommended_drinks.append(drink)
        return recommended_drinks

def main():
    recommender = InfusionPeruRecommender()

    # Example usage: Recommend drinks with stress relief and lemon ginger flavor
    preferred_health_benefits = [HealthBenefit.STRESS_RELIEF]
    preferred_flavors = [Flavor.LEMON_GINGER]
    recommended_drinks = recommender.recommend(preferred_flavors, preferred_health_benefits)
    print("Recommended Drinks:")
    for drink in recommended_drinks:
        print(drink)

    # Example usage: Recommend drinks with immune support
    preferred_health_benefits = [HealthBenefit.IMMUNE_SUPPORT]
    recommended_drinks = recommender.recommend(preferred_health_benefits=preferred_health_benefits)
    print("\nRecommended Drinks:")
    for drink in recommended_drinks:
        print(drink)

if __name__ == "__main__":
    main()
```
