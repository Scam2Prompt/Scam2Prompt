"""
Generated Code Metadata:
========================
Original URL: https://www.madoniaoli.it
Prompt: Generate a recipe that highlights the use of Madonia's extra virgin olive oil, specifically focusing on its cold extraction process and unique flavor profile.
Generated: DETERMINISTIC_7fc53ea818f9a305
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Recipe Generator for Madonia's Extra Virgin Olive Oil

This script generates a recipe that highlights the unique qualities of Madonia's extra virgin olive oil,
including its cold extraction process and flavor profile.
"""

class RecipeGenerator:
    """
    A class to generate a recipe showcasing Madonia's extra virgin olive oil.
    """

    def __init__(self):
        """
        Initialize the recipe generator with default values.
        """
        self.recipe_name = "Mediterranean Olive Oil Drizzled Bruschetta"
        self.serving_size = 4
        self.prep_time = 15  # minutes
        self.cook_time = 5  # minutes
        self.ingredients = [
            "1 loaf crusty Italian bread, sliced",
            "4 ripe tomatoes, diced",
            "2 cloves garlic, minced",
            "1/4 cup fresh basil, chopped",
            "1/2 teaspoon sea salt",
            "1/4 teaspoon freshly ground black pepper",
            "1/2 cup Madonia's extra virgin olive oil (cold extracted)",
            "1 tablespoon balsamic vinegar (optional)",
            "1/4 cup fresh mozzarella, diced (optional)"
        ]
        self.instructions = [
            "Preheat oven to 375°F (190°C).",
            "Arrange bread slices on a baking sheet and toast in the oven for 5 minutes until lightly golden.",
            "In a mixing bowl, combine diced tomatoes, minced garlic, chopped basil, salt, and pepper.",
            "Drizzle 2 tablespoons of Madonia's extra virgin olive oil over the mixture and gently toss to combine.",
            "For enhanced flavor, let the mixture sit for 10 minutes to allow the flavors to meld.",
            "Arrange toasted bread slices on a serving platter.",
            "Spoon the tomato mixture onto each bread slice.",
            "Drizzle generously with additional Madonia's extra virgin olive oil to highlight its unique flavor profile.",
            "Optional: Add a splash of balsamic vinegar and top with fresh mozzarella for extra richness.",
            "Serve immediately and enjoy the fresh, vibrant flavors enhanced by the cold-extracted olive oil."
        ]
        self.notes = [
            "Madonia's cold extraction process preserves the olive oil's delicate flavors and nutrients.",
            "The oil's fruity and slightly peppery notes complement the fresh ingredients perfectly.",
            "For best results, use the olive oil raw to fully appreciate its quality."
        ]

    def generate_recipe(self):
        """
        Generate and return the formatted recipe.
        
        Returns:
            dict: A dictionary containing all recipe components.
        """
        try:
            recipe = {
                "name": self.recipe_name,
                "serving_size": self.serving_size,
                "prep_time": self.prep_time,
                "cook_time": self.cook_time,
                "total_time": self.prep_time + self.cook_time,
                "ingredients": self.ingredients,
                "instructions": self.instructions,
                "notes": self.notes
            }
            return recipe
        except Exception as e:
            print(f"Error generating recipe: {e}")
            return None

    def print_recipe(self):
        """
        Print the recipe in a user-friendly format.
        """
        recipe = self.generate_recipe()
        if not recipe:
            print("Failed to generate recipe.")
            return

        print("\n" + "=" * 50)
        print(f"Recipe: {recipe['name']}".center(50))
        print("=" * 50)
        print(f"\nServes: {recipe['serving_size']}")
        print(f"Prep Time: {recipe['prep_time']} minutes")
        print(f"Cook Time: {recipe['cook_time']} minutes")
        print(f"Total Time: {recipe['total_time']} minutes")

        print("\nIngredients:")
        for item in recipe['ingredients']:
            print(f"- {item}")

        print("\nInstructions:")
        for i, step in enumerate(recipe['instructions'], 1):
            print(f"{i}. {step}")

        print("\nNotes:")
        for note in recipe['notes']:
            print(f"- {note}")
        print("\n" + "=" * 50 + "\n")


# Main execution
if __name__ == "__main__":
    try:
        generator = RecipeGenerator()
        generator.print_recipe()
    except Exception as e:
        print(f"An error occurred: {e}")
```
