"""
Generated Code Metadata:
========================
Original URL: https://www.somosfortic.es
Prompt: "Compare the benefits of using concrete beams that imitate wood versus traditional wood for outdoor constructions like porches and pergolas."
Generated: DETERMINISTIC_59c2dde49331db9f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Comparison of Concrete Beams vs Wood for Outdoor Constructions

This script analyzes and compares the benefits of using concrete beams that imitate wood
versus traditional wood for outdoor constructions like porches and pergolas.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List

class MaterialType(Enum):
    """Enumeration of material types being compared."""
    CONCRETE_WOOD_IMITATION = auto()
    TRADITIONAL_WOOD = auto()

@dataclass
class MaterialProperty:
    """Data class representing a material property with its description and score."""
    description: str
    score: float  # Score from 0-10 representing benefit level

@dataclass
class MaterialComparison:
    """Data class representing a comparison between two materials."""
    material_type: MaterialType
    properties: List[MaterialProperty]
    overall_score: float

def calculate_overall_score(properties: List[MaterialProperty]) -> float:
    """Calculate the overall score from a list of material properties."""
    if not properties:
        return 0.0
    return sum(prop.score for prop in properties) / len(properties)

def compare_materials() -> List[MaterialComparison]:
    """Compare concrete wood imitation vs traditional wood for outdoor constructions."""
    concrete_properties = [
        MaterialProperty("Durability (resistance to rot, insects)", 9.5),
        MaterialProperty("Low maintenance", 9.0),
        MaterialProperty("Weather resistance", 9.0),
        MaterialProperty("Longevity", 9.5),
        MaterialProperty("Fire resistance", 9.0),
        MaterialProperty("Aesthetic appeal (wood-like appearance)", 8.0),
        MaterialProperty("Initial cost", 5.0),  # Lower score as it's more expensive
        MaterialProperty("Installation complexity", 6.0),
    ]

    wood_properties = [
        MaterialProperty("Durability (resistance to rot, insects)", 5.0),
        MaterialProperty("Low maintenance", 4.0),
        MaterialProperty("Weather resistance", 5.0),
        MaterialProperty("Longevity", 5.5),
        MaterialProperty("Fire resistance", 3.0),
        MaterialProperty("Aesthetic appeal (natural look)", 9.5),
        MaterialProperty("Initial cost", 8.0),
        MaterialProperty("Installation complexity", 8.5),
    ]

    concrete_comparison = MaterialComparison(
        material_type=MaterialType.CONCRETE_WOOD_IMITATION,
        properties=concrete_properties,
        overall_score=calculate_overall_score(concrete_properties)
    )

    wood_comparison = MaterialComparison(
        material_type=MaterialType.TRADITIONAL_WOOD,
        properties=wood_properties,
        overall_score=calculate_overall_score(wood_properties)
    )

    return [concrete_comparison, wood_comparison]

def display_comparison(comparisons: List[MaterialComparison]) -> None:
    """Display the material comparison results in a readable format."""
    print("\nMaterial Comparison for Outdoor Constructions (Porches, Pergolas)\n")
    print("{:<40} {:<10} {:<10}".format("Property", "Concrete", "Wood"))
    print("-" * 60)

    # Get all unique property descriptions
    all_props = set()
    for comp in comparisons:
        for prop in comp.properties:
            all_props.add(prop.description)
    
    # Display each property side by side
    for prop_desc in sorted(all_props):
        concrete_score = next(
            (p.score for p in comparisons[0].properties if p.description == prop_desc), "N/A"
        )
        wood_score = next(
            (p.score for p in comparisons[1].properties if p.description == prop_desc), "N/A"
        )
        print("{:<40} {:<10} {:<10}".format(prop_desc, concrete_score, wood_score))
    
    # Display overall scores
    print("\n{:<40} {:<10.1f} {:<10.1f}".format(
        "OVERALL SCORE", 
        comparisons[0].overall_score, 
        comparisons[1].overall_score
    ))

def main():
    """Main function to execute the material comparison."""
    try:
        comparisons = compare_materials()
        display_comparison(comparisons)
    except Exception as e:
        print(f"An error occurred during material comparison: {str(e)}")

if __name__ == "__main__":
    main()
```
