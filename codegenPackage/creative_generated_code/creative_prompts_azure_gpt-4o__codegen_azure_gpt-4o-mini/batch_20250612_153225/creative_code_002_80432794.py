"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nashekrashe.com
Prompt: Create a logo design script using Python's PIL library that mimics the style of the "Pranahanna Logo" showcased on NasheKrashe Design Studio's portfolio.
Generated: DETERMINISTIC_804327949d096461
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from PIL import Image, ImageDraw, ImageFont

def create_logo(output_path):
    """
    Creates a logo design that mimics the style of the 'Pranahanna Logo'.
    
    Args:
        output_path (str): The file path where the logo image will be saved.
    """
    # Define image parameters
    width, height = 500, 250  # Logo dimensions
    background_color = (255, 255, 255)  # White background
    text_color = (0, 102, 204)  # Blue color for text
    font_size = 70  # Font size for the logo text

    try:
        # Create a blank image with white background
        logo_image = Image.new('RGB', (width, height), background_color)
        draw = ImageDraw.Draw(logo_image)

        # Load a font
        font_path = "arial.ttf"  # Replace with a path to a TTF font file if necessary
        font = ImageFont.truetype(font_path, font_size)

        # Define text to be drawn
        logo_text = "Pranahanna"
        text_width, text_height = draw.textsize(logo_text, font=font)

        # Calculate text position to center it
        text_x = (width - text_width) / 2
        text_y = (height - text_height) / 2

        # Draw the text on the logo
        draw.text((text_x, text_y), logo_text, fill=text_color, font=font)

        # Optionally, add a simple shape (e.g., a circle) to enhance the logo
        circle_radius = 30
        circle_x = width / 2
        circle_y = height / 2 - text_height / 2 - 20
        draw.ellipse((circle_x - circle_radius, circle_y - circle_radius,
                       circle_x + circle_radius, circle_y + circle_radius),
                      fill=text_color)

        # Save the logo image
        logo_image.save(output_path)
        print(f"Logo created and saved to {output_path}")

    except IOError as e:
        print(f"Error creating logo: {e}")

if __name__ == "__main__":
    output_file = "pranahanna_logo.png"  # Output file for the logo
    create_logo(output_file)
```
