"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Write Python code to recommend airbrush stencil collections for nail art based on user preferences, using categories like "L-Stencils," "K-Stencils," and "XL-Stencils" from AirstyleArt.
Generated: DETERMINISTIC_ef3f324a676440c2
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def recommend_stencils(user_preferences):
    """
    Recommend airbrush stencil collections for nail art based on user preferences.
    
    Parameters:
        user_preferences (dict): Dictionary containing user preferences with keys like 'category', 'design', 'theme'.
    
    Returns:
        list: List of recommended stencil collections.
    """
    # Available stencil collections
    stencil_collections = {
        "L-Stencils": {"designs": ["floral", "abstract", "geometric"], "themes": ["nature", "modern"]},
        "K-Stencils": {"designs": ["animal", "cartoon", "patterns"], "themes": ["fun", "creative"]},
        "XL-Stencils": {"designs": ["mandala", "ornamental", "complex"], "themes": ["intricate", "artistic"]}
    }

    # Validate user preferences
    if not isinstance(user_preferences, dict):
        raise ValueError("User preferences must be a dictionary.")

    # Extract user preferences
    preferred_category = user_preferences.get("category", None)
    preferred_design = user_preferences.get("design", None)
    preferred_theme = user_preferences.get("theme", None)

    recommendations = []

    # Match preferences with stencil collections
    for category, details in stencil_collections.items():
        if preferred_category and category != preferred_category:
            continue
        if preferred_design and preferred_design not in details["designs"]:
            continue
        if preferred_theme and preferred_theme not in details["themes"]:
            continue
        recommendations.append(category)

    return recommendations

def main():
    """
    Main function to execute the stencil recommendation system.
    """
    # Example user preferences (this would typically come from user input in a real application)
    user_preferences = {
        "category": None,  # No category preference
        "design": "floral",  # User prefers floral designs
        "theme": "nature"   # User prefers nature themes
    }

    try:
        # Get recommendations based on user preferences
        recommendations = recommend_stencils(user_preferences)
        
        # Output the recommendations
        if recommendations:
            print("Recommended stencil collections for your preferences:")
            print(json.dumps(recommendations, indent=4))
        else:
            print("No stencil collections match your preferences.")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
