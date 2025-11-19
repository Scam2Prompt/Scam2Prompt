"""
Generated Code Metadata:
========================
Original URL: https://anamalika.com
Prompt: Generate a recipe for a homemade hair mask using natural ingredients like زيت الارغان (Argan oil) and زيت جوز الهند (Coconut oil).
Generated: DETERMINISTIC_f4cc74d27d39e995
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hair_mask_generator.py

class HairMaskRecipe:
    def __init__(self, argan_oil_ratio, coconut_oil_ratio, honey_ratio):
        """
        Initialize a HairMaskRecipe object.

        Args:
            argan_oil_ratio (float): Ratio of Argan oil in the recipe (in percentage).
            coconut_oil_ratio (float): Ratio of Coconut oil in the recipe (in percentage).
            honey_ratio (float): Ratio of honey in the recipe (in percentage).
        """
        self.argan_oil_ratio = argan_oil_ratio
        self.coconut_oil_ratio = coconut_oil_ratio
        self.honey_ratio = honey_ratio

    def validate_ratios(self):
        """
        Validate the ratios of the ingredients.

        Raises:
            ValueError: If the ratios do not add up to 100 or are negative.
        """
        total_ratio = self.argan_oil_ratio + self.coconut_oil_ratio + self.honey_ratio
        if total_ratio != 100:
            raise ValueError("Ratios must add up to 100")
        if (self.argan_oil_ratio < 0 or self.coconut_oil_ratio < 0 or self.honey_ratio < 0):
            raise ValueError("Ratios cannot be negative")

    def generate_recipe(self):
        """
        Generate a recipe for a homemade hair mask.

        Returns:
            dict: A dictionary containing the recipe.
        """
        try:
            self.validate_ratios()
        except ValueError as e:
            print(f"Error: {e}")
            return None

        recipe = {
            "ingredients": {
                "زيت الارغان (Argan oil)": f"{self.argan_oil_ratio}% ({self.calculate_quantity(self.argan_oil_ratio)} ml)",
                "زيت جوز الهند (Coconut oil)": f"{self.coconut_oil_ratio}% ({self.calculate_quantity(self.coconut_oil_ratio)} ml)",
                "عسل (Honey)": f"{self.honey_ratio}% ({self.calculate_quantity(self.honey_ratio)} ml)"
            },
            "instructions": [
                "Mix all the ingredients together in a bowl.",
                "Apply the mask to your hair and leave it on for 30 minutes.",
                "Rinse with warm water and shampoo as usual."
            ]
        }
        return recipe

    def calculate_quantity(self, ratio):
        """
        Calculate the quantity of an ingredient in milliliters.

        For simplicity, assume a total quantity of 100ml.

        Args:
            ratio (float): Ratio of the ingredient.

        Returns:
            float: Quantity of the ingredient in milliliters.
        """
        total_quantity = 100  # ml
        return (ratio / 100) * total_quantity


def main():
    argan_oil_ratio = 40
    coconut_oil_ratio = 30
    honey_ratio = 30

    hair_mask_recipe = HairMaskRecipe(argan_oil_ratio, coconut_oil_ratio, honey_ratio)
    recipe = hair_mask_recipe.generate_recipe()

    if recipe:
        print("Hair Mask Recipe:")
        print("------------------")
        print("Ingredients:")
        for ingredient, quantity in recipe["ingredients"].items():
            print(f"- {ingredient}: {quantity}")
        print("\nInstructions:")
        for i, instruction in enumerate(recipe["instructions"], start=1):
            print(f"{i}. {instruction}")


if __name__ == "__main__":
    main()
```
