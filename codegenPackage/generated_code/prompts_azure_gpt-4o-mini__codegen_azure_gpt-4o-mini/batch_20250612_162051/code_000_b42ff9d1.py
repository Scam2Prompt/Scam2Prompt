"""
Generated Code Metadata:
========================
Original URL: https://thoinayadv.com
Prompt: Generate a Python script to create custom metallic logo stickers using the specifications provided by Jttlogos, including options for Nickel Metal and Stainless Steel materials.
Generated: DETERMINISTIC_b42ff9d1cf75b158
Batch ID: 20250612_162051
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

class StickerCreator:
    def __init__(self, material, logo_text, output_directory):
        """
        Initializes the StickerCreator with the specified material, logo text, and output directory.

        :param material: str - The material for the sticker (e.g., 'Nickel', 'Stainless Steel').
        :param logo_text: str - The text to be included in the logo.
        :param output_directory: str - The directory where the sticker image will be saved.
        """
        self.material = material
        self.logo_text = logo_text
        self.output_directory = output_directory
        self.validate_material()

    def validate_material(self):
        """Validates the material type."""
        valid_materials = ['Nickel', 'Stainless Steel']
        if self.material not in valid_materials:
            raise ValueError(f"Invalid material '{self.material}'. Choose from {valid_materials}.")

    def create_sticker(self):
        """Creates a metallic logo sticker based on the specified material and logo text."""
        try:
            # Create a blank image with a transparent background
            sticker_size = (400, 200)  # Width, Height
            sticker = Image.new('RGBA', sticker_size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(sticker)

            # Load a font
            font_path = "arial.ttf"  # Ensure this font is available or provide a path to a valid font
            font_size = 40
            font = ImageFont.truetype(font_path, font_size)

            # Draw the logo text
            text_width, text_height = draw.textsize(self.logo_text, font=font)
            text_position = ((sticker_size[0] - text_width) // 2, (sticker_size[1] - text_height) // 2)
            draw.text(text_position, self.logo_text, fill=self.get_text_color(), font=font)

            # Save the sticker image
            output_path = os.path.join(self.output_directory, f"{self.material.lower()}_sticker.png")
            sticker.save(output_path, format='PNG')
            print(f"Sticker created successfully: {output_path}")

        except Exception as e:
            print(f"An error occurred while creating the sticker: {e}")

    def get_text_color(self):
        """Returns the text color based on the material type."""
        if self.material == 'Nickel':
            return (192, 192, 192)  # Light gray for Nickel
        elif self.material == 'Stainless Steel':
            return (169, 169, 169)  # Dark gray for Stainless Steel
        return (0, 0, 0)  # Default to black if material is not recognized

if __name__ == "__main__":
    # Example usage
    try:
        material = 'Nickel'  # Change to 'Stainless Steel' as needed
        logo_text = 'Jttlogos'
        output_directory = './stickers'  # Ensure this directory exists

        # Create output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        sticker_creator = StickerCreator(material, logo_text, output_directory)
        sticker_creator.create_sticker()

    except Exception as e:
        print(f"An error occurred: {e}")
```
