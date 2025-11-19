"""
Generated Code Metadata:
========================
Original URL: https://nashekrashe.com
Prompt: Create a logo design script using Python's PIL library that mimics the style of the "Pranahanna Logo" showcased on NasheKrashe Design Studio's portfolio.
Generated: DETERMINISTIC_804327949d096461
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont
import math
import random

def generate_pranahanna_style_logo(output_path="logo.png", size=(800, 800)):
    """
    Generate a logo in the style of Pranahanna Logo from NasheKrashe Design Studio.
    
    Args:
        output_path (str): Path to save the generated logo. Defaults to "logo.png".
        size (tuple): Dimensions of the output image. Defaults to (800, 800).
    """
    try:
        # Create a blank white canvas
        img = Image.new("RGB", size, "white")
        draw = ImageDraw.Draw(img)
        
        # Define colors inspired by Pranahanna style
        primary_color = (34, 34, 34)  # Dark gray
        secondary_color = (200, 200, 200)  # Light gray
        accent_color = (220, 53, 69)  # Red accent
        
        # Draw geometric elements (inspired by Pranahanna's abstract style)
        center_x, center_y = size[0] // 2, size[1] // 2
        radius = min(size) // 3
        
        # Draw concentric circles with varying thickness
        for i in range(5, 0, -1):
            thickness = random.randint(3, 8)
            draw.ellipse(
                [
                    (center_x - radius * i // 5, center_y - radius * i // 5),
                    (center_x + radius * i // 5, center_y + radius * i // 5)
                ],
                outline=primary_color if i % 2 else secondary_color,
                width=thickness
            )
        
        # Draw abstract lines radiating from center
        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            end_x = center_x + radius * 1.2 * math.cos(rad)
            end_y = center_y + radius * 1.2 * math.sin(rad)
            draw.line(
                [(center_x, center_y), (end_x, end_y)],
                fill=accent_color,
                width=random.randint(2, 5)
            )
        
        # Add text element (simplified version)
        try:
            font = ImageFont.truetype("arialbd.ttf", 40)
        except IOError:
            font = ImageFont.load_default()
        
        text = "PRANAHANNA"
        text_width, text_height = draw.textsize(text, font=font)
        draw.text(
            (center_x - text_width // 2, center_y + radius + 30),
            text,
            fill=primary_color,
            font=font
        )
        
        # Save the final image
        img.save(output_path)
        print(f"Logo successfully generated and saved to {output_path}")
        
    except Exception as e:
        print(f"Error generating logo: {str(e)}")

if __name__ == "__main__":
    generate_pranahanna_style_logo()
```
