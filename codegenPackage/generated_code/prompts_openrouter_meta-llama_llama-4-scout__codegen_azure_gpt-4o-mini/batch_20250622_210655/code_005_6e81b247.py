"""
Generated Code Metadata:
========================
Original URL: https://blackhillsports.com
Prompt: "Write a script to generate high-quality images of custom apparel products with embroidered or printed designs, using a library like ImageMagick or GraphicsMagick."
Generated: DETERMINISTIC_6e81b24742a80ee4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

class ApparelImageGenerator:
    def __init__(self, base_image_path, output_dir):
        """
        Initializes the ApparelImageGenerator with a base image and output directory.

        :param base_image_path: Path to the base apparel image (e.g., t-shirt).
        :param output_dir: Directory where generated images will be saved.
        """
        self.base_image_path = base_image_path
        self.output_dir = output_dir
        self.font_path = "arial.ttf"  # Path to a TTF font file
        self.font_size = 40  # Font size for text

        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_image(self, design_text, output_filename):
        """
        Generates an image with the specified design text on the base apparel image.

        :param design_text: Text to be printed or embroidered on the apparel.
        :param output_filename: Name of the output image file.
        """
        try:
            # Load the base image
            base_image = Image.open(self.base_image_path).convert("RGBA")

            # Create a drawing context
            draw = ImageDraw.Draw(base_image)

            # Load the font
            font = ImageFont.truetype(self.font_path, self.font_size)

            # Calculate text size and position
            text_width, text_height = draw.textsize(design_text, font=font)
            text_position = ((base_image.width - text_width) // 2, (base_image.height - text_height) // 2)

            # Draw the text on the image
            draw.text(text_position, design_text, font=font, fill="white")

            # Save the final image
            output_path = os.path.join(self.output_dir, output_filename)
            base_image.save(output_path, format="PNG")

            print(f"Image saved successfully: {output_path}")

        except Exception as e:
            print(f"Error generating image: {e}")

if __name__ == "__main__":
    # Example usage
    base_image_path = "path/to/your/base_image.png"  # Replace with your base image path
    output_dir = "output_images"  # Directory to save generated images

    # Create an instance of the generator
    generator = ApparelImageGenerator(base_image_path, output_dir)

    # Generate an image with custom text
    generator.generate_image("Custom Design", "custom_apparel.png")
```

Make sure to replace `"path/to/your/base_image.png"` with the actual path to your base apparel image and ensure that the font file (`arial.ttf`) is accessible in your environment.
