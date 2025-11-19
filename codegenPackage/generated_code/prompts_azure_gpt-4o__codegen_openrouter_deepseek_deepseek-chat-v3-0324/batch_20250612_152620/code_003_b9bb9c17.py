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

def add_watermark(input_image_path, output_image_path, watermark_text, font_path=None, opacity=0.5):
    """
    Add a watermark to an image with specified text.
    
    Args:
        input_image_path (str): Path to the input image file.
        output_image_path (str): Path to save the watermarked image.
        watermark_text (str): Text to be used as watermark.
        font_path (str, optional): Path to a custom font file. If None, uses default font.
        opacity (float, optional): Opacity of the watermark (0.0 to 1.0). Default is 0.5.
    
    Raises:
        FileNotFoundError: If input image or font file is not found.
        ValueError: If opacity is not between 0.0 and 1.0.
    """
    try:
        # Validate opacity
        if not 0.0 <= opacity <= 1.0:
            raise ValueError("Opacity must be between 0.0 and 1.0")
        
        # Open the original image
        with Image.open(input_image_path).convert("RGBA") as base_image:
            # Create a transparent layer for the watermark
            watermark = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
            
            # Initialize drawing context
            draw = ImageDraw.Draw(watermark)
            
            # Set font
            try:
                if font_path:
                    font = ImageFont.truetype(font_path, 36)
                else:
                    font = ImageFont.load_default()
            except IOError:
                raise FileNotFoundError("Font file not found or invalid")
            
            # Calculate text size and position (bottom right corner with padding)
            text_width, text_height = draw.textsize(watermark_text, font=font)
            margin = 20
            x = base_image.width - text_width - margin
            y = base_image.height - text_height - margin
            
            # Draw the watermark text with specified opacity
            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, int(255 * opacity)))
            
            # Combine the original image with the watermark
            watermarked_image = Image.alpha_composite(base_image, watermark)
            
            # Convert back to RGB if saving as JPEG
            if output_image_path.lower().endswith('.jpg') or output_image_path.lower().endswith('.jpeg'):
                watermarked_image = watermarked_image.convert("RGB")
            
            # Save the watermarked image
            watermarked_image.save(output_image_path)
            
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Input image not found: {input_image_path}") from e
    except Exception as e:
        raise Exception(f"An error occurred while watermarking the image: {str(e)}") from e

# Example usage:
# add_watermark(
#     input_image_path="property.jpg",
#     output_image_path="property_watermarked.jpg",
#     watermark_text="Simon Harris - Perth Real Estate Photography",
#     font_path="arial.ttf",
#     opacity=0.7
# )
```
