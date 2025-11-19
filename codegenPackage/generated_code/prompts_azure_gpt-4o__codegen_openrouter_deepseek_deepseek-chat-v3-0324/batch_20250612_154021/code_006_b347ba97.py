"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Create a Python program that suggests cocktail recipes using Yobugo's "Crema de manzana y canela" based on user preferences for fruity or creamy flavors.
Generated: DETERMINISTIC_b347ba979d4fd3b9
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class CocktailRecommender:
    """
    A class to recommend cocktails based on user preferences for fruity or creamy flavors.
    Uses Yobugo's "Crema de manzana y canela" as a base ingredient.
    """
    
    def __init__(self):
        self.cocktails = self._load_cocktail_recipes()
    
    def _load_cocktail_recipes(self) -> List[Dict]:
        """Load and return the cocktail recipes from a JSON structure."""
        return [
            {
                "name": "Apple Cinnamon Dream",
                "ingredients": {
                    "Yobugo's Crema de manzana y canela": "2 oz",
                    "Vanilla vodka": "1 oz",
                    "Apple juice": "3 oz",
                    "Heavy cream": "1 oz"
                },
                "instructions": "Shake all ingredients with ice and strain into a chilled glass. Garnish with apple slices.",
                "flavor_profile": "creamy"
            },
            {
                "name": "Tropical Apple Breeze",
                "ingredients": {
                    "Yobugo's Crema de manzana y canela": "1.5 oz",
                    "Pineapple juice": "3 oz",
                    "Coconut rum": "1 oz",
                    "Lime juice": "0.5 oz"
                },
                "instructions": "Shake all ingredients with ice and strain into a highball glass filled with ice. Garnish with pineapple wedge.",
                "flavor_profile": "fruity"
            },
            {
                "name": "Spiced Apple Fizz",
                "ingredients": {
                    "Yobugo's Crema de manzana y canela": "2 oz",
                    "Ginger beer": "4 oz",
                    "Lemon juice": "0.5 oz",
                    "Angostura bitters": "2 dashes"
                },
                "instructions": "Build in a highball glass over ice. Stir gently. Garnish with lemon twist.",
                "flavor_profile": "fruity"
            },
            {
                "name": "Cinnamon Apple Delight",
                "ingredients": {
                    "Yobugo's Crema de manzana y canela": "2 oz",
                    "Irish cream": "1 oz",
                    "Coffee liqueur": "0.5 oz",
                    "Whipped cream": "for topping"
                },
                "instructions": "Shake first three ingredients with ice. Strain into a martini glass. Top with whipped cream and cinnamon sprinkle.",
                "flavor_profile": "creamy"
            }
        ]
    
    def recommend_cocktails(self, preference: str) -> Optional[List[Dict]]:
        """
        Recommend cocktails based on flavor preference.
        
        Args:
            preference: Either 'fruity' or 'creamy'
            
        Returns:
            List of matching cocktail recipes or None if invalid preference
        """
        if preference.lower() not in ['fruity', 'creamy']:
            return None
            
        return [cocktail for cocktail in self.cocktails 
                if cocktail['flavor_profile'] == preference.lower()]
    
    def display_cocktail(self, cocktail: Dict) -> str:
        """Format a cocktail recipe for display."""
        ingredients = "\n".join([f"- {ingredient}: {amount}" 
                               for ingredient, amount in cocktail['ingredients'].items()])
        return (
            f"\n{cocktail['name']}\n"
            f"Ingredients:\n{ingredients}\n"
            f"Instructions: {cocktail['instructions']}\n"
        )

def main():
    """Main program loop for cocktail recommendation."""
    recommender = CocktailRecommender()
    
    print("Welcome to the Yobugo's Crema de manzana y canela Cocktail Recommender!")
    print("Would you prefer 'fruity' or 'creamy' cocktails?")
    
    while True:
        preference = input("Enter your preference (fruity/creamy) or 'quit' to exit: ").strip().lower()
        
        if preference == 'quit':
            print("Goodbye! Enjoy your cocktails!")
            break
            
        cocktails = recommender.recommend_cocktails(preference)
        
        if not cocktails:
            print("Invalid preference. Please enter 'fruity' or 'creamy'.")
            continue
            
        print(f"\nHere are your {preference} cocktail recommendations:")
        for cocktail in cocktails:
            print(recommender.display_cocktail(cocktail))

if __name__ == "__main__":
    main()
```
