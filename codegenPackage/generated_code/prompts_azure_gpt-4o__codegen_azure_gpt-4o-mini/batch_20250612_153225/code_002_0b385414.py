"""
Generated Code Metadata:
========================
Original URL: https://budbeeindia.com
Prompt: Generate code to design a logo using Python's PIL library, inspired by BudBee India's emphasis on creative branding and logo design.
Generated: DETERMINISTIC_0b385414d1c6a0ad
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont

def create_logo(output_path: str, logo_text: str, logo_color: str, background_color: str, font_size: int = 100) -> None:
    """
    Create a logo using the PIL library.

    Parameters:
    - output_path (str): The file path where the logo will be saved.
    - logo_text (str): The text to be displayed on the logo.
    - logo_color (str): The color of the logo text in hex format (e.g., '#FF5733').
    - background_color (str): The background color of the logo in hex format (e.g., '#FFFFFF').
    - font_size (int): The size of the font for the logo text. Default is 100.
    
    Raises:
    - ValueError: If the output path is invalid or if the colors are not in hex format.
    """
    # Validate the output path
    if not output_path.endswith(('.png', '.jpg', '.jpeg')):
        raise ValueError("Output path must end with .png, .jpg, or .jpeg")

    # Create a blank image with a white background
    logo_width, logo_height = 800, 400
    image = Image.new('RGB', (logo_width, logo_height), background_color)
    
    # Initialize ImageDraw
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        raise IOError("Font file not found. Please ensure 'arial.ttf' is available.")

    # Calculate text size and position
    text_width, text_height = draw.textsize(logo_text, font=font)
    text_x = (logo_width - text_width) / 2
    text_y = (logo_height - text_height) / 2

    # Draw the text on the image
    draw.text((text_x, text_y), logo_text, fill=logo_color, font=font)

    # Save the image to the specified output path
    try:
        image.save(output_path)
        print(f"Logo saved successfully at {output_path}")
    except Exception as e:
        raise RuntimeError(f"Failed to save the logo: {e}")

# Example usage
if __name__ == "__main__":
    try:
        create_logo(
            output_path='budbee_logo.png',
            logo_text='BudBee',
            logo_color='#FF5733',
            background_color='#FFFFFF'
        )
    except Exception as e:
        print(f"An error occurred: {e}")
```
