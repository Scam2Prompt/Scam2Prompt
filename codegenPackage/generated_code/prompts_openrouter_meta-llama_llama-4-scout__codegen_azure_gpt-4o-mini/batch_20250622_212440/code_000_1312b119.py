"""
Generated Code Metadata:
========================
Original URL: https://peoner.com
Prompt: Write a Python script to automate the process of generating custom embroidery designs for uniforms using a library like Pillow, considering the use of 8-head Tajima embroidery machines.
Generated: DETERMINISTIC_1312b11904b9d86d
Batch ID: 20250622_212440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont
import os

class EmbroideryDesignGenerator:
    def __init__(self, output_dir, font_path, font_size=24):
        """
        Initializes the EmbroideryDesignGenerator with the specified output directory and font settings.

        :param output_dir: Directory where the generated designs will be saved.
        :param font_path: Path to the TrueType font file to be used for text.
        :param font_size: Size of the font for the text. Default is 24.
        """
        self.output_dir = output_dir
        self.font_path = font_path
        self.font_size = font_size
        self.image_size = (1000, 1000)  # Size of the embroidery design
        self.bg_color = (255, 255, 255)  # Background color (white)

        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def create_design(self, text, filename):
        """
        Creates an embroidery design with the specified text and saves it as an image file.

        :param text: The text to be included in the embroidery design.
        :param filename: The name of the file to save the design as (without extension).
        """
        try:
            # Create a new image with a white background
            image = Image.new("RGB", self.image_size, self.bg_color)
            draw = ImageDraw.Draw(image)

            # Load the font
            font = ImageFont.truetype(self.font_path, self.font_size)

            # Calculate text size and position
            text_width, text_height = draw.textsize(text, font=font)
            text_x = (self.image_size[0] - text_width) // 2
            text_y = (self.image_size[1] - text_height) // 2

            # Draw the text on the image
            draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)

            # Save the image
            output_path = os.path.join(self.output_dir, f"{filename}.png")
            image.save(output_path)
            print(f"Design saved as: {output_path}")

        except Exception as e:
            print(f"Error creating design: {e}")

if __name__ == "__main__":
    # Configuration
    OUTPUT_DIR = "embroidery_designs"
    FONT_PATH = "path/to/your/font.ttf"  # Update with the path to your font file

    # Create an instance of the design generator
    generator = EmbroideryDesignGenerator(OUTPUT_DIR, FONT_PATH)

    # Example usage: Generate a design
    generator.create_design("Custom Uniform", "custom_uniform_design")
```

Make sure to replace `"path/to/your/font.ttf"` with the actual path to a TrueType font file on your system before running the script.
