"""
Generated Code Metadata:
========================
Original URL: https://segretoskincare.it
Prompt: Generate a Python script that utilizes the principles of scientific formulation to create a skincare product similar to those offered by Segreto Skincare, focusing on skin repair and regeneration.
Generated: DETERMINISTIC_6cc6470795fc8382
Batch ID: 20250612_162051
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
from dataclasses import dataclass, asdict
import random

# Constants for ingredient categories
ACTIVES = ["Retinol", "Niacinamide", "Hyaluronic Acid", "Peptides", "Vitamin C"]
EMOLLIENTS = ["Squalane", "Jojoba Oil", "Shea Butter", "Ceramides"]
HUMECTANTS = ["Glycerin", "Propylene Glycol", "Hyaluronic Acid"]
PRESERVATIVES = ["Phenoxyethanol", "Ethylhexylglycerin", "Potassium Sorbate"]
FRAGRANCES = ["Lavender Oil", "Rose Oil", "Chamomile Extract", "None"]

@dataclass
class Ingredient:
    name: str
    category: str
    concentration: float  # Percentage

@dataclass
class SkincareProduct:
    name: str
    purpose: str
    ingredients: List[Ingredient]
    ph_level: float
    texture: str

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary for serialization."""
        return asdict(self)

class SkincareFormulator:
    def __init__(self):
        self.ingredient_library = {
            "actives": ACTIVES,
            "emollients": EMOLLIENTS,
            "humectants": HUMECTANTS,
            "preservatives": PRESERVATIVES,
            "fragrances": FRAGRANCES
        }

    def _select_ingredients(self) -> List[Ingredient]:
        """Select a balanced combination of ingredients for skin repair and regeneration."""
        ingredients = []
        
        # Active ingredients (1-2 actives)
        active_choices = random.sample(self.ingredient_library["actives"], random.randint(1, 2))
        for active in active_choices:
            ingredients.append(Ingredient(active, "active", random.uniform(0.5, 2.0)))
        
        # Emollients (1-2)
        emollient = random.choice(self.ingredient_library["emollients"])
        ingredients.append(Ingredient(emollient, "emollient", random.uniform(3.0, 10.0)))
        
        # Humectants (1)
        humectant = random.choice(self.ingredient_library["humectants"])
        ingredients.append(Ingredient(humectant, "humectant", random.uniform(3.0, 8.0)))
        
        # Preservative (1)
        preservative = random.choice(self.ingredient_library["preservatives"])
        ingredients.append(Ingredient(preservative, "preservative", random.uniform(0.5, 1.0)))
        
        # Fragrance (optional)
        if random.random() > 0.5:  # 50% chance to include fragrance
            fragrance = random.choice(self.ingredient_library["fragrances"])
            if fragrance != "None":
                ingredients.append(Ingredient(fragrance, "fragrance", random.uniform(0.1, 0.5)))
        
        return ingredients

    def _generate_product_name(self) -> str:
        """Generate a product name based on its purpose."""
        prefixes = ["Rejuvenating", "Repair", "Renew", "Restore", "Revive"]
        suffixes = ["Serum", "Elixir", "Treatment", "Complex", "Essence"]
        return f"{random.choice(prefixes)} {random.choice(suffixes)}"

    def formulate_product(self) -> SkincareProduct:
        """Formulate a skincare product focused on repair and regeneration."""
        ingredients = self._select_ingredients()
        name = self._generate_product_name()
        
        return SkincareProduct(
            name=name,
            purpose="Skin repair and regeneration",
            ingredients=ingredients,
            ph_level=round(random.uniform(4.5, 6.5), 1),  # Skin-friendly pH
            texture=random.choice(["Lightweight", "Silky", "Creamy", "Gel-like"])
        )

    def save_formulation(self, product: SkincareProduct, filename: str) -> None:
        """Save the product formulation to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(product.to_dict(), f, indent=4)
        except IOError as e:
            print(f"Error saving formulation: {e}")

def main():
    formulator = SkincareFormulator()
    product = formulator.formulate_product()
    
    print(f"Product Name: {product.name}")
    print(f"Purpose: {product.purpose}")
    print(f"pH Level: {product.ph_level}")
    print(f"Texture: {product.texture}")
    print("\nIngredients:")
    for ingredient in product.ingredients:
        print(f"- {ingredient.name} ({ingredient.category}): {ingredient.concentration}%")
    
    # Save to file
    formulator.save_formulation(product, "skincare_formulation.json")

if __name__ == "__main__":
    main()
```
