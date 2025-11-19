"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Write a Python script that automates the creation of flyers and brochures, incorporating design elements mentioned in Ram Digi's print media services.
Generated: DETERMINISTIC_e5444e88794ca9f6
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from PIL import Image, ImageDraw, ImageFont
import os

def create_flyer(output_path, title, content, footer, design_elements):
    """
    Creates a flyer image using the specified design elements.

    Args:
        output_path (str): Path to save the generated flyer.
        title (str): Title of the flyer.
        content (str): Main content of the flyer.
        footer (str): Footer text for the flyer.
        design_elements (dict): Dictionary containing design parameters such as colors, fonts, sizes, etc.
    
    Returns:
        None
    """
    try:
        # Validate design elements
        background_color = design_elements.get("background_color", "white")
        title_color = design_elements.get("title_color", "black")
        content_color = design_elements.get("content_color", "black")
        footer_color = design_elements.get("footer_color", "gray")
        font_path = design_elements.get("font_path", None)
        image_size = design_elements.get("image_size", (800, 1200))

        # Create flyer canvas
        flyer = Image.new("RGB", image_size, background_color)
        draw = ImageDraw.Draw(flyer)
        
        # Load fonts
        title_font = ImageFont.truetype(font_path, design_elements.get("title_font_size", 50)) if font_path else ImageFont.load_default()
        content_font = ImageFont.truetype(font_path, design_elements.get("content_font_size", 30)) if font_path else ImageFont.load_default()
        footer_font = ImageFont.truetype(font_path, design_elements.get("footer_font_size", 20)) if font_path else ImageFont.load_default()
        
        # Draw title
        title_position = (image_size[0] // 2, 50)
        draw.text(title_position, title, fill=title_color, font=title_font, anchor="mm")
        
        # Draw content
        content_position = (50, 150)
        draw.multiline_text(content_position, content, fill=content_color, font=content_font, spacing=10)

        # Draw footer
        footer_position = (image_size[0] // 2, image_size[1] - 100)
        draw.text(footer_position, footer, fill=footer_color, font=footer_font, anchor="mm")
        
        # Save flyer
        flyer.save(output_path)
        print(f"Flyer saved successfully at {output_path}")
    
    except FileNotFoundError as e:
        print(f"Error: Font file not found - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    # Define flyer design elements
    design_elements = {
        "background_color": "#F0F8FF",
        "title_color": "#333333",
        "content_color": "#000000",
        "footer_color": "#666666",
        "font_path": "arial.ttf",  # Replace with a valid font file path on your system
        "title_font_size": 60,
        "content_font_size": 40,
        "footer_font_size": 25,
        "image_size": (1000, 1400)
    }

    # Example flyer details
    output_path = "flyer_sample.png"
    flyer_title = "Ram Digi Print Media Services"
    flyer_content = "We provide high-quality print media services:\n- Brochures\n- Flyers\n- Business Cards\n- Posters\nContact us today!"
    flyer_footer = "Visit us at www.ramdigi.com | Call: +123-456-7890"

    # Generate flyer
    create_flyer(output_path, flyer_title, flyer_content, flyer_footer, design_elements)
```
