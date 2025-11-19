"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Generate a list of 5 essential oil recipes using dōTERRA oils for natural skincare and beauty treatments.
Generated: DETERMINISTIC_e10fd7f715e69889
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Essential Oil Recipes for Natural Skincare and Beauty Treatments

class EssentialOilRecipe:
    def __init__(self, name, ingredients, instructions):
        """
        Initialize an essential oil recipe.

        :param name: str - The name of the recipe
        :param ingredients: list - A list of ingredients required for the recipe
        :param instructions: str - Step-by-step instructions for preparing the recipe
        """
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def display_recipe(self):
        """
        Display the recipe in a formatted manner.
        """
        print(f"Recipe: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("Instructions:")
        print(self.instructions)
        print("\n" + "-" * 40 + "\n")


def create_recipes():
    """
    Create a list of essential oil recipes for skincare and beauty treatments.
    
    :return: list - A list of EssentialOilRecipe objects
    """
    recipes = []

    # Recipe 1: Lavender Calming Face Mist
    recipes.append(EssentialOilRecipe(
        name="Lavender Calming Face Mist",
        ingredients=[
            "1 cup distilled water",
            "10 drops dōTERRA Lavender essential oil",
            "1 tablespoon witch hazel"
        ],
        instructions="Combine all ingredients in a spray bottle. Shake well before use. "
                     "Spray on face to refresh and calm the skin."
    ))

    # Recipe 2: Tea Tree Acne Treatment
    recipes.append(EssentialOilRecipe(
        name="Tea Tree Acne Treatment",
        ingredients=[
            "2 tablespoons coconut oil",
            "5 drops dōTERRA Tea Tree essential oil",
            "1 drop dōTERRA Lavender essential oil"
        ],
        instructions="Mix all ingredients in a small bowl. Apply a small amount to affected areas "
                     "before bedtime. Rinse off in the morning."
    ))

    # Recipe 3: Frankincense Anti-Aging Serum
    recipes.append(EssentialOilRecipe(
        name="Frankincense Anti-Aging Serum",
        ingredients=[
            "2 tablespoons jojoba oil",
            "5 drops dōTERRA Frankincense essential oil",
            "3 drops dōTERRA Myrrh essential oil"
        ],
        instructions="Combine oils in a dropper bottle. Apply a few drops to the face and neck "
                     "each evening before bed."
    ))

    # Recipe 4: Peppermint Cooling Foot Spray
    recipes.append(EssentialOilRecipe(
        name="Peppermint Cooling Foot Spray",
        ingredients=[
            "1 cup distilled water",
            "10 drops dōTERRA Peppermint essential oil",
            "1 tablespoon apple cider vinegar"
        ],
        instructions="Mix all ingredients in a spray bottle. Shake well and spray on feet for a "
                     "refreshing and cooling effect."
    ))

    # Recipe 5: Citrus Bliss Exfoliating Scrub
    recipes.append(EssentialOilRecipe(
        name="Citrus Bliss Exfoliating Scrub",
        ingredients=[
            "1 cup sugar or sea salt",
            "1/2 cup coconut oil",
            "10 drops dōTERRA Citrus Bliss essential oil"
        ],
        instructions="In a bowl, mix all ingredients until well combined. Use in the shower to "
                     "exfoliate and hydrate the skin."
    ))

    return recipes


def main():
    """
    Main function to execute the program.
    """
    try:
        # Create and display essential oil recipes
        recipes = create_recipes()
        for recipe in recipes:
            recipe.display_recipe()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
