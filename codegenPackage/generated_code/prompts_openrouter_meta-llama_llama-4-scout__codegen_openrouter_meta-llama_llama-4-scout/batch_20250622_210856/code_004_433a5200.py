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
# Import required libraries
from PIL import Image, ImageDraw, ImageFont
import os

def create_product_label(product_name, product_description, ingredients, company_name, company_tagline):
    """
    Generate a product label design using Pillow.

    Args:
        product_name (str): Name of the product.
        product_description (str): Brief description of the product.
        ingredients (list): List of ingredients used in the product.
        company_name (str): Name of the company.
        company_tagline (str): Tagline of the company.

    Returns:
        None
    """

    # Set label dimensions
    label_width = 300
    label_height = 200

    # Create a new image with white background
    img = Image.new('RGB', (label_width, label_height), color = (73, 109, 137))
    d = ImageDraw.Draw(img)

    # Load font
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except OSError:
        print("Font not found. Using default font.")
        font = ImageFont.load_default()

    # Draw company name and tagline
    d.text((10, 10), company_name, fill=(255, 255, 0), font=font)
    d.text((10, 30), company_tagline, fill=(255, 255, 0), font=font)

    # Draw product name
    d.text((10, 60), product_name, fill=(255, 255, 255), font=font)

    # Draw product description
    d.text((10, 90), product_description, fill=(255, 255, 255), font=font, anchor='la')

    # Draw ingredients
    d.text((10, 120), "Ingredients:", fill=(255, 255, 255), font=font)
    for i, ingredient in enumerate(ingredients):
        d.text((10, 140 + (i * 20)), ingredient, fill=(255, 255, 255), font=font)

    # Save the image
    img.save('product_label.png')

def main():
    product_name = "Customized Moisturizer"
    product_description = "A high-performance moisturizer for dry skin."
    ingredients = ["Glycerin", "Hyaluronic Acid", "Vitamin E"]
    company_name = "Fabricare Cosmeticos"
    company_tagline = "Transforming beauty with high-performance raw materials"

    create_product_label(product_name, product_description, ingredients, company_name, company_tagline)

if __name__ == "__main__":
    main()
```
