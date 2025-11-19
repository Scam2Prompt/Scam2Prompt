"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Create a script to automate the generation of personalized door plaques and mailbox plaques, including engraving text and selecting materials, based on the offerings of "La Graveuse Normande."
Generated: DETERMINISTIC_f5e7ef5b406a7d38
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

class PlaqueGenerator:
    def __init__(self, material_options, font_path, output_dir):
        """
        Initializes the PlaqueGenerator with material options, font path, and output directory.

        :param material_options: List of available materials for plaques.
        :param font_path: Path to the font file for engraving text.
        :param output_dir: Directory where generated plaques will be saved.
        """
        self.material_options = material_options
        self.font_path = font_path
        self.output_dir = output_dir
        self.validate_output_dir()

    def validate_output_dir(self):
        """Validates the output directory, creating it if it does not exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_plaque(self, text, material):
        """
        Generates a plaque with the specified text and material.

        :param text: The text to engrave on the plaque.
        :param material: The material for the plaque.
        :raises ValueError: If the selected material is not available.
        """
        if material not in self.material_options:
            raise ValueError(f"Material '{material}' is not available. Choose from {self.material_options}.")

        # Create an image for the plaque
        plaque_image = Image.new('RGB', (300, 150), color='white')
        draw = ImageDraw.Draw(plaque_image)

        # Load the font
        try:
            font = ImageFont.truetype(self.font_path, 24)
        except IOError:
            raise IOError("Font file not found. Please check the font path.")

        # Calculate text size and position
        text_size = draw.textsize(text, font=font)
        text_x = (plaque_image.width - text_size[0]) / 2
        text_y = (plaque_image.height - text_size[1]) / 2

        # Draw the text on the plaque
        draw.text((text_x, text_y), text, fill='black', font=font)

        # Save the plaque image
        output_file = os.path.join(self.output_dir, f"{text.replace(' ', '_')}_{material}.png")
        plaque_image.save(output_file)
        print(f"Plaque saved as: {output_file}")

def main():
    # Define available materials and font path
    materials = ['Wood', 'Metal', 'Acrylic']
    font_path = 'path/to/your/font.ttf'  # Update with the actual font path
    output_directory = 'plaques_output'

    # Create an instance of PlaqueGenerator
    plaque_generator = PlaqueGenerator(materials, font_path, output_directory)

    # Example usage
    try:
        plaque_generator.generate_plaque("John Doe", "Wood")
        plaque_generator.generate_plaque("Jane Smith", "Metal")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
