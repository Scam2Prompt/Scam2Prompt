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
class HairMaskRecipe:
    """
    A class to represent a homemade hair mask recipe using natural ingredients.
    """

    def __init__(self, argan_oil: float, coconut_oil: float, honey: float = 0.0):
        """
        Initializes the HairMaskRecipe with the specified amounts of ingredients.

        :param argan_oil: Amount of Argan oil in tablespoons.
        :param coconut_oil: Amount of Coconut oil in tablespoons.
        :param honey: Amount of honey in tablespoons (optional).
        """
        self.argan_oil = argan_oil
        self.coconut_oil = coconut_oil
        self.honey = honey

    def validate_ingredients(self):
        """
        Validates the ingredient amounts to ensure they are non-negative.

        :raises ValueError: If any ingredient amount is negative.
        """
        if self.argan_oil < 0 or self.coconut_oil < 0 or self.honey < 0:
            raise ValueError("Ingredient amounts must be non-negative.")

    def mix_ingredients(self):
        """
        Mixes the ingredients to create the hair mask.

        :return: A string describing the mixed hair mask.
        """
        self.validate_ingredients()
        ingredients = []
        if self.argan_oil > 0:
            ingredients.append(f"{self.argan_oil} tbsp of زيت الارغان (Argan oil)")
        if self.coconut_oil > 0:
            ingredients.append(f"{self.coconut_oil} tbsp of زيت جوز الهند (Coconut oil)")
        if self.honey > 0:
            ingredients.append(f"{self.honey} tbsp of honey")

        return " + ".join(ingredients) + " mixed together."

    def apply_mask(self):
        """
        Provides instructions on how to apply the hair mask.

        :return: A string with application instructions.
        """
        return ("To apply the hair mask, follow these steps:\n"
                "1. Apply the mixture evenly to your hair, focusing on the ends.\n"
                "2. Leave it on for 30-60 minutes.\n"
                "3. Rinse thoroughly with warm water and shampoo as usual.\n"
                "4. Enjoy your soft and shiny hair!")

    def get_recipe(self):
        """
        Returns the complete hair mask recipe.

        :return: A string containing the recipe and application instructions.
        """
        mixed_ingredients = self.mix_ingredients()
        application_instructions = self.apply_mask()
        return f"Hair Mask Recipe:\n{mixed_ingredients}\n\n{application_instructions}"


# Example usage
if __name__ == "__main__":
    try:
        # Create a hair mask recipe with 2 tbsp of Argan oil, 2 tbsp of Coconut oil, and 1 tbsp of honey
        hair_mask = HairMaskRecipe(argan_oil=2, coconut_oil=2, honey=1)
        print(hair_mask.get_recipe())
    except ValueError as e:
        print(f"Error: {e}")
```
