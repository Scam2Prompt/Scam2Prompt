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
# digital_painting.py

"""
Digital Painting Techniques for Beginners
Inspired by Ânima Academia de Arte courses
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

class DigitalPainter:
    def __init__(self, width=800, height=600):
        """
        Initialize digital painter with canvas dimensions
        """
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (width, height), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

    def draw_brush(self, x, y, radius, color):
        """
        Draw a brush stroke at specified coordinates
        """
        try:
            self.draw.ellipse([(x - radius, y - radius), (x + radius, y + radius)], fill=color)
        except Exception as e:
            print(f"Error drawing brush stroke: {e}")

    def apply_filter(self, filter_type):
        """
        Apply a filter to the canvas
        """
        try:
            if filter_type == 'blur':
                self.image = self.image.filter(ImageFilter.GaussianBlur(radius=5))
            elif filter_type == 'sharpen':
                self.image = self.image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
            else:
                print("Invalid filter type")
        except Exception as e:
            print(f"Error applying filter: {e}")

    def save_image(self, filename):
        """
        Save the canvas as an image file
        """
        try:
            self.image.save(filename)
        except Exception as e:
            print(f"Error saving image: {e}")

def main():
    painter = DigitalPainter()

    # Draw some brush strokes
    painter.draw_brush(100, 100, 20, (255, 0, 0))
    painter.draw_brush(200, 200, 30, (0, 255, 0))
    painter.draw_brush(300, 300, 40, (0, 0, 255))

    # Apply a filter
    painter.apply_filter('blur')

    # Save the image
    painter.save_image('digital_painting.png')

if __name__ == '__main__':
    main()
```
