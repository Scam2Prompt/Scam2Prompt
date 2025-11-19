"""
Generated Code Metadata:
========================
Original URL: https://xn--vocaprende-o7a.store
Prompt: "Generate a recipe for gluten-free French bread using a mix of alternative flours, similar to those found in the collection by Chef Juliana Fontes."
Generated: DETERMINISTIC_d10ba05d6f04a6b3
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gluten_free_french_bread_recipe.py

class GlutenFreeFrenchBreadRecipe:
    """
    A recipe for gluten-free French bread using alternative flours.
    Inspired by Chef Juliana Fontes' collection.
    """

    def __init__(self):
        self.ingredients = {
            'dry': {
                'brown rice flour': '300g',
                'tapioca flour': '200g',
                'potato starch': '100g',
                'xanthan gum': '2 tsp',
                'salt': '1.5 tsp',
                'instant yeast': '2 tsp',
                'sugar': '1 tsp'
            },
            'wet': {
                'warm water (110°F/43°C)': '350ml',
                'olive oil': '2 tbsp',
                'apple cider vinegar': '1 tbsp',
                'egg whites (room temperature)': '2 large'
            }
        }
        self.equipment = [
            'stand mixer with paddle and dough hook attachments',
            'large mixing bowl',
            'plastic wrap',
            'baking stone or steel',
            'parchment paper',
            'sharp knife or lame',
            'spray bottle with water'
        ]
        self.instructions = [
            "1. In the stand mixer bowl, whisk together all dry ingredients.",
            "2. Add warm water, olive oil, and apple cider vinegar. Mix with paddle attachment on low for 1 minute.",
            "3. Switch to dough hook and knead for 5 minutes on medium speed.",
            "4. Add egg whites one at a time, kneading until fully incorporated (about 3 minutes).",
            "5. Cover bowl with plastic wrap and let rise in warm place for 60-90 minutes until doubled.",
            "6. Preheat oven to 450°F (230°C) with baking stone/steel for at least 30 minutes.",
            "7. Turn dough onto floured surface (use rice flour), shape into baguette form.",
            "8. Place on parchment-lined peel or tray, cover, and proof for 30 minutes.",
            "9. Score top with sharp knife, mist with water.",
            "10. Bake for 20 minutes, then reduce heat to 400°F (200°C) and bake 15 more minutes.",
            "11. Cool on wire rack for at least 30 minutes before slicing."
        ]
        self.notes = [
            "For crispier crust: place a pan of water in oven during preheating.",
            "Dough will be stickier than wheat dough - handle with wet hands.",
            "Best consumed within 24 hours or freeze for later use."
        ]

    def print_recipe(self):
        """Prints the formatted recipe with ingredients and instructions."""
        print("GLUTEN-FREE FRENCH BREAD RECIPE\n")
        print("INGREDIENTS:")
        print("\nDry Ingredients:")
        for ingredient, amount in self.ingredients['dry'].items():
            print(f"- {ingredient}: {amount}")
        
        print("\nWet Ingredients:")
        for ingredient, amount in self.ingredients['wet'].items():
            print(f"- {ingredient}: {amount}")
        
        print("\nEQUIPMENT NEEDED:")
        for item in self.equipment:
            print(f"- {item}")
        
        print("\nINSTRUCTIONS:")
        for step in self.instructions:
            print(step)
        
        print("\nNOTES:")
        for note in self.notes:
            print(f"- {note}")


if __name__ == "__main__":
    try:
        recipe = GlutenFreeFrenchBreadRecipe()
        recipe.print_recipe()
    except Exception as e:
        print(f"Error generating recipe: {str(e)}")
```
