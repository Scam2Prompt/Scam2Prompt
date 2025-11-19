"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Illustrate how to use Karnataka Aromas' flavor ingredients in a recipe application by writing a function that suggests combinations based on user preferences.
Generated: DETERMINISTIC_ee04de79cb13ad00
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# RecipeSuggestion class to encapsulate flavor ingredient logic
class RecipeSuggestion:
    def __init__(self):
        # Predefined flavor ingredients from Karnataka Aromas
        self.flavor_ingredients = {
            "spicy": ["ginger", "chili", "pepper"],
            "sweet": ["vanilla", "cinnamon", "cardamom"],
            "savory": ["garlic", "onion", "cumin"],
            "fruity": ["mango", "pineapple", "coconut"],
            "herbal": ["mint", "basil", "thyme"]
        }

    def suggest_combinations(self, preferences):
        """
        Suggests ingredient combinations based on user preferences.
        
        :param preferences: List of flavor categories (e.g., ['sweet', 'herbal'])
        :type preferences: list
        :return: List of suggested ingredient combinations
        :rtype: list
        """
        if not preferences:
            raise ValueError("Preferences must not be empty.")
        
        suggestions = []
        
        for preference in preferences:
            if preference in self.flavor_ingredients:
                # Randomly select two ingredients from the preferred flavor category
                combinations = random.sample(self.flavor_ingredients[preference], 2)
                suggestions.append(combinations)
            else:
                raise ValueError(f"Invalid preference: {preference}. Valid options are {list(self.flavor_ingredients.keys())}.")
        
        return suggestions


# Example usage
if __name__ == "__main__":
    try:
        # Instantiate the RecipeSuggestion class
        recipe_suggestion = RecipeSuggestion()

        # User preferences (this can be gathered from user input in a real application)
        user_preferences = ["sweet", "spicy", "fruity"]
        
        # Generate and display suggestions
        suggestions = recipe_suggestion.suggest_combinations(user_preferences)
        print("Ingredient combinations based on your preferences:")
        for i, combination in enumerate(suggestions, start=1):
            print(f"{i}. {combination}")
    except ValueError as e:
        # Handle errors related to user input
        print(f"Error: {e}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")
```
