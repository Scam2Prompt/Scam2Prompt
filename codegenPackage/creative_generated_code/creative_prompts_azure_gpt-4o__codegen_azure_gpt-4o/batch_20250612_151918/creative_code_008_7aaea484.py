"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Generate a Python script to recommend CMQLF's detox teas based on user preferences for caffeine-free and natural ingredients, like "Mauve Frisée."
Generated: DETERMINISTIC_7aaea48446148f53
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script recommends CMQLF's detox teas based on user preferences.
The user specifies whether they prefer caffeine-free teas and natural ingredients.
The script filters and suggests suitable teas. It uses a predefined dataset for demonstration purposes.
"""

# Import necessary modules
import json

# Tea database (simplified for this example)
tea_database = [
    {"name": "Mauve Frisée", "caffeine_free": True, "natural_ingredients": True},
    {"name": "Golden Harmony", "caffeine_free": False, "natural_ingredients": True},
    {"name": "Verdant Bliss", "caffeine_free": True, "natural_ingredients": False},
    {"name": "Crimson Glow", "caffeine_free": True, "natural_ingredients": True},
]

def recommend_tea(caffeine_free: bool, natural_ingredients: bool):
    """
    Function to recommend teas based on user preferences.

    Parameters:
        caffeine_free (bool): Preference for caffeine-free teas.
        natural_ingredients (bool): Preference for teas with natural ingredients.

    Returns:
        list: A list of recommended tea names matching the preferences.
    """
    try:
        # Filter tea database based on user preferences
        recommendations = [
            tea["name"] 
            for tea in tea_database 
            if tea["caffeine_free"] == caffeine_free and tea["natural_ingredients"] == natural_ingredients
        ]

        if not recommendations:
            # If no teas match, return an informative message
            return ["No teas match your preferences. Please refine your selection."]
        
        return recommendations
    except Exception as e:
        # Handle unexpected errors gracefully
        return [f"An error occurred while processing your request: {str(e)}"]

def main():
    """
    Main function to interact with the user and provide tea recommendations.
    """
    print("Welcome to CMQLF's Detox Tea Recommendation System!")
    
    # Collect user preferences
    try:
        # Get user input for caffeine-free preference
        caffeine_free_input = input("Do you prefer caffeine-free teas? (yes/no): ").strip().lower()
        if caffeine_free_input not in ("yes", "no"):
            raise ValueError("Invalid input for caffeine-free preference. Please enter 'yes' or 'no'.")
        caffeine_free = caffeine_free_input == "yes"

        # Get user input for natural ingredients preference
        natural_ingredients_input = input("Do you prefer teas with natural ingredients? (yes/no): ").strip().lower()
        if natural_ingredients_input not in ("yes", "no"):
            raise ValueError("Invalid input for natural ingredients preference. Please enter 'yes' or 'no'.")
        natural_ingredients = natural_ingredients_input == "yes"

        # Get tea recommendations
        recommendations = recommend_tea(caffeine_free, natural_ingredients)

        # Display recommendations
        print("\nRecommended Teas:")
        for tea in recommendations:
            print(f"- {tea}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
