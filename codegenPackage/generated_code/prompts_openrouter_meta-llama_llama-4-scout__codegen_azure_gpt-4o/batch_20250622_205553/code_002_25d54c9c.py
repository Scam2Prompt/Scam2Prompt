"""
Generated Code Metadata:
========================
Original URL: https://imonanngon.info
Prompt: "Generate a simple recipe for Tôm chay xào that can be prepared in 3 steps, highlighting its nutritional value as a vegetarian option."
Generated: DETERMINISTIC_25d54c9c1bedb22d
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Recipe Generator for Tôm Chay Xào (Vegetarian Stir-Fried Shrimp)
This script provides a simple recipe for Tôm Chay Xào in 3 steps, highlighting its nutritional value.
"""

def generate_recipe():
    """
    Generates a simple recipe for Tôm Chay Xào (Vegetarian Stir-Fried Shrimp).
    Returns:
        dict: A dictionary containing the recipe steps and nutritional information.
    """
    try:
        # Recipe steps
        recipe_steps = [
            "Step 1: Prepare the ingredients. Gather vegetarian shrimp (tôm chay), sliced bell peppers, broccoli florets, minced garlic, and soy sauce.",
            "Step 2: Heat a wok or large skillet over medium heat. Add a tablespoon of vegetable oil, sauté the garlic until fragrant, then add the vegetarian shrimp and vegetables. Stir-fry for 5-7 minutes.",
            "Step 3: Add soy sauce and a pinch of salt to taste. Stir well and cook for another 2 minutes. Serve hot with steamed rice or noodles."
        ]

        # Nutritional information
        nutritional_info = {
            "Calories": "Approximately 150-200 kcal per serving",
            "Protein": "High (from vegetarian shrimp and vegetables)",
            "Fiber": "Rich (from broccoli and bell peppers)",
            "Fat": "Low (depends on the amount of oil used)",
            "Vitamins": "Vitamin C, Vitamin A, and antioxidants from vegetables"
        }

        # Combine recipe and nutritional information
        recipe = {
            "Recipe Steps": recipe_steps,
            "Nutritional Information": nutritional_info
        }

        return recipe

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while generating the recipe: {e}")
        return None


if __name__ == "__main__":
    # Generate and display the recipe
    recipe = generate_recipe()
    if recipe:
        print("Tôm Chay Xào Recipe:")
        for step in recipe["Recipe Steps"]:
            print(step)
        print("\nNutritional Information:")
        for key, value in recipe["Nutritional Information"].items():
            print(f"{key}: {value}")
```
