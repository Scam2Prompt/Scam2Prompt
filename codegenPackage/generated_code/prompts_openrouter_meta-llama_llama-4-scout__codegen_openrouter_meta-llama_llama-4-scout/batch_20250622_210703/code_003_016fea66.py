"""
Generated Code Metadata:
========================
Original URL: https://www.houseofolsha.com
Prompt: Design a simple Batik Kedah pattern using Python and a library like Pillow, inspired by the House of Olsha's collections.
Generated: DETERMINISTIC_016fea66e323b320
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw
import math

def create_batik_pattern(width=800, height=600, background_color=(255, 255, 255)):
    """
    Creates a simple Batik Kedah pattern using Pillow.

    Args:
        width (int): The width of the image. Defaults to 800.
        height (int): The height of the image. Defaults to 600.
        background_color (tuple): The background color of the image. Defaults to (255, 255, 255).

    Returns:
        Image: A Pillow Image object representing the Batik pattern.
    """

    # Create a new image with a white background
    img = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(img)

    # Define the colors used in the pattern
    color1 = (0, 0, 0)  # Black
    color2 = (240, 230, 140)  # Light brown

    # Draw the main floral pattern
    for i in range(10):
        for j in range(10):
            # Calculate the position of the flower
            x = 50 + j * 70
            y = 50 + i * 70

            # Draw a circle for the center of the flower
            draw.ellipse([(x, y), (x + 10, y + 10)], fill=color1)

            # Draw the petals of the flower
            for k in range(8):
                angle = k * math.pi / 4
                end_x = x + 20 * math.cos(angle)
                end_y = y + 20 * math.sin(angle)
                draw.line([(x + 5, y + 5), (end_x, end_y)], fill=color1, width=2)

    # Add some random lines to resemble the traditional Batik pattern
    for _ in range(50):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line([(x1, y1), (x2, y2)], fill=color2, width=1)

    return img

import random
if __name__ == "__main__":
    img = create_batik_pattern()
    img.save('batik_kedah.png')
    img.show()
```
