"""
Generated Code Metadata:
========================
Original URL: https://tsfonts.com
Prompt: Write a Python script to generate a preview of variable fonts, specifically using font categories like "Text," "Display," and "Variable" mentioned on TS Fonts.
Generated: DETERMINISTIC_95f5f67ac1cbd030
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# Define a function to generate a preview of variable fonts
def generate_font_preview(font_path, categories, sample_text="The quick brown fox jumps over the lazy dog"):
    """
    Generates a preview of variable fonts based on specified categories.

    Parameters:
    - font_path (str): The path to the variable font file.
    - categories (dict): A dictionary containing font categories and their respective styles.
    - sample_text (str): The text to display in the font preview.
    """
    try:
        # Create a figure for displaying font previews
        fig, axes = plt.subplots(len(categories), 1, figsize=(10, 2 * len(categories)))
        fig.suptitle('Variable Font Preview', fontsize=16)

        # Iterate through each category and its styles
        for ax, (category, styles) in zip(axes, categories.items()):
            ax.set_title(category, fontsize=14)
            ax.axis('off')  # Hide axes

            # Generate a preview for each style in the category
            for style in styles:
                # Create a FontProperties object for the current style
                font_prop = FontProperties(fname=font_path, weight=style.get('weight', 'normal'), 
                                           style=style.get('style', 'normal'), size=20)
                ax.text(0.5, 0.5, sample_text, fontproperties=font_prop, ha='center', va='center')

        plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout
        plt.show()  # Display the font preview

    except Exception as e:
        print(f"An error occurred while generating the font preview: {e}")

# Define the path to the variable font file
font_path = 'path/to/your/variable-font.ttf'  # Update this path

# Define font categories and their styles
font_categories = {
    "Text": [
        {"weight": "400", "style": "normal"},
        {"weight": "700", "style": "normal"},
        {"weight": "400", "style": "italic"},
    ],
    "Display": [
        {"weight": "900", "style": "normal"},
        {"weight": "400", "style": "italic"},
    ],
    "Variable": [
        {"weight": "100", "style": "normal"},
        {"weight": "900", "style": "normal"},
    ]
}

# Generate the font preview
generate_font_preview(font_path, font_categories)
```

Make sure to replace `'path/to/your/variable-font.ttf'` with the actual path to your variable font file before running the script.
