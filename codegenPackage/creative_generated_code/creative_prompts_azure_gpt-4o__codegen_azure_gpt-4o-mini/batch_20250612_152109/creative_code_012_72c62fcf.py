"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Write a Python script to create printable templates for kids' shopping totes, inspired by Craft Intra's DIY project.
Generated: DETERMINISTIC_72c62fcfd977b6db
Batch ID: 20250612_152109
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


class ToteTemplateGenerator:
    def __init__(self, width=800, height=600, background_color=(255, 255, 255)):
        """
        Initialize the ToteTemplateGenerator with specified dimensions and background color.

        :param width: Width of the template in pixels.
        :param height: Height of the template in pixels.
        :param background_color: Background color of the template as an RGB tuple.
        """
        self.width = width
        self.height = height
        self.background_color = background_color

    def create_template(self, file_name, text, font_size=40, text_color=(0, 0, 0)):
        """
        Create a printable tote template with specified text.

        :param file_name: Name of the output image file.
        :param text: Text to be printed on the tote template.
        :param font_size: Size of the font for the text.
        :param text_color: Color of the text as an RGB tuple.
        """
        try:
            # Create a blank image with the specified background color
            image = Image.new("RGB", (self.width, self.height), self.background_color)
            draw = ImageDraw.Draw(image)

            # Load a font
            font = ImageFont.truetype("arial.ttf", font_size)  # Ensure arial.ttf is available in your environment

            # Calculate text size and position
            text_width, text_height = draw.textsize(text, font=font)
            text_x = (self.width - text_width) // 2
            text_y = (self.height - text_height) // 2

            # Draw the text on the image
            draw.text((text_x, text_y), text, fill=text_color, font=font)

            # Save the image to a file
            image.save(file_name)
            print(f"Template created and saved as '{file_name}'.")

        except Exception as e:
            print(f"An error occurred while creating the template: {e}")

    def generate_multiple_templates(self, template_data):
        """
        Generate multiple tote templates based on provided template data.

        :param template_data: A list of tuples containing (file_name, text) for each template.
        """
        for file_name, text in template_data:
            self.create_template(file_name, text)


if __name__ == "__main__":
    # Define the template data (file name and text) for each tote template
    templates = [
        ("tote_template_1.png", "Let's Go Shopping!"),
        ("tote_template_2.png", "Adventure Awaits!"),
        ("tote_template_3.png", "Super Shopper!"),
    ]

    # Create a generator instance
    generator = ToteTemplateGenerator()

    # Generate the templates
    generator.generate_multiple_templates(templates)
```

Make sure to have the Pillow library installed in your environment. You can install it using the following command:

```bash
pip install Pillow
``` 

Also, ensure that the font file `arial.ttf` is available in your environment, or adjust the font loading to use a different one as necessary.
