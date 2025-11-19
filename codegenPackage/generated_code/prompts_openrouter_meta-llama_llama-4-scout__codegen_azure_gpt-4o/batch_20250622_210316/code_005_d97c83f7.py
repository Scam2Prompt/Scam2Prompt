"""
Generated Code Metadata:
========================
Original URL: https://laropaestampada.com
Prompt: "Suggest libraries for generating custom patterns and themes for clothing using Python."
Generated: DETERMINISTIC_d97c83f7b7ef46c8
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the use of libraries for generating custom patterns and themes for clothing using Python.
It utilizes popular libraries such as PIL (Pillow) for image manipulation and matplotlib for pattern generation.
"""

# Import necessary libraries
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_pattern(output_path="pattern.png", width=500, height=500, colors=None):
    """
    Generates a custom geometric pattern and saves it as an image file.

    Args:
        output_path (str): Path to save the generated pattern image.
        width (int): Width of the pattern image.
        height (int): Height of the pattern image.
        colors (list): List of colors to use in the pattern. Defaults to a predefined palette.

    Returns:
        None
    """
    try:
        # Default color palette if none is provided
        if colors is None:
            colors = ["#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#8E44AD"]

        # Create a blank image
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)

        # Draw random geometric shapes
        for _ in range(100):  # Number of shapes
            shape_type = np.random.choice(["circle", "rectangle", "line"])
            color = np.random.choice(colors)
            x1, y1 = np.random.randint(0, width), np.random.randint(0, height)
            x2, y2 = np.random.randint(0, width), np.random.randint(0, height)

            if shape_type == "circle":
                draw.ellipse([x1, y1, x2, y2], fill=color, outline=color)
            elif shape_type == "rectangle":
                draw.rectangle([x1, y1, x2, y2], fill=color, outline=color)
            elif shape_type == "line":
                draw.line([x1, y1, x2, y2], fill=color, width=3)

        # Save the generated pattern
        image.save(output_path)
        print(f"Pattern saved to {output_path}")

    except Exception as e:
        print(f"An error occurred while generating the pattern: {e}")


def generate_theme(output_path="theme.png", width=500, height=500, colors=None):
    """
    Generates a custom theme using matplotlib and saves it as an image file.

    Args:
        output_path (str): Path to save the generated theme image.
        width (int): Width of the theme image.
        height (int): Height of the theme image.
        colors (list): List of colors to use in the theme. Defaults to a predefined palette.

    Returns:
        None
    """
    try:
        # Default color palette if none is provided
        if colors is None:
            colors = ["#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#8E44AD"]

        # Generate a random grid pattern
        grid_size = 50  # Size of each grid cell
        rows, cols = height // grid_size, width // grid_size
        data = np.random.choice(colors, size=(rows, cols))

        # Create a figure and plot the grid
        fig, ax = plt.subplots(figsize=(width / 100, height / 100), dpi=100)
        ax.imshow(data, interpolation="nearest")
        ax.axis("off")  # Hide axes

        # Save the generated theme
        plt.savefig(output_path, bbox_inches="tight", pad_inches=0)
        plt.close()
        print(f"Theme saved to {output_path}")

    except Exception as e:
        print(f"An error occurred while generating the theme: {e}")


if __name__ == "__main__":
    # Ensure output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Generate a pattern
    generate_pattern(output_path=os.path.join(output_dir, "custom_pattern.png"))

    # Generate a theme
    generate_theme(output_path=os.path.join(output_dir, "custom_theme.png"))
```
