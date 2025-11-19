"""
Generated Code Metadata:
========================
Original URL: https://abstract.co.in
Prompt: How can I generate abstract art using Python libraries like Pillow and Random?
Generated: DETERMINISTIC_7d988f53affb77c1
Batch ID: 20250622_211427
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
import random

def generate_abstract_art(width: int = 800, height: int = 600, num_shapes: int = 100) -> Image:
    """
    Generate an abstract art image using Pillow and Random libraries.

    Args:
    width (int): The width of the image. Defaults to 800.
    height (int): The height of the image. Defaults to 600.
    num_shapes (int): The number of shapes to draw. Defaults to 100.

    Returns:
    Image: A Pillow Image object representing the abstract art.
    """

    # Create a new image with white background
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Define a list of possible shapes and colors
    shapes = ['circle', 'rectangle', 'triangle']
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(10)]

    try:
        # Draw random shapes
        for _ in range(num_shapes):
            shape = random.choice(shapes)
            color = random.choice(colors)
            x = random.randint(0, width)
            y = random.randint(0, height)
            size = random.randint(10, 100)

            if shape == 'circle':
                draw.ellipse([(x, y), (x + size, y + size)], fill=color)
            elif shape == 'rectangle':
                draw.rectangle([(x, y), (x + size, y + size)], fill=color)
            elif shape == 'triangle':
                draw.polygon([(x, y), (x + size, y), (x + size / 2, y + size)], fill=color)

        return img

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Generate and save the abstract art
    art = generate_abstract_art()
    if art:
        art.save('abstract_art.png')

if __name__ == "__main__":
    main()
```
