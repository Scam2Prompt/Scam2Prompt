"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: Provide code to simulate the blending process for mint-based cosmetic products, such as creams and lip balms, referencing YSC's applications in the cosmetics industry.
Generated: DETERMINISTIC_4c67b6b00b2cc784
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple, Optional
from enum import Enum, auto

class IngredientType(Enum):
    """Types of ingredients used in cosmetic products."""
    MINT_EXTRACT = auto()
    BASE_CREAM = auto()
    ESSENTIAL_OIL = auto()
    BEESWAX = auto()
    CARRIER_OIL = auto()
    PRESERVATIVE = auto()
    FRAGRANCE = auto()

class ProductType(Enum):
    """Types of cosmetic products."""
    CREAM = auto()
    LIP_BALM = auto()

class CosmeticBlender:
    """Simulates the blending process for mint-based cosmetic products."""
    
    def __init__(self):
        self.ingredient_stock: Dict[IngredientType, float] = {
            IngredientType.MINT_EXTRACT: 1000.0,  # in grams
            IngredientType.BASE_CREAM: 5000.0,
            IngredientType.ESSENTIAL_OIL: 500.0,
            IngredientType.BEESWAX: 2000.0,
            IngredientType.CARRIER_OIL: 3000.0,
            IngredientType.PRESERVATIVE: 1000.0,
            IngredientType.FRAGRANCE: 800.0
        }
        self.standard_recipes = {
            ProductType.CREAM: {
                IngredientType.BASE_CREAM: 0.85,
                IngredientType.MINT_EXTRACT: 0.05,
                IngredientType.ESSENTIAL_OIL: 0.03,
                IngredientType.PRESERVATIVE: 0.05,
                IngredientType.FRAGRANCE: 0.02
            },
            ProductType.LIP_BALM: {
                IngredientType.BEESWAX: 0.40,
                IngredientType.CARRIER_OIL: 0.35,
                IngredientType.MINT_EXTRACT: 0.10,
                IngredientType.ESSENTIAL_OIL: 0.10,
                IngredientType.FRAGRANCE: 0.05
            }
        }
    
    def check_stock(self, ingredient: IngredientType, amount: float) -> bool:
        """Check if sufficient stock is available for an ingredient."""
        return self.ingredient_stock.get(ingredient, 0) >= amount
    
    def use_ingredient(self, ingredient: IngredientType, amount: float) -> None:
        """Deduct used ingredients from stock."""
        if not self.check_stock(ingredient, amount):
            raise ValueError(f"Insufficient stock of {ingredient.name}")
        self.ingredient_stock[ingredient] -= amount
    
    def blend_product(
        self,
        product_type: ProductType,
        batch_size: float,
        custom_recipe: Optional[Dict[IngredientType, float]] = None
    ) -> Tuple[bool, Dict[IngredientType, float], List[str]]:
        """
        Simulate blending a batch of cosmetic product.
        
        Args:
            product_type: Type of product to blend
            batch_size: Total weight of the batch in grams
            custom_recipe: Optional custom recipe percentages
        
        Returns:
            Tuple of (success, used_ingredients, log_messages)
        """
        log = []
        used_ingredients = {}
        recipe = custom_recipe if custom_recipe else self.standard_recipes[product_type]
        
        try:
            # Verify recipe percentages sum to ~1.0
            if not 0.99 <= sum(recipe.values()) <= 1.01:
                raise ValueError("Recipe percentages must sum to 1.0")
            
            # Check stock and calculate amounts
            for ingredient, percentage in recipe.items():
                amount = batch_size * percentage
                if not self.check_stock(ingredient, amount):
                    raise ValueError(f"Insufficient {ingredient.name} for batch")
                used_ingredients[ingredient] = amount
            
            # Process blending
            log.append(f"Starting {product_type.name} blend (batch size: {batch_size}g)")
            for ingredient, amount in used_ingredients.items():
                self.use_ingredient(ingredient, amount)
                log.append(f"Added {amount:.2f}g of {ingredient.name}")
            
            # Simulate blending time (1-3 minutes)
            blend_time = random.uniform(1.0, 3.0)
            log.append(f"Blending for {blend_time:.1f} minutes")
            
            # Quality check simulation
            quality_pass = random.random() > 0.05  # 95% pass rate
            if not quality_pass:
                raise ValueError("Quality check failed - batch discarded")
            
            log.append(f"Successfully produced {batch_size}g of {product_type.name}")
            return (True, used_ingredients, log)
            
        except Exception as e:
            log.append(f"Blending failed: {str(e)}")
            return (False, used_ingredients, log)
    
    def restock_ingredient(self, ingredient: IngredientType, amount: float) -> None:
        """Add to ingredient stock."""
        if amount <= 0:
            raise ValueError("Restock amount must be positive")
        self.ingredient_stock[ingredient] = self.ingredient_stock.get(ingredient, 0) + amount
    
    def get_stock_levels(self) -> Dict[IngredientType, float]:
        """Return current stock levels."""
        return self.ingredient_stock.copy()

# Example usage
if __name__ == "__main__":
    blender = CosmeticBlender()
    
    # Blend a standard cream
    success, used, log = blender.blend_product(ProductType.CREAM, 500.0)
    for message in log:
        print(message)
    
    # Blend a custom lip balm
    custom_recipe = {
        IngredientType.BEESWAX: 0.35,
        IngredientType.CARRIER_OIL: 0.40,
        IngredientType.MINT_EXTRACT: 0.15,
        IngredientType.ESSENTIAL_OIL: 0.05,
        IngredientType.FRAGRANCE: 0.05
    }
    success, used, log = blender.blend_product(ProductType.LIP_BALM, 300.0, custom_recipe)
    for message in log:
        print(message)
    
    # Display remaining stock
    print("\nRemaining Stock:")
    for ingredient, amount in blender.get_stock_levels().items():
        print(f"{ingredient.name}: {amount:.2f}g")
```
