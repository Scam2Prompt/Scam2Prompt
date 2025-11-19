"""
Generated Code Metadata:
========================
Original URL: https://chumchums.xyz
Prompt: "Develop a basic script to generate unique digital art pieces, inspired by the 'Chum Generator 3000' concept."
Generated: DETERMINISTIC_4ae0d9928b28227c
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from PIL import Image, ImageDraw
import colorsys
import random

def generate_art(width=512, height=512):
    """
    Generate a unique digital art piece.

    Args:
        width (int): The width of the art piece. Defaults to 512.
        height (int): The height of the art piece. Defaults to 512.

    Returns:
        PIL.Image: The generated art piece.
    """
    # Create a new image with a white background
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Define the number of shapes to draw
    num_shapes = random.randint(50, 200)

    # Draw shapes
    for _ in range(num_shapes):
        # Randomly select shape type
        shape_type = random.randint(1, 3)

        # Randomly select position, size, and color
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(10, 50)
        hue = random.random()
        saturation = random.uniform(0.5, 1.0)
        value = random.uniform(0.5, 1.0)
        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
        r, g, b = int(r * 255), int(g * 255), int(b * 255)

        # Draw shape
        if shape_type == 1:  # Circle
            draw.ellipse([(x, y), (x + size, y + size)], fill=(r, g, b))
        elif shape_type == 2:  # Square
            draw.rectangle([(x, y), (x + size, y + size)], fill=(r, g, b))
        else:  # Triangle
            draw.polygon([(x, y), (x + size, y), (x + size / 2, y + size)], fill=(r, g, b))

    return img

def save_art(img, filename):
    """
    Save the art piece to a file.

    Args:
        img (PIL.Image): The art piece to save.
        filename (str): The filename to save the art piece as.
    """
    try:
        img.save(filename)
        print(f"Art piece saved to {filename}")
    except Exception as e:
        print(f"Error saving art piece: {e}")

def main():
    # Generate and save art piece
    art = generate_art()
    save_art(art, "art_piece.png")

if __name__ == "__main__":
    main()
```
