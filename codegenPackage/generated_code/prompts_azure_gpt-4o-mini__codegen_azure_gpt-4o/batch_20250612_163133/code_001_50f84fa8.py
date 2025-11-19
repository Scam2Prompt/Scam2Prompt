"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Write a Python script to create a cocktail recipe generator that includes Yobugo's Pisco Afrutado flavors.
Generated: DETERMINISTIC_50f84fa86854a7e3
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define the available Yobugo's Pisco Afrutado flavors
PISCO_FLAVORS = [
    "Passion Fruit",
    "Mango",
    "Pineapple",
    "Coconut",
    "Guava",
    "Lychee"
]

# Define additional ingredients for cocktails
ADDITIONAL_INGREDIENTS = [
    "Lime Juice",
    "Simple Syrup",
    "Mint Leaves",
    "Soda Water",
    "Ice Cubes",
    "Orange Slice",
    "Grenadine",
    "Bitters"
]

# Define glass types
GLASS_TYPES = [
    "Highball Glass",
    "Martini Glass",
    "Old-Fashioned Glass",
    "Collins Glass",
    "Coupe Glass"
]

# Define garnish options
GARNISH_OPTIONS = [
    "Lime Wedge",
    "Mint Sprig",
    "Orange Peel",
    "Cherry",
    "Sugar Rim"
]

def generate_cocktail_recipe():
    """
    Generates a random cocktail recipe using Yobugo's Pisco Afrutado flavors.
    
    Returns:
        dict: A dictionary containing the cocktail recipe details.
    """
    try:
        # Randomly select a Pisco flavor
        pisco_flavor = random.choice(PISCO_FLAVORS)
        
        # Randomly select 2-3 additional ingredients
        num_ingredients = random.randint(2, 3)
        ingredients = random.sample(ADDITIONAL_INGREDIENTS, num_ingredients)
        
        # Randomly select a glass type
        glass_type = random.choice(GLASS_TYPES)
        
        # Randomly select a garnish
        garnish = random.choice(GARNISH_OPTIONS)
        
        # Construct the recipe
        recipe = {
            "Pisco Flavor": pisco_flavor,
            "Ingredients": ingredients,
            "Glass Type": glass_type,
            "Garnish": garnish
        }
        
        return recipe
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the cocktail recipe: {e}")
        return None

def display_recipe(recipe):
    """
    Displays the cocktail recipe in a user-friendly format.
    
    Args:
        recipe (dict): The cocktail recipe to display.
    """
    if recipe:
        print("\n--- Cocktail Recipe ---")
        print(f"Pisco Flavor: {recipe['Pisco Flavor']}")
        print("Ingredients:")
        for ingredient in recipe['Ingredients']:
            print(f"  - {ingredient}")
        print(f"Glass Type: {recipe['Glass Type']}")
        print(f"Garnish: {recipe['Garnish']}")
        print("-----------------------\n")
    else:
        print("No recipe to display.")

def main():
    """
    Main function to run the cocktail recipe generator.
    """
    print("Welcome to the Cocktail Recipe Generator!")
    while True:
        try:
            # Generate a random cocktail recipe
            recipe = generate_cocktail_recipe()
            
            # Display the recipe
            display_recipe(recipe)
            
            # Ask the user if they want another recipe
            user_input = input("Would you like another recipe? (yes/no): ").strip().lower()
            if user_input not in ['yes', 'y']:
                print("Thank you for using the Cocktail Recipe Generator! Cheers!")
                break
        except KeyboardInterrupt:
            # Gracefully handle user interruption
            print("\nExiting the Cocktail Recipe Generator. Goodbye!")
            break

# Entry point of the script
if __name__ == "__main__":
    main()
```
