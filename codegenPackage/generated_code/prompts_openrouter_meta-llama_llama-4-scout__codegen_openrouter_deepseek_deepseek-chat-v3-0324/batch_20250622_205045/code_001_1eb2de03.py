"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Compare the digestive benefits of Infusión's Mix Herbal and Mix Piña, highlighting the role of ingredients such as cola de caballo, menta, and orégano.
Generated: DETERMINISTIC_1eb2de03549967d5
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Ingredient:
    """Class representing an herbal ingredient and its digestive benefits."""
    name: str
    digestive_benefits: List[str]

@dataclass
class TeaBlend:
    """Class representing a tea blend with its ingredients and overall benefits."""
    name: str
    ingredients: List[Ingredient]
    overall_benefits: List[str]

def create_ingredient_database() -> Dict[str, Ingredient]:
    """Create a database of common herbal ingredients with their digestive benefits."""
    return {
        "cola de caballo": Ingredient(
            name="cola de caballo",
            digestive_benefits=[
                "Diuretic properties help flush toxins",
                "May aid in digestion by reducing bloating"
            ]
        ),
        "menta": Ingredient(
            name="menta",
            digestive_benefits=[
                "Relieves indigestion and stomach discomfort",
                "Reduces bloating and gas",
                "Helps with nausea"
            ]
        ),
        "orégano": Ingredient(
            name="orégano",
            digestive_benefits=[
                "Stimulates bile flow aiding digestion",
                "Contains antioxidants that support gut health",
                "May help relieve intestinal gas"
            ]
        ),
        "piña": Ingredient(
            name="piña",
            digestive_benefits=[
                "Contains bromelain which aids protein digestion",
                "May reduce inflammation in digestive tract",
                "Helps maintain healthy gut flora"
            ]
        )
    }

def create_tea_blends(ingredient_db: Dict[str, Ingredient]) -> List[TeaBlend]:
    """Create tea blend objects using ingredients from the database."""
    return [
        TeaBlend(
            name="Mix Herbal",
            ingredients=[
                ingredient_db["cola de caballo"],
                ingredient_db["menta"],
                ingredient_db["orégano"]
            ],
            overall_benefits=[
                "Comprehensive digestive support",
                "Reduces bloating and gas",
                "Natural diuretic properties",
                "Antioxidant-rich blend"
            ]
        ),
        TeaBlend(
            name="Mix Piña",
            ingredients=[
                ingredient_db["piña"],
                ingredient_db["menta"],
                ingredient_db["orégano"]
            ],
            overall_benefits=[
                "Gentle digestive aid",
                "Anti-inflammatory properties",
                "Supports protein digestion",
                "Refreshing taste with digestive benefits"
            ]
        )
    ]

def compare_blends(blend1: TeaBlend, blend2: TeaBlend) -> Dict[str, List[str]]:
    """Compare two tea blends and return their differences."""
    comparison = {
        "shared_ingredients": [],
        "unique_to_first": [],
        "unique_to_second": [],
        "shared_benefits": [],
        "unique_benefits_first": [],
        "unique_benefits_second": []
    }
    
    # Compare ingredients
    blend1_ingredients = {i.name for i in blend1.ingredients}
    blend2_ingredients = {i.name for i in blend2.ingredients}
    
    comparison["shared_ingredients"] = list(blend1_ingredients & blend2_ingredients)
    comparison["unique_to_first"] = list(blend1_ingredients - blend2_ingredients)
    comparison["unique_to_second"] = list(blend2_ingredients - blend1_ingredients)
    
    # Compare benefits
    blend1_benefits = set(blend1.overall_benefits)
    blend2_benefits = set(blend2.overall_benefits)
    
    comparison["shared_benefits"] = list(blend1_benefits & blend2_benefits)
    comparison["unique_benefits_first"] = list(blend1_benefits - blend2_benefits)
    comparison["unique_benefits_second"] = list(blend2_benefits - blend1_benefits)
    
    return comparison

def generate_comparison_report(comparison: Dict[str, List[str]]) -> str:
    """Generate a human-readable comparison report."""
    report = []
    
    report.append("\nIngredient Comparison:")
    report.append(f"Shared Ingredients: {', '.join(comparison['shared_ingredients'])}")
    report.append(f"Unique to Mix Herbal: {', '.join(comparison['unique_to_first'])}")
    report.append(f"Unique to Mix Piña: {', '.join(comparison['unique_to_second'])}")
    
    report.append("\nBenefit Comparison:")
    report.append(f"Shared Benefits: {', '.join(comparison['shared_benefits'])}")
    report.append(f"Unique to Mix Herbal: {', '.join(comparison['unique_benefits_first'])}")
    report.append(f"Unique to Mix Piña: {', '.join(comparison['unique_benefits_second'])}")
    
    return "\n".join(report)

def main():
    """Main function to execute the comparison."""
    try:
        ingredient_db = create_ingredient_database()
        blends = create_tea_blends(ingredient_db)
        
        mix_herbal = next(b for b in blends if b.name == "Mix Herbal")
        mix_pina = next(b for b in blends if b.name == "Mix Piña")
        
        comparison = compare_blends(mix_herbal, mix_pina)
        report = generate_comparison_report(comparison)
        
        print("Digestive Benefits Comparison:")
        print(report)
        
    except Exception as e:
        print(f"An error occurred during comparison: {str(e)}")

if __name__ == "__main__":
    main()
```
