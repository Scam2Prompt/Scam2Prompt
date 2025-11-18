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

def add_watermark(input_image_path, output_image_path, watermark_text, font_path="arial.ttf", font_size=40):
    """
    Adds a watermark to a given image.

    Parameters:
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the watermarked image.
        watermark_text (str): The branding text to use as a watermark.
        font_path (str): Path to the font file to be used. Defaults to Arial.
        font_size (int): Font size for the watermark. Defaults to 40.
    """
    try:
        # Open the input image
        original_image = Image.open(input_image_path).convert("RGBA")
        width, height = original_image.size

        # Create a transparent overlay for the watermark
        watermark_overlay = Image.new("RGBA", original_image.size, (255, 255, 255, 0))

        # Setup font
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            raise ValueError(f"Font file not found at {font_path}. Please provide a valid font path.")

        # Create drawing context for the overlay
        draw = ImageDraw.Draw(watermark_overlay)

        # Calculate position for the watermark (bottom-right corner)
        text_width, text_height = draw.textsize(watermark_text, font=font)
        margin = 10
        x = width - text_width - margin
        y = height - text_height - margin

        # Add the watermark text to the overlay
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))  # White text with transparency

        # Combine the original image with the watermark overlay
        watermarked_image = Image.alpha_composite(original_image, watermark_overlay)

        # Convert to RGB mode for saving as JPEG
        watermarked_image = watermarked_image.convert("RGB")

        # Save the resulting image
        watermarked_image.save(output_image_path, format="JPEG", quality=95)

    except Exception as e:
        raise RuntimeError(f"An error occurred while adding watermark: {str(e)}")


if __name__ == "__main__":
    # Example usage
    input_image = "fashion_photo.jpg"  # Path to the input image
    output_image = "fashion_photo_watermarked.jpg"  # Path to save the output image
    watermark = "Officine dell’Immagine"  # Branding text for the watermark
    font = "arial.ttf"  # Path to font file (ensure this exists or replace with desired font)

    # Check if input image exists
    if not os.path.exists(input_image):
        raise FileNotFoundError(f"Input image file not found: {input_image}")

    # Add watermark to the image
    add_watermark(input_image, output_image, watermark, font_path=font, font_size=40)
    print(f"Watermarked image saved to: {output_image}")
```
