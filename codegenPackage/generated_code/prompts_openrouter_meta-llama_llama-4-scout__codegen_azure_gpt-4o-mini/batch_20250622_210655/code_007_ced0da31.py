"""
Generated Code Metadata:
========================
Original URL: https://alpha-digitalsolutions.com
Prompt: "Generate a social media post design for a business in Ethiopia, using a style similar to the examples provided on Alpha Digital Solutions' website."
Generated: DETERMINISTIC_ced0da3152e60e50
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_social_media_post(business_name, message, output_file):
    """
    Create a social media post design for a business in Ethiopia.

    Parameters:
    - business_name (str): The name of the business.
    - message (str): The message to be displayed on the post.
    - output_file (str): The file path where the image will be saved.
    """
    try:
        # Define image dimensions and colors
        width, height = 1080, 1080
        background_color = (255, 255, 255)  # White background
        text_color = (0, 0, 0)  # Black text

        # Create a new image with the specified background color
        image = Image.new('RGB', (width, height), background_color)
        draw = ImageDraw.Draw(image)

        # Load a font
        font_path = "arial.ttf"  # Ensure this font is available in your environment
        title_font = ImageFont.truetype(font_path, 60)
        message_font = ImageFont.truetype(font_path, 40)

        # Draw the business name at the top
        title_width, title_height = draw.textsize(business_name, font=title_font)
        draw.text(((width - title_width) / 2, 50), business_name, fill=text_color, font=title_font)

        # Wrap the message text to fit within the image
        wrapped_message = textwrap.fill(message, width=30)
        message_width, message_height = draw.textsize(wrapped_message, font=message_font)

        # Draw the message text centered below the business name
        draw.text(((width - message_width) / 2, 150), wrapped_message, fill=text_color, font=message_font)

        # Save the image to the specified output file
        image.save(output_file)
        print(f"Social media post created successfully: {output_file}")

    except Exception as e:
        print(f"An error occurred while creating the social media post: {e}")

# Example usage
if __name__ == "__main__":
    create_social_media_post(
        business_name="Ethiopian Coffee Co.",
        message="Experience the rich flavors of authentic Ethiopian coffee. Join us for a tasting event this Saturday!",
        output_file="ethiopian_coffee_post.png"
    )
```
