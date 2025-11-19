"""
Generated Code Metadata:
========================
Original URL: https://arcofaurora.com
Prompt: Create a script to generate a customized Diamond Detox Bath recipe based on an individual's vibrational frequency and energy needs.
Generated: DETERMINISTIC_d81a6bb56e13a3c3
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from typing import Dict, List, Optional

# Constants for ingredient categories and their properties
INGREDIENT_CATEGORIES = {
    "salts": {
        "Epsom": {"frequency": 7.83, "properties": ["relaxation", "muscle relief"]},
        "Himalayan": {"frequency": 8.0, "properties": ["mineral replenishment", "detox"]},
        "Dead Sea": {"frequency": 7.5, "properties": ["skin nourishment", "circulation"]}
    },
    "essential_oils": {
        "Lavender": {"frequency": 7.5, "properties": ["calming", "sleep"]},
        "Peppermint": {"frequency": 8.2, "properties": ["energizing", "focus"]},
        "Frankincense": {"frequency": 9.0, "properties": ["spiritual", "grounding"]},
        "Rose": {"frequency": 8.5, "properties": ["love", "emotional healing"]}
    },
    "herbs": {
        "Rose Petals": {"frequency": 7.8, "properties": ["self-love", "beauty"]},
        "Lavender Buds": {"frequency": 7.5, "properties": ["relaxation", "peace"]},
        "Chamomile": {"frequency": 7.3, "properties": ["calm", "sleep"]},
        "Mint Leaves": {"frequency": 8.1, "properties": ["refreshment", "clarity"]}
    },
    "crystals": {
        "Clear Quartz": {"frequency": 9.5, "properties": ["amplification", "clarity"]},
        "Amethyst": {"frequency": 8.8, "properties": ["intuition", "peace"]},
        "Rose Quartz": {"frequency": 8.3, "properties": ["love", "compassion"]},
        "Black Tourmaline": {"frequency": 7.0, "properties": ["protection", "grounding"]}
    }
}

class DiamondDetoxBathGenerator:
    """
    Generates a customized Diamond Detox Bath recipe based on vibrational frequency and energy needs.
    """
    
    def __init__(self):
        self.recipes = self._load_recipes()
    
    def _load_recipes(self) -> Dict:
        """Load predefined recipes from file if available"""
        try:
            with open('recipes.json', 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def _save_recipes(self) -> None:
        """Save generated recipes to file"""
        with open('recipes.json', 'w') as f:
            json.dump(self.recipes, f, indent=2)
    
    def _select_ingredients(self, target_frequency: float, needs: List[str]) -> Dict[str, str]:
        """
        Select ingredients based on target frequency and energy needs.
        
        Args:
            target_frequency: Desired vibrational frequency
            needs: List of desired properties (e.g., relaxation, clarity)
            
        Returns:
            Dictionary of selected ingredients by category
        """
        selected = {}
        
        for category, ingredients in INGREDIENT_CATEGORIES.items():
            # Filter ingredients that match at least one desired property
            matching = [
                (name, data) for name, data in ingredients.items()
                if any(prop in needs for prop in data["properties"])
            ]
            
            if not matching:
                # Fallback to closest frequency match if no property matches
                matching = list(ingredients.items())
            
            # Select the ingredient with frequency closest to target
            best_match = min(
                matching,
                key=lambda x: abs(x[1]["frequency"] - target_frequency)
            )
            selected[category] = best_match[0]
        
        return selected
    
    def generate_recipe(self, name: str, target_frequency: float, needs: List[str]) -> Dict:
        """
        Generate a customized bath recipe.
        
        Args:
            name: Name for the recipe
            target_frequency: Desired vibrational frequency
            needs: List of desired properties
            
        Returns:
            Dictionary containing the recipe details
        """
        if not name or target_frequency <= 0 or not needs:
            raise ValueError("Invalid input parameters")
        
        ingredients = self._select_ingredients(target_frequency, needs)
        
        recipe = {
            "name": name,
            "target_frequency": target_frequency,
            "needs": needs,
            "ingredients": ingredients,
            "instructions": self._generate_instructions(ingredients)
        }
        
        self.recipes[name] = recipe
        self._save_recipes()
        
        return recipe
    
    def _generate_instructions(self, ingredients: Dict[str, str]) -> List[str]:
        """Generate preparation instructions based on selected ingredients"""
        instructions = [
            "1. Fill your bathtub with warm water (about 100°F or 38°C)",
            f"2. Add 2 cups of {ingredients['salts']} salt to the water and stir to dissolve",
            f"3. Add 5-10 drops of {ingredients['essential_oils']} essential oil",
            f"4. Sprinkle a handful of {ingredients['herbs']} into the water",
            f"5. Place a cleansed {ingredients['crystals']} crystal near the tub or in the water",
            "6. Soak for 20-30 minutes, focusing on your intention",
            "7. Rinse with clean water after your bath"
        ]
        
        return instructions
    
    def get_recipe(self, name: str) -> Optional[Dict]:
        """Retrieve a previously generated recipe by name"""
        return self.recipes.get(name)
    
    def list_recipes(self) -> List[str]:
        """List all available recipe names"""
        return list(self.recipes.keys())

# Example usage
if __name__ == "__main__":
    generator = DiamondDetoxBathGenerator()
    
    try:
        recipe = generator.generate_recipe(
            name="Evening Relaxation Bath",
            target_frequency=7.6,
            needs=["relaxation", "sleep", "calm"]
        )
        
        print(f"Generated Recipe: {recipe['name']}")
        print("Ingredients:")
        for category, ingredient in recipe['ingredients'].items():
            print(f"  - {category.replace('_', ' ').title()}: {ingredient}")
        
        print("\nInstructions:")
        for step in recipe['instructions']:
            print(f"  {step}")
    
    except ValueError as e:
        print(f"Error generating recipe: {e}")
```
