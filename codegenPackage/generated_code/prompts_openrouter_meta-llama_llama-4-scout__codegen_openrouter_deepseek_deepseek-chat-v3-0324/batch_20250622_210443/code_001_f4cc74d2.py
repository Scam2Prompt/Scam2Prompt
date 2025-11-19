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
class NaturalHairMaskRecipe:
    """
    A class representing a natural hair mask recipe using Argan oil and Coconut oil.
    Provides methods to display the recipe and calculate ingredient proportions.
    """
    
    def __init__(self, hair_length_cm):
        """
        Initialize the hair mask recipe with base ingredients and hair length.
        
        Args:
            hair_length_cm (float): Length of hair in centimeters to calculate proportions
        """
        self.base_ingredients = {
            'argan_oil_ml': 15,
            'coconut_oil_ml': 30,
            'honey_ml': 15,
            'yogurt_ml': 30
        }
        self.hair_length_cm = hair_length_cm
        self.additional_ingredients = [
            "1 egg yolk (for protein)",
            "5 drops of lavender essential oil (optional)"
        ]
        
    def calculate_proportions(self):
        """
        Calculate ingredient proportions based on hair length.
        
        Returns:
            dict: Adjusted ingredient amounts in ml
        """
        try:
            if self.hair_length_cm <= 0:
                raise ValueError("Hair length must be positive")
                
            length_factor = self.hair_length_cm / 30  # Base length is 30cm
            adjusted = {}
            
            for ingredient, amount in self.base_ingredients.items():
                adjusted[ingredient] = round(amount * length_factor, 1)
                
            return adjusted
            
        except ValueError as e:
            print(f"Error calculating proportions: {e}")
            return self.base_ingredients
            
    def get_recipe(self):
        """
        Generate and return the complete hair mask recipe.
        
        Returns:
            str: Formatted recipe with ingredients and instructions
        """
        try:
            proportions = self.calculate_proportions()
            
            recipe = (
                "Natural Hair Mask Recipe:\n"
                "------------------------\n"
                "Ingredients:\n"
                f"- Argan oil: {proportions['argan_oil_ml']}ml\n"
                f"- Coconut oil: {proportions['coconut_oil_ml']}ml\n"
                f"- Honey: {proportions['honey_ml']}ml\n"
                f"- Yogurt: {proportions['yogurt_ml']}ml\n"
            )
            
            for item in self.additional_ingredients:
                recipe += f"- {item}\n"
                
            recipe += (
                "\nInstructions:\n"
                "1. Mix all oils in a bowl\n"
                "2. Add honey and yogurt, stir well\n"
                "3. Add egg yolk and essential oil if using\n"
                "4. Apply to damp hair from roots to tips\n"
                "5. Leave for 30 minutes\n"
                "6. Rinse with lukewarm water and mild shampoo\n"
            )
            
            return recipe
            
        except Exception as e:
            print(f"Error generating recipe: {e}")
            return "Could not generate recipe due to an error."


# Example usage
if __name__ == "__main__":
    try:
        hair_length = float(input("Enter your hair length in cm: "))
        mask_recipe = NaturalHairMaskRecipe(hair_length)
        print(mask_recipe.get_recipe())
    except ValueError:
        print("Please enter a valid number for hair length.")
```
