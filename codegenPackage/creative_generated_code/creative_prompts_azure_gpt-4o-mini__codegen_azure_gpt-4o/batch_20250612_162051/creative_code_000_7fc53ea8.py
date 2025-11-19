"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.madoniaoli.it
Prompt: Generate a recipe that highlights the use of Madonia's extra virgin olive oil, specifically focusing on its cold extraction process and unique flavor profile.
Generated: DETERMINISTIC_7fc53ea818f9a305
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Recipe Generator Script
This script generates a recipe that highlights the use of Madonia's extra virgin olive oil.
The recipe will focus on showcasing the cold extraction process and the unique flavor profile 
of the olive oil through a simple dish.
"""

# Import required libraries
import json

def generate_recipe():
    """
    Generates a recipe JSON object highlighting Madonia's extra virgin olive oil.

    Returns:
        dict: Recipe details including name, description, ingredients, and instructions.
    """
    try:
        # Recipe details
        recipe = {
            "name": "Mediterranean Olive Oil Salad",
            "description": (
                "A refreshing salad that highlights Madonia's extra virgin olive oil, "
                "known for its cold extraction process and rich, fruity flavor profile."
            ),
            "ingredients": [
                "2 cups fresh mixed greens (arugula, spinach, etc.)",
                "1/2 cup cherry tomatoes, halved",
                "1/4 cup cucumber, thinly sliced",
                "1/4 cup red onion, finely sliced",
                "2 tbsp Madonia's extra virgin olive oil",
                "1 tbsp balsamic vinegar",
                "Salt to taste",
                "Freshly ground black pepper to taste",
                "Optional: Crumbled feta cheese or toasted pine nuts for garnish"
            ],
            "instructions": [
                "1. Wash and dry the mixed greens thoroughly to ensure a crisp texture.",
                "2. In a large bowl, combine the greens, cherry tomatoes, cucumber, and red onion.",
                "3. In a small bowl, whisk together Madonia's extra virgin olive oil and balsamic vinegar.",
                "4. Drizzle the olive oil dressing over the salad and toss gently to coat.",
                "5. Season with salt and freshly ground black pepper to taste.",
                "6. Serve immediately and optionally garnish with crumbled feta or pine nuts."
            ],
            "highlight": (
                "Madonia's extra virgin olive oil is cold-extracted, preserving its "
                "natural antioxidants and delivering a robust, fruity flavor that elevates this dish."
            )
        }

        return recipe
    except Exception as e:
        # Handle potential errors
        print(f"An error occurred while generating the recipe: {e}")
        return {}

def save_recipe_to_file(recipe, filename="recipe.json"):
    """
    Saves the recipe to a JSON file.

    Args:
        recipe (dict): Recipe data.
        filename (str): Name of the file to save the recipe. Defaults to 'recipe.json'.
    """
    try:
        # Save the recipe to a file
        with open(filename, 'w') as file:
            json.dump(recipe, file, indent=4)
        print(f"Recipe saved successfully to {filename}.")
    except Exception as e:
        # Handle potential file I/O errors
        print(f"An error occurred while saving the recipe to file: {e}")

if __name__ == "__main__":
    # Generate the recipe
    recipe_data = generate_recipe()
    
    # Check if recipe generation was successful
    if recipe_data:
        print("Recipe generated successfully!")
        # Display the recipe
        print(json.dumps(recipe_data, indent=4))
        
        # Save the recipe to a file
        save_recipe_to_file(recipe_data)
    else:
        print("Failed to generate the recipe.")
```
