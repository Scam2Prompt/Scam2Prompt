"""
Generated Code Metadata:
========================
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: What are some natural ingredients used in C'est Moi Qui L'ai Fait pour Vous' solid cosmetics, and how do they benefit the skin and hair?
Generated: DETERMINISTIC_5dc80398edb8ad79
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A module to showcase natural ingredients used in C'est Moi Qui L'ai Fait pour Vous cosmetics
and their benefits for skin and hair.
"""

from typing import Dict, List, Tuple

class NaturalIngredient:
    """Represents a natural ingredient with its properties and benefits."""
    
    def __init__(self, name: str, source: str, benefits: List[str]):
        """
        Initialize a natural ingredient.
        
        Args:
            name: Name of the ingredient
            source: Natural source of the ingredient (plant, mineral, etc.)
            benefits: List of benefits for skin/hair
        """
        self.name = name
        self.source = source
        self.benefits = benefits
    
    def __str__(self) -> str:
        """Return a formatted string representation of the ingredient."""
        return f"{self.name} (from {self.source}): {', '.join(self.benefits)}"

def get_common_ingredients() -> Dict[str, NaturalIngredient]:
    """
    Returns a dictionary of common natural ingredients used in the cosmetics line.
    
    Returns:
        Dictionary where keys are ingredient names and values are NaturalIngredient objects
    """
    ingredients = {
        "Shea Butter": NaturalIngredient(
            name="Shea Butter",
            source="Shea Tree nuts",
            benefits=[
                "Deeply moisturizes skin",
                "Reduces inflammation",
                "Protects hair from breakage"
            ]
        ),
        "Coconut Oil": NaturalIngredient(
            name="Coconut Oil",
            source="Coconut fruit",
            benefits=[
                "Softens skin and hair",
                "Has antibacterial properties",
                "Helps prevent protein loss in hair"
            ]
        ),
        "Beeswax": NaturalIngredient(
            name="Beeswax",
            source="Honeybees",
            benefits=[
                "Creates protective barrier on skin",
                "Locks in moisture",
                "Adds natural shine to hair"
            ]
        ),
        "Kaolin Clay": NaturalIngredient(
            name="Kaolin Clay",
            source="Natural clay deposits",
            benefits=[
                "Gently exfoliates skin",
                "Absorbs excess oil",
                "Purifies hair and scalp"
            ]
        ),
        "Essential Oils": NaturalIngredient(
            name="Essential Oils",
            source="Various plants",
            benefits=[
                "Provide natural fragrance",
                "Offer therapeutic benefits",
                "Can promote hair growth"
            ]
        )
    }
    return ingredients

def display_ingredients() -> None:
    """Display all ingredients and their benefits in a formatted way."""
    ingredients = get_common_ingredients()
    
    print("Natural Ingredients in C'est Moi Qui L'ai Fait pour Vous Cosmetics:")
    print("=" * 70)
    for name, ingredient in ingredients.items():
        print(f"\n- {ingredient}")
    
    print("\nThese natural ingredients provide gentle, effective care for skin and hair.")

if __name__ == "__main__":
    display_ingredients()
```
