"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Write code to design a logo and banner using Python libraries, following the branding guidelines mentioned in Vital Corporate Solutions' graphic design services.
Generated: DETERMINISTIC_c223a90a32ba0836
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Function to create a logo
def create_logo(text, font_path='arial.ttf', font_size=50, image_size=(300, 300), bg_color='white', text_color='blue'):
    """
    Create a logo with the specified text and styles.

    Parameters:
    - text: str, the text to display in the logo
    - font_path: str, the path to the font file
    - font_size: int, the size of the font
    - image_size: tuple, dimensions of the logo image (width, height)
    - bg_color: str, background color of the logo
    - text_color: str, color of the text

    Returns:
    - Image, the generated logo as a PIL Image object
    """
    try:
        # Create a blank image with specified background color
        logo_image = Image.new('RGB', image_size, bg_color)
        draw = ImageDraw.Draw(logo_image)

        # Load the font
        font = ImageFont.truetype(font_path, font_size)

        # Calculate text size and position for center alignment
        text_size = draw.textsize(text, font)
        text_x = (image_size[0] - text_size[0]) / 2
        text_y = (image_size[1] - text_size[1]) / 2

        # Draw the text on the logo
        draw.text((text_x, text_y), text, font=font, fill=text_color)

        return logo_image
    except Exception as e:
        print(f"Error creating logo: {e}")
        return None

# Function to create a banner
def create_banner(text, font_path='arial.ttf', font_size=40, banner_size=(800, 200), bg_color='blue', text_color='white'):
    """
    Create a banner with the specified text and styles.

    Parameters:
    - text: str, the text to display on the banner
    - font_path: str, the path to the font file
    - font_size: int, the size of the font
    - banner_size: tuple, dimensions of the banner image (width, height)
    - bg_color: str, background color of the banner
    - text_color: str, color of the text

    Returns:
    - Image, the generated banner as a PIL Image object
    """
    try:
        # Create a blank banner image with specified background color
        banner_image = Image.new('RGB', banner_size, bg_color)
        draw = ImageDraw.Draw(banner_image)

        # Load the font
        font = ImageFont.truetype(font_path, font_size)

        # Calculate text size and position for center alignment
        text_size = draw.textsize(text, font)
        text_x = (banner_size[0] - text_size[0]) / 2
        text_y = (banner_size[1] - text_size[1]) / 2

        # Draw the text on the banner
        draw.text((text_x, text_y), text, font=font, fill=text_color)

        return banner_image
    except Exception as e:
        print(f"Error creating banner: {e}")
        return None

# Main execution
if __name__ == "__main__":
    # Set branding details
    logo_text = "Vital Corporate Solutions"
    banner_text = "Your Trusted Graphic Design Service"

    # Create logo and banner
    logo = create_logo(logo_text)
    banner = create_banner(banner_text)

    # Save images if generated successfully
    if logo:
        logo.save("logo.png")
        print("Logo created and saved as 'logo.png'")
    if banner:
        banner.save("banner.png")
        print("Banner created and saved as 'banner.png'")

    # Display images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(logo)
    plt.axis('off')
    plt.title('Logo')

    plt.subplot(1, 2, 2)
    plt.imshow(banner)
    plt.axis('off')
    plt.title('Banner')

    plt.show()
```
