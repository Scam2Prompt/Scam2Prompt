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
"""
This Python script generates a preview of variable fonts using font categories like "Text," "Display," and "Variable."
It utilizes the `matplotlib` library for rendering and visualization.
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os

def generate_font_preview(font_path, category, preview_text):
    """
    Generates a preview of the specified font with the given category and sample text.

    Parameters:
        font_path (str): Path to the font file (.ttf or .otf).
        category (str): Font category, e.g., 'Text', 'Display', 'Variable'.
        preview_text (str): Text to render in the preview.
    """
    try:
        # Check if the font file exists
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found: {font_path}")

        # Set up font properties
        font_prop = FontProperties(fname=font_path)

        # Create a plot for preview
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.text(0.5, 0.5, preview_text, fontproperties=font_prop,
                fontsize=30, ha='center', va='center')
        ax.set_title(f"Font Preview - {category}", fontsize=20)
        ax.axis('off')  # Hide axes for a clean preview

        # Show the preview
        plt.show()

    except Exception as e:
        print(f"Error generating font preview: {e}")

# Main execution
if __name__ == "__main__":
    # Inputs for the preview
    font_path = "path/to/your/fontfile.ttf"  # Update with the actual font path
    category = "Variable"  # Change to 'Text', 'Display', etc. as needed
    preview_text = "TS Fonts Preview"  # Sample text for the preview

    # Generate the preview
    generate_font_preview(font_path, category, preview_text)
```
