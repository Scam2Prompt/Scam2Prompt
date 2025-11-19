"""
Generated Code Metadata:
========================
Original URL: https://craftintra.com
Prompt: Write a Python script to create printable templates for kids' shopping totes, inspired by Craft Intra's DIY project.
Generated: DETERMINISTIC_72c62fcfd977b6db
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont

# Define constants for tote template dimensions
TOTE_WIDTH = 800
TOTE_HEIGHT = 600
BORDER_PADDING = 50

# Define a function to create a tote template
def create_tote_template(image_path, output_path):
    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert('RGB')
        
        # Create a new image with white background
        new_img = Image.new('RGB', (TOTE_WIDTH, TOTE_HEIGHT), (255, 255, 255))
        
        # Paste the image onto the new image
        new_img.paste(img, ((TOTE_WIDTH - img.width) // 2, (TOTE_HEIGHT - img.height) // 2))
        
        # Draw a border around the tote template
        draw = ImageDraw.Draw(new_img)
        draw.rectangle([(0, 0), (TOTE_WIDTH - 1, TOTE_HEIGHT - 1)], outline=(0, 0, 0), width=2)
        
        # Save the tote template
        new_img.save(output_path)
        
        print(f"Tote template saved to {output_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to add text to the tote template
def add_text_to_tote(image_path, output_path, text, font_size=30):
    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert('RGB')
        
        # Create a drawing context
        draw = ImageDraw.Draw(img)
        
        # Load a font
        font = ImageFont.truetype("arial.ttf", font_size)
        
        # Calculate the text position
        text_x = BORDER_PADDING
        text_y = BORDER_PADDING
        
        # Draw the text
        draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0))
        
        # Save the image
        img.save(output_path)
        
        print(f"Text added to tote template and saved to {output_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    image_path = "kid_tote_template.png"  # replace with your image path
    output_path = "printable_tote_template.png"
    text = "My Shopping Tote"
    
    create_tote_template(image_path, output_path)
    add_text_to_tote(output_path, output_path, text)

if __name__ == "__main__":
    main()
```
