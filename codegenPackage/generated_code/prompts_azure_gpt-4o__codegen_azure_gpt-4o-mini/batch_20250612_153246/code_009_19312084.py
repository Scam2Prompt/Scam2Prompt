"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Develop a Python script to create templates for engraved plaques for machine tools, including material selection and text formatting, inspired by "La Graveuse Normande."
Generated: DETERMINISTIC_19312084ffd61d41
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
    A class to create templates for engraved plaques for machine tools.
    """

    def __init__(self, width: int, height: int, material: str, text: str):
        """
        Initializes the plaque template with specified dimensions, material, and text.

        :param width: Width of the plaque in pixels.
        :param height: Height of the plaque in pixels.
        :param material: Material type for the plaque (e.g., 'wood', 'metal').
        :param text: Text to be engraved on the plaque.
        """
        self.width = width
        self.height = height
        self.material = material
        self.text = text
        self.image = None

    def create_template(self):
        """
        Creates a blank plaque template based on the specified dimensions and material.
        """
        try:
            # Create a blank image with white background
            self.image = Image.new('RGB', (self.width, self.height), 'white')
            draw = ImageDraw.Draw(self.image)

            # Draw a border based on material type
            if self.material.lower() == 'wood':
                draw.rectangle([0, 0, self.width, self.height], outline='brown', width=5)
            elif self.material.lower() == 'metal':
                draw.rectangle([0, 0, self.width, self.height], outline='gray', width=5)
            else:
                draw.rectangle([0, 0, self.width, self.height], outline='black', width=5)

            # Add text to the plaque
            self.add_text(draw)

            # Save the image
            self.save_template()

        except Exception as e:
            print(f"Error creating template: {e}")

    def add_text(self, draw: ImageDraw.Draw):
        """
        Adds the specified text to the plaque.

        :param draw: The ImageDraw object to draw on the image.
        """
        try:
            # Load a font
            font_path = "arial.ttf"  # Ensure this font is available in your environment
            font_size = 24
            font = ImageFont.truetype(font_path, font_size)

            # Calculate text size and position
            text_width, text_height = draw.textsize(self.text, font=font)
            text_x = (self.width - text_width) / 2
            text_y = (self.height - text_height) / 2

            # Draw the text on the image
            draw.text((text_x, text_y), self.text, fill='black', font=font)

        except Exception as e:
            print(f"Error adding text: {e}")

    def save_template(self):
        """
        Saves the created plaque template as a PNG file.
        """
        try:
            output_dir = "plaque_templates"
            os.makedirs(output_dir, exist_ok=True)
            file_path = os.path.join(output_dir, f"plaque_{self.material}.png")
            self.image.save(file_path)
            print(f"Template saved as {file_path}")

        except Exception as e:
            print(f"Error saving template: {e}")

if __name__ == "__main__":
    # Example usage
    plaque = PlaqueTemplate(width=400, height=200, material='wood', text='Engraved Text Here')
    plaque.create_template()
```
