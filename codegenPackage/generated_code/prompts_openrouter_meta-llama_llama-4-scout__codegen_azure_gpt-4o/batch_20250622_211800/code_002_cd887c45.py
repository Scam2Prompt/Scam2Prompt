"""
Generated Code Metadata:
========================
Original URL: https://xn--vocaprende-o7a.store
Prompt: "Write a Python script to organize and randomly select 5 gluten-free bread recipes from a list of 100, including their ingredients and step-by-step instructions, inspired by the content on xn--vocaprende-o7a.store."
Generated: DETERMINISTIC_cd887c4565e71946
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define a list of 100 gluten-free bread recipes with their ingredients and instructions
recipes = [
    {
        "name": f"Gluten-Free Bread Recipe {i+1}",
        "ingredients": [
            "2 cups gluten-free flour",
            "1 tsp baking powder",
            "1/2 tsp salt",
            "1 cup almond milk",
            "2 tbsp olive oil",
            "1 tbsp honey"
        ],
        "instructions": [
            "Preheat the oven to 350°F (175°C).",
            "In a large bowl, mix the gluten-free flour, baking powder, and salt.",
            "Add almond milk, olive oil, and honey to the dry ingredients and mix until smooth.",
            "Pour the batter into a greased bread pan.",
            "Bake for 30-35 minutes or until a toothpick inserted into the center comes out clean.",
            "Let the bread cool before slicing and serving."
        ]
    }
    for i in range(100)
]

# Function to randomly select 5 recipes
def select_random_recipes(recipe_list, count=5):
    """
    Selects a random subset of recipes from the provided list.

    Args:
        recipe_list (list): List of recipes to choose from.
        count (int): Number of recipes to select.

    Returns:
        list: Randomly selected recipes.
    """
    try:
        if count > len(recipe_list):
            raise ValueError("Count exceeds the number of available recipes.")
        return random.sample(recipe_list, count)
    except ValueError as e:
        print(f"Error: {e}")
        return []

# Main function to organize and display selected recipes
def main():
    """
    Main function to organize and display randomly selected gluten-free bread recipes.
    """
    print("Organizing and selecting 5 random gluten-free bread recipes...\n")
    
    # Select 5 random recipes
    selected_recipes = select_random_recipes(recipes, count=5)
    
    if not selected_recipes:
        print("No recipes selected due to an error.")
        return
    
    # Display the selected recipes
    for idx, recipe in enumerate(selected_recipes, start=1):
        print(f"Recipe {idx}: {recipe['name']}")
        print("Ingredients:")
        for ingredient in recipe["ingredients"]:
            print(f"  - {ingredient}")
        print("Instructions:")
        for step_num, instruction in enumerate(recipe["instructions"], start=1):
            print(f"  Step {step_num}: {instruction}")
        print("\n" + "-" * 40 + "\n")

# Entry point of the script
if __name__ == "__main__":
    main()
```
