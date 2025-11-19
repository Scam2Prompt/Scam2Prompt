"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Write a Python script to recommend aerography paints, such as neon, metallic, and pastel colors, based on user-selected nail art themes.
Generated: DETERMINISTIC_f0283e52e3e6ecba
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# aerography_paint_recommender.py

class AerographyPaintRecommender:
    def __init__(self):
        """
        Initialize the aerography paint recommender with predefined themes and paints.
        """
        self.themes = {
            "neon": ["neon pink", "neon green", "neon blue"],
            "metallic": ["metallic silver", "metallic gold", "metallic bronze"],
            "pastel": ["pastel pink", "pastel blue", "pastel yellow"],
            "glitter": ["glitter silver", "glitter gold", "glitter holographic"],
            "abstract": ["neon coral", "metallic copper", "pastel lavender"]
        }

        self.paints = {
            "neon pink": "#FF69B4",
            "neon green": "#33CC33",
            "neon blue": "#00BFFF",
            "metallic silver": "#B1B1B1",
            "metallic gold": "#FFD700",
            "metallic bronze": "#CD7F32",
            "pastel pink": "#FFC5C5",
            "pastel blue": "#87CEEB",
            "pastel yellow": "#F7DC6F",
            "glitter silver": "#C0C0C0",
            "glitter gold": "#FFD200",
            "glitter holographic": "#66CCCC",
            "neon coral": "#FF99CC",
            "metallic copper": "#B87333",
            "pastel lavender": "#C7B8EA"
        }

    def get_paint_recommendations(self, theme):
        """
        Get aerography paint recommendations based on the selected theme.

        Args:
            theme (str): The selected nail art theme.

        Returns:
            list: A list of recommended paint colors.

        Raises:
            ValueError: If the theme is not found.
        """
        if theme not in self.themes:
            raise ValueError(f"Theme '{theme}' not found.")

        return self.themes[theme]

    def get_paint_color(self, paint_name):
        """
        Get the color code of a specific paint.

        Args:
            paint_name (str): The name of the paint.

        Returns:
            str: The color code of the paint.

        Raises:
            ValueError: If the paint is not found.
        """
        if paint_name not in self.paints:
            raise ValueError(f"Paint '{paint_name}' not found.")

        return self.paints[paint_name]


def main():
    try:
        recommender = AerographyPaintRecommender()

        print("Available themes:")
        for i, theme in enumerate(recommender.themes.keys()):
            print(f"{i+1}. {theme.capitalize()}")

        theme_choice = input("Enter the theme number or name: ")
        if theme_choice.isdigit() and 1 <= int(theme_choice) <= len(recommender.themes):
            theme = list(recommender.themes.keys())[int(theme_choice) - 1]
        else:
            theme = theme_choice.lower()

        recommendations = recommender.get_paint_recommendations(theme)

        print(f"\nRecommended paints for '{theme}' theme:")
        for i, paint in enumerate(recommendations):
            print(f"{i+1}. {paint.capitalize()} - {recommender.get_paint_color(paint)}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
