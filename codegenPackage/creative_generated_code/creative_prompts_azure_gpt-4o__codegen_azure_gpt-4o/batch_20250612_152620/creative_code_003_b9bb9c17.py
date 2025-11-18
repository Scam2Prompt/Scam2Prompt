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

def add_watermark(input_image_path: str, output_image_path: str, watermark_text: str, font_path: str = "arial.ttf", font_size: int = 36):
    """
    Adds a watermark to a real estate photo without obscuring key elements of the image.

    Parameters:
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the watermarked image.
        watermark_text (str): Text to be used as the watermark.
        font_path (str): Path to the .ttf font file. Defaults to "arial.ttf".
        font_size (int): Size of the font for the watermark. Defaults to 36.

    Raises:
        FileNotFoundError: If the input image or font file does not exist.
        ValueError: If the input image path is empty or invalid.
    """
    try:
        # Verify input image exists
        if not os.path.exists(input_image_path):
            raise FileNotFoundError(f"Input image not found: {input_image_path}")

        # Verify font file exists
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found: {font_path}")
        
        # Open the image
        with Image.open(input_image_path) as image:
            # Convert to RGBA to support transparency
            image = image.convert("RGBA")
            
            # Create a transparent overlay
            overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(overlay)

            # Load the font
            font = ImageFont.truetype(font_path, font_size)
            
            # Calculate position for watermark (bottom-right corner)
            text_width, text_height = draw.textsize(watermark_text, font=font)
            x = image.width - text_width - 20  # 20px padding from the right
            y = image.height - text_height - 20  # 20px padding from the bottom
            
            # Add text watermark to the overlay
            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))  # Semi-transparent white text
            
            # Combine the original image with the overlay
            watermarked_image = Image.alpha_composite(image, overlay)
            
            # Save the watermarked image
            watermarked_image.convert("RGB").save(output_image_path)

    except Exception as e:
        print(f"Error adding watermark: {e}")
        raise

# Example usage:
# add_watermark("house.jpg", "house_watermarked.jpg", "Simon Harris - Perth Real Estate Photography")
```
