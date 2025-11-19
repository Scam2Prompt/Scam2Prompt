"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Write a Python script to generate a customized plaque design with a company's logo and name using laser engraving on aluminum.
Generated: DETERMINISTIC_b5709f8aebc73c79
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image, ImageDraw, ImageFont

def generate_plaque(company_name, logo_path, output_path, plaque_size=(800, 400), font_path="arial.ttf"):
    """
    Generates a customized plaque design with a company's logo and name.

    Parameters:
        company_name (str): The name of the company to be engraved on the plaque.
        logo_path (str): Path to the company's logo image file.
        output_path (str): Path to save the generated plaque design.
        plaque_size (tuple): Size of the plaque in pixels (width, height).
        font_path (str): Path to the font file for rendering text.

    Returns:
        None
    """
    try:
        # Validate inputs
        if not os.path.exists(logo_path):
            raise FileNotFoundError(f"Logo file not found at: {logo_path}")
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found at: {font_path}")

        # Create a blank plaque
        plaque = Image.new("RGB", plaque_size, color="silver")
        draw = ImageDraw.Draw(plaque)

        # Load and resize the logo
        logo = Image.open(logo_path)
        logo_width = plaque_size[0] // 4  # Logo width is 1/4th of the plaque width
        logo_height = int(logo_width * (logo.height / logo.width))  # Maintain aspect ratio
        logo = logo.resize((logo_width, logo_height), Image.ANTIALIAS)

        # Paste the logo onto the plaque
        logo_x = (plaque_size[0] - logo_width) // 2  # Center horizontally
        logo_y = plaque_size[1] // 4 - logo_height // 2  # Position in the upper half
        plaque.paste(logo, (logo_x, logo_y))

        # Load the font
        font_size = plaque_size[0] // 20  # Font size relative to plaque width
        font = ImageFont.truetype(font_path, font_size)

        # Add the company name
        text_x = plaque_size[0] // 2  # Center horizontally
        text_y = plaque_size[1] * 3 // 4  # Position in the lower half
        text_width, text_height = draw.textsize(company_name, font=font)
        draw.text(
            (text_x - text_width // 2, text_y - text_height // 2),
            company_name,
            fill="black",
            font=font
        )

        # Save the plaque design
        plaque.save(output_path)
        print(f"Plaque design saved successfully at: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    company_name = "Tech Innovators Inc."
    logo_path = "company_logo.png"  # Replace with the actual path to the logo
    output_path = "plaque_design.png"  # Replace with the desired output path
    font_path = "arial.ttf"  # Replace with the actual path to the font file

    generate_plaque(company_name, logo_path, output_path, font_path=font_path)
```
