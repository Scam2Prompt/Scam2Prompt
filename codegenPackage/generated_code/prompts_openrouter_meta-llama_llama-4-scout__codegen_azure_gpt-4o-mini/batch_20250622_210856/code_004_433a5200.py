"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Generate a product label design using a library like Python's Pillow, inspired by Fabricare Cosmeticos' focus on customized cosmetic products and high-performance raw materials.
Generated: DETERMINISTIC_433a52001b2f6015
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont
import os

def create_product_label(product_name, ingredients, volume, output_path):
    """
    Create a product label design using Pillow.

    Parameters:
    - product_name (str): The name of the product.
    - ingredients (str): The list of ingredients.
    - volume (str): The volume of the product (e.g., "100ml").
    - output_path (str): The path where the label image will be saved.
    """
    # Define label dimensions and colors
    label_width = 400
    label_height = 600
    background_color = (255, 255, 255)  # White background
    text_color = (0, 0, 0)  # Black text

    # Create a new image with the specified background color
    label_image = Image.new('RGB', (label_width, label_height), background_color)
    draw = ImageDraw.Draw(label_image)

    # Load a font
    try:
        font_path = "arial.ttf"  # Ensure this font file is available
        title_font = ImageFont.truetype(font_path, 36)
        text_font = ImageFont.truetype(font_path, 24)
    except IOError:
        print("Font file not found. Using default font.")
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()

    # Draw the product name
    draw.text((20, 20), product_name, fill=text_color, font=title_font)

    # Draw the ingredients
    draw.text((20, 80), "Ingredients:", fill=text_color, font=text_font)
    draw.text((20, 120), ingredients, fill=text_color, font=text_font)

    # Draw the volume
    draw.text((20, 500), f"Volume: {volume}", fill=text_color, font=text_font)

    # Save the label image
    try:
        label_image.save(output_path)
        print(f"Label saved successfully at {output_path}")
    except Exception as e:
        print(f"Error saving label image: {e}")

if __name__ == "__main__":
    # Example usage
    product_name = "Custom Face Cream"
    ingredients = "Aqua, Glycerin, Shea Butter, Vitamin E, Fragrance"
    volume = "100ml"
    output_path = "product_label.png"

    create_product_label(product_name, ingredients, volume, output_path)
```
