"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Write code to design and export templates for engraved intercom or signage plaques, ensuring compatibility with laser engraving machines, inspired by "La Graveuse Normande."
Generated: DETERMINISTIC_ed046a93ab51093c
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

class PlaqueTemplate:
    """
    A class to create and export templates for engraved intercom or signage plaques.
    """

    def __init__(self, width: int, height: int, background_color: str = "white"):
        """
        Initializes the plaque template with specified dimensions and background color.

        :param width: Width of the plaque in pixels.
        :param height: Height of the plaque in pixels.
        :param background_color: Background color of the plaque.
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.image = Image.new("RGB", (self.width, self.height), self.background_color)
        self.draw = ImageDraw.Draw(self.image)

    def add_text(self, text: str, position: tuple, font_size: int = 20, font_color: str = "black"):
        """
        Adds text to the plaque template.

        :param text: The text to be added to the plaque.
        :param position: A tuple (x, y) representing the position to place the text.
        :param font_size: The size of the font.
        :param font_color: The color of the font.
        """
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
            self.draw.text(position, text, fill=font_color, font=font)
        except Exception as e:
            print(f"Error adding text: {e}")

    def save_template(self, filename: str):
        """
        Saves the plaque template as a PNG file.

        :param filename: The name of the file to save the template.
        """
        try:
            self.image.save(filename, "PNG")
            print(f"Template saved as {filename}")
        except Exception as e:
            print(f"Error saving template: {e}")

    def clear_template(self):
        """
        Clears the current template, resetting it to the background color.
        """
        self.image = Image.new("RGB", (self.width, self.height), self.background_color)
        self.draw = ImageDraw.Draw(self.image)

def main():
    """
    Main function to create a plaque template and export it.
    """
    plaque = PlaqueTemplate(width=800, height=400, background_color="lightgrey")
    plaque.add_text("Welcome to Our Facility", position=(50, 150), font_size=30, font_color="black")
    plaque.add_text("Please Ring the Bell", position=(50, 200), font_size=20, font_color="black")
    
    # Ensure the output directory exists
    output_dir = "plaque_templates"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the template
    plaque.save_template(os.path.join(output_dir, "plaque_template.png"))

if __name__ == "__main__":
    main()
```
