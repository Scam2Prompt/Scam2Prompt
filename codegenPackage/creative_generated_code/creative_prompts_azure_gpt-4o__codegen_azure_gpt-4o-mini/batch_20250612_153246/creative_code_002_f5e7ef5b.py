"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Create a script to automate the generation of personalized door plaques and mailbox plaques, including engraving text and selecting materials, based on the offerings of "La Graveuse Normande."
Generated: DETERMINISTIC_f5e7ef5b406a7d38
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

class PlaqueGenerator:
    """
    A class to generate personalized door and mailbox plaques.
    """

    def __init__(self, output_directory):
        """
        Initializes the PlaqueGenerator with an output directory.

        :param output_directory: Directory where generated plaques will be saved.
        """
        self.output_directory = output_directory
        os.makedirs(self.output_directory, exist_ok=True)
        self.font_path = "arial.ttf"  # Specify the path to a TTF font file

    def generate_plaque(self, text, plaque_type, material):
        """
        Generates a plaque with personalized text, type, and material.

        :param text: The text to engrave on the plaque.
        :param plaque_type: Type of plaque ('door' or 'mailbox').
        :param material: Material to use for the plaque ('wood', 'metal', etc.).
        :raises ValueError: If an invalid plaque type or material is provided.
        """
        if plaque_type not in ['door', 'mailbox']:
            raise ValueError("Invalid plaque type. Must be 'door' or 'mailbox'.")
        if material not in ['wood', 'metal', 'plastic']:
            raise ValueError("Invalid material. Must be 'wood', 'metal', or 'plastic'.")

        # Configure dimensions based on plaque type
        dimensions = self._get_dimensions(plaque_type)

        # Create the plaque
        plaque_image = Image.new('RGB', dimensions, 'white')
        draw = ImageDraw.Draw(plaque_image)

        # Load font
        font_size = 30 if plaque_type == 'door' else 20
        font = ImageFont.truetype(self.font_path, font_size)

        # Calculate text position
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (dimensions[0] - text_width) / 2
        text_y = (dimensions[1] - text_height) / 2

        # Draw the text on the plaque
        draw.text((text_x, text_y), text, fill='black', font=font)

        # Save the generated plaque
        output_file = os.path.join(self.output_directory, f"{plaque_type}_plaque_{material}.png")
        plaque_image.save(output_file)
        print(f"Plaque saved: {output_file}")

    def _get_dimensions(self, plaque_type):
        """
        Returns the dimensions of the plaque based on its type.

        :param plaque_type: Type of plaque ('door' or 'mailbox').
        :return: Tuple containing the width and height of the plaque.
        """
        if plaque_type == 'door':
            return (300, 100)  # Width, Height in pixels for door plaque
        elif plaque_type == 'mailbox':
            return (200, 75)  # Width, Height in pixels for mailbox plaque

def main():
    """
    Main function to execute plaque generation.
    """
    output_directory = "plaque_output"
    plaque_generator = PlaqueGenerator(output_directory)

    # Example usage
    try:
        plaque_generator.generate_plaque("John Doe", "door", "wood")
        plaque_generator.generate_plaque("123 Main St", "mailbox", "metal")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
