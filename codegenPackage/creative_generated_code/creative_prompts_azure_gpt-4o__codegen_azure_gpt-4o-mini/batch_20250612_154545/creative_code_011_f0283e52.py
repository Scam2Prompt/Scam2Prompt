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

# Define a data structure for themes and their recommended paints
PAINT_RECOMMENDATIONS = {
    "Floral": ["Pastel Pink", "Lavender", "Mint Green", "Sunflower Yellow"],
    "Geometric": ["Neon Green", "Electric Blue", "Hot Pink", "Metallic Silver"],
    "Galaxy": ["Metallic Purple", "Neon Blue", "Dark Blue", "Black"],
    "Ocean": ["Teal", "Turquoise", "Coral", "Pastel Blue"],
    "Vintage": ["Pastel Peach", "Muted Yellow", "Dusty Rose", "Metallic Gold"]
}

def get_user_input():
    """Prompt the user to select a nail art theme and return the selection."""
    print("Select a nail art theme from the following options:")
    for theme in PAINT_RECOMMENDATIONS.keys():
        print(f"- {theme}")
    
    while True:
        user_theme = input("Enter your chosen theme: ").strip()
        if user_theme in PAINT_RECOMMENDATIONS:
            return user_theme
        else:
            print("Invalid theme. Please select a valid theme from the list.")

def recommend_paints(theme):
    """Return a list of recommended paints for the given theme."""
    return PAINT_RECOMMENDATIONS.get(theme, [])

def main():
    """Main function to execute the paint recommendation script."""
    try:
        selected_theme = get_user_input()
        recommended_paints = recommend_paints(selected_theme)
        
        print(f"\nRecommended aerography paints for the '{selected_theme}' theme:")
        for paint in recommended_paints:
            print(f"- {paint}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
