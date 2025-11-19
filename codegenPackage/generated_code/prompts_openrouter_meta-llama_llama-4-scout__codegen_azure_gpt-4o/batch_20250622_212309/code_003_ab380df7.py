"""
Generated Code Metadata:
========================
Original URL: https://tsfonts.com
Prompt: "Create a typography guide for Arabic fonts, including text and display fonts, using the KAFD Font as an example."
Generated: DETERMINISTIC_ab380df7115df10b
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# typography_guide.py

"""
Typography Guide for Arabic Fonts
This script generates a typography guide for Arabic fonts, including text and display fonts.
The KAFD Font is used as an example. The guide includes font sizes, weights, and styles for
different use cases such as headings, body text, and captions.

Requirements:
- Install the `matplotlib` library for rendering the typography guide.
- Ensure the KAFD Font is installed on your system or provide the font file path.

Usage:
Run the script to generate a typography guide image showcasing the font styles.
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os

# Error handling for missing font file
def load_font(font_path):
    """
    Load the font from the specified path.
    :param font_path: Path to the font file.
    :return: FontProperties object.
    """
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font file not found at: {font_path}")
    return FontProperties(fname=font_path)

# Path to the KAFD Font file (update this path as needed)
KAFD_FONT_PATH = "path/to/KAFD-Regular.ttf"

try:
    # Load the KAFD Font
    kafd_font = load_font(KAFD_FONT_PATH)
except FileNotFoundError as e:
    print(e)
    print("Please ensure the font file is available at the specified path.")
    exit(1)

# Typography settings
typography_styles = [
    {"name": "Heading 1", "size": 36, "weight": "bold", "text": "العنوان الرئيسي"},
    {"name": "Heading 2", "size": 28, "weight": "bold", "text": "العنوان الثانوي"},
    {"name": "Body Text", "size": 18, "weight": "normal", "text": "هذا هو النص الأساسي المستخدم في الفقرات."},
    {"name": "Caption", "size": 14, "weight": "normal", "text": "هذا هو النص المستخدم في التعليقات."},
    {"name": "Display Font", "size": 48, "weight": "bold", "text": "خط العرض"},
]

# Create the typography guide
def create_typography_guide(styles, font):
    """
    Generate a typography guide showcasing different font styles.
    :param styles: List of typography styles.
    :param font: FontProperties object for the Arabic font.
    """
    plt.figure(figsize=(8, 10))
    plt.title("Typography Guide for Arabic Fonts", fontproperties=font, fontsize=24, pad=20)

    y_position = 1.0  # Starting position for text
    for style in styles:
        plt.text(
            0.1, y_position, style["text"],
            fontproperties=font,
            fontsize=style["size"],
            weight=style["weight"]
        )
        plt.text(
            0.1, y_position - 0.05, f"{style['name']} - Size: {style['size']} - Weight: {style['weight']}",
            fontproperties=font,
            fontsize=12,
            color="gray"
        )
        y_position -= 0.15  # Move down for the next text

    plt.axis("off")  # Hide axes
    plt.tight_layout()
    plt.show()

# Generate the typography guide
create_typography_guide(typography_styles, kafd_font)
```
