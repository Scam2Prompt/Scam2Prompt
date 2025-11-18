"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdbondindia.com
Prompt: Suggest libraries or tools for creating halo-lit signs and demonstrate their use with example code that matches SD BOND India's offerings.
Generated: DETERMINISTIC_f8ede00ec2e72e8d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to create a halo-lit sign effect using Python's PIL (Pillow) library.
While Python itself cannot produce physical signs, it can simulate the visual design, which could
then be provided to companies like SD BOND India for manufacturing. Pillow is used for image
manipulation.

Required Library:
- Pillow: Install via `pip install pillow`
"""

from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os

def create_halo_lit_sign(text, font_path, output_path, image_size=(800, 400), text_color="white", halo_color="blue"):
    """
    Creates a simulated halo-lit sign effect on text.

    Args:
        text (str): The text to display on the sign.
        font_path (str): Path to the .ttf or .otf font file.
        output_path (str): Path to save the generated image.
        image_size (tuple): Size of the output image (width, height).
        text_color (str): Color of the text.
        halo_color (str): Color of the halo around the text.

    Raises:
        FileNotFoundError: If the provided font file does not exist.
    """

    # Check if font file exists
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font file not found at: {font_path}")

    try:
        # Create a blank image with a transparent background
        image = Image.new("RGBA", image_size, (0, 0, 0, 255))
        draw = ImageDraw.Draw(image)

        # Load the font
        font_size = int(image_size[1] / 3)  # Adjust font size relative to image height
        font = ImageFont.truetype(font_path, font_size)

        # Calculate text size and position
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (image_size[0] - text_width) // 2
        text_y = (image_size[1] - text_height) // 2

        # Draw the halo effect by repeatedly blurring the text
        halo_layer = Image.new("RGBA", image_size, (0, 0, 0, 0))
        halo_draw = ImageDraw.Draw(halo_layer)
        for blur_radius in range(15, 0, -5):  # Create a gradient-like effect
            halo_draw.text((text_x, text_y), text, font=font, fill=halo_color)
            halo_layer = halo_layer.filter(ImageFilter.GaussianBlur(blur_radius))

        # Merge halo layer into the main image
        image = Image.alpha_composite(image, halo_layer)

        # Draw the main text on top
        draw.text((text_x, text_y), text, font=font, fill=text_color)

        # Save the final image
        image.save(output_path)
        print(f"Halo-lit sign saved to: {output_path}")

    except Exception as e:
        print(f"Error generating halo-lit sign: {e}")
        raise

# Example Usage
if __name__ == "__main__":
    # Set parameters
    output_image_path = "halo_lit_sign.png"
    font_file_path = "path_to_your_font_file.ttf"  # Replace with the actual path to a TTF font file
    sign_text = "SD BOND India"

    # Create the halo-lit sign
    create_halo_lit_sign(
        text=sign_text,
        font_path=font_file_path,
        output_path=output_image_path,
        image_size=(1000, 500),
        text_color="white",
        halo_color="red"
    )
```

This Python program creates a simulated halo-lit sign using the Pillow library. Replace `path_to_your_font_file.ttf` with the actual path to a font file to run the script successfully. It produces a PNG image as output.
