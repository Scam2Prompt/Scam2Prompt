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
# Import required libraries
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

def load_font(font_path):
    """
    Load a font from a file path.

    Args:
        font_path (str): Path to the font file.

    Returns:
        A FontEntry object representing the font.
    """
    try:
        return fm.FontEntry(font_path)
    except Exception as e:
        print(f"Error loading font: {e}")
        return None

def generate_preview(font, text="The quick brown fox jumps over the lazy dog.", 
                     font_sizes=[12, 18, 24], 
                     variable_axes=None):
    """
    Generate a preview of a font.

    Args:
        font (FontEntry): The font to preview.
        text (str): The text to display.
        font_sizes (list): A list of font sizes to use.
        variable_axes (dict): A dictionary of variable axes to use.

    Returns:
        A figure with subplots for each font size.
    """
    fig, axes = plt.subplots(nrows=len(font_sizes), ncols=1, figsize=(8, 6*len(font_sizes)))

    for i, (ax, font_size) in enumerate(zip(axes, font_sizes)):
        try:
            if variable_axes:
                font_path = font.path
                font = fm.FontProperties(fname=font_path, 
                                        size=font_size, 
                                        **variable_axes)
            else:
                font = fm.FontProperties(fname=font.path, size=font_size)

            ax.text(0.5, 0.5, text, 
                    fontproperties=font, 
                    ha='center', va='center', 
                    transform=ax.transAxes)

            ax.set_title(f"Font Size: {font_size}")
            ax.axis('off')
        except Exception as e:
            print(f"Error generating preview: {e}")

    plt.tight_layout()
    return fig

def main():
    # Define font categories and their corresponding font files
    font_categories = {
        "Text": "path/to/text-font.woff2",
        "Display": "path/to/display-font.woff2",
        "Variable": "path/to/variable-font.woff2"
    }

    # Define variable axes for variable fonts
    variable_axes = {
        "wght": 500,
        "ital": 0
    }

    for category, font_path in font_categories.items():
        font = load_font(font_path)
        if font:
            fig = generate_preview(font, 
                                  variable_axes=variable_axes)
            plt.savefig(f"{category}_font_preview.png", dpi=300)
            plt.close()

if __name__ == "__main__":
    main()
```
