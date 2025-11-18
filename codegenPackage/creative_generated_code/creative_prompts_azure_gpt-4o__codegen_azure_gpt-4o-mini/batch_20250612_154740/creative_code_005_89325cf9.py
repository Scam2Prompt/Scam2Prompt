"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officineimmagine.it
Prompt: Create code to watermark fashion photography images with branding elements, ensuring high-quality visuals as described in Officine dell’Immagine's fashion services.
Generated: DETERMINISTIC_89325cf978424a9d
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(input_image_path, output_image_path, watermark_text, position=(0, 0), opacity=128):
    """
    Adds a watermark to the specified image.

    :param input_image_path: Path to the input image.
    :param output_image_path: Path to save the watermarked image.
    :param watermark_text: The text to be used as a watermark.
    :param position: A tuple (x, y) for the position of the watermark.
    :param opacity: Opacity of the watermark (0 to 255).
    """

    try:
        # Open the original image
        base_image = Image.open(input_image_path).convert("RGBA")
        
        # Create a new blank image with the same size
        watermark_layer = Image.new("RGBA", base_image.size, (0, 0, 0, 0))

        # Initialize the drawing context
        draw = ImageDraw.Draw(watermark_layer)

        # Load font
        font_path = "arial.ttf"  # Adjust the path to the font as necessary
        font_size = int(base_image.size[1] / 10)  # Size based on image height
        font = ImageFont.truetype(font_path, font_size)

        # Add text to the watermark layer
        draw.text(position, watermark_text, fill=(255, 255, 255, opacity), font=font)  # White text with specified opacity

        # Combine the original image with the watermark
        watermarked_image = Image.alpha_composite(base_image, watermark_layer)

        # Save the resulting image
        watermarked_image = watermarked_image.convert("RGB")  # Convert back to RGB
        watermarked_image.save(output_image_path, "JPEG", quality=95)  # Save with high quality

        print(f"Watermarked image saved as: {output_image_path}")

    except FileNotFoundError:
        print(f"Error: The file {input_image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
if __name__ == "__main__":
    input_image = "fashion_photo.jpg"  # Path to input fashion image
    output_image = "watermarked_fashion_photo.jpg"  # Path for output watermarked image
    watermark = "© Officine dell’Immagine"  # Watermark text
    watermark_position = (10, 10)  # Position of watermark (10 pixels from top-left corner)
    watermark_opacity = 128  # Opacity level

    add_watermark(input_image, output_image, watermark, watermark_position, watermark_opacity)
```

Make sure you have the Pillow library installed. You can install it using:
```bash
pip install Pillow
```

Also, ensure that you have the `arial.ttf` font file or replace it with the path to a different font file available on your system.
