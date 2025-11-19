"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Develop a program to create laser engraving designs for wedding place cards or baptism plaques, referencing the customization options mentioned on "La Graveuse Normande."
Generated: DETERMINISTIC_e5438804180e03f7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image, ImageDraw, ImageFont

class LaserEngravingDesign:
    def __init__(self, width=400, height=200, background_color=(255, 255, 255)):
        """
        Initialize the LaserEngravingDesign with specified dimensions and background color.

        :param width: Width of the design in pixels
        :param height: Height of the design in pixels
        :param background_color: Background color in RGB tuple
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.image = Image.new("RGB", (self.width, self.height), self.background_color)
        self.draw = ImageDraw.Draw(self.image)

    def add_text(self, text, position, font_size=20, font_color=(0, 0, 0), font_path=None):
        """
        Add text to the engraving design.

        :param text: The text to engrave
        :param position: Tuple (x, y) for text position
        :param font_size: Size of the font
        :param font_color: Color of the font in RGB tuple
        :param font_path: Path to the .ttf font file
        """
        try:
            if font_path:
                font = ImageFont.truetype(font_path, font_size)
            else:
                font = ImageFont.load_default()
            self.draw.text(position, text, fill=font_color, font=font)
        except Exception as e:
            print(f"Error adding text: {e}")

    def save_design(self, filename):
        """
        Save the design to a file.

        :param filename: The filename to save the design as
        """
        try:
            self.image.save(filename)
            print(f"Design saved as {filename}")
        except Exception as e:
            print(f"Error saving design: {e}")

    def show_design(self):
        """
        Display the design.
        """
        try:
            self.image.show()
        except Exception as e:
            print(f"Error displaying design: {e}")

def main():
    # Create an instance of the LaserEngravingDesign
    design = LaserEngravingDesign()

    # Customize the design with text
    design.add_text("John & Jane", position=(50, 50), font_size=30, font_color=(0, 0, 0))
    design.add_text("Wedding Place Card", position=(50, 100), font_size=20, font_color=(0, 0, 0))

    # Save the design to a file
    design.save_design("wedding_place_card.png")

    # Show the design
    design.show_design()

if __name__ == "__main__":
    main()
```

Make sure to have the `Pillow` library installed to run this code. You can install it using pip:

```bash
pip install Pillow
```
