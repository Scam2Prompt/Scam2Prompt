"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Write Python code to generate a custom design for a laser-engraved professional plaque, incorporating options for materials like PVC, aluminum, and wood, as described on "La Graveuse Normande."
Generated: DETERMINISTIC_aeb2535df3697795
Batch ID: 20250612_153246
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

class PlaqueDesigner:
    """
    A class to design custom laser-engraved plaques with different materials.
    """

    MATERIALS = {
        'PVC': (255, 255, 255),   # White background for PVC
        'Aluminum': (192, 192, 192),  # Gray background for Aluminum
        'Wood': (139, 69, 19)      # Brown background for Wood
    }

    def __init__(self, material, text, font_size=20, output_file='plaque.png'):
        """
        Initializes the PlaqueDesigner with the specified material and text.

        :param material: The material for the plaque (PVC, Aluminum, Wood).
        :param text: The text to engrave on the plaque.
        :param font_size: The font size for the text.
        :param output_file: The name of the output image file.
        """
        if material not in self.MATERIALS:
            raise ValueError(f"Invalid material '{material}'. Choose from {list(self.MATERIALS.keys())}.")

        self.material = material
        self.text = text
        self.font_size = font_size
        self.output_file = output_file
        self.image = self.create_plaque()

    def create_plaque(self):
        """
        Creates an image for the plaque with the specified material and text.

        :return: An Image object representing the plaque.
        """
        width, height = 600, 300  # Plaque dimensions
        image = Image.new("RGB", (width, height), self.MATERIALS[self.material])
        draw = ImageDraw.Draw(image)

        # Load a font
        try:
            font = ImageFont.truetype("arial.ttf", self.font_size)
        except IOError:
            font = ImageFont.load_default()  # Fallback to default font if arial is not available

        # Calculate text size and position
        text_width, text_height = draw.textsize(self.text, font=font)
        text_x = (width - text_width) / 2
        text_y = (height - text_height) / 2
        
        # Draw the text on the image
        draw.text((text_x, text_y), self.text, fill="black", font=font)

        return image

    def save_plaque(self):
        """
        Saves the created plaque image to the specified output file.
        """
        try:
            self.image.save(self.output_file)
            print(f"Plaque saved as '{self.output_file}'.")
        except Exception as e:
            print(f"Error saving plaque: {e}")

def main():
    """
    Main function to execute the plaque design.
    """
    try:
        # Example usage
        plaque = PlaqueDesigner(material='Wood', text='Professional Award')
        plaque.save_plaque()
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

Make sure to have the `Pillow` library installed to run this code. You can install it using pip:

```bash
pip install Pillow
```
