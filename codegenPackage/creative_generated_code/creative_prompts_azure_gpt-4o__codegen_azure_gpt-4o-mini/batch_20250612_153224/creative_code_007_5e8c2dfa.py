"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://printserves.com
Prompt: Create a program that generates branded packaging designs (e.g., paper cups and gift wraps) based on user input and prepares the files for upload to Printserves Nigeria.
Generated: DETERMINISTIC_5e8c2dfad2a20a2a
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
from typing import Tuple

class PackagingDesigner:
    def __init__(self, template_size: Tuple[int, int], output_dir: str, font_path: str):
        """
        Initialize the PackagingDesigner with template size, output directory, and font path.
        
        :param template_size: Tuple containing the width and height of the template in pixels.
        :param output_dir: Directory where the generated images will be saved.
        :param font_path: Path to the font file for text rendering.
        """
        self.template_size = template_size
        self.output_dir = output_dir
        self.font_path = font_path

        # Ensure the output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def create_design(self, text: str, background_color: Tuple[int, int, int], design_type: str) -> str:
        """
        Create a branded packaging design and save it as an image file.

        :param text: The text to be displayed on the design.
        :param background_color: Background color of the design in RGB format.
        :param design_type: Type of the design (e.g., "cup", "wrap").
        :return: Path to the saved image file.
        """
        try:
            # Create a new image with the specified background color
            image = Image.new("RGB", self.template_size, background_color)
            draw = ImageDraw.Draw(image)

            # Load the font
            font_size = 40  # Set a default font size
            font = ImageFont.truetype(self.font_path, font_size)

            # Calculate text size and position
            text_width, text_height = draw.textsize(text, font=font)
            text_x = (self.template_size[0] - text_width) // 2
            text_y = (self.template_size[1] - text_height) // 2

            # Draw the text on the image
            draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)

            # Generate filename based on design type and text
            file_name = f"{design_type}_design.png"
            file_path = os.path.join(self.output_dir, file_name)

            # Save the image
            image.save(file_path)
            print(f"Design saved at: {file_path}")

            return file_path
        except Exception as e:
            print(f"Error creating design: {e}")
            return ""

if __name__ == "__main__":
    # User input for design parameters
    user_text = input("Enter the text for the design: ")
    user_color = input("Enter the background color (r, g, b) as comma separated values: ")
    user_design_type = input("Enter the type of design (e.g., cup, wrap): ")

    # Parse the background color input
    try:
        background_color = tuple(map(int, user_color.split(',')))
        if len(background_color) != 3 or any(c < 0 or c > 255 for c in background_color):
            raise ValueError("Invalid color format. Please provide three integers (0-255).")
    except Exception as e:
        print(f"Error parsing color: {e}")
        exit(1)

    # Prepare the PackagingDesigner
    designer = PackagingDesigner(template_size=(600, 400), output_dir='packaging_designs', font_path='arial.ttf')

    # Create and save the design
    designer.create_design(text=user_text, background_color=background_color, design_type=user_design_type)
```

Make sure to replace `'arial.ttf'` with the actual path to a TTF font file on your system. The generated designs will be saved in the `packaging_designs` directory.
