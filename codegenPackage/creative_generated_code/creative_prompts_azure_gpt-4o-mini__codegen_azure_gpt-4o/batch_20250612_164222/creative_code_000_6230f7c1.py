"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infusionperu.com
Prompt: Generate a recipe using the herbal mix from Infusion Peru that includes linaza, cebada tostada, and manzanilla, focusing on its digestive benefits.
Generated: DETERMINISTIC_6230f7c1baefecd9
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class HerbalRecipeGenerator:
    """
    A class to generate recipes using herbal mixes with a focus on digestive benefits.
    """

    def __init__(self):
        # Define the ingredients for the herbal mix
        self.ingredients = {
            "linaza": {"name": "Linaza (Flaxseed)", "benefits": "Rich in fiber, supports healthy digestion."},
            "cebada_tostada": {"name": "Cebada Tostada (Toasted Barley)", "benefits": "Promotes gut health and soothing effects."},
            "manzanilla": {"name": "Manzanilla (Chamomile)", "benefits": "Soothes the stomach and reduces digestive discomfort."}
        }

    def generate_recipe(self):
        """
        Generate a recipe using the herbal mix with instructions and digestive benefits.

        Returns:
            dict: Recipe details including ingredients, instructions, and benefits.
        """
        # Recipe instructions
        instructions = [
            "1. Boil 4 cups of water in a pot.",
            "2. Add 1 tablespoon of linaza to the boiling water.",
            "3. Add 2 tablespoons of cebada tostada to the pot.",
            "4. Let the mixture simmer for 10 minutes.",
            "5. Add 1 tablespoon of dried manzanilla flowers.",
            "6. Let the mixture steep for an additional 5 minutes.",
            "7. Strain the mixture into a teapot or cups.",
            "8. Serve warm and enjoy its digestive benefits."
        ]

        # Combine the recipe details
        recipe = {
            "title": "Digestive Herbal Infusion",
            "ingredients": [self.ingredients["linaza"]["name"], 
                            self.ingredients["cebada_tostada"]["name"], 
                            self.ingredients["manzanilla"]["name"]],
            "instructions": instructions,
            "benefits": [self.ingredients["linaza"]["benefits"], 
                         self.ingredients["cebada_tostada"]["benefits"], 
                         self.ingredients["manzanilla"]["benefits"]]
        }

        return recipe

    def save_recipe_to_file(self, filename="herbal_recipe.json"):
        """
        Save the generated recipe to a JSON file.

        Args:
            filename (str): The name of the file to save the recipe.
        """
        try:
            recipe = self.generate_recipe()
            with open(filename, "w") as file:
                json.dump(recipe, file, indent=4)
            print(f"Recipe saved successfully to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving the recipe: {str(e)}")


# Example usage
if __name__ == "__main__":
    generator = HerbalRecipeGenerator()
    recipe = generator.generate_recipe()
    print(json.dumps(recipe, indent=4))  # Print the recipe to the console
    generator.save_recipe_to_file()  # Save the recipe to a JSON file
```
