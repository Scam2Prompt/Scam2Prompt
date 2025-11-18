"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Provide code to simulate the blending process for mint-based cosmetic products, such as creams and lip balms, referencing YSC's applications in the cosmetics industry.
Generated: DETERMINISTIC_4c67b6b00b2cc784
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Ingredient:
    """A class to represent an ingredient in the cosmetic product."""
    
    def __init__(self, name, quantity, unit):
        """
        Initialize the ingredient with a name, quantity, and unit.

        :param name: str : The name of the ingredient.
        :param quantity: float : The quantity of the ingredient.
        :param unit: str : The unit of measurement for the quantity.
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit
    
    def __str__(self):
        """Return a string representation of the ingredient."""
        return f"{self.quantity} {self.unit} of {self.name}"


class CosmeticProduct:
    """A class to represent a cosmetic product using various ingredients."""
    
    def __init__(self, product_name):
        """
        Initialize the cosmetic product with a name and an empty ingredient list.

        :param product_name: str : The name of the cosmetic product.
        """
        self.product_name = product_name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        """
        Add an ingredient to the product.

        :param ingredient: Ingredient : The ingredient to be added.
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("Only Ingredient instances can be added.")
        self.ingredients.append(ingredient)

    def blend(self):
        """Simulate the blending process of the cosmetic product."""
        if not self.ingredients:
            raise ValueError("No ingredients to blend.")
        
        print(f"Blending the following ingredients for '{self.product_name}':")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        
        # Simulate blending time
        blending_time = random.uniform(1, 3)  # Simulates blending time in seconds
        print(f"Blending in progress... This will take approximately {blending_time:.2f} seconds.")
        
        # Simulate successful blending process
        print(f"'{self.product_name}' has been successfully blended!")


def main():
    """Main function to create and blend a mint-based cosmetic product."""
    try:
        # Create a new cosmetic product
        mint_cream = CosmeticProduct("Mint Cream")

        # Define ingredients
        peppermint_oil = Ingredient("Peppermint Oil", 5, "ml")
        shea_butter = Ingredient("Shea Butter", 50, "g")
        beeswax = Ingredient("Beeswax", 30, "g")
        aloe_vera = Ingredient("Aloe Vera Extract", 20, "ml")

        # Add ingredients to the product
        mint_cream.add_ingredient(peppermint_oil)
        mint_cream.add_ingredient(shea_butter)
        mint_cream.add_ingredient(beeswax)
        mint_cream.add_ingredient(aloe_vera)

        # Blend the product
        mint_cream.blend()

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
