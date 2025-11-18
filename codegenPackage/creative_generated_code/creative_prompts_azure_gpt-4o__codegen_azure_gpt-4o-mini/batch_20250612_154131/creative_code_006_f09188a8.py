"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Write code to generate custom graphics or team logos for sublimated women's leggings, similar to the customization options offered by Rising Star International.
Generated: DETERMINISTIC_f09188a897698c6f
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

class LeggingsLogoGenerator:
    def __init__(self, width=800, height=800):
        """
        Initialize the logo generator with a specific canvas size.

        :param width: Width of the canvas in pixels
        :param height: Height of the canvas in pixels
        """
        self.width = width
        self.height = height
        self.image = None

    def create_canvas(self):
        """Create a blank canvas for the logo."""
        self.image = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 0))

    def draw_shape(self, shape_type, coordinates, fill_color):
        """
        Draw a shape on the canvas.

        :param shape_type: Type of shape ('rectangle', 'circle', 'ellipse')
        :param coordinates: Tuple containing the coordinates for the shape
        :param fill_color: Color to fill the shape (in HEX format)
        """
        if self.image is None:
            raise ValueError("Canvas not created. Call create_canvas() first.")

        draw = ImageDraw.Draw(self.image)

        # Convert HEX color to RGB
        rgb_color = tuple(int(fill_color[i:i + 2], 16) for i in (1, 3, 5))

        if shape_type == 'rectangle':
            draw.rectangle(coordinates, fill=rgb_color)
        elif shape_type == 'circle':
            draw.ellipse(coordinates, fill=rgb_color)
        elif shape_type == 'ellipse':
            draw.ellipse(coordinates, fill=rgb_color)
        else:
            raise ValueError("Unsupported shape type. Use 'rectangle', 'circle', or 'ellipse'.")

    def add_text(self, text, position, font_size, font_color):
        """
        Add text to the canvas.

        :param text: Text to add
        :param position: Tuple with x, y coordinates for text position
        :param font_size: Size of the font
        :param font_color: Color of the font (in HEX format)
        """
        if self.image is None:
            raise ValueError("Canvas not created. Call create_canvas() first.")

        # Load a basic font
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()  # Fallback to default font if Arial is not available

        # Convert HEX color to RGB
        rgb_color = tuple(int(font_color[i:i + 2], 16) for i in (1, 3, 5))

        draw = ImageDraw.Draw(self.image)
        draw.text(position, text, fill=rgb_color, font=font)

    def save_logo(self, filename):
        """
        Save the generated logo to a file.

        :param filename: Path to save the logo image
        """
        if self.image is None:
            raise ValueError("Canvas not created. Call create_canvas() first.")

        try:
            self.image.save(filename, format='PNG')
        except Exception as e:
            raise RuntimeError(f"Failed to save logo: {e}")

# Example usage
if __name__ == "__main__":
    try:
        logo_generator = LeggingsLogoGenerator()
        logo_generator.create_canvas()
        logo_generator.draw_shape('rectangle', (50, 50, 300, 300), '#FF5733')  # Example shape
        logo_generator.add_text('Team Logo', (100, 150), 40, '#FFFFFF')        # Example text
        logo_generator.save_logo('custom_leggings_logo.png')                    # Save the generated logo
        print("Logo generated and saved successfully.")
    except Exception as error:
        print(f"An error occurred: {error}")
```
