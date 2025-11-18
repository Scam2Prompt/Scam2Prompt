"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Write a Python script to create printable templates for kids' shopping totes, inspired by Craft Intra's DIY project.
Generated: DETERMINISTIC_72c62fcfd977b6db
Batch ID: 20250612_152109
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

def create_shopping_tote_template(output_dir, design_text, tote_width=400, tote_height=500, font_size=40):
    """
    Creates a printable template for a kids' shopping tote with custom text.
    
    Parameters:
        output_dir (str): The directory where the template will be saved.
        design_text (str): The text to be included in the design.
        tote_width (int): Width of the tote template in pixels. Default is 400.
        tote_height (int): Height of the tote template in pixels. Default is 500.
        font_size (int): Font size for the design text. Default is 40.
    """
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Create a blank canvas for the tote design
        canvas = Image.new('RGB', (tote_width, tote_height), 'white')
        draw = ImageDraw.Draw(canvas)

        # Load a font for the text design
        try:
            font = ImageFont.truetype('arial.ttf', font_size)
        except IOError:
            # Fallback to default font if 'arial.ttf' is not available
            font = ImageFont.load_default()

        # Calculate text position to center it on the canvas
        text_width, text_height = draw.textsize(design_text, font=font)
        text_x = (tote_width - text_width) // 2
        text_y = (tote_height - text_height) // 2

        # Draw the design text on the canvas
        draw.text((text_x, text_y), design_text, font=font, fill='black')

        # Add a decorative border around the canvas
        border_width = 10
        draw.rectangle([(border_width, border_width), 
                        (tote_width - border_width, tote_height - border_width)], 
                       outline='black', width=border_width)

        # Save the canvas as an image file
        output_path = os.path.join(output_dir, 'kids_shopping_tote_template.png')
        canvas.save(output_path, 'PNG')

        print(f"Template saved successfully at: {output_path}")
    
    except Exception as e:
        print(f"An error occurred while creating the template: {e}")

# Example usage
if __name__ == "__main__":
    # Define the parameters
    output_directory = "output_templates"
    template_text = "Craft Intra DIY Tote"

    # Create the shopping tote template
    create_shopping_tote_template(output_directory, template_text)
```
