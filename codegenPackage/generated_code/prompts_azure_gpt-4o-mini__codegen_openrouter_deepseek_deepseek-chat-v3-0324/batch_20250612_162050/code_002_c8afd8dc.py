"""
Generated Code Metadata:
========================
Original URL: https://veganismfood.com
Prompt: How can I implement a search function in a vegan recipe app that filters by ingredients and dietary restrictions?
Generated: DETERMINISTIC_c8afd8dc9b4291b5
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from enum import Enum

class DietaryRestriction(Enum):
    """Enum representing different dietary restrictions."""
    GLUTEN_FREE = "gluten_free"
    NUT_FREE = "nut_free"
    SOY_FREE = "soy_free"
    OIL_FREE = "oil_free"
    SUGAR_FREE = "sugar_free"

class Recipe:
    """Class representing a vegan recipe."""
    
    def __init__(self, name: str, ingredients: List[str], dietary_restrictions: List[DietaryRestriction]):
        """
        Initialize a Recipe instance.
        
        Args:
            name: Name of the recipe
            ingredients: List of ingredients
            dietary_restrictions: List of dietary restrictions the recipe complies with
        """
        self.name = name
        self.ingredients = ingredients
        self.dietary_restrictions = dietary_restrictions

class RecipeSearch:
    """Class for searching and filtering vegan recipes."""
    
    def __init__(self, recipes: List[Recipe]):
        """
        Initialize RecipeSearch with a list of recipes.
        
        Args:
            recipes: List of Recipe objects to search through
        """
        self.recipes = recipes
    
    def search(
        self,
        included_ingredients: Optional[List[str]] = None,
        excluded_ingredients: Optional[List[str]] = None,
        dietary_restrictions: Optional[List[DietaryRestriction]] = None
    ) -> List[Recipe]:
        """
        Search recipes based on ingredients and dietary restrictions.
        
        Args:
            included_ingredients: Ingredients that must be present (None for no filter)
            excluded_ingredients: Ingredients that must not be present (None for no filter)
            dietary_restrictions: Dietary restrictions to filter by (None for no filter)
            
        Returns:
            List of Recipe objects that match the search criteria
        """
        filtered_recipes = self.recipes
        
        # Filter by included ingredients
        if included_ingredients:
            filtered_recipes = [
                recipe for recipe in filtered_recipes
                if all(ingredient in recipe.ingredients for ingredient in included_ingredients)
            ]
        
        # Filter by excluded ingredients
        if excluded_ingredients:
            filtered_recipes = [
                recipe for recipe in filtered_recipes
                if all(ingredient not in recipe.ingredients for ingredient in excluded_ingredients)
            ]
        
        # Filter by dietary restrictions
        if dietary_restrictions:
            filtered_recipes = [
                recipe for recipe in filtered_recipes
                if all(restriction in recipe.dietary_restrictions for restriction in dietary_restrictions)
            ]
        
        return filtered_recipes

# Example usage
if __name__ == "__main__":
    # Sample recipes
    recipes = [
        Recipe(
            "Chickpea Curry",
            ["chickpeas", "coconut milk", "curry powder", "onion"],
            [DietaryRestriction.GLUTEN_FREE, DietaryRestriction.NUT_FREE]
        ),
        Recipe(
            "Almond Butter Smoothie",
            ["almond butter", "banana", "almond milk"],
            [DietaryRestriction.GLUTEN_FREE, DietaryRestriction.SOY_FREE]
        ),
        Recipe(
            "Oil-Free Salad",
            ["lettuce", "tomato", "cucumber", "lemon juice"],
            [DietaryRestriction.GLUTEN_FREE, DietaryRestriction.NUT_FREE, DietaryRestriction.OIL_FREE]
        )
    ]
    
    # Initialize search
    recipe_search = RecipeSearch(recipes)
    
    # Search for gluten-free, nut-free recipes with chickpeas
    results = recipe_search.search(
        included_ingredients=["chickpeas"],
        dietary_restrictions=[DietaryRestriction.GLUTEN_FREE, DietaryRestriction.NUT_FREE]
    )
    
    # Print results
    for recipe in results:
        print(f"Recipe: {recipe.name}")
        print(f"Ingredients: {', '.join(recipe.ingredients)}")
        print(f"Dietary Restrictions: {', '.join([r.value for r in recipe.dietary_restrictions])}")
        print()
```
