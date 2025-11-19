"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Write a Python code snippet to recommend infusion mixes based on user-inputted health benefits, considering the properties of ingredients like linaza, cebada tostada, and hierba luisa.
Generated: DETERMINISTIC_f92651e54513ee1b
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

# Database of infusion ingredients and their properties
INGREDIENTS_DB = {
    "linaza": {
        "benefits": ["digestion", "heart_health", "skin_health"],
        "flavor": "nutty",
        "caffeine_free": True
    },
    "cebada_tostada": {
        "benefits": ["digestion", "energy", "bone_health"],
        "flavor": "malty",
        "caffeine_free": True
    },
    "hierba_luisa": {
        "benefits": ["relaxation", "digestion", "immune_support"],
        "flavor": "citrus",
        "caffeine_free": True
    },
    "manzanilla": {
        "benefits": ["relaxation", "digestion", "sleep_aid"],
        "flavor": "floral",
        "caffeine_free": True
    },
    "menta": {
        "benefits": ["digestion", "respiratory_health", "energy"],
        "flavor": "minty",
        "caffeine_free": True
    }
}

class InfusionRecommender:
    """
    Recommends infusion mixes based on desired health benefits.
    """
    def __init__(self, ingredients_db: Dict = INGREDIENTS_DB):
        self.ingredients_db = ingredients_db
    
    def find_ingredients_by_benefits(self, desired_benefits: List[str]) -> Dict[str, List[str]]:
        """
        Find ingredients that match any of the desired health benefits.
        
        Args:
            desired_benefits: List of health benefits the user wants
            
        Returns:
            Dictionary with ingredients as keys and matching benefits as values
        """
        matching_ingredients = {}
        
        for ingredient, properties in self.ingredients_db.items():
            common_benefits = [
                benefit for benefit in properties["benefits"] 
                if benefit in desired_benefits
            ]
            if common_benefits:
                matching_ingredients[ingredient] = common_benefits
                
        return matching_ingredients
    
    def recommend_mix(
        self, 
        desired_benefits: List[str], 
        max_ingredients: int = 3,
        exclude: Optional[List[str]] = None
    ) -> List[Dict]:
        """
        Recommend infusion mixes based on desired health benefits.
        
        Args:
            desired_benefits: List of health benefits the user wants
            max_ingredients: Maximum number of ingredients in the mix
            exclude: List of ingredients to exclude from recommendations
            
        Returns:
            List of recommended mixes with ingredients and matched benefits
        """
        if exclude is None:
            exclude = []
            
        matching_ingredients = self.find_ingredients_by_benefits(desired_benefits)
        
        # Filter out excluded ingredients
        matching_ingredients = {
            ing: benefits for ing, benefits in matching_ingredients.items()
            if ing not in exclude
        }
        
        if not matching_ingredients:
            return []
        
        # Sort ingredients by number of matching benefits (descending)
        sorted_ingredients = sorted(
            matching_ingredients.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )
        
        # Create recommendations with up to max_ingredients
        recommendations = []
        for i in range(1, min(max_ingredients, len(sorted_ingredients)) + 1):
            mix_ingredients = sorted_ingredients[:i]
            recommendations.append({
                "ingredients": [ing[0] for ing in mix_ingredients],
                "matched_benefits": list(set(
                    benefit for ing in mix_ingredients for benefit in ing[1]
                ))
            })
        
        return recommendations
    
    def get_ingredient_details(self, ingredient_name: str) -> Optional[Dict]:
        """
        Get details about a specific ingredient.
        
        Args:
            ingredient_name: Name of the ingredient to look up
            
        Returns:
            Dictionary with ingredient details or None if not found
        """
        return self.ingredients_db.get(ingredient_name)

def main():
    """
    Example usage of the InfusionRecommender.
    """
    recommender = InfusionRecommender()
    
    print("Available ingredients and their benefits:")
    for ingredient, details in recommender.ingredients_db.items():
        print(f"- {ingredient}: {', '.join(details['benefits'])}")
    
    print("\nEnter your desired health benefits (comma-separated):")
    user_input = input("> ").strip().lower()
    desired_benefits = [b.strip() for b in user_input.split(",") if b.strip()]
    
    print("\nAny ingredients to exclude? (comma-separated, leave empty if none):")
    user_input = input("> ").strip().lower()
    exclude = [i.strip() for i in user_input.split(",") if i.strip()]
    
    recommendations = recommender.recommend_mix(
        desired_benefits=desired_benefits,
        exclude=exclude
    )
    
    if not recommendations:
        print("\nNo matching infusions found for your criteria.")
        return
    
    print("\nRecommended infusion mixes:")
    for i, mix in enumerate(recommendations, 1):
        print(f"\nOption {i}:")
        print(f"Ingredients: {', '.join(mix['ingredients'])}")
        print(f"Matched benefits: {', '.join(mix['matched_benefits'])}")
        
        print("\nIngredient details:")
        for ing in mix['ingredients']:
            details = recommender.get_ingredient_details(ing)
            print(f"- {ing}:")
            print(f"  Flavor: {details['flavor']}")
            print(f"  Caffeine free: {'Yes' if details['caffeine_free'] else 'No'}")

if __name__ == "__main__":
    main()
```
