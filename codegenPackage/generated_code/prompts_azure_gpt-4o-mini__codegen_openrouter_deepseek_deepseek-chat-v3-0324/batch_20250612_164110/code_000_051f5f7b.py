"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: Generate a Python script that utilizes the properties of menthol for creating a cosmetic formula, referencing the applications mentioned on the YSC website.
Generated: DETERMINISTIC_051f5f7b9740af0f
Batch ID: 20250612_164110
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

class CosmeticIngredient:
    """Represents a cosmetic ingredient with its properties."""
    
    def __init__(self, name: str, concentration: float, properties: List[str]):
        """
        Initialize a cosmetic ingredient.
        
        Args:
            name: Name of the ingredient.
            concentration: Concentration in percentage (0-100).
            properties: List of properties/benefits of the ingredient.
        """
        self.name = name
        self.concentration = concentration
        self.properties = properties

    def to_dict(self) -> Dict:
        """Convert the ingredient to a dictionary."""
        return {
            "name": self.name,
            "concentration": self.concentration,
            "properties": self.properties
        }

class CosmeticFormula:
    """Represents a cosmetic formula containing multiple ingredients."""
    
    def __init__(self, name: str):
        """
        Initialize a cosmetic formula.
        
        Args:
            name: Name of the formula.
        """
        self.name = name
        self.ingredients = []
    
    def add_ingredient(self, ingredient: CosmeticIngredient) -> None:
        """
        Add an ingredient to the formula.
        
        Args:
            ingredient: CosmeticIngredient object to add.
        
        Raises:
            ValueError: If concentration exceeds 100% when added.
        """
        total_concentration = sum(ing.concentration for ing in self.ingredients) + ingredient.concentration
        if total_concentration > 100:
            raise ValueError("Total concentration cannot exceed 100%")
        self.ingredients.append(ingredient)
    
    def get_formula(self) -> Dict:
        """
        Get the formula details as a dictionary.
        
        Returns:
            Dictionary containing formula name and ingredients.
        """
        return {
            "formula_name": self.name,
            "ingredients": [ing.to_dict() for ing in self.ingredients]
        }
    
    def save_to_file(self, filename: str) -> None:
        """
        Save the formula to a JSON file.
        
        Args:
            filename: Name of the file to save to.
        
        Raises:
            IOError: If file writing fails.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_formula(), f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save formula to file: {e}")

def create_menthol_formula() -> CosmeticFormula:
    """
    Create a cosmetic formula utilizing menthol based on YSC applications.
    
    Returns:
        CosmeticFormula object with menthol and complementary ingredients.
    """
    formula = CosmeticFormula("Menthol Cooling Lotion")
    
    # Menthol properties referenced from YSC applications
    menthol = CosmeticIngredient(
        name="Menthol",
        concentration=1.0,
        properties=["Cooling", "Soothing", "Anti-irritant"]
    )
    
    # Complementary ingredients
    aloe_vera = CosmeticIngredient(
        name="Aloe Vera",
        concentration=15.0,
        properties=["Moisturizing", "Healing"]
    )
    
    glycerin = CosmeticIngredient(
        name="Glycerin",
        concentration=5.0,
        properties=["Humectant", "Skin conditioning"]
    )
    
    water = CosmeticIngredient(
        name="Water",
        concentration=79.0,
        properties=["Solvent", "Base"]
    )
    
    try:
        formula.add_ingredient(menthol)
        formula.add_ingredient(aloe_vera)
        formula.add_ingredient(glycerin)
        formula.add_ingredient(water)
    except ValueError as e:
        print(f"Error creating formula: {e}")
        raise
    
    return formula

if __name__ == "__main__":
    try:
        formula = create_menthol_formula()
        print(json.dumps(formula.get_formula(), indent=4))
        formula.save_to_file("menthol_cosmetic_formula.json")
        print("Formula saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
