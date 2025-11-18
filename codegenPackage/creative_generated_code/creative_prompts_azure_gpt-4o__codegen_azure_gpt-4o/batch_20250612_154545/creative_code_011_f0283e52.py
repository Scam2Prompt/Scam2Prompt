"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Write a Python script to recommend aerography paints, such as neon, metallic, and pastel colors, based on user-selected nail art themes.
Generated: DETERMINISTIC_f0283e52e3e6ecba
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

# Define paint options for different themes
PAINTS = {
    "floral": ["pastel pink", "pastel green", "metallic gold", "neon yellow"],
    "galaxy": ["metallic silver", "metallic blue", "neon purple", "black"],
    "retro": ["neon pink", "neon orange", "pastel blue", "metallic green"],
    "minimalist": ["pastel beige", "white", "metallic rose gold", "gray"],
    "abstract": ["neon red", "neon green", "metallic yellow", "black"]
}

def get_paint_recommendations(theme):
    """
    Get recommended aerography paints based on the nail art theme.
    
    Args:
        theme (str): The selected nail art theme.
        
    Returns:
        list: List of recommended paint colors.
        
    Raises:
        ValueError: If the theme is not recognized.
    """
    if theme not in PAINTS:
        raise ValueError(f"Theme '{theme}' not recognized. Available themes: {', '.join(PAINTS.keys())}.")
    return PAINTS[theme]

def main():
    """
    Main function to interact with the user and recommend nail art paints.
    """
    print("Welcome to the Nail Art Paint Recommender!")
    print("Available themes: floral, galaxy, retro, minimalist, abstract")
    
    try:
        # Get user input for theme
        theme = input("Please enter your nail art theme: ").strip().lower()
        
        # Fetch recommendations
        recommendations = get_paint_recommendations(theme)
        
        print("\nRecommended Paints for Theme '{}':".format(theme.capitalize()))
        for paint in recommendations:
            print(f"- {paint}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the Nail Art Paint Recommender!")

if __name__ == "__main__":
    main()
```
