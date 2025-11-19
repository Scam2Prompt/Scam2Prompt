"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Write a Python script to create a cocktail recipe generator that includes Yobugo's Pisco Afrutado flavors.
Generated: DETERMINISTIC_50f84fa86854a7e3
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Define the available Pisco Afrutado flavors from Yobugo
PISCO_FLAVORS = [
    "Pisco Afrutado Mango",
    "Pisco Afrutado Passion Fruit",
    "Pisco Afrutado Pineapple",
    "Pisco Afrutado Berry",
    "Pisco Afrutado Citrus"
]

# Define other cocktail ingredients
COCKTAIL_BASES = ["Soda Water", "Tonic Water", "Ginger Ale", "Lemonade"]
SWEETENERS = ["Sugar Syrup", "Honey", "Agave Syrup"]
GARNISHES = ["Lime Slice", "Mint Leaves", "Cherries", "Orange Peel", "Berries"]
EXTRAS = ["Ice Cubes", "Crushed Ice", "Fresh Fruit Pieces"]

# Function to generate a random cocktail recipe
def generate_cocktail_recipe():
    """
    Generate a random cocktail recipe featuring Yobugo's Pisco Afrutado flavors.

    Returns:
        dict: A dictionary containing the cocktail recipe.
    """
    try:
        # Randomly select one flavor, base, sweetener, garnish, and extra ingredients
        flavor = random.choice(PISCO_FLAVORS)
        base = random.choice(COCKTAIL_BASES)
        sweetener = random.choice(SWEETENERS)
        garnish = random.choice(GARNISHES)
        extra = random.choice(EXTRAS)

        # Construct the recipe
        recipe = {
            "Main Flavor": flavor,
            "Base": base,
            "Sweetener": sweetener,
            "Garnish": garnish,
            "Extra": extra,
            "Instructions": "Mix the Pisco Afrutado flavor with the base and sweetener in a shaker. "
                            "Pour into a glass over the extra ingredient, and garnish with the selected garnish. Enjoy!"
        }

        return recipe
    
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while generating the cocktail recipe: {e}")
        return None

# Main function to run the cocktail recipe generator
def main():
    """
    Main function to execute the cocktail recipe generator.
    """
    try:
        print("Welcome to the Yobugo Pisco Afrutado Cocktail Recipe Generator!")
        print("Generating a random cocktail recipe for you...\n")
        
        # Generate and display the recipe
        recipe = generate_cocktail_recipe()
        if recipe:
            print("Here is your cocktail recipe:\n")
            for key, value in recipe.items():
                print(f"{key}: {value}")
        else:
            print("Failed to generate a recipe. Please try again.")
    
    except KeyboardInterrupt:
        print("\nOperation interrupted by user. Exiting the program.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
