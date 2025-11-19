"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Write a Python function to watermark real estate photos with photographer details, such as "Simon Harris - Perth Real Estate Photography," ensuring the watermark does not obscure key elements of the image.
Generated: DETERMINISTIC_b9bb9c174a6e6e53
Batch ID: 20250612_152620
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

def add_watermark(image_path, watermark_text, output_path, opacity=0.5, font_size=30):
    """
    Adds a watermark to a real estate photo.

    Args:
        image_path (str): Path to the input image.
        watermark_text (str): Text to use for the watermark.
        output_path (str): Path to save the watermarked image.
        opacity (float, optional): Opacity of the watermark. Defaults to 0.5.
        font_size (int, optional): Font size of the watermark. Defaults to 30.

    Raises:
        FileNotFoundError: If the input image does not exist.
        ValueError: If opacity or font_size is invalid.
    """

    # Check if input image exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Input image not found: {image_path}")

    # Check if opacity and font_size are valid
    if opacity < 0 or opacity > 1:
        raise ValueError("Opacity must be between 0 and 1")
    if font_size <= 0:
        raise ValueError("Font size must be a positive integer")

    # Open the image
    with Image.open(image_path) as img:
        # Calculate the position for the watermark
        width, height = img.size
        margin = 10
        font = ImageFont.truetype("arial.ttf", font_size)
        text_width, text_height = font.getsize(watermark_text)
        x = margin
        y = height - text_height - margin

        # Create a semi-transparent overlay for the watermark
        overlay = Image.new('RGBA', img.size, (0,0,0,0))
        draw = ImageDraw.Draw(overlay)
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, int(255 * opacity)))

        # Overlay the watermark onto the original image
        out = Image.alpha_composite(img.convert('RGBA'), overlay)

        # Save the watermarked image
        out.convert('RGB').save(output_path)

# Example usage
if __name__ == "__main__":
    image_path = "input.jpg"
    watermark_text = "Simon Harris - Perth Real Estate Photography"
    output_path = "output.jpg"
    add_watermark(image_path, watermark_text, output_path)
```
