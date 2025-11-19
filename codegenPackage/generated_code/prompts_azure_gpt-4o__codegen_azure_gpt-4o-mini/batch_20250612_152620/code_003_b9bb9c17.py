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

def watermark_image(input_image_path, output_image_path, watermark_text, position='bottom_right', opacity=128):
    """
    Watermarks an image with the specified text.

    Parameters:
    - input_image_path (str): Path to the input image file.
    - output_image_path (str): Path to save the watermarked image.
    - watermark_text (str): The text to use as the watermark.
    - position (str): Position of the watermark ('top_left', 'top_right', 'bottom_left', 'bottom_right').
    - opacity (int): Opacity of the watermark (0-255).

    Raises:
    - FileNotFoundError: If the input image file does not exist.
    - ValueError: If the opacity is not in the range of 0-255.
    """
    
    # Validate opacity
    if not (0 <= opacity <= 255):
        raise ValueError("Opacity must be between 0 and 255.")

    # Check if the input image exists
    if not os.path.isfile(input_image_path):
        raise FileNotFoundError(f"The file {input_image_path} does not exist.")

    # Open the original image
    with Image.open(input_image_path).convert("RGBA") as base:
        # Create a transparent layer for the watermark
        watermark_layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
        
        # Initialize ImageDraw
        draw = ImageDraw.Draw(watermark_layer)

        # Load a font
        try:
            font = ImageFont.truetype("arial.ttf", 36)  # Adjust font size as needed
        except IOError:
            font = ImageFont.load_default()  # Fallback to default font if arial.ttf is not found

        # Calculate text size and position
        text_width, text_height = draw.textsize(watermark_text, font=font)
        
        if position == 'top_left':
            text_position = (10, 10)
        elif position == 'top_right':
            text_position = (base.width - text_width - 10, 10)
        elif position == 'bottom_left':
            text_position = (10, base.height - text_height - 10)
        elif position == 'bottom_right':
            text_position = (base.width - text_width - 10, base.height - text_height - 10)
        else:
            raise ValueError("Position must be one of: 'top_left', 'top_right', 'bottom_left', 'bottom_right'.")

        # Draw the watermark text on the watermark layer
        draw.text(text_position, watermark_text, fill=(255, 255, 255, opacity), font=font)

        # Combine the original image with the watermark
        watermarked_image = Image.alpha_composite(base.convert("RGBA"), watermark_layer)

        # Save the result
        watermarked_image.convert("RGB").save(output_image_path, "JPEG")

# Example usage
if __name__ == "__main__":
    try:
        watermark_image(
            input_image_path="real_estate_photo.jpg",
            output_image_path="watermarked_photo.jpg",
            watermark_text="Simon Harris - Perth Real Estate Photography",
            position='bottom_right',
            opacity=128
        )
        print("Watermarking completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
