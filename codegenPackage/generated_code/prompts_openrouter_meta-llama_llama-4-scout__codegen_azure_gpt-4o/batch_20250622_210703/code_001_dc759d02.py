"""
Generated Code Metadata:
========================
Original URL: https://paintersmorningtonpeninsula.com.au
Prompt: Write a Python script to generate a color palette for a residential painting project in Mornington Peninsula, considering factors like natural lighting, existing decor, and personal preferences, as discussed on the Painters Mornington Peninsula website.
Generated: DETERMINISTIC_dc759d02205fe8fc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random

# Define a function to generate a color palette based on user preferences and environmental factors
def generate_color_palette(natural_lighting, existing_decor, personal_preferences):
    """
    Generate a color palette for a residential painting project.

    Parameters:
        natural_lighting (str): The type of natural lighting (e.g., "bright", "dim", "neutral").
        existing_decor (list): A list of existing decor colors (e.g., ["beige", "gray"]).
        personal_preferences (list): A list of preferred colors (e.g., ["blue", "green"]).

    Returns:
        dict: A dictionary containing the generated color palette.
    """
    # Define base color options based on natural lighting
    lighting_based_colors = {
        "bright": ["white", "light yellow", "sky blue", "pastel green"],
        "dim": ["warm beige", "soft gray", "deep blue", "earthy brown"],
        "neutral": ["off-white", "light gray", "sage green", "soft pink"]
    }

    # Validate natural lighting input
    if natural_lighting not in lighting_based_colors:
        raise ValueError("Invalid natural lighting value. Choose from 'bright', 'dim', or 'neutral'.")

    # Generate a base palette from lighting-based colors
    base_palette = lighting_based_colors[natural_lighting]

    # Incorporate existing decor colors into the palette
    decor_palette = [color for color in existing_decor if color not in base_palette]

    # Incorporate personal preferences into the palette
    preference_palette = [color for color in personal_preferences if color not in base_palette]

    # Combine all palettes and ensure uniqueness
    final_palette = list(set(base_palette + decor_palette + preference_palette))

    # Randomly shuffle the palette for variety
    random.shuffle(final_palette)

    # Return the final palette as a dictionary
    return {
        "natural_lighting": natural_lighting,
        "existing_decor": existing_decor,
        "personal_preferences": personal_preferences,
        "generated_palette": final_palette
    }

# Main function to interact with the user and generate the palette
def main():
    """
    Main function to interact with the user and generate a color palette.
    """
    print("Welcome to the Residential Painting Color Palette Generator!")
    print("Please provide the following details to generate your custom palette.")

    try:
        # Get user input for natural lighting
        natural_lighting = input("Enter the type of natural lighting (bright, dim, neutral): ").strip().lower()

        # Get user input for existing decor colors
        existing_decor = input("Enter existing decor colors (comma-separated, e.g., beige, gray): ").strip().lower().split(',')

        # Get user input for personal preferences
        personal_preferences = input("Enter your preferred colors (comma-separated, e.g., blue, green): ").strip().lower().split(',')

        # Generate the color palette
        palette = generate_color_palette(natural_lighting, existing_decor, personal_preferences)

        # Display the generated palette
        print("\nGenerated Color Palette:")
        print(json.dumps(palette, indent=4))

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
