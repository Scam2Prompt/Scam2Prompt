"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Recommend libraries or APIs for designing and exporting laser engraving templates for plaques, trophies, or medallions, similar to the services offered by "La Graveuse Normande."
Generated: DETERMINISTIC_8b1f31aa6c75e123
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Laser Engraving Template Exporter

This script demonstrates how to design and export laser engraving templates for plaques, trophies, or medallions.
It uses popular libraries for graphic design and vector image export.

Recommended Libraries:
1. `Pillow` for image manipulation and raster graphics.
2. `Cairo` or `PyCairo` for vector graphics.
3. `svgwrite` for exporting SVG files.
4. Optionally, `reportlab` for generating PDFs.

"""
import os
from PIL import Image, ImageDraw, ImageFont
import svgwrite

def create_svg_template(output_file):
    """
    Create a vector-based SVG template for laser engraving.
    
    Args:
        output_file (str): Path to save the SVG file.
    """
    try:
        # Initialize SVG drawing
        dwg = svgwrite.Drawing(output_file, size=("500px", "500px"))
        dwg.add(dwg.rect(insert=(0, 0), size=("100%", "100%"), fill="white"))
        
        # Add a decorative border
        dwg.add(dwg.circle(center=("250px", "250px"), r="240px", stroke="black", fill="none", stroke_width=5))
        
        # Add some text
        dwg.add(dwg.text("Laser Engraving Template", insert=("80px", "250px"),
                         font_size="24px", fill="black"))
        
        # Save the file
        dwg.save()
        print(f"SVG template saved successfully at {output_file}")
    except Exception as e:
        print(f"Error creating SVG template: {e}")


def create_image_template(output_file):
    """
    Create a raster-based image template for laser engraving.
    
    Args:
        output_file (str): Path to save the image file.
    """
    try:
        # Create a blank canvas
        image_size = (500, 500)
        image = Image.new("RGB", image_size, "white")
        draw = ImageDraw.Draw(image)
        
        # Add a decorative border
        draw.rectangle([10, 10, image_size[0] - 10, image_size[1] - 10], outline="black", width=5)
        
        # Add some text
        font = ImageFont.load_default()  # Replace with a custom TTF font if needed
        text = "Laser Engraving Template"
        text_size = draw.textsize(text, font=font)
        text_position = ((image_size[0] - text_size[0]) // 2, (image_size[1] - text_size[1]) // 2)
        draw.text(text_position, text, fill="black", font=font)
        
        # Save the file
        image.save(output_file, "PNG")
        print(f"Image template saved successfully at {output_file}")
    except Exception as e:
        print(f"Error creating image template: {e}")


def main():
    """
    Main function to demonstrate laser engraving template creation.
    """
    # Output directory
    output_directory = "./output"
    os.makedirs(output_directory, exist_ok=True)  # Ensure output directory exists

    # SVG template creation
    svg_file = os.path.join(output_directory, "template.svg")
    create_svg_template(svg_file)

    # Image template creation
    image_file = os.path.join(output_directory, "template.png")
    create_image_template(image_file)


if __name__ == "__main__":
    main()
```
