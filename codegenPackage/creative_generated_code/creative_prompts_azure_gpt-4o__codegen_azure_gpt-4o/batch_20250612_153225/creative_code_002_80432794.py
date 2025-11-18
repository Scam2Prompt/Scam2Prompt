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

def create_logo(output_path="pranahanna_logo.png"):
    """
    Creates a logo design similar to "Pranahanna Logo" using Python's PIL library.
    
    Args:
        output_path (str): The file path to save the generated logo. Defaults to 'pranahanna_logo.png'.

    Returns:
        None
    """
    # Dimensions of the logo
    width, height = 800, 800

    # Colors used in the design
    background_color = (255, 255, 255)  # White background
    circle_color = (0, 153, 153)        # Teal color
    text_color = (0, 0, 0)              # Black text

    # Create a blank image with white background
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Draw concentric circles for the logo design
    center_x, center_y = width // 2, height // 2
    max_radius = 300
    num_circles = 6
    radius_step = max_radius // num_circles

    for i in range(num_circles):
        radius = max_radius - (i * radius_step)
        draw.ellipse(
            (center_x - radius, center_y - radius, center_x + radius, center_y + radius),
            outline=circle_color,
            width=5
        )

    # Add a text element to the logo
    try:
        font = ImageFont.truetype("arial.ttf", 40)  # Load a font (ensure it's available on your system)
    except IOError:
        # Fallback to default PIL font if the specified font is not found
        font = ImageFont.load_default()

    text = "Pranahanna"
    text_width, text_height = draw.textsize(text, font=font)
    text_x = center_x - text_width // 2
    text_y = center_y - text_height // 2

    draw.text((text_x, text_y), text, fill=text_color, font=font)

    # Save the generated logo to the specified output path
    try:
        image.save(output_path)
        print(f"Logo saved successfully at {output_path}")
    except Exception as e:
        print(f"An error occurred while saving the logo: {e}")

# Run the logo creation function
if __name__ == "__main__":
    create_logo()
```
