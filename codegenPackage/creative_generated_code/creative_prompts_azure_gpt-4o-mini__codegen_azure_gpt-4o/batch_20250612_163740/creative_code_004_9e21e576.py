"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancaskewap.finance
Prompt: Develop a program that suggests pancake toppings based on user preferences, including options for sweet and savory combinations.
Generated: DETERMINISTIC_9e21e5762a46f5b4
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def get_pancake_toppings(preferences):
    """
    Suggest pancake toppings based on user preferences.

    Parameters:
        preferences (dict): Dictionary containing user's preferences with the keys:
            - 'sweet': bool indicating preference for sweet toppings
            - 'savory': bool indicating preference for savory toppings
            - 'dietary_restrictions': list of dietary restrictions (e.g., 'vegan', 'gluten-free')

    Returns:
        list: List of suggested toppings.
    """
    # Sweet toppings
    sweet_toppings = {
        "vegan": ["maple syrup", "fresh fruits", "agave nectar"],
        "gluten-free": ["maple syrup", "fresh fruits", "honey"],
        "default": ["maple syrup", "whipped cream", "chocolate chips", "fresh fruits"]
    }

    # Savory toppings
    savory_toppings = {
        "vegan": ["avocado slices", "sautéed vegetables", "hummus"],
        "gluten-free": ["fried egg", "bacon", "cheese"],
        "default": ["fried egg", "bacon", "cheese", "avocado slices"]
    }

    try:
        # Determine user's dietary restrictions
        dietary_restrictions = preferences.get("dietary_restrictions", [])
        sweet = preferences.get("sweet", False)
        savory = preferences.get("savory", False)

        # Filter toppings based on dietary restrictions
        if "vegan" in dietary_restrictions:
            selected_sweet_toppings = sweet_toppings["vegan"]
            selected_savory_toppings = savory_toppings["vegan"]
        elif "gluten-free" in dietary_restrictions:
            selected_sweet_toppings = sweet_toppings["gluten-free"]
            selected_savory_toppings = savory_toppings["gluten-free"]
        else:
            selected_sweet_toppings = sweet_toppings["default"]
            selected_savory_toppings = savory_toppings["default"]

        # Suggest toppings based on preferences
        suggested_toppings = []
        if sweet:
            suggested_toppings.extend(selected_sweet_toppings)
        if savory:
            suggested_toppings.extend(selected_savory_toppings)

        # Remove duplicates and return the list
        return list(set(suggested_toppings))
    except Exception as e:
        print(f"Error processing preferences: {e}", file=sys.stderr)
        return []

def main():
    """
    Main function to interact with the user and suggest pancake toppings.
    """
    print("Welcome to the Pancake Topping Suggestion Program!")
    
    # Gather user preferences
    try:
        sweet = input("Do you prefer sweet toppings? (yes/no): ").strip().lower() == "yes"
        savory = input("Do you prefer savory toppings? (yes/no): ").strip().lower() == "yes"
        
        dietary_restrictions_input = input("Do you have any dietary restrictions? (e.g., vegan, gluten-free, none): ").strip().lower()
        dietary_restrictions = dietary_restrictions_input.split(",") if dietary_restrictions_input != "none" else []
        
        preferences = {
            "sweet": sweet,
            "savory": savory,
            "dietary_restrictions": [restriction.strip() for restriction in dietary_restrictions]
        }

        # Get suggested toppings
        toppings = get_pancake_toppings(preferences)
        
        if toppings:
            print("\nBased on your preferences, we suggest the following pancake toppings:")
            for topping in toppings:
                print(f"- {topping}")
        else:
            print("\nSorry, we couldn't find any suitable toppings for your preferences.")
    except Exception as e:
        print(f"An error occurred while gathering preferences: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
