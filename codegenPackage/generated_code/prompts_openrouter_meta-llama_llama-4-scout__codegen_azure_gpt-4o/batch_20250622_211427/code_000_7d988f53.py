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

def generate_abstract_art(image_width=800, image_height=800, num_shapes=50, output_file="abstract_art.png"):
    """
    Generates an abstract art image using random shapes and colors.

    Parameters:
        image_width (int): Width of the image in pixels.
        image_height (int): Height of the image in pixels.
        num_shapes (int): Number of random shapes to draw.
        output_file (str): File name to save the generated image.
    """
    try:
        # Create a blank white image
        image = Image.new("RGB", (image_width, image_height), "white")
        draw = ImageDraw.Draw(image)

        for _ in range(num_shapes):
            # Randomly choose a shape type: rectangle, ellipse, or polygon
            shape_type = random.choice(["rectangle", "ellipse", "polygon"])

            # Generate random coordinates for the shape
            x1, y1 = random.randint(0, image_width), random.randint(0, image_height)
            x2, y2 = random.randint(0, image_width), random.randint(0, image_height)

            # Generate a random color
            color = (
                random.randint(0, 255),  # Red
                random.randint(0, 255),  # Green
                random.randint(0, 255)   # Blue
            )

            if shape_type == "rectangle":
                # Draw a rectangle
                draw.rectangle([x1, y1, x2, y2], fill=color)

            elif shape_type == "ellipse":
                # Draw an ellipse
                draw.ellipse([x1, y1, x2, y2], fill=color)

            elif shape_type == "polygon":
                # Draw a polygon with random vertices
                num_vertices = random.randint(3, 6)  # Number of vertices for the polygon
                vertices = [(random.randint(0, image_width), random.randint(0, image_height)) for _ in range(num_vertices)]
                draw.polygon(vertices, fill=color)

        # Save the generated image to a file
        image.save(output_file)
        print(f"Abstract art saved to {output_file}")

    except Exception as e:
        print(f"An error occurred while generating abstract art: {e}")

# Example usage
if __name__ == "__main__":
    generate_abstract_art()
```
