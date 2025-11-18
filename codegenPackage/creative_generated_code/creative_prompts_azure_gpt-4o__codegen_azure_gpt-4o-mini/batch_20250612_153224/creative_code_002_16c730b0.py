"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createxpro.com
Prompt: Provide code examples for designing promotional items, such as ceramic mugs or hoodies, using sublimation techniques similar to those offered by CreatexPro.
Generated: DETERMINISTIC_16c730b0f13da969
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

class SublimationDesigner:
    def __init__(self, output_directory='promotional_items'):
        """Initialize the designer with an output directory for generated items."""
        self.output_directory = output_directory
        self.create_output_directory()

    def create_output_directory(self):
        """Create the output directory if it does not exist."""
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def create_mug_design(self, text, image_path, output_filename):
        """
        Create a design for a ceramic mug.

        :param text: Text to be added to the mug design.
        :param image_path: Path to the image to be used on the mug.
        :param output_filename: Name for the output file.
        """
        try:
            # Load the base image for the mug
            base_image = Image.open(image_path)
            draw = ImageDraw.Draw(base_image)

            # Load a font
            font = ImageFont.load_default()

            # Calculate text size and position
            text_width, text_height = draw.textsize(text, font=font)
            position = ((base_image.width - text_width) / 2, base_image.height - text_height - 10)

            # Add text to image
            draw.text(position, text, fill="black", font=font)

            # Save the design
            output_path = os.path.join(self.output_directory, output_filename)
            base_image.save(output_path)
            print(f"Mug design saved to {output_path}")

        except Exception as e:
            print(f"An error occurred while creating mug design: {e}")

    def create_hoodie_design(self, text, output_filename):
        """
        Create a design for a hoodie.

        :param text: Text to be added to the hoodie design.
        :param output_filename: Name for the output file.
        """
        try:
            # Create a blank hoodie design (assumed size)
            hoodie_image = Image.new('RGB', (800, 600), 'white')
            draw = ImageDraw.Draw(hoodie_image)

            # Load a font
            font = ImageFont.load_default()

            # Calculate text size and position
            text_width, text_height = draw.textsize(text, font=font)
            position = ((hoodie_image.width - text_width) / 2, (hoodie_image.height - text_height) / 2)

            # Add text to hoodie design
            draw.text(position, text, fill="black", font=font)

            # Save the design
            output_path = os.path.join(self.output_directory, output_filename)
            hoodie_image.save(output_path)
            print(f"Hoodie design saved to {output_path}")

        except Exception as e:
            print(f"An error occurred while creating hoodie design: {e}")

if __name__ == '__main__':
    # Example usage
    designer = SublimationDesigner()

    # Creating a mug design
    designer.create_mug_design(
        text="Best Coffee Ever!",
        image_path="mug_template.jpg",  # Replace with a valid image path
        output_filename="mug_design.png"
    )

    # Creating a hoodie design
    designer.create_hoodie_design(
        text="Stay Cozy!",
        output_filename="hoodie_design.png"
    )
```

**Note:** To run the above code, ensure you have the `Pillow` library installed, and replace `"mug_template.jpg"` with a valid image path for the mug design.
