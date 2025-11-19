"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Create a list of possible infusion mixes that combine ingredients like camu camu, maracuyá, and chicha, considering their potential health benefits and flavor profiles.
Generated: DETERMINISTIC_d19ae13606ce5dff
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Ingredient:
    name: str
    health_benefits: List[str]
    flavor_profile: str
    compatible_with: List[str]

@dataclass
class InfusionMix:
    ingredients: List[str]
    combined_health_benefits: List[str]
    flavor_profile: str
    compatibility_score: int

class InfusionMixGenerator:
    def __init__(self):
        self.ingredients = self._initialize_ingredients()
    
    def _initialize_ingredients(self) -> Dict[str, Ingredient]:
        """Initialize the base ingredients with their properties."""
        return {
            "camu camu": Ingredient(
                name="camu camu",
                health_benefits=["high vitamin C", "antioxidant", "immune support"],
                flavor_profile="tart",
                compatible_with=["maracuyá", "chicha", "ginger", "mint"]
            ),
            "maracuyá": Ingredient(
                name="maracuyá",
                health_benefits=["rich in fiber", "vitamin A", "calming effects"],
                flavor_profile="sweet-tart",
                compatible_with=["camu camu", "chicha", "honey", "lemongrass"]
            ),
            "chicha": Ingredient(
                name="chicha",
                health_benefits=["probiotics", "digestive health", "hydration"],
                flavor_profile="earthy-sweet",
                compatible_with=["camu camu", "maracuyá", "cinnamon", "berries"]
            ),
            "ginger": Ingredient(
                name="ginger",
                health_benefits=["anti-inflammatory", "digestive aid", "nausea relief"],
                flavor_profile="spicy",
                compatible_with=["camu camu", "lemongrass", "honey"]
            ),
            "mint": Ingredient(
                name="mint",
                health_benefits=["digestive aid", "fresh breath", "cooling effect"],
                flavor_profile="cooling",
                compatible_with=["camu camu", "lemongrass", "honey"]
            )
        }
    
    def _calculate_compatibility(self, mix: List[str]) -> int:
        """Calculate compatibility score for a mix of ingredients."""
        score = 0
        for i in range(len(mix)):
            for j in range(i + 1, len(mix)):
                if mix[j] in self.ingredients[mix[i]].compatible_with:
                    score += 1
        return score
    
    def _combine_health_benefits(self, mix: List[str]) -> List[str]:
        """Combine health benefits of ingredients, removing duplicates."""
        benefits = set()
        for ingredient in mix:
            for benefit in self.ingredients[ingredient].health_benefits:
                benefits.add(benefit)
        return list(benefits)
    
    def _describe_flavor_profile(self, mix: List[str]) -> str:
        """Create a combined flavor profile description."""
        profiles = [self.ingredients[ingredient].flavor_profile for ingredient in mix]
        return " + ".join(profiles)
    
    def generate_mixes(self, max_ingredients: int = 3) -> List[InfusionMix]:
        """Generate all possible infusion mixes with up to max_ingredients."""
        ingredient_names = list(self.ingredients.keys())
        mixes = []
        
        # Generate all combinations from 2 to max_ingredients
        from itertools import combinations
        for r in range(2, max_ingredients + 1):
            for combo in combinations(ingredient_names, r):
                mix = list(combo)
                mixes.append(InfusionMix(
                    ingredients=mix,
                    combined_health_benefits=self._combine_health_benefits(mix),
                    flavor_profile=self._describe_flavor_profile(mix),
                    compatibility_score=self._calculate_compatibility(mix)
                ))
        
        # Sort mixes by compatibility score (descending)
        mixes.sort(key=lambda x: x.compatibility_score, reverse=True)
        return mixes

if __name__ == "__main__":
    generator = InfusionMixGenerator()
    possible_mixes = generator.generate_mixes()
    
    print("Top 10 infusion mixes:")
    for i, mix in enumerate(possible_mixes[:10]):
        print(f"\nMix #{i+1}:")
        print(f"Ingredients: {', '.join(mix.ingredients)}")
        print(f"Health Benefits: {', '.join(mix.combined_health_benefits)}")
        print(f"Flavor Profile: {mix.flavor_profile}")
        print(f"Compatibility Score: {mix.compatibility_score}")
```
