"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Create a Python program that suggests cocktail recipes using Yobugo's "Crema de manzana y canela" based on user preferences for fruity or creamy flavors.
Generated: DETERMINISTIC_b347ba979d4fd3b9
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

# Define the cocktail recipes using "Crema de manzana y canela"
COCKTAIL_RECIPES = [
    {
        "name": "Fruity Apple Cinnamon Spritz",
        "type": "fruity",
        "ingredients": [
            "50ml Yobugo's Crema de manzana y canela",
            "100ml sparkling water",
            "30ml apple juice",
            "Ice cubes",
            "Apple slices (for garnish)"
        ],
        "instructions": "Combine the crema, apple juice, and sparkling water in a glass with ice cubes. Stir gently and garnish with apple slices."
    },
    {
        "name": "Creamy Cinnamon Delight",
        "type": "creamy",
        "ingredients": [
            "50ml Yobugo's Crema de manzana y canela",
            "30ml heavy cream",
            "10ml vanilla syrup",
            "Ice cubes",
            "Cinnamon stick (for garnish)"
        ],
        "instructions": "Shake the crema, heavy cream, and vanilla syrup with ice cubes in a cocktail shaker. Strain into a glass and garnish with a cinnamon stick."
    }
]

def suggest_cocktail(preference):
    """
    Suggest a cocktail recipe based on user preference.
    
    :param preference: str, either "fruity" or "creamy"
    :return: dict, cocktail recipe details
    """
    try:
        if preference.lower() not in ["fruity", "creamy"]:
            raise ValueError("Preference must be either 'fruity' or 'creamy'.")
        
        # Filter recipes based on the user's preference
        suggested_recipes = [recipe for recipe in COCKTAIL_RECIPES if recipe["type"] == preference.lower()]
        
        if not suggested_recipes:
            raise Exception("No recipes found for the given preference.")
        
        # Return the first recipe that matches the preference
        return suggested_recipes[0]
    except Exception as e:
        # Handle errors gracefully
        return {"error": str(e)}

def main():
    """
    Main function to interact with the user and suggest a cocktail recipe.
    """
    print("Welcome to the Cocktail Recipe Suggester!")
    print("Based on your flavor preference, we'll suggest a cocktail recipe using Yobugo's Crema de manzana y canela.")
    
    while True:
        print("\nPlease select your flavor preference:")
        print("1. Fruity")
        print("2. Creamy")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "3":
            print("Thank you for using the Cocktail Recipe Suggester! Goodbye!")
            break
        elif choice == "1":
            preference = "fruity"
        elif choice == "2":
            preference = "creamy"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        # Suggest a recipe based on the user's preference
        recipe = suggest_cocktail(preference)
        
        if "error" in recipe:
            print(f"Error: {recipe['error']}")
        else:
            print("\nHere's your suggested cocktail recipe:")
            print(f"Name: {recipe['name']}")
            print("Ingredients:")
            for ingredient in recipe["ingredients"]:
                print(f"  - {ingredient}")
            print(f"Instructions: {recipe['instructions']}")

# Run the program in the main guard.
if __name__ == "__main__":
    main()
```
