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
import os
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap

# Constants for the ad design
AD_WIDTH = 800
AD_HEIGHT = 400
BACKGROUND_COLOR = (255, 255, 255)  # White background
TEXT_COLOR = (0, 0, 0)  # Black text
FONT_PATH = "arial.ttf"  # Path to a .ttf font file
FONT_SIZE = 40
OUTPUT_DIR = "ad_designs"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_ad_design(title: str, subtitle: str, filename: str) -> None:
    """
    Create a social media ad design with a title and subtitle.

    :param title: The main title of the ad.
    :param subtitle: The subtitle of the ad.
    :param filename: The filename to save the ad design.
    """
    try:
        # Create a blank image with the specified background color
        ad_image = Image.new('RGB', (AD_WIDTH, AD_HEIGHT), BACKGROUND_COLOR)
        draw = ImageDraw.Draw(ad_image)

        # Load the font
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

        # Draw the title
        title_text = textwrap.fill(title, width=30)
        draw.text((50, 50), title_text, fill=TEXT_COLOR, font=font)

        # Draw the subtitle
        subtitle_text = textwrap.fill(subtitle, width=40)
        draw.text((50, 150), subtitle_text, fill=TEXT_COLOR, font=font)

        # Save the image
        ad_image.save(os.path.join(OUTPUT_DIR, filename))
        print(f"Ad design saved as: {filename}")

    except Exception as e:
        print(f"Error creating ad design: {e}")

def generate_random_ad() -> None:
    """
    Generate a random ad design with a random title and subtitle.
    """
    titles = [
        "Boost Your Business",
        "Unleash Your Creativity",
        "Transform Your Ideas",
        "Innovate with Us",
        "Design Your Future"
    ]
    
    subtitles = [
        "Get noticed with stunning visuals.",
        "Let your brand shine.",
        "Crafting unique experiences.",
        "Your vision, our design.",
        "Elevate your marketing strategy."
    ]

    # Randomly select a title and subtitle
    title = random.choice(titles)
    subtitle = random.choice(subtitles)
    filename = f"ad_{random.randint(1000, 9999)}.png"

    # Create the ad design
    create_ad_design(title, subtitle, filename)

if __name__ == "__main__":
    # Generate a random ad design
    generate_random_ad()
```
