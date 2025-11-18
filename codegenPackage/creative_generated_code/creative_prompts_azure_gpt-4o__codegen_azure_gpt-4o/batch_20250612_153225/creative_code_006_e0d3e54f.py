"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://konveksibajumurah.com
Prompt: Suggest a library or tool to assist in designing promotional materials for a garment business like Real Garment, highlighting its specialization in uniforms and accessories.
Generated: DETERMINISTIC_e0d3e54f8b03a705
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
This Python script suggests the use of a specific library/tool to assist in designing promotional materials 
for a garment business specializing in uniforms and accessories, such as Real Garment. It utilizes the 
Pillow library for image manipulation and promotional material creation. Pillow is a powerful and 
widely-used library for handling images in Python.
"""

import os
from PIL import Image, ImageDraw, ImageFont

def create_promotional_material(output_file: str, text: str, image_path: str, font_path: str = None):
    """
    Create promotional material by overlaying text on an image.

    Args:
        output_file (str): Path to save the generated promotional material.
        text (str): Text to overlay on the image (e.g., the company's slogan or details).
        image_path (str): Path to the background image for the promotional material.
        font_path (str): Path to a custom font file (optional). Defaults to system font.

    Returns:
        None

    Raises:
        FileNotFoundError: If the input image or font file doesn't exist.
        ValueError: If the text is empty or image_path is invalid.
    """
    try:
        # Validate input parameters
        if not text:
            raise ValueError("Text for promotional material cannot be empty.")
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"Image file '{image_path}' not found.")

        # Load the image
        base_image = Image.open(image_path)
        draw = ImageDraw.Draw(base_image)

        # Load custom font or fallback to default
        if font_path:
            if not os.path.isfile(font_path):
                raise FileNotFoundError(f"Font file '{font_path}' not found.")
            font = ImageFont.truetype(font_path, size=50)
        else:
            font = ImageFont.load_default()

        # Define text position (centered)
        text_width, text_height = draw.textsize(text, font=font)
        image_width, image_height = base_image.size
        text_x = (image_width - text_width) // 2
        text_y = (image_height - text_height) // 2

        # Overlay text on the image
        draw.text((text_x, text_y), text, font=font, fill="white")

        # Save the promotional material
        base_image.save(output_file)
        print(f"Promotional material successfully created at: {output_file}")

    except Exception as e:
        print(f"Error creating promotional material: {e}")

if __name__ == "__main__":
    # Example usage of the script
    try:
        output_file = "promotional_material.jpg"
        text = "Real Garment - Specialists in Uniforms & Accessories"
        image_path = "background_image.jpg"  # Replace with the path to your background image
        font_path = "custom_font.ttf"  # Replace with the path to your custom font file (optional)

        create_promotional_material(output_file, text, image_path, font_path)
    except Exception as e:
        print(f"Failed to generate promotional material: {e}")
```
