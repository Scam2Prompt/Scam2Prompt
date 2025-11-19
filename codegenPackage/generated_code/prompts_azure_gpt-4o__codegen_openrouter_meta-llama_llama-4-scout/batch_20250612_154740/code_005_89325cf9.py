"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Create code to watermark fashion photography images with branding elements, ensuring high-quality visuals as described in Officine dell’Immagine's fashion services.
Generated: DETERMINISTIC_89325cf978424a9d
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Image Watermarking Script**
==========================

```python
from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(image_path, watermark_path, output_path, opacity=0.5):
    """
    Adds a watermark to an image.

    Args:
        image_path (str): Path to the input image.
        watermark_path (str): Path to the watermark image.
        output_path (str): Path to save the output image.
        opacity (float, optional): Opacity of the watermark. Defaults to 0.5.

    Raises:
        FileNotFoundError: If the input image or watermark is not found.
        ValueError: If the opacity is not between 0 and 1.
    """

    # Check if the input image and watermark exist
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Input image not found: {image_path}")
    if not os.path.exists(watermark_path):
        raise FileNotFoundError(f"Watermark not found: {watermark_path}")

    # Check if the opacity is valid
    if opacity < 0 or opacity > 1:
        raise ValueError("Opacity must be between 0 and 1")

    # Open the input image and watermark
    image = Image.open(image_path)
    watermark = Image.open(watermark_path)

    # Ensure the watermark is in RGBA mode
    if watermark.mode != 'RGBA':
        watermark = watermark.convert('RGBA')

    # Calculate the position to place the watermark
    image_width, image_height = image.size
    watermark_width, watermark_height = watermark.size
    position = ((image_width - watermark_width) // 2, (image_height - watermark_height) // 2)

    # Overlay the watermark onto the input image
    overlay = Image.new('RGBA', image.size, (0, 0, 0, 0))
    overlay.paste(watermark, position, watermark)
    image.paste(overlay, (0, 0), overlay)

    # Apply opacity to the watermark
    image = image.convert('RGBA')
    pixels = image.load()
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = pixels[x, y]
            if pixel[3] != 0:  # If the pixel is not transparent
                pixels[x, y] = (pixel[0], pixel[1], pixel[2], int(255 * opacity))

    # Save the output image
    image = image.convert('RGB')
    image.save(output_path)

def main():
    image_path = "path_to_your_image.jpg"
    watermark_path = "path_to_your_watermark.png"
    output_path = "output.jpg"

    try:
        add_watermark(image_path, watermark_path, output_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
