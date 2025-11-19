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

def create_art_block(image_size=(800, 800), block_size=100, output_file="art_block.png"):
    """
    Generates a digital art block image using the Pillow library.

    Parameters:
        image_size (tuple): Size of the output image (width, height).
        block_size (int): Size of each block in the grid.
        output_file (str): File name for saving the generated image.

    Returns:
        None
    """
    try:
        # Create a blank image with a white background
        img = Image.new("RGB", image_size, "white")
        draw = ImageDraw.Draw(img)

        # Calculate the number of blocks in the grid
        rows = image_size[1] // block_size
        cols = image_size[0] // block_size

        # Generate random colors and draw blocks
        for row in range(rows):
            for col in range(cols):
                # Generate a random color
                color = (
                    random.randint(0, 255),  # Red
                    random.randint(0, 255),  # Green
                    random.randint(0, 255)   # Blue
                )
                # Calculate the block's position
                x0 = col * block_size
                y0 = row * block_size
                x1 = x0 + block_size
                y1 = y0 + block_size
                # Draw the block
                draw.rectangle([x0, y0, x1, y1], fill=color)

        # Save the generated image
        img.save(output_file)
        print(f"Art block saved as '{output_file}'")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    create_art_block(image_size=(800, 800), block_size=100, output_file="art_block.png")
```
