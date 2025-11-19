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

```python
from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(input_image_path, output_image_path, watermark_text, position, opacity=128):
    """
    Adds a watermark to an image.

    Parameters:
    - input_image_path: str, path to the input image file
    - output_image_path: str, path to save the watermarked image
    - watermark_text: str, text to be used as the watermark
    - position: tuple, (x, y) coordinates for the watermark position
    - opacity: int, opacity level of the watermark (0-255)

    Raises:
    - FileNotFoundError: if the input image file does not exist
    - ValueError: if the opacity is not in the range 0-255
    """
    
    # Validate opacity
    if not (0 <= opacity <= 255):
        raise ValueError("Opacity must be between 0 and 255.")

    # Check if the input image exists
    if not os.path.isfile(input_image_path):
        raise FileNotFoundError(f"The file {input_image_path} does not exist.")

    # Open the original image
    original = Image.open(input_image_path).convert("RGBA")

    # Create a transparent layer for the watermark
    watermark_layer = Image.new("RGBA", original.size, (0, 0, 0, 0))

    # Initialize ImageDraw
    draw = ImageDraw.Draw(watermark_layer)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 36)  # Adjust font size as needed
    except IOError:
        font = ImageFont.load_default()  # Fallback to default font if custom font is not found

    # Calculate text size and position
    text_size = draw.textsize(watermark_text, font)
    text_x = position[0]
    text_y = position[1]

    # Draw the watermark text on the transparent layer
    draw.text((text_x, text_y), watermark_text, fill=(255, 255, 255, opacity), font=font)

    # Combine the original image with the watermark
    watermarked = Image.alpha_composite(original, watermark_layer)

    # Save the result
    watermarked.convert("RGB").save(output_image_path, "JPEG")

# Example usage
if __name__ == "__main__":
    try:
        add_watermark(
            input_image_path="fashion_photo.jpg",
            output_image_path="watermarked_fashion_photo.jpg",
            watermark_text="Officine dell’Immagine",
            position=(10, 10),  # Top-left corner
            opacity=128
        )
        print("Watermark added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
