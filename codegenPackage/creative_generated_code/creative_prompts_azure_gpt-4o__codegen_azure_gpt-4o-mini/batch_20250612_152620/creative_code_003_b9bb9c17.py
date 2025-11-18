"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Write a Python function to watermark real estate photos with photographer details, such as "Simon Harris - Perth Real Estate Photography," ensuring the watermark does not obscure key elements of the image.
Generated: DETERMINISTIC_b9bb9c174a6e6e53
Batch ID: 20250612_152620
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

def watermark_image(input_image_path: str, output_image_path: str, watermark_text: str, position: str = 'bottom-right', opacity: int = 128) -> None:
    """
    Watermark an image with specified text.
    
    :param input_image_path: Path to the input image file
    :param output_image_path: Path to save the watermarked image file
    :param watermark_text: The text to be used as the watermark
    :param position: Position of the watermark (options: 'top-left', 'top-right', 'bottom-left', 'bottom-right')
    :param opacity: Opacity of the watermark (0-255, where 255 is fully opaque)
    :raises FileNotFoundError: If the input image path does not exist
    :raises ValueError: If the position is not recognized
    """
    # Check if input image exists
    if not os.path.exists(input_image_path):
        raise FileNotFoundError(f"The input image '{input_image_path}' does not exist.")

    # Load the image
    with Image.open(input_image_path).convert("RGBA") as base_image:
        # Create a transparent overlay for the watermark
        watermark = Image.new('RGBA', base_image.size, (255, 255, 255, 0))
        
        # Set up drawing context
        draw = ImageDraw.Draw(watermark)

        # Load a font
        try:
            font = ImageFont.truetype("arial.ttf", 36)
        except IOError:
            font = ImageFont.load_default()

        # Calculate text size and position
        text_size = draw.textsize(watermark_text, font=font)
        if position == 'top-left':
            position = (10, 10)
        elif position == 'top-right':
            position = (base_image.width - text_size[0] - 10, 10)
        elif position == 'bottom-left':
            position = (10, base_image.height - text_size[1] - 10)
        elif position == 'bottom-right':
            position = (base_image.width - text_size[0] - 10, base_image.height - text_size[1] - 10)
        else:
            raise ValueError("Position must be one of: 'top-left', 'top-right', 'bottom-left', 'bottom-right'.")

        # Draw the watermark text on the overlay
        draw.text(position, watermark_text, fill=(255, 255, 255, opacity), font=font)

        # Combine the base image with the watermark
        watermarked_image = Image.alpha_composite(base_image.convert("RGBA"), watermark)

        # Save the watermarked image
        watermarked_image.convert("RGB").save(output_image_path, "JPEG")

# Example usage
# watermark_image('input_photo.jpg', 'output_photo.jpg', 'Simon Harris - Perth Real Estate Photography')
```
