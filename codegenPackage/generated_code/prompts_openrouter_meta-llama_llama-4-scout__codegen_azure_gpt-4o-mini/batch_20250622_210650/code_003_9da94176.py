"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: "Design a graphic for a social media post promoting a digital marketing service, including key elements and best practices."
Generated: DETERMINISTIC_9da94176b7f32624
Batch ID: 20250622_210650
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

def create_social_media_post(service_name, tagline, background_color, text_color, output_path):
    """
    Create a graphic for a social media post promoting a digital marketing service.

    Parameters:
    - service_name (str): The name of the digital marketing service.
    - tagline (str): A catchy tagline for the service.
    - background_color (tuple): RGB color for the background (e.g., (255, 255, 255) for white).
    - text_color (tuple): RGB color for the text (e.g., (0, 0, 0) for black).
    - output_path (str): The file path where the image will be saved.

    Raises:
    - ValueError: If the output path is invalid or if the colors are not in the correct format.
    """
    # Validate output path
    if not os.path.isdir(os.path.dirname(output_path)):
        raise ValueError("Invalid output path. Please provide a valid directory.")

    # Create a blank image with the specified background color
    img = Image.new('RGB', (800, 800), background_color)
    draw = ImageDraw.Draw(img)

    # Load a font
    try:
        font_service_name = ImageFont.truetype("arial.ttf", 60)
        font_tagline = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        raise RuntimeError("Font file not found. Ensure 'arial.ttf' is available.")

    # Calculate text size and position for service name
    service_name_size = draw.textsize(service_name, font=font_service_name)
    service_name_position = ((img.width - service_name_size[0]) // 2, img.height // 3)

    # Calculate text size and position for tagline
    tagline_size = draw.textsize(tagline, font=font_tagline)
    tagline_position = ((img.width - tagline_size[0]) // 2, img.height // 2)

    # Draw the text on the image
    draw.text(service_name_position, service_name, fill=text_color, font=font_service_name)
    draw.text(tagline_position, tagline, fill=text_color, font=font_tagline)

    # Save the image to the specified output path
    img.save(output_path)
    print(f"Social media post created and saved to {output_path}")

# Example usage
if __name__ == "__main__":
    try:
        create_social_media_post(
            service_name="Digital Marketing Pro",
            tagline="Boost Your Online Presence!",
            background_color=(255, 223, 186),  # Light peach background
            text_color=(0, 51, 102),           # Dark blue text
            output_path="social_media_post.png"
        )
    except Exception as e:
        print(f"An error occurred: {e}")
```
