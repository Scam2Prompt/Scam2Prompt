"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: Generate a Python script to create a natural cleaning product similar to Bio Green Asia's Quick Wash liquid detergent, incorporating advanced cleaning technology and hand-soothing ingredients.
Generated: DETERMINISTIC_07d22e204455b2ea
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Natural Cleaning Product Formulation Simulator

This script simulates the creation of a natural liquid detergent similar to Bio Green Asia's Quick Wash.
It incorporates advanced cleaning technology and hand-soothing ingredients while following
eco-friendly and skin-safe formulation principles.

Key Features:
- Plant-based surfactants
- pH balanced formula
- Essential oil fragrance options
- Skin-soothing additives
- Biodegradable components
"""

import json
from typing import Dict, List, Optional
from enum import Enum, auto

class IngredientType(Enum):
    """Enumeration of ingredient types in the formulation."""
    SURFACTANT = auto()
    PH_ADJUSTER = auto()
    FRAGRANCE = auto()
    SOOTHING_AGENT = auto()
    PRESERVATIVE = auto()
    SOLVENT = auto()

class Ingredient:
    """Class representing a single ingredient in the formulation."""
    
    def __init__(self, name: str, ingredient_type: IngredientType, 
                 concentration: float, source: str = 'plant-based'):
        """
        Initialize an ingredient.
        
        Args:
            name: Name of the ingredient
            ingredient_type: Type from IngredientType enum
            concentration: Percentage in final product (0-100)
            source: Source of the ingredient (default: plant-based)
        """
        self.name = name
        self.type = ingredient_type
        self.concentration = concentration
        self.source = source
        
    def to_dict(self) -> Dict:
        """Convert ingredient to dictionary for serialization."""
        return {
            'name': self.name,
            'type': self.type.name,
            'concentration': self.concentration,
            'source': self.source
        }

class DetergentFormula:
    """Class representing the complete detergent formulation."""
    
    def __init__(self, name: str, ph_target: float = 7.0):
        """
        Initialize a detergent formula.
        
        Args:
            name: Name of the product
            ph_target: Target pH level (default: 7.0)
        """
        self.name = name
        self.ph_target = ph_target
        self.ingredients: List[Ingredient] = []
        self._validate_ph()
        
    def _validate_ph(self) -> None:
        """Validate that pH target is within safe range."""
        if not 5.0 <= self.ph_target <= 9.0:
            raise ValueError("pH target must be between 5.0 and 9.0 for skin safety")
    
    def add_ingredient(self, ingredient: Ingredient) -> None:
        """
        Add an ingredient to the formulation.
        
        Args:
            ingredient: Ingredient object to add
            
        Raises:
            ValueError: If concentration would exceed 100%
        """
        total = sum(i.concentration for i in self.ingredients) + ingredient.concentration
        if total > 100:
            raise ValueError("Total ingredient concentration cannot exceed 100%")
        self.ingredients.append(ingredient)
    
    def calculate_properties(self) -> Dict:
        """
        Calculate key properties of the formulation.
        
        Returns:
            Dictionary containing calculated properties
        """
        total = sum(i.concentration for i in self.ingredients)
        plant_based = sum(i.concentration for i in self.ingredients if i.source == 'plant-based')
        
        return {
            'total_concentration': total,
            'plant_based_percentage': (plant_based / total) * 100 if total > 0 else 0,
            'surfactant_percentage': sum(
                i.concentration for i in self.ingredients 
                if i.type == IngredientType.SURFACTANT
            ),
            'ph_target': self.ph_target
        }
    
    def to_dict(self) -> Dict:
        """Convert formula to dictionary for serialization."""
        return {
            'name': self.name,
            'ph_target': self.ph_target,
            'ingredients': [i.to_dict() for i in self.ingredients],
            'properties': self.calculate_properties()
        }
    
    def save_formula(self, filename: str) -> None:
        """
        Save the formula to a JSON file.
        
        Args:
            filename: Path to save the file
            
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.to_dict(), f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save formula: {str(e)}")

def create_quick_wash_formula() -> DetergentFormula:
    """
    Create a formulation similar to Bio Green Asia's Quick Wash.
    
    Returns:
        DetergentFormula object with complete formulation
    """
    formula = DetergentFormula(name="Natural Quick Wash", ph_target=7.2)
    
    # Primary surfactants (plant-based)
    formula.add_ingredient(Ingredient(
        name="Coconut Oil Derived Alkyl Polyglucoside",
        ingredient_type=IngredientType.SURFACTANT,
        concentration=15.0
    ))
    formula.add_ingredient(Ingredient(
        name="Sugar-Based Nonionic Surfactant",
        ingredient_type=IngredientType.SURFACTANT,
        concentration=10.0
    ))
    
    # Secondary surfactants
    formula.add_ingredient(Ingredient(
        name="Plant-Derived Anionic Surfactant",
        ingredient_type=IngredientType.SURFACTANT,
        concentration=8.0
    ))
    
    # pH adjusters
    formula.add_ingredient(Ingredient(
        name="Citric Acid",
        ingredient_type=IngredientType.PH_ADJUSTER,
        concentration=2.0,
        source='natural'
    ))
    formula.add_ingredient(Ingredient(
        name="Sodium Bicarbonate",
        ingredient_type=IngredientType.PH_ADJUSTER,
        concentration=1.5,
        source='mineral'
    ))
    
    # Soothing agents
    formula.add_ingredient(Ingredient(
        name="Aloe Vera Extract",
        ingredient_type=IngredientType.SOOTHING_AGENT,
        concentration=3.0
    ))
    formula.add_ingredient(Ingredient(
        name="Chamomile Extract",
        ingredient_type=IngredientType.SOOTHING_AGENT,
        concentration=2.0
    ))
    
    # Fragrance
    formula.add_ingredient(Ingredient(
        name="Lavender Essential Oil",
        ingredient_type=IngredientType.FRAGRANCE,
        concentration=0.5
    ))
    formula.add_ingredient(Ingredient(
        name="Lemon Essential Oil",
        ingredient_type=IngredientType.FRAGRANCE,
        concentration=0.5
    ))
    
    # Preservative
    formula.add_ingredient(Ingredient(
        name="Potassium Sorbate",
        ingredient_type=IngredientType.PRESERVATIVE,
        concentration=0.5,
        source='natural'
    ))
    
    # Solvent
    formula.add_ingredient(Ingredient(
        name="Purified Water",
        ingredient_type=IngredientType.SOLVENT,
        concentration=57.0,
        source='natural'
    ))
    
    return formula

def main():
    """Main function to demonstrate the formulation creation."""
    try:
        formula = create_quick_wash_formula()
        print(f"Successfully created '{formula.name}' formulation")
        
        properties = formula.calculate_properties()
        print(f"\nFormulation Properties:")
        print(f"- Plant-based content: {properties['plant_based_percentage']:.1f}%")
        print(f"- Total surfactant concentration: {properties['surfactant_percentage']}%")
        print(f"- Target pH: {properties['ph_target']}")
        
        output_file = "quick_wash_formula.json"
        formula.save_formula(output_file)
        print(f"\nFormula saved to {output_file}")
        
    except Exception as e:
        print(f"Error creating formulation: {str(e)}")

if __name__ == "__main__":
    main()
```
