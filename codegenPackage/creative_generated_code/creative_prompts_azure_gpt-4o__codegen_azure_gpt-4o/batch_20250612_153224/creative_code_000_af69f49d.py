"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createxpro.com
Prompt: Write Python code to generate a design template for textile customization using techniques like serigraphy or sublimation, as described on CreatexPro's website.
Generated: DETERMINISTIC_af69f49d63b39b3d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont

def create_design_template(output_path, width=3000, height=2000, dpi=300):
    """
    Generate a design template for textile customization using techniques like serigraphy or sublimation.

    Parameters:
        output_path (str): Path where the output design template will be saved.
        width (int): Width of the template in pixels. Default is 3000px.
        height (int): Height of the template in pixels. Default is 2000px.
        dpi (int): Resolution of the template in dots per inch. Default is 300 DPI.

    Returns:
        None
    """
    try:
        # Create a blank canvas with white background
        template = Image.new("RGB", (width, height), "white")

        # Initialize drawing context
        draw = ImageDraw.Draw(template)

        # Add a grid for alignment and positioning
        grid_spacing = 100  # Pixels between grid lines
        for x in range(0, width, grid_spacing):
            draw.line([(x, 0), (x, height)], fill="lightgray", width=1)
        for y in range(0, height, grid_spacing):
            draw.line([(0, y), (width, y)], fill="lightgray", width=1)

        # Add a center marker
        center_x, center_y = width // 2, height // 2
        draw.line([(center_x, 0), (center_x, height)], fill="red", width=2)
        draw.line([(0, center_y), (width, center_y)], fill="red", width=2)

        # Add a title and instructions
        font_path = os.path.join(os.path.dirname(__file__), "arial.ttf")  # Path to font file
        if os.path.exists(font_path):
            font = ImageFont.truetype(font_path, size=36)
        else:
            font = ImageFont.load_default()

        title = "Textile Design Template"
        instructions = "Use this template for serigraphy or sublimation. Keep key design elements within central area."

        text_padding = 10
        text_width, text_height = draw.textsize(title, font=font)
        draw.text(
            ((width - text_width) // 2, text_padding),
            title,
            fill="black",
            font=font,
        )
        draw.text(
            (text_padding, height - text_height - text_padding),
            instructions,
            fill="black",
            font=font,
        )

        # Save the template to the specified output path
        template.save(output_path, dpi=(dpi, dpi))
        print(f"Design template successfully created at: {output_path}")

    except Exception as e:
        print(f"An error occurred while creating the design template: {e}")

# Example usage
if __name__ == "__main__":
    output_file = "textile_design_template.png"
    create_design_template(output_file)
```
