"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Suggest tools or libraries for designing eye-catching marketing materials for pubs and bars, and write code to generate sample designs using those tools.
Generated: DETERMINISTIC_33488af408b11879
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Marketing Materials Generator**
=====================================

### Required Libraries

* `Pillow` for image processing
* `numpy` for numerical operations

### Installation

```bash
pip install Pillow numpy
```

### Code

```python
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random

# Define a function to generate a sample poster design
def generate_poster_design(width=800, height=600):
    """
    Generate a sample poster design for a pub or bar.

    Args:
        width (int): The width of the poster. Defaults to 800.
        height (int): The height of the poster. Defaults to 600.

    Returns:
        Image: The generated poster design.
    """
    # Create a new image with a white background
    img = Image.new('RGB', (width, height), color = (73, 109, 137))
    d = ImageDraw.Draw(img)

    # Add a title
    font = ImageFont.load_default()
    title = "Welcome to our Pub"
    d.text((width/2 - 100, 50), title, font=font, fill=(255, 255, 0))

    # Add a subtitle
    subtitle = "Come and enjoy our drinks"
    d.text((width/2 - 100, 100), subtitle, font=font, fill=(255, 255, 0))

    # Add a promotional offer
    offer = "Buy one get one free on all drinks"
    d.text((width/2 - 150, 200), offer, font=font, fill=(255, 0, 0))

    # Add an image
    image_path = "path_to_your_image.jpg"
    try:
        image = Image.open(image_path)
        image.thumbnail((300, 300))
        img.paste(image, (width/2 - 150, 300))
    except FileNotFoundError:
        print("Image not found.")

    return img

# Define a function to generate a sample social media post design
def generate_social_media_post_design(width=500, height=500):
    """
    Generate a sample social media post design for a pub or bar.

    Args:
        width (int): The width of the post. Defaults to 500.
        height (int): The height of the post. Defaults to 500.

    Returns:
        Image: The generated social media post design.
    """
    # Create a new image with a white background
    img = Image.new('RGB', (width, height), color = (73, 109, 137))
    d = ImageDraw.Draw(img)

    # Add a title
    font = ImageFont.load_default()
    title = "Happy Hour"
    d.text((50, 50), title, font=font, fill=(255, 255, 0))

    # Add a description
    description = "Join us for happy hour and enjoy discounts on all drinks"
    d.text((50, 100), description, font=font, fill=(255, 255, 0))

    # Add an image
    image_path = "path_to_your_image.jpg"
    try:
        image = Image.open(image_path)
        image.thumbnail((200, 200))
        img.paste(image, (150, 150))
    except FileNotFoundError:
        print("Image not found.")

    return img

# Generate and save sample designs
if __name__ == "__main__":
    poster_design = generate_poster_design()
    poster_design.save("poster_design.png")

    social_media_post_design = generate_social_media_post_design()
    social_media_post_design.save("social_media_post_design.png")
```
