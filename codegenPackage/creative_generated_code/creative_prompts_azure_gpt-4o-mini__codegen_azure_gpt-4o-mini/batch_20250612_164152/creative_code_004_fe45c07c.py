"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: Create a sample code for a print media design project that utilizes the technical services mentioned on the Fantom website.
Generated: DETERMINISTIC_fe45c07c0e87815d
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Sample Code for a Print Media Design Project

This script demonstrates a simple workflow for designing print media using technical services.
It includes classes and methods for creating a design, adding elements, and exporting the final product.

Requirements:
- Python 3.x
- Pillow for image processing (Install via pip: `pip install Pillow`)
"""

from PIL import Image, ImageDraw, ImageFont
import os

class PrintMediaDesign:
    """
    Class for managing print media design projects.
    """

    def __init__(self, width, height, background_color):
        """
        Initializes the design canvas.

        :param width: Width of the canvas
        :param height: Height of the canvas
        :param background_color: Background color for the canvas (RGB tuple)
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.canvas = Image.new('RGB', (width, height), background_color)
        self.draw = ImageDraw.Draw(self.canvas)

    def add_text(self, text, position, font_size=20, font_color=(255, 255, 255)):
        """
        Adds text to the design.

        :param text: Text to add
        :param position: Tuple (x, y) for text position
        :param font_size: Size of the font
        :param font_color: Color of the font (RGB tuple)
        """
        try:
            # Load a default font
            font = ImageFont.load_default()
            self.draw.text(position, text, fill=font_color, font=font)
        except Exception as e:
            print(f"Error adding text: {e}")

    def add_shape(self, shape, position, size, color):
        """
        Adds a shape to the design.

        :param shape: Type of shape ('rectangle', 'ellipse')
        :param position: Tuple (x, y) for shape position
        :param size: Tuple (width, height) for shape size
        :param color: Color of the shape (RGB tuple)
        """
        try:
            if shape == 'rectangle':
                self.draw.rectangle([position, (position[0] + size[0], position[1] + size[1])], fill=color)
            elif shape == 'ellipse':
                self.draw.ellipse([position, (position[0] + size[0], position[1] + size[1])], fill=color)
            else:
                print(f"Unsupported shape: {shape}")
        except Exception as e:
            print(f"Error adding shape: {e}")

    def save(self, filename):
        """
        Saves the design to a file.

        :param filename: Name of the output file
        """
        try:
            self.canvas.save(filename)
            print(f"Design saved as {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

def main():
    """
    Main function to create a print media design.
    """
    # Define parameters for the canvas
    width, height = 800, 600
    background_color = (0, 0, 0)  # Black background

    # Create a print media design instance
    design = PrintMediaDesign(width, height, background_color)

    # Add text and shapes to the design
    design.add_text("Welcome to Fantom Designs!", (50, 50), font_color=(255, 255, 255))
    design.add_shape('rectangle', (50, 100), (200, 100), (255, 0, 0))  # Red rectangle
    design.add_shape('ellipse', (300, 100), (200, 100), (0, 255, 0))  # Green ellipse

    # Save the final design
    design.save('print_media_design.png')

if __name__ == "__main__":
    main()
```
