"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pozymedia.com
Prompt: Recommend a framework or library for creating custom graphic designs for event branding, as described by Pozy Media's event planning services.
Generated: DETERMINISTIC_7f772cbbf1e618ed
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python script leveraging the `Pillow` library (a widely-used Python Imaging Library) for creating custom graphic designs for event branding.

```python
from PIL import Image, ImageDraw, ImageFont
import os

def create_event_branding_graphic(output_path, event_name, date, logo_path=None):
    """
    Generate a custom graphic design for event branding.

    Parameters:
        output_path (str): Path to save the generated graphic.
        event_name (str): Name of the event.
        date (str): Date of the event.
        logo_path (str, optional): Path to a logo image to include in the graphic.

    Raises:
        FileNotFoundError: If the logo_path does not exist.
        ValueError: If output_path is not a valid save path.
    """
    try:
        # Validate the logo file path if provided
        if logo_path and not os.path.isfile(logo_path):
            raise FileNotFoundError(f"Logo file not found at path: {logo_path}")

        # Validate the output path
        if not os.path.isdir(os.path.dirname(output_path)):
            raise ValueError(f"Invalid output path directory: {os.path.dirname(output_path)}")

        # Create a blank canvas (800x600 pixels, white background)
        canvas_width, canvas_height = 800, 600
        image = Image.new("RGB", (canvas_width, canvas_height), "white")

        # Initialize a drawing context
        draw = ImageDraw.Draw(image)

        # Set up fonts (ensure you have the font file, e.g., Arial)
        try:
            font_title = ImageFont.truetype("arial.ttf", size=40)
            font_date = ImageFont.truetype("arial.ttf", size=20)
        except IOError:
            raise FileNotFoundError("Font file not found. Ensure 'arial.ttf' is installed.")

        # Add event name
        text_x, text_y = 50, 50
        draw.text((text_x, text_y), event_name, fill="black", font=font_title)

        # Add event date
        date_x, date_y = 50, 120
        draw.text((date_x, date_y), date, fill="gray", font=font_date)

        # Optionally include a logo
        if logo_path:
            logo = Image.open(logo_path)
            logo.thumbnail((200, 200))  # Resize logo to fit canvas
            logo_x = canvas_width - logo.width - 50
            logo_y = canvas_height - logo.height - 50
            image.paste(logo, (logo_x, logo_y))  # Paste logo onto canvas

        # Save the generated graphic
        image.save(output_path)
        print(f"Graphic successfully saved at: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    create_event_branding_graphic(
        output_path="branding_graphic.png",
        event_name="Pozy Media Annual Gala",
        date="December 10, 2023",
        logo_path="logo.png"  # Optional logo file path
    )
```

### Notes:
- This script uses the `Pillow` library (`pip install pillow`) to create and manipulate images.
- Ensure you have a valid `.ttf` font file (e.g., `arial.ttf`) and logo image file in the appropriate locations.
- Modify paths or parameters as needed for your specific environment.
