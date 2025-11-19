"""
Generated Code Metadata:
========================
Original URL: https://art-blocks.site
Prompt: "Generate Python code for creating digital art blocks using the Pillow library."
Generated: DETERMINISTIC_b5d68be31131bbb5
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw
import random

def create_art_block(size=(100, 100), colors=None, num_shapes=10):
    """
    Create a digital art block with random shapes and colors.

    Parameters:
    - size (tuple): The size of the image in pixels (width, height).
    - colors (list): A list of colors to use for the shapes. If None, a default set of colors will be used.
    - num_shapes (int): The number of shapes to draw on the image.

    Returns:
    - Image: A Pillow Image object containing the generated art block.
    """
    # Set default colors if none are provided
    if colors is None:
        colors = [
            (255, 0, 0),   # Red
            (0, 255, 0),   # Green
            (0, 0, 255),   # Blue
            (255, 255, 0), # Yellow
            (255, 0, 255), # Magenta
            (0, 255, 255), # Cyan
            (255, 165, 0)  # Orange
        ]

    # Create a new image with a white background
    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)

    for _ in range(num_shapes):
        # Randomly select a color
        color = random.choice(colors)

        # Randomly select shape parameters
        shape_type = random.choice(['rectangle', 'ellipse'])
        x1 = random.randint(0, size[0])
        y1 = random.randint(0, size[1])
        x2 = random.randint(0, size[0])
        y2 = random.randint(0, size[1])

        # Draw the selected shape
        if shape_type == 'rectangle':
            draw.rectangle([x1, y1, x2, y2], fill=color, outline="black")
        elif shape_type == 'ellipse':
            draw.ellipse([x1, y1, x2, y2], fill=color, outline="black")

    return image

def save_art_block(image, filename):
    """
    Save the generated art block to a file.

    Parameters:
    - image (Image): The Pillow Image object to save.
    - filename (str): The filename to save the image as.

    Raises:
    - IOError: If the image cannot be saved.
    """
    try:
        image.save(filename)
        print(f"Art block saved as {filename}")
    except IOError as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    # Create a digital art block
    art_block = create_art_block(size=(300, 300), num_shapes=20)

    # Save the art block to a file
    save_art_block(art_block, "art_block.png")
```
