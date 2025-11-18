"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budbeeindia.com
Prompt: Generate code to design a logo using Python's PIL library, inspired by BudBee India's emphasis on creative branding and logo design.
Generated: DETERMINISTIC_0b385414d1c6a0ad
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from PIL import Image, ImageDraw, ImageFont

def create_logo(output_path: str, logo_text: str = "BudBee", font_path: str = "arial.ttf", logo_color: tuple = (255, 204, 0), bg_color: tuple = (0, 0, 0), size: tuple = (500, 500)):
    """
    Creates a logo with the specified text, colors, and size.

    Parameters:
        output_path (str): The path where the logo image will be saved.
        logo_text (str): The text to be displayed on the logo. Default is "BudBee".
        font_path (str): The path to the font file. Default is "arial.ttf".
        logo_color (tuple): The color of the logo text in RGB format. Default is yellow.
        bg_color (tuple): The background color of the logo in RGB format. Default is black.
        size (tuple): The size of the logo (width, height). Default is (500, 500).
    """
    try:
        # Create a blank image with the specified background color
        logo_image = Image.new('RGB', size, bg_color)
        
        # Initialize the drawing context
        draw = ImageDraw.Draw(logo_image)
        
        # Load the specified font
        font_size = int(size[1] * 0.2)  # Font size is 20% of the logo height
        font = ImageFont.truetype(font_path, font_size)
        
        # Calculate text size and position
        text_width, text_height = draw.textsize(logo_text, font=font)
        text_x = (size[0] - text_width) // 2
        text_y = (size[1] - text_height) // 2
        
        # Draw the logo text on the image
        draw.text((text_x, text_y), logo_text, fill=logo_color, font=font)
        
        # Save the logo image to the specified path
        logo_image.save(output_path)
        print(f"Logo saved successfully to {output_path}")

    except FileNotFoundError:
        print(f"Error: Font file not found at {font_path}. Please check the path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Specify output path and create the logo
    create_logo(output_path='budbee_logo.png')
```
