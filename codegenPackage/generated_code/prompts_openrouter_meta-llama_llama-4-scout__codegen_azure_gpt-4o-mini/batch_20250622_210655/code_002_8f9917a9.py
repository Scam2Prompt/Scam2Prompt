"""
Generated Code Metadata:
========================
Original URL: https://blackhillsports.com
Prompt: "Generate code to automate the process of creating custom sublimation designs for activewear and uniforms using a library like Pillow or OpenCV."
Generated: DETERMINISTIC_8f9917a9f9114491
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
from PIL import Image, ImageDraw, ImageFont

class SublimationDesignGenerator:
    def __init__(self, output_directory):
        """
        Initializes the SublimationDesignGenerator with the specified output directory.
        
        :param output_directory: Directory where generated designs will be saved.
        """
        self.output_directory = output_directory
        os.makedirs(self.output_directory, exist_ok=True)

    def create_design(self, base_image_path, text, font_path, font_size, output_filename):
        """
        Creates a custom sublimation design by overlaying text on a base image.
        
        :param base_image_path: Path to the base image for the design.
        :param text: Text to overlay on the image.
        :param font_path: Path to the font file to use for the text.
        :param font_size: Size of the font for the text.
        :param output_filename: Name of the output file (should include .png extension).
        """
        try:
            # Load the base image
            base_image = Image.open(base_image_path).convert("RGBA")
            draw = ImageDraw.Draw(base_image)

            # Load the font
            font = ImageFont.truetype(font_path, font_size)

            # Calculate text size and position
            text_width, text_height = draw.textsize(text, font=font)
            text_position = ((base_image.width - text_width) // 2, (base_image.height - text_height) // 2)

            # Draw the text on the image
            draw.text(text_position, text, font=font, fill=(255, 255, 255, 255))  # White text

            # Save the final design
            output_path = os.path.join(self.output_directory, output_filename)
            base_image.save(output_path, format='PNG')
            print(f"Design saved to {output_path}")

        except FileNotFoundError as e:
            print(f"Error: {e}. Please check the file paths.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    output_dir = "sublimation_designs"
    generator = SublimationDesignGenerator(output_dir)

    # Define parameters for the design
    base_image = "path/to/base_image.png"  # Replace with your base image path
    overlay_text = "Your Custom Text"
    font_file = "path/to/font.ttf"  # Replace with your font file path
    font_size = 40
    output_file = "custom_design.png"

    # Create the design
    generator.create_design(base_image, overlay_text, font_file, font_size, output_file)
```
