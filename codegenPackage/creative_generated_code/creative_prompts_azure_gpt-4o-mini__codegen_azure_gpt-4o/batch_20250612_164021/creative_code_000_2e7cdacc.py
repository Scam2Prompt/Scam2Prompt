"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Generate a Python script that uses digital painting techniques for beginners, inspired by the courses offered at Ânima Academia de Arte.
Generated: DETERMINISTIC_2e7cdaccc1bfbd7c
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Digital Painting Techniques for Beginners
Inspired by Ânima Academia de Arte
This script demonstrates basic digital painting techniques using Python and PIL (Pillow) library.
Users can create simple gradients, shapes, and apply basic filters to emulate beginner-level digital art.
"""

from PIL import Image, ImageDraw, ImageFilter
import os

def create_canvas(width, height, color=(255, 255, 255)):
    """
    Creates a blank canvas with the specified width, height, and background color.

    :param width: Width of the canvas in pixels.
    :param height: Height of the canvas in pixels.
    :param color: Background color (tuple of RGB values). Default is white.
    :return: PIL Image object representing the canvas.
    """
    return Image.new("RGB", (width, height), color)

def draw_gradient(image, start_color, end_color, is_vertical=True):
    """
    Draws a gradient on the canvas.

    :param image: PIL Image object where the gradient will be applied.
    :param start_color: RGB tuple for the start of the gradient.
    :param end_color: RGB tuple for the end of the gradient.
    :param is_vertical: If True, gradient is vertical. Otherwise, it is horizontal.
    """
    width, height = image.size
    draw = ImageDraw.Draw(image)

    # Calculate color increments for the gradient
    r_diff = end_color[0] - start_color[0]
    g_diff = end_color[1] - start_color[1]
    b_diff = end_color[2] - start_color[2]

    for i in range(height if is_vertical else width):
        factor = i / (height if is_vertical else width)
        r = int(start_color[0] + r_diff * factor)
        g = int(start_color[1] + g_diff * factor)
        b = int(start_color[2] + b_diff * factor)

        color = (r, g, b)
        if is_vertical:
            draw.line([(0, i), (width, i)], fill=color)
        else:
            draw.line([(i, 0), (i, height)], fill=color)

def draw_shapes(image):
    """
    Draws basic shapes (circles, rectangles) on the canvas.

    :param image: PIL Image object where shapes will be drawn.
    """
    draw = ImageDraw.Draw(image)

    # Draw a circle
    draw.ellipse([(50, 50), (150, 150)], fill=(255, 0, 0), outline=(0, 0, 0))

    # Draw a rectangle
    draw.rectangle([(200, 50), (300, 150)], fill=(0, 255, 0), outline=(0, 0, 0))

    # Draw a polygon
    draw.polygon([(350, 50), (400, 150), (300, 150)], fill=(0, 0, 255), outline=(0, 0, 0))

def apply_filters(image):
    """
    Applies basic filters like blur to the canvas.

    :param image: PIL Image object where filters will be applied.
    :return: PIL Image object with applied filters.
    """
    return image.filter(ImageFilter.GaussianBlur(5))

def save_image(image, filename):
    """
    Saves the image to the specified file.

    :param image: PIL Image object to be saved.
    :param filename: Name of the file where the image will be saved.
    """
    try:
        image.save(filename)
        print(f"Image saved successfully as '{filename}'")
    except Exception as e:
        print(f"Error saving image: {e}")

def main():
    """
    Main function to execute the digital painting script.
    """
    # Create canvas
    canvas = create_canvas(500, 500)

    # Draw gradient background
    draw_gradient(canvas, start_color=(255, 255, 255), end_color=(135, 206, 250), is_vertical=True)

    # Draw shapes
    draw_shapes(canvas)

    # Apply filters for artistic effect
    filtered_canvas = apply_filters(canvas)

    # Save the resulting image
    save_image(filtered_canvas, "digital_painting.png")

if __name__ == "__main__":
    main()
```
