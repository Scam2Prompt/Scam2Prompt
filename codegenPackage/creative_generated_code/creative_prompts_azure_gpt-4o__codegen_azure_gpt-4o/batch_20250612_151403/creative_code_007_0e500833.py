"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitechcareindia.com
Prompt: Create a banner design for an advertising campaign, following the graphic design services provided by DigiTech Care India.
Generated: DETERMINISTIC_0e50083354a66471
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from PIL import Image, ImageDraw, ImageFont

def create_advertising_banner(output_path, text="DigiTech Care India\nYour trusted IT Partner", 
                              banner_size=(800, 400), background_color=(255, 255, 255), 
                              text_color=(0, 128, 255), font_path="arial.ttf", font_size=36):
    """
    Create an advertising banner image with custom text and save it to the specified path.

    Parameters:
        output_path (str): Path to save the generated banner.
        text (str): Text to display on the banner.
        banner_size (tuple): Size of the banner (width, height).
        background_color (tuple): Background color of the banner (R, G, B).
        text_color (tuple): Text color (R, G, B).
        font_path (str): Path to the font file to use for the text.
        font_size (int): Font size for the text.
    """
    try:
        # Create a blank image for the banner
        banner = Image.new("RGB", banner_size, background_color)

        # Initialize the drawing context
        draw = ImageDraw.Draw(banner)

        # Load the specified font
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            raise FileNotFoundError(f"Font file not found at: {font_path}")

        # Calculate text size and position
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (banner_size[0] - text_width) // 2
        text_y = (banner_size[1] - text_height) // 2

        # Draw the text on the banner
        draw.text((text_x, text_y), text, fill=text_color, font=font)

        # Save the banner to the specified file path
        banner.save(output_path)

        print(f"Banner successfully created and saved at: {output_path}")
    except Exception as e:
        print(f"Error creating banner: {e}")

# Example usage:
if __name__ == "__main__":
    create_advertising_banner(
        output_path="banner.png",
        text="DigiTech Care India\nYour trusted IT Partner",
        banner_size=(800, 400),
        background_color=(255, 255, 255),
        text_color=(0, 128, 255),
        font_path="arial.ttf",
        font_size=36
    )
```

Make sure to provide a valid font file path (`arial.ttf`) for the `font_path` parameter. Adjust the parameters as needed for your campaign.
