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
import random
from PIL import Image, ImageDraw

def generate_abstract_art(width=800, height=600, num_shapes=50, output_file='abstract_art.png'):
    """
    Generate an abstract art image using random shapes and colors.

    Parameters:
    - width (int): Width of the image.
    - height (int): Height of the image.
    - num_shapes (int): Number of random shapes to draw.
    - output_file (str): Filename to save the generated image.
    """
    try:
        # Create a new image with a white background
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)

        for _ in range(num_shapes):
            # Randomly choose shape parameters
            shape_type = random.choice(['rectangle', 'ellipse'])
            x0 = random.randint(0, width)
            y0 = random.randint(0, height)
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            fill_color = (
                random.randint(0, 255),  # Red
                random.randint(0, 255),  # Green
                random.randint(0, 255)   # Blue
            )
            outline_color = (
                random.randint(0, 255),  # Red
                random.randint(0, 255),  # Green
                random.randint(0, 255)   # Blue
            )

            # Draw the shape
            if shape_type == 'rectangle':
                draw.rectangle([x0, y0, x1, y1], fill=fill_color, outline=outline_color)
            elif shape_type == 'ellipse':
                draw.ellipse([x0, y0, x1, y1], fill=fill_color, outline=outline_color)

        # Save the generated image
        image.save(output_file)
        print(f"Abstract art generated and saved as '{output_file}'.")

    except Exception as e:
        print(f"An error occurred while generating abstract art: {e}")

if __name__ == "__main__":
    generate_abstract_art()
```
