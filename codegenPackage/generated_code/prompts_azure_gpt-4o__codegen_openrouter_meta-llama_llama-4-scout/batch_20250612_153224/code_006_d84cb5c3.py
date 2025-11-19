"""
Generated Code Metadata:
========================
Original URL: https://alpha-digitalsolutions.com
Prompt: Write a Python script to automate the generation of social media ad designs, inspired by Alpha Digital Solutions' graphic design services.
Generated: DETERMINISTIC_d84cb5c32998f016
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from PIL import Image, ImageDraw, ImageFont
from typing import Dict

# Define constants
FONT_SIZE = 30
FONT_PATH = 'arial.ttf'
IMAGE_WIDTH = 1080
IMAGE_HEIGHT = 1920
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

def generate_ad_design(ad_data: Dict) -> str:
    """
    Generate a social media ad design based on provided data.

    Args:
    ad_data (Dict): A dictionary containing ad data.
        - 'image_path' (str): The path to save the generated image.
        - 'background_image_path' (str): The path to the background image.
        - 'title' (str): The title of the ad.
        - 'description' (str): The description of the ad.
        - 'call_to_action' (str): The call to action of the ad.

    Returns:
    str: The path to the generated image.
    """

    try:
        # Load background image or create a new one if not provided
        if ad_data.get('background_image_path'):
            background_image = Image.open(ad_data['background_image_path'])
        else:
            background_image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), BACKGROUND_COLOR)

        # Resize background image if necessary
        if background_image.size != (IMAGE_WIDTH, IMAGE_HEIGHT):
            background_image = background_image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))

        # Create a drawing context
        draw = ImageDraw.Draw(background_image)

        # Load font
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

        # Draw title
        title_x = 50
        title_y = 50
        draw.text((title_x, title_y), ad_data['title'], font=font, fill=TEXT_COLOR)

        # Draw description
        description_x = 50
        description_y = title_y + FONT_SIZE + 20
        draw.multiline_text((description_x, description_y), ad_data['description'], font=font, fill=TEXT_COLOR, spacing=10)

        # Draw call to action
        call_to_action_x = 50
        call_to_action_y = IMAGE_HEIGHT - FONT_SIZE - 50
        draw.text((call_to_action_x, call_to_action_y), ad_data['call_to_action'], font=font, fill=TEXT_COLOR)

        # Save the image
        image_path = ad_data.get('image_path', 'ad_design.png')
        background_image.save(image_path)

        return image_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    ad_data = {
        'image_path': 'ad_design.png',
        'background_image_path': '',
        'title': 'Get 20% Off Your First Purchase',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.',
        'call_to_action': 'Shop Now'
    }

    generated_image_path = generate_ad_design(ad_data)
    if generated_image_path:
        print(f"Ad design generated and saved to: {generated_image_path}")


if __name__ == "__main__":
    main()
```
