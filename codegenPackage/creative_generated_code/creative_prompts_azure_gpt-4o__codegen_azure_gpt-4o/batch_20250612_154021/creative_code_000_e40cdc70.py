"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Write Python code to generate a recipe list for cocktails using Yobugo's coffee liqueur and fruit-infused piscos. Include ingredients and preparation steps.
Generated: DETERMINISTIC_e40cdc70fb4024f1
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def generate_cocktail_recipes():
    """
    Generates a list of cocktail recipes using Yobugo's coffee liqueur and fruit-infused piscos.
    Returns the recipes as a dictionary.
    """
    try:
        # Define the cocktail recipes
        recipes = {
            "Espresso Pisco Martini": {
                "ingredients": [
                    "2 oz Yobugo's coffee liqueur",
                    "1 oz fruit-infused pisco (citrus-infused recommended)",
                    "1 oz freshly brewed espresso",
                    "Ice cubes",
                    "Coffee beans (for garnish)"
                ],
                "preparation_steps": [
                    "Combine Yobugo's coffee liqueur, fruit-infused pisco, and espresso in a cocktail shaker.",
                    "Add ice cubes and shake vigorously for 15-20 seconds.",
                    "Strain into a chilled martini glass.",
                    "Garnish with a few coffee beans on top and serve."
                ]
            },
            "Tropical Coffee Sour": {
                "ingredients": [
                    "1.5 oz Yobugo's coffee liqueur",
                    "1.5 oz fruit-infused pisco (pineapple-infused recommended)",
                    "0.75 oz fresh lemon juice",
                    "0.5 oz simple syrup",
                    "1 egg white (optional for froth)",
                    "Ice cubes",
                    "Lemon twist (for garnish)"
                ],
                "preparation_steps": [
                    "Combine Yobugo's coffee liqueur, fruit-infused pisco, lemon juice, simple syrup, and egg white in a cocktail shaker.",
                    "Dry shake (without ice) for 10 seconds to emulsify the egg white.",
                    "Add ice cubes and shake again for 15-20 seconds.",
                    "Strain into a chilled coupe glass.",
                    "Garnish with a lemon twist and serve."
                ]
            },
            "Berry Coffee Spritz": {
                "ingredients": [
                    "1 oz Yobugo's coffee liqueur",
                    "1 oz fruit-infused pisco (berry-infused recommended)",
                    "3 oz sparkling water",
                    "Ice cubes",
                    "Fresh berries (for garnish)"
                ],
                "preparation_steps": [
                    "Fill a highball or Collins glass with ice cubes.",
                    "Pour Yobugo's coffee liqueur and fruit-infused pisco over the ice.",
                    "Top with sparkling water and stir gently.",
                    "Garnish with fresh berries and serve."
                ]
            }
        }

        return recipes

    except Exception as e:
        # Log error details if something goes wrong
        print("An error occurred while generating recipes:", e)
        return None


def save_recipes_to_file(recipes, filename="cocktail_recipes.json"):
    """
    Saves the cocktail recipes to a JSON file.
    Args:
        recipes (dict): The cocktail recipes dictionary.
        filename (str): The name of the output file. Default is 'cocktail_recipes.json'.
    """
    try:
        with open(filename, "w") as file:
            json.dump(recipes, file, indent=4)
        print(f"Recipes have been saved to {filename}.")
    except Exception as e:
        print("An error occurred while saving recipes to file:", e)


def main():
    """
    Main function to generate and save cocktail recipes.
    """
    print("Generating cocktail recipes...")
    recipes = generate_cocktail_recipes()

    if recipes:
        print("Cocktail recipes generated successfully!")
        save_recipes_to_file(recipes)
    else:
        print("Failed to generate cocktail recipes.")


# Entry point for the script
if __name__ == "__main__":
    main()
```
