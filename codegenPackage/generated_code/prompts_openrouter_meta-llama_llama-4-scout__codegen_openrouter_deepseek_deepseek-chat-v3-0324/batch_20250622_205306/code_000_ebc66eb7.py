"""
Generated Code Metadata:
========================
Original URL: https://woopytee.com
Prompt: "Design a t-shirt for a cancer awareness campaign with a slogan 'Breast Cancer Is Boo Sheet' similar to the one found on WoopyTee."
Generated: DETERMINISTIC_ebc66eb76246b941
Batch ID: 20250622_205306
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

def create_tshirt_design(output_path="tshirt_design.png"):
    """
    Creates a t-shirt design for a breast cancer awareness campaign with the slogan 'Breast Cancer Is Boo Sheet'.
    
    Args:
        output_path (str): Path to save the generated t-shirt design image. Defaults to "tshirt_design.png".
    """
    try:
        # Create a blank t-shirt image (white background)
        width, height = 800, 1000
        tshirt_color = (255, 192, 203)  # Pink color for breast cancer awareness
        image = Image.new("RGB", (width, height), tshirt_color)
        draw = ImageDraw.Draw(image)
        
        # Load fonts
        try:
            title_font = ImageFont.truetype("arialbd.ttf", 60)
            subtitle_font = ImageFont.truetype("arial.ttf", 30)
        except IOError:
            # Fallback fonts if specified fonts aren't available
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
        
        # Slogan text
        slogan = "Breast Cancer Is Boo Sheet"
        
        # Calculate text positioning
        text_width, text_height = draw.textsize(slogan, font=title_font)
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        
        # Draw the slogan
        draw.text((x, y), slogan, fill="black", font=title_font)
        
        # Add ribbon symbol (simplified)
        ribbon_points = [
            (width/2 - 100, y - 80),
            (width/2 - 50, y - 120),
            (width/2 + 50, y - 120),
            (width/2 + 100, y - 80),
            (width/2 + 50, y - 40),
            (width/2 - 50, y - 40)
        ]
        draw.polygon(ribbon_points, fill="pink", outline="black")
        
        # Add supporting text
        support_text = "Support Awareness • Early Detection Saves Lives"
        support_width, support_height = draw.textsize(support_text, font=subtitle_font)
        support_x = (width - support_width) / 2
        draw.text((support_x, y + text_height + 20), support_text, fill="black", font=subtitle_font)
        
        # Save the image
        image.save(output_path)
        print(f"T-shirt design successfully saved to {output_path}")
        
    except Exception as e:
        print(f"Error creating t-shirt design: {str(e)}")
        raise

if __name__ == "__main__":
    create_tshirt_design()
```
