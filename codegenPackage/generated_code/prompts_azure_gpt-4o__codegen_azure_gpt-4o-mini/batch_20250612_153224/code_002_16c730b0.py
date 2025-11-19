"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Provide code examples for designing promotional items, such as ceramic mugs or hoodies, using sublimation techniques similar to those offered by CreatexPro.
Generated: DETERMINISTIC_16c730b0f13da969
Batch ID: 20250612_153224
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

class PromotionalItemDesigner:
    """
    A class to design promotional items using sublimation techniques.
    """

    def __init__(self, item_type, dimensions, output_directory):
        """
        Initializes the designer with item type, dimensions, and output directory.

        :param item_type: Type of the promotional item (e.g., 'mug', 'hoodie').
        :param dimensions: Tuple representing the dimensions (width, height) in pixels.
        :param output_directory: Directory where the designed item will be saved.
        """
        self.item_type = item_type
        self.dimensions = dimensions
        self.output_directory = output_directory

        # Ensure the output directory exists
        os.makedirs(self.output_directory, exist_ok=True)

    def create_design(self, text, font_size=40, font_path=None):
        """
        Creates a design for the promotional item.

        :param text: Text to be printed on the item.
        :param font_size: Size of the font for the text.
        :param font_path: Path to the font file. If None, a default font will be used.
        :return: Path to the saved design image.
        """
        try:
            # Create a blank image with a white background
            image = Image.new('RGB', self.dimensions, 'white')
            draw = ImageDraw.Draw(image)

            # Load the font
            font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()

            # Calculate text size and position
            text_width, text_height = draw.textsize(text, font=font)
            text_x = (self.dimensions[0] - text_width) / 2
            text_y = (self.dimensions[1] - text_height) / 2

            # Draw the text on the image
            draw.text((text_x, text_y), text, fill='black', font=font)

            # Save the image
            output_path = os.path.join(self.output_directory, f"{self.item_type}_design.png")
            image.save(output_path)

            return output_path

        except Exception as e:
            print(f"Error creating design: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Define item type, dimensions, and output directory
    item_type = 'mug'
    dimensions = (800, 600)  # Width x Height in pixels
    output_directory = './designs'

    # Create an instance of the designer
    designer = PromotionalItemDesigner(item_type, dimensions, output_directory)

    # Create a design with specified text
    design_path = designer.create_design("Best Coffee Ever!", font_size=50)

    if design_path:
        print(f"Design created successfully: {design_path}")
    else:
        print("Failed to create design.")
```
