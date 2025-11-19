"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Generate a Python script that uses digital painting techniques for beginners, inspired by the courses offered at Ânima Academia de Arte.
Generated: DETERMINISTIC_2e7cdaccc1bfbd7c
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Painting Techniques for Beginners
This script provides a basic framework for digital painting using Python's PIL (Pillow) library.
It allows users to create a canvas, draw basic shapes, and apply simple effects.
Inspired by courses offered at Ânima Academia de Arte.
"""

from PIL import Image, ImageDraw, ImageFilter
import os

def create_canvas(width=800, height=600, color=(255, 255, 255)):
    """
    Creates a blank canvas with the specified dimensions and background color.
    
    Args:
        width (int): Width of the canvas in pixels.
        height (int): Height of the canvas in pixels.
        color (tuple): Background color in RGB format.
    
    Returns:
        Image: A PIL Image object representing the canvas.
    """
    return Image.new("RGB", (width, height), color)

def draw_shapes(draw, shape_type="circle", position=(100, 100, 200, 200), color=(0, 0, 0)):
    """
    Draws basic shapes on the canvas.
    
    Args:
        draw (ImageDraw.Draw): A drawing object to draw on the canvas.
        shape_type (str): Type of shape to draw ("circle", "rectangle", "line").
        position (tuple): Coordinates for the shape (varies by shape type).
        color (tuple): Color of the shape in RGB format.
    """
    if shape_type == "circle":
        draw.ellipse(position, fill=color)
    elif shape_type == "rectangle":
        draw.rectangle(position, fill=color)
    elif shape_type == "line":
        draw.line(position, fill=color, width=3)
    else:
        raise ValueError("Unsupported shape type. Use 'circle', 'rectangle', or 'line'.")

def apply_effects(image, effect_type="blur"):
    """
    Applies simple effects to the canvas.
    
    Args:
        image (Image): The canvas image to apply effects to.
        effect_type (str): Type of effect to apply ("blur", "sharpen").
    
    Returns:
        Image: The modified image with the applied effect.
    """
    if effect_type == "blur":
        return image.filter(ImageFilter.BLUR)
    elif effect_type == "sharpen":
        return image.filter(ImageFilter.SHARPEN)
    else:
        raise ValueError("Unsupported effect type. Use 'blur' or 'sharpen'.")

def save_canvas(image, filename="digital_painting.png"):
    """
    Saves the canvas to a file.
    
    Args:
        image (Image): The canvas image to save.
        filename (str): Name of the file to save the image as.
    """
    try:
        image.save(filename)
        print(f"Canvas saved as {filename}")
    except Exception as e:
        print(f"Error saving canvas: {e}")

def main():
    """
    Main function to demonstrate digital painting techniques.
    """
    # Create a blank canvas
    canvas = create_canvas()

    # Create a drawing object
    draw = ImageDraw.Draw(canvas)

    # Draw some shapes
    draw_shapes(draw, shape_type="circle", position=(100, 100, 200, 200), color=(255, 0, 0))
    draw_shapes(draw, shape_type="rectangle", position=(300, 100, 400, 200), color=(0, 255, 0))
    draw_shapes(draw, shape_type="line", position=(500, 100, 600, 200), color=(0, 0, 255))

    # Apply effects
    canvas = apply_effects(canvas, effect_type="blur")

    # Save the canvas
    save_canvas(canvas)

if __name__ == "__main__":
    main()
```
