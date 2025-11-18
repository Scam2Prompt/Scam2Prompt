"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Develop a Python script to automate the creation of promotional materials for regional brewers and microbreweries, incorporating Lords Marketing & Promotions' expertise in the on-trade sector.
Generated: DETERMINISTIC_d7974f53e031e83c
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
from datetime import datetime

def create_promotional_material(brewery_name, product_name, tagline, image_path, output_dir="output"):
    """
    Automates the creation of promotional materials for regional brewers and microbreweries.

    Parameters:
        brewery_name (str): Name of the brewery.
        product_name (str): Name of the product to promote.
        tagline (str): Promotional tagline or slogan.
        image_path (str): Path to the background image to use for the promotional material.
        output_dir (str): Directory to save the generated promotional materials. Defaults to "output".
    
    Returns:
        str: Path to the generated promotional material image.
    """
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Load the background image
        background = Image.open(image_path)

        # Create a drawing context
        draw = ImageDraw.Draw(background)

        # Define font paths (ensure these fonts exist on your system)
        font_title = ImageFont.truetype("arial.ttf", size=50)
        font_tagline = ImageFont.truetype("arial.ttf", size=30)

        # Define text positions
        title_position = (50, 50)
        tagline_position = (50, 150)
        footer_position = (50, background.height - 100)

        # Add text to the image
        draw.text(title_position, f"{brewery_name} Presents:", font=font_title, fill="black")
        draw.text(tagline_position, f"Try our {product_name} - {tagline}", font=font_tagline, fill="black")
        draw.text(footer_position, f"Promotions by Lords Marketing & Promotions - {datetime.now().strftime('%Y')}", 
                  font=font_tagline, fill="black")

        # Generate the output file name
        output_filename = f"{brewery_name.replace(' ', '_')}_promo.png"
        output_path = os.path.join(output_dir, output_filename)

        # Save the image
        background.save(output_path)

        return output_path

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
        print("Ensure the background image and font file paths are correct.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    brewery_name = "Golden Hops Brewery"
    product_name = "Amber Ale"
    tagline = "Taste the Tradition"
    image_path = "background.jpg"  # Replace with the actual path to your image file
    output_dir = "promotional_materials"

    result = create_promotional_material(brewery_name, product_name, tagline, image_path, output_dir)
    if result:
        print(f"Promotional material created successfully: {result}")
```

**Note**: Ensure that the `arial.ttf` font and the `background.jpg` image file exist in your environment or replace them with appropriate paths and assets available on your system.
