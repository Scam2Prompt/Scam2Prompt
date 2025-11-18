"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsfonts.com
Prompt: Write a Python script to generate a preview of variable fonts, specifically using font categories like "Text," "Display," and "Variable" mentioned on TS Fonts.
Generated: DETERMINISTIC_95f5f67ac1cbd030
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Define font categories and sample texts for preview
font_categories = {
    "Text": "The quick brown fox jumps over the lazy dog.",
    "Display": "Variable Fonts are the future of typography!",
    "Variable": "Explore the versatility of variable fonts.",
}

# Define the path to the variable font files (update with actual font file paths)
font_paths = {
    "Text": "path/to/your/text-variable-font.ttf",
    "Display": "path/to/your/display-variable-font.ttf",
    "Variable": "path/to/your/variable-font.ttf",
}

def preview_variable_fonts(categories, paths):
    """
    Generates and displays a preview of variable fonts based on the provided categories and font paths.

    :param categories: Dictionary with font category names as keys and sample text as values.
    :param paths: Dictionary with font category names as keys and corresponding font file paths as values.
    """
    # Create a figure for displaying font previews
    fig, axes = plt.subplots(len(categories), 1, figsize=(10, 8))
    fig.suptitle("Variable Font Preview", fontsize=16)

    # Iterate through each category and plot the sample text
    for ax, (category, sample_text) in zip(axes, categories.items()):
        try:
            # Load the font properties
            font_prop = FontProperties(fname=paths[category])
            ax.text(0.5, 0.5, sample_text, fontproperties=font_prop, fontsize=24, ha='center', va='center')
            ax.set_title(category, fontsize=14)
            ax.axis('off')  # Hide axes
        except Exception as e:
            ax.text(0.5, 0.5, f"Error loading font: {e}", fontsize=12, ha='center', va='center')
            ax.axis('off')  # Hide axes for error message

    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout
    plt.show()

if __name__ == "__main__":
    preview_variable_fonts(font_categories, font_paths)
```

Ensure to replace the placeholder paths in the `font_paths` dictionary with the actual paths to your variable font files before running the script.
