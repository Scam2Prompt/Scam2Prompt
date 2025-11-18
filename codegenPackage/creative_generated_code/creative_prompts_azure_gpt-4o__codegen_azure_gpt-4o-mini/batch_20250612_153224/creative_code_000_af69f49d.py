"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createxpro.com
Prompt: Write Python code to generate a design template for textile customization using techniques like serigraphy or sublimation, as described on CreatexPro's website.
Generated: DETERMINISTIC_af69f49d63b39b3d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont

class TextileCustomizationTemplate:
    def __init__(self, width, height, background_color=(255, 255, 255)):
        """
        Initialize the template for textile customization.

        :param width: Width of the template in pixels
        :param height: Height of the template in pixels
        :param background_color: Background color of the template in RGB format
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.template_image = Image.new("RGB", (self.width, self.height), self.background_color)

    def add_design(self, design_image_path, position=(0, 0)):
        """
        Add a design image to the template.

        :param design_image_path: Path to the design image
        :param position: Tuple indicating the position on the template where the design will be placed
        """
        try:
            design_image = Image.open(design_image_path).convert("RGBA")
            self.template_image.paste(design_image, position, design_image)
        except Exception as e:
            print(f"Error adding design: {e}")

    def add_text(self, text, position=(10, 10), font_path=None, font_size=20, color=(0, 0, 0)):
        """
        Add text to the template.

        :param text: Text to add to the template
        :param position: Tuple indicating the position on the template where the text will be placed
        :param font_path: Path to the font file. If None, default font will be used
        :param font_size: Size of the font
        :param color: Text color in RGB format
        """
        try:
            draw = ImageDraw.Draw(self.template_image)
            font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()
            draw.text(position, text, fill=color, font=font)
        except Exception as e:
            print(f"Error adding text: {e}")

    def save_template(self, output_path):
        """
        Save the template to a file.

        :param output_path: Path where the template will be saved
        """
        try:
            self.template_image.save(output_path)
            print(f"Template saved to {output_path}")
        except Exception as e:
            print(f"Error saving template: {e}")

def main():
    # Define template dimensions and background color
    width, height = 800, 600
    background_color = (240, 240, 240)

    # Create a textile customization template
    template = TextileCustomizationTemplate(width, height, background_color)

    # Add a design from an image file to the template
    template.add_design("path/to/design_image.png", position=(100, 100))

    # Add text to the template
    template.add_text("Custom Text", position=(150, 150), font_size=30, color=(255, 0, 0))

    # Save the final template
    template.save_template("output/custom_template.png")

if __name__ == "__main__":
    main()
```
